from openai import OpenAI
import streamlit as st
import fitz
from docx import Document
import os
import tempfile

openai_api_key =  st.secrets["openai_api_key"]

st.title("🦜🔗 Code Generation Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []
    st.session_state["document_content"] = ""
    st.session_state["previous_assistant_message"] = ""

def reset_session():
    st.session_state["messages"] = []
    st.session_state["document_content"] = ""
    st.session_state["previous_assistant_message"] = ""

if st.session_state["document_content"] == "":
    st.info("Upload a document to start the conversation.")
else:
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

execute_document_upload = st.session_state["document_content"] == ""

if execute_document_upload:
    # static_prompt = "Generate Python code based on the extracted text from the document: "
    static_prompt = "Generate a complete Python code, including proper imports, functions, docstrings, and comments, based on the given specifications. Display it in a pythonic form inside a code block: "

    uploaded_file = st.file_uploader("Upload a PDF or DOC document", type=["pdf", "doc", "docx"])

    if uploaded_file is not None:
        content = ""
        file_type = uploaded_file.name.split(".")[-1].lower()

        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        if file_type == "pdf":
            pdf_document = fitz.open(temp_file_path)
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                content += page.get_text()
        elif file_type in ["doc", "docx"]:
            doc = Document(temp_file_path)
            for paragraph in doc.paragraphs:
                content += paragraph.text

        os.remove(temp_file_path)

        st.session_state["document_content"] = content

        user_input = f"{static_prompt}{content}"

        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        new_message = response.choices[0].message.content

        st.session_state.messages.append({"role": "assistant", "content": new_message})
        st.chat_message("assistant").write(new_message)

# Text box for follow-up questions at the bottom of the page
follow_up_question = st.text_input("Ask a new question or follow-up question")

if follow_up_question:
    st.session_state.messages.append({"role": "user", "content": follow_up_question})
    st.chat_message("user").write(follow_up_question)

    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    new_message = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": new_message})
    st.chat_message("assistant").write(new_message)
