import streamlit as st
from dotenv import load_dotenv
import os

from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

load_dotenv()

# APIキーが読み込まれているかチェック（任意）
if not os.getenv("OPENAI_API_KEY"):
    st.error("⚠️ OPENAI_API_KEY が設定されていません。.envを確認してください。")
else:
    st.title("LangChain × Streamlit チャットアプリ")

    user_input = st.text_input("あなたの質問を入力してください")
    if user_input:
        llm = ChatOpenAI(model="gpt-3.5-turbo")
        memory = ConversationBufferMemory()
        chain = ConversationChain(llm=llm, memory=memory)
        response = chain.run(user_input)
        st.write("AI:", response)
