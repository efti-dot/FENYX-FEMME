import streamlit as st
from prompt import OpenAIConfig
import fitz  # PyMuPDF

api_key = "api-key"
openai_config = OpenAIConfig(api_key=api_key)

pdf_content = ""

def extract_text_from_pdf(pdf_path):
    global pdf_content
    with open(pdf_path, "rb") as file:
        pdf_data = file.read()
        doc = fitz.open(stream=pdf_data, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        pdf_content = text

pdf_path = 'D:\Efti\Project\FENYX FEMME\PDF\AI_Women.pdf'

extract_text_from_pdf(pdf_path)

def naive_bar():
    with st.sidebar:
        st.title("FENYX FEMME")
        page = st.selectbox("Select an option", ["Talk with AI Coach", "Dashboard"])
    
    return page

def talk_with_AI():
    st.subheader("Talk with Your Wellness Coach")
    st.write("Share your feelings, symptoms, and energy levels to get personalized wellness suggestions.")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    user_input = st.chat_input("You: ", key="input")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        response = openai_config.get_response(user_input, st.session_state.messages, context=pdf_content)
        
        with st.chat_message("assistant"):
            st.markdown(response)




def dashboard():
    st.subheader("Dashboard")
    st.write("This is where you can view your wellness data and insights.")

    period = st.selectbox("Do you have a regular cycle?", ["No", "Yes"], index=0)
    phase = st.selectbox("Select your current phase", ["Follicular", "Ovulation", "Luteal", "Menstrual"], index=0)
    submit_btn = st.button("Generate FENYX Insight")

    if submit_btn:
        if period == "Yes" and phase:
            insight = openai_config.generate_insight(cycle=period, phase=phase, context=pdf_content)
            st.write("FENYX Insight:", insight)
            st.write("\n\n")
            goal = openai_config.get_goal(cycle=period, phase=phase, context=pdf_content)
            st.write("Goal-Oriented Response:", goal)
            st.write("\n\n")
            food = openai_config.get_food(cycle=period, phase=phase, context=pdf_content)
            st.write("Food Suggestions:", food)
            st.write("\n\n")
            supplement = openai_config.get_supplement(cycle=period, phase=phase, context=pdf_content)
            st.write("Supplement Suggestions:", supplement)
            st.write("\n\n")
        else:
            st.write("Please ensure you have selected your cycle and phase correctly.")



def main():
    page = naive_bar()
    
    if page == "Talk with AI Coach":
        talk_with_AI()
    elif page == "Dashboard":
        dashboard()


main()
