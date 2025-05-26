import streamlit as st
import streamlit.components.v1 as components

# st.set_page_config(page_title="Dashboard Viewer", layout="wide")

def run_dashboard_viewer():
    st.title("📊 Dashboard")
    st.markdown("---")

    # dashboard link
    dashboard_url = "https://app.powerbi.com/view?r=eyJrIjoiMjI5Y2ExYjItMjJlYS00MWUyLWFjNTUtYzMwYzY3MjM1YWZjIiwidCI6IjIxNzY5YTc2LTgxZTItNDcyNS1hODkzLWQ0MDQ5YjFhMDRlZSJ9"
   # Show dashboard
    components.iframe(src=dashboard_url, height=650, scrolling=True)

