def run_return_status_app():
    import streamlit as st
    import pickle as pkl
    import pandas as pd
    from collections import Counter

    # st.set_page_config(page_title="Return Status Prediction", page_icon="💬", layout="wide")


    model_names = ['KNN', 'Decision_tree', 'SVC', 'XGBoost', 'AdaBoost']


    def load_model(name):
        return pkl.load(open(f"models/{name}.pkl", "rb"))


    cat_cols = ['state_code', 'carrier', 'status', 'payment_method']
    encoders = {}
    for col in cat_cols:
        encoders[col] = pkl.load(open(f"encoding/{col}_encoder.pkl", "rb"))


    scaler = pkl.load(open("scaler/scaler.pkl", "rb"))

    st.markdown("<h1 style='color:white; font-weight:bold;'>📦 Return Status Prediction</h1>", unsafe_allow_html=True)

    # st.title("📦 Return Status Prediction")
    st.markdown("---")



    selected_model = 'All Models' #st.selectbox("Choose Model (or select ALL):", ['All Models'] + model_names)


    col1, col2, col3 = st.columns(3)

    with col1:
        state_codes = [
        "HI", "SD", "GU", "AZ", "GA", "PR", "AS", "MO", "OK", "Unit", "VI", "OR", "MN", "IL", 
        "FL", "AK", "IN", "ID", "USNS", "MS", "UT", "TX", "NM", "USNV", "WI", "PA", "IA", "NY", 
        "MD", "USS", "NV", "ND", "CA", "FM", "AR", "MI", "WV", "WY", "RI", "Box", "TN", "CO", 
        "AL", "KS", "DE", "NH"]
        state_code = st.selectbox("State Code", state_codes)
        total_sales = st.number_input("Total Sales", min_value=0.0, value=100.0)
        return_days = st.number_input("Return Days", min_value=0, value=5)
        shipping_month = st.slider("Shipping Month", 1, 12, 1)

    with col2:
        status = st.selectbox("Order Status", ['shipped', 'delivered', 'processing','pending','cancelled'])
        quantity = st.number_input("Quantity", min_value=1, value=1)

    with col3:
        carrier = st.selectbox("Carrier", ['UPS', 'FedEx', 'DHL'])
        payment_method = st.selectbox("Payment Method", ['credit_card', 'paypal', 'bank_transfer'])
        is_active = st.selectbox("Is Active Discount?", [True, False])
        percentage = st.slider("Discount Percentage", 0, 100, 0)


    if st.button("Predict Return Status"):
        try:
            input_dict = {
                'state_code': encoders['state_code'].transform([state_code])[0],
                'carrier': encoders['carrier'].transform([carrier])[0],
                'status': encoders['status'].transform([status])[0],
                'payment_method': encoders['payment_method'].transform([payment_method])[0],
                'total_sales': total_sales,
                'quantity': quantity,
                'is_active': is_active,
                'percentage': percentage,
                'return_days': return_days,
                'shipping_month': shipping_month
            }

            input_df = pd.DataFrame([input_dict])
            input_scaled = scaler.transform(input_df)
            return_status_labels = {0:'Approved', 1:'Completed', 2:'Pending', 3:'Rejected'}

            if selected_model == 'All Models':
                predictions = []
                model_votes = {}

                for name in model_names:
                    model = load_model(name)
                    if name == 'Decision_tree':
                        pred = model.predict(input_df)[0]
                    else:
                        pred = model.predict(input_scaled)[0]

                    predictions.append(pred)
                    model_votes[name] = pred

                vote_counts = Counter(predictions)
                total_votes = len(predictions)
                colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#d62728']
                cols = st.columns(len(model_names)) 

              #  st.markdown("## 🔍 Model Results")

                # for idx, (model_name, pred) in enumerate(model_votes.items()):
                #     percent = (vote_counts[pred] / total_votes) * 100
                #     label = return_status_labels[pred]

                #     with cols[idx]:
                #         st.markdown(
                #             f"""
                #             <div style="
                #                 padding: 8px 12px;
                #                 border-radius: 12px;
                #                 background: linear-gradient(135deg, #e0f7fa, #ffffff);
                #                 box-shadow: 0 2px 5px rgba(0,0,0,0.08);
                #                 border: 1px solid #b2ebf2;
                #                 display: flex;
                #                 align-items: center;
                #                 justify-content: space-between;
                #                 min-height: 60px;
                #                 ">
                #                 <span style="color:{colors[idx % len(colors)]}; font-weight: 600; font-size: 18px;">🔹 {model_name}</span>
                #                 <span style="color:#00796b; font-weight: bold; font-size: 16px;">{label}</span>
                #             </div>
                #             """,
                #             unsafe_allow_html=True
                #         )

                most_common = vote_counts.most_common(1)[0][0]
                final_label = return_status_labels[most_common]

              #  st.markdown("---")

                st.markdown(
                    f"""
                    <div style="
                        background-color: #d4edda;
                        color: #155724;
                        padding: 15px 25px;
                        border-radius: 12px;
                        border: 1px solid #c3e6cb;
                        box-shadow: 0 4px 8px rgba(21, 87, 36, 0.2);
                        font-size: 30px;
                        font-weight: 800;
                        text-align: center;
                        max-width: 500px;
                        margin: 15px auto;
                    ">
                        🏆 Final Decision : <span style="color:#0b6623;">{final_label}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            else:
                model = load_model(selected_model)
                if selected_model == 'Decision_tree':
                    prediction = model.predict(input_df)[0]
                else:
                    prediction = model.predict(input_scaled)[0]

                st.markdown(
                    f"""
                    <div style="
                        background-color: #cce5ff;
                        color: #004085;
                        padding: 15px 25px;
                        border-radius: 30px;
                        border: 1px solid #b8daff;
                        box-shadow: 0 4px 8px rgba(0, 72, 133, 0.2);
                        font-size: 30px;
                        font-weight: 800;
                        text-align: center;
                        max-width: 550px;
                        margin: 20px auto;
                    ">
                        {selected_model} Prediction: <span style='color:#9467bd;'>{return_status_labels[prediction]}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        except Exception as e:
            st.error(f"❌ Error: {str(e)}")