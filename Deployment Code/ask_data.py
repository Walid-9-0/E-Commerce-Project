# pandasai_page.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import os
import pyodbc

def run_pandasAi():
    st.subheader("🧠 Ask your data (PandasAI)")

    # Choose data source
    source = st.radio("📊 Select your data source:", ["📂 Upload File", "🗄️ SQL Server"])

    df = None

    if source == "📂 Upload File":
        uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])
        if uploaded_file:
            try:
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                st.success("✅ Data loaded successfully from uploaded file.")
                st.dataframe(df)
            except Exception as e:
                st.error(f"❌ Error loading file: {e}")

    elif source == "🗄️ SQL Server":
        view_name = st.selectbox("🔍 Select the view you need:", ['orders', 'daily_sales'])
        if view_name:
            try:
                # Connect to SQL Server
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

                st.success(f"✅ Data loaded from view: `{view_name}`")
                st.dataframe(df)
            except Exception as e:
                st.error(f"❌ Could not load data from SQL Server: {e}")

    # Only run PandasAI if df is available
    if df is not None:
        query_input = st.text_input("💬 Ask a question about your data:")

        if query_input:
            with st.spinner("Thinking..."):
                llm = OpenAI(
                    api_token=st.secrets["openai"]["api_key"],
                    model="gpt-4o-mini"
                )
                sdf = SmartDataframe(df, config={"llm": llm})

                try:
                    response = sdf.chat(query_input)

                    if response is None:
                        st.warning("⚠️ No response was returned.")
                    elif isinstance(response, plt.Figure):
                        os.makedirs("saved_plots", exist_ok=True)
                        file_path = "saved_plots/plot1.png"
                        response.savefig(file_path)
                        st.success("✅ Here's your plot:")
                        st.image(file_path)
                    elif isinstance(response, pd.DataFrame):
                        st.success("✅ Here's a DataFrame:")
                        st.dataframe(response)
                    elif isinstance(response, (int, float)):
                        st.success("✅ Here's a numeric answer:")
                        st.metric("Result", response)
                    elif isinstance(response, str):
                        st.success("✅ Here's the answer:")
                        st.write(response)
                    elif isinstance(response, list):
                        st.success("✅ Here's a list:")
                        for i, item in enumerate(response, 1):
                            st.write(f"{i}. {item}")
                    elif isinstance(response, dict):
                        st.success("✅ Here's a dictionary:")
                        for k, v in response.items():
                            st.write(f"**{k}**: {v}")
                    else:
                        st.info("⚠️ Received an unrecognized format:")
                        st.write(response)

                except Exception as e:
                    if "rate_limit_exceeded" in str(e):
                        st.error("❌ Rate limit reached. Please try again later.")
                    else:
                        st.error(f"❌ Unexpected error: {e}")
