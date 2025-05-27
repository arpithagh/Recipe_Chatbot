#!/usr/bin/env python
# coding: utf-8

# ---------------------------------------
# 🍽️ Recipe Chat Bot using Gradio + Groq
# ---------------------------------------

# 🔧 Install dependencies (run in terminal, not in script):
# pip install gradio groq python-dotenv

# 📦 Import packages
import gradio as gr
from groq import Groq
from dotenv import load_dotenv
import os

# 🔐 Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 📌 Initialize system prompt
def initialize_messages():
    return [{
        "role": "system",
        "content": (
            "You are a friendly and knowledgeable recipe expert who helps people cook delicious meals. "
            "You understand a wide range of cuisines — including Indian, Italian, Chinese, and continental dishes. "
            "Your role is to suggest recipes based on ingredients, dietary needs, or cuisine preferences. "
            "You offer clear, step-by-step instructions, cooking tips, and alternatives for missing ingredients. "
            "Respond in an engaging, easy-to-understand manner suitable for beginners and food enthusiasts alike."
        )
    }]

# 🎯 Chat message history
messages_prmt = initialize_messages()

# 🤖 Chatbot logic
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )

    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply

# 💬 Gradio UI setup
iface = gr.ChatInterface(
    customLLMBot,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me for a recipe or suggest based on ingredients"),
    title="🍽️ Recipe ChatBot",
    description="Your friendly cooking assistant! Ask for recipes, cooking tips, or suggestions based on ingredients.",
    theme="soft",
    examples=[
        "I have rice, carrots, and peas",
        "How do I make butter chicken?",
        "Suggest a vegan dinner",
        "What can I cook in 15 minutes?"
    ],
    submit_btn=True
)

# 🚀 Launch the app
iface.launch(share=True)
