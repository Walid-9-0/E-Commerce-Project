def run_sentiment_app():
    import streamlit as st
    import pickle
    import pandas as pd
    import io
    import matplotlib.pyplot as plt
    import re
    import nltk
    from nltk.corpus import stopwords
    import pyodbc

    nltk.download('stopwords')

    @st.cache_resource
    def load_model():
        with open(r"models/log_model_tfidf.pkl", "rb") as f:
            model = pickle.load(f)
        with open(r"models/tfidf_vectorizer.pkl", "rb") as f:
            tfidf = pickle.load(f)
        return model, tfidf

    model, tfidf = load_model()

    label_map = {
        0: ("Negative", "😠", "red"),
        1: ("Positive", "😊", "green")
    }


    st.markdown("<h1 style='color:white; font-weight:bold;'>💬 Sentiment Classifier</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h7 style='color:gray;'>Enter a sentence, upload a file, or load from SQL Server View to classify as Positive or Negative.</h7>", unsafe_allow_html=True)

    if "history" not in st.session_state:
        st.session_state.history = []

    # Stopwords setup
    stop_words = set(stopwords.words('english'))
    negations = {
        "not", "no", "nor", "n't",
        "don't", "doesn't", "didn't", "won't", "wouldn't", "couldn't",
        "shouldn't", "wasn't", "weren't", "haven't", "hasn't", "hadn't",
        "isn't", "aren't", "mustn't", "mightn't", "needn't", "shan't"
    }
    stop_words = stop_words - negations

    def preprocess_text(text):
        text = text.lower()
        text = re.sub(r'@\w+', '', text)
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        tokens = re.findall(r'\b\w+\b', text)
        tokens = [word for word in tokens if word not in stop_words]
        return ' '.join(tokens)

    # Input method selection
    input_option = st.radio("Choose input type:", ["Text Input", "Upload File", "Load from SQL Server View"])

    if input_option == "Text Input":
        text = st.text_area("📝 Enter text", height=100)
        if st.button("🔍 Classify") and text.strip():
            cleaned_text = preprocess_text(text)
            X = tfidf.transform([cleaned_text])
            label = model.predict(X)[0]
            prob = model.predict_proba(X)[0]
            conf = max(prob) * 100
            sentiment, emoji, color = label_map.get(label, ("Unknown", "❓", "gray"))
            st.markdown(f"""
                <div style='background:{color};color:white;padding:1rem;border-radius:10px;text-align:center;font-weight:bold'>
                    {emoji} {sentiment} ({conf:.2f}%)
                </div>
            """, unsafe_allow_html=True)
            st.session_state.history.append({
                "Text": text, "Prediction": sentiment, "Confidence (%)": f"{conf:.2f}"
            })

    elif input_option == "Upload File":
        uploaded_file = st.file_uploader("📎 Upload CSV / Excel file", type=["csv", "xlsx"])
        text_column = st.text_input("Column name containing text", value="Text")

        if uploaded_file:
            if uploaded_file.name.endswith(".csv"):
                try:
                    df = pd.read_csv(uploaded_file, encoding="utf-8")
                except UnicodeDecodeError:
                    df = pd.read_csv(uploaded_file, encoding="latin1")
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            else:
                df = pd.read_csv(uploaded_file, delimiter="\n", header=None, names=["Text"])

            if text_column not in df.columns:
                st.warning(f"⚠️ Column '{text_column}' not found.")
            else:
                texts = df[text_column].dropna().astype(str).tolist()
                cleaned_texts = [preprocess_text(t) for t in texts]
                X = tfidf.transform(cleaned_texts)
                labels = model.predict(X)
                probs = model.predict_proba(X)
                for text, label, prob in zip(texts, labels, probs):
                    conf = max(prob) * 100
                    sentiment, _, _ = label_map[label]
                    st.session_state.history.append({
                        "Text": text, "Prediction": sentiment, "Confidence (%)": f"{conf:.2f}"
                    })
                st.success(f"✅ Classified {len(texts)} rows.")

    elif input_option == "Load from SQL Server View":
        view_name = st.text_input("Enter SQL Server View name", value="Reviews_text")

        if st.button("📥 Load from SQL View") and view_name.strip():
            try:
                import pyodbc
                server = st.secrets["sql"]["server"]
                database = st.secrets["sql"]["database"]
                conn = pyodbc.connect(
                    f'DRIVER={{SQL Server}};'
                    f'SERVER={server};'
                    f'DATABASE={database};'
                    f'Trusted_Connection=yes;'
                )

                query = f"SELECT * FROM {view_name}"
                df = pd.read_sql(query, conn)
                conn.close()

                if df.empty:
                    st.warning(f"⚠️ View `{view_name}` is empty.")
                else:
                    st.success(f"✅ Loaded {len(df)} records from view `{view_name}`")

                    text_column = st.selectbox("Select the column containing text:", df.columns)

                    if text_column:
                        texts = df[text_column].dropna().astype(str).tolist()
                        cleaned_texts = [preprocess_text(t) for t in texts]
                        X = tfidf.transform(cleaned_texts)
                        labels = model.predict(X)
                        probs = model.predict_proba(X)

                        for text, label, prob in zip(texts, labels, probs):
                            conf = max(prob) * 100
                            sentiment, _, _ = label_map[label]
                            st.session_state.history.append({
                                "Text": text, "Prediction": sentiment, "Confidence (%)": f"{conf:.2f}"
                            })

                        st.success(f"✅ Classified {len(texts)} rows from SQL View.")
            except Exception as e:
                st.error(f"❌ Failed to load data from SQL view: {e}")




    if st.session_state.history:
        df_history = pd.DataFrame(st.session_state.history)
        st.subheader("📚 Classification History")
        st.dataframe(df_history, use_container_width=True)

        st.subheader("📊 Sentiment Distribution")
        sentiment_counts = df_history["Prediction"].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%',
                colors=["green", "red"], startangle=90)
        ax1.set_title("Sentiment Distribution (Pie Chart)")
        st.pyplot(fig1)

        st.write(sentiment_counts,unsafe_allow_html=True)

        csv_buffer = io.StringIO()
        df_history.to_csv(csv_buffer, index=False)
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv_buffer.getvalue(),
            file_name="sentiment_results.csv",
            mime="text/csv"
        )

    if st.button("🗑️ Clear History"):
        st.session_state.history = []