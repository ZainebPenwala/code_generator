from openai import OpenAI
import streamlit as st
import fitz  # PyMuPDF for PDF extraction
from docx import Document  # python-docx for DOC extraction
import os
import tempfile

openai_api_key = ''

st.title("💬 Code Generation Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    st.session_state["document_content"] = ""

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

execute_document_upload = True  # Flag to determine whether to execute document upload section

if execute_document_upload:
    static_prompt = "Generate Python code based on the extracted text from the document: "
    st.write(static_prompt)

    uploaded_file = st.file_uploader("Upload a PDF or DOC document", type=["pdf", "doc", "docx"])

    if uploaded_file is not None:
        content = ""
        file_type = uploaded_file.name.split(".")[-1].lower()

        # Save the uploaded file to a temporary file
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

        # Remove the temporary file
        os.remove(temp_file_path)

        st.session_state["document_content"] = content

        user_input = f"{static_prompt}{content}"

        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

# Allow the user to provide additional input without document upload
if prompt := st.chat_input():
    # Only include the latest user input and the latest assistant response
    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages = [{"role": "user", "content": prompt}]  # Clear previous messages

    if st.session_state["document_content"]:
        st.session_state.messages[0]["content"] = prompt
        st.chat_message("user").write(st.session_state.messages[0]["content"])

    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
