import streamlit as st
from retriever import load_documents, retrieve_context
from llm_layer import generate_answer

st.set_page_config(
    page_title="RAG AI Chatbot",
    page_icon="🤖",
    layout="centered"
)
st.markdown("""
<style>
    .stChatMessage {
        padding: 10px;
        border-radius: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 RAG AI Assistant")
st.caption("Ask questions from your knowledge base")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box at bottom
if prompt := st.chat_input("Ask something..."):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):

            documents = load_documents()
            context = retrieve_context(prompt, documents)

            answer = generate_answer(context, prompt)

            st.markdown(answer)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )