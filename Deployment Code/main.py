import streamlit as st
import base64
from streamlit_option_menu import option_menu
from overview import run_overview
from dashboard import run_dashboard_viewer
from sentiment_model import run_sentiment_app
from return_model import run_return_status_app
from ask_data import run_pandasAi


st.set_page_config( page_title="Control page",layout="wide")

# Main App Function
def run_app():
    with st.sidebar:
        st.image("Background/seenn.jpg", width=600)

        selected = option_menu(
            menu_title='App Navigation',
            options=['Overview', 'Dashboard', 'Ask My Data', 'Return Status Prediction', 'Sentiment Classification'],
            icons=['info-circle', 'bar-chart', 'robot', 'box', 'chat-dots'],
            menu_icon='cast',
            default_index=0,
        )




    if selected == 'Return Status Prediction':
        run_return_status_app()
    elif selected == 'Sentiment Classification':
        run_sentiment_app()
    elif selected == 'Dashboard':
        run_dashboard_viewer()
    elif selected == 'Overview':
        run_overview()
    elif selected =='Ask My Data':
        run_pandasAi()
    
    #run background
    set_background("Background/back.jpeg")



    


#background image
def set_background(image_path: str):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        image_base64 = f"data:image/png;base64,{encoded}"

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{image_base64}");
            background-size: cover;
            background-position: center;
        }}
        .content-box {{
            background-color: rgba(255,255,255,0.85);
            padding: 2rem;
            border-radius: 15px;
            margin-top: 2rem;
        }}
        </style>
    """, unsafe_allow_html=True)







# Run the app
if __name__ == '__main__':
    run_app()





#  .venv\Scripts\Activate
#  streamlit run main.py
#  deactivate