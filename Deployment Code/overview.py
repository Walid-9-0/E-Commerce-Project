import streamlit as st

def run_overview():

    st.title("📄 Project Overview")
    st.markdown("---")
    st.markdown("## 📦 Welcome to the E-commerce Analysis & Prediction App")
    
    st.markdown("""
    This interactive web application is designed to help you **analyze**  data, 
    **predict return orders**, and **understand customer sentiment**. Whether you're a 
    data analyst, a business manager, or just curious, this tool empowers you to gain valuable insights 
    from complex data easily and visually.
    
    ### 🔍 What's Inside This App?
    
    **1. 📈 Dashboard**  
    Visualize business performance metrics through interactive **Power BI dashboards**.  
    Understand trends, KPIs, and customer behavior in one glance.
    
    **2. 🤖 Chat With Data**  
    A smart AI-powered interface to explore your dataset conversationally (feature coming soon).
    
    **3. 🛒 Return Orders Prediction**  
    Use machine learning to predict the return status of new orders based on their attributes.  
    Powered by a **Decision Tree classifier** trained on real data.
    
    **4. 😊 Sentiment Analysis**  
    Analyze **customer reviews** or uploaded files to classify feedback as **Positive** or **Negative**.
    
    ---
    ### 💡 How to Use
    - Navigate between sections using the **tabs above**.
    - Fill in inputs or upload files as needed.
    - View predictions, visualizations, and insights instantly.""")

