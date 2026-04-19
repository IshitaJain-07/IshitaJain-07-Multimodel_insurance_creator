
# my_pages/chat.py
import streamlit as st
from llm import generate_text


def render():
    st.header("AI Expert Chat")
    st.markdown("Ask anything about insurance — policies, claims, coverage, premiums, exclusions, real-life scenarios...")

    # Initialize messages if not present
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {"role": "assistant", "content": "Hi! I'm your insurance expert. How can I help you today?"}
        ]

    # Display chat history
    for message in st.session_state.chat_messages:
        avatar = "🤖" if message["role"] == "assistant" else "👤"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Ask your insurance question..."):
        # Add user message immediately
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        
        # Show user message right away
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # You can improve the system prompt here
                    full_prompt = (
                        "You are a knowledgeable, friendly insurance expert.\n"
                        "Answer clearly, accurately, in simple language.\n"
                        "Use bullet points or short paragraphs when helpful.\n\n"
                        f"User: {prompt}"
                    )
                    response = generate_text(full_prompt)
                except Exception as e:
                    response = f"⚠️ Sorry, I couldn't connect right now.\n({str(e)})"

            st.markdown(response)
            st.session_state.chat_messages.append({"role": "assistant", "content": response})

        # No need for st.rerun() anymore — Streamlit 1.12+ handles this automatically