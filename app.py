#!/usr/bin/env python
# coding: utf-8

# #Install Packages

# In[9]:


pip install groq


# In[10]:


pip install gradio


# # Import the Packages

# In[11]:


import gradio
from groq import Groq


# In[12]:


client = Groq(
    api_key="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",
)


# #Define a function to give content and role

# In[13]:


def initialize_messages():
    return [{"role": "system",
             "content": "You are a friendly and knowledgeable recipe expert who helps people cook delicious meals. You understand a wide range of cuisines — including Indian, Italian, Chinese, and continental dishes. Your role is to suggest recipes based on ingredients, dietary needs, or cuisine preferences. You offer clear, step-by-step instructions, cooking tips, and alternatives for missing ingredients. Respond in an engaging, easy-to-understand manner suitable for beginners and food enthusiasts alike."}]


# #Assign it to a variable

# In[14]:


messages_prmt = initialize_messages()


# In[15]:


print(type(messages_prmt))


# In[16]:


[{},{}]


# #Define a function to connect with LLM

# In[17]:


def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply


# #Create an object of chat interface class in gradio

# In[18]:


iface = gradio.ChatInterface(customLLMBot,
    chatbot=gradio.Chatbot(height=300),
    textbox=gradio.Textbox(placeholder="Ask me for a recipe or suggest based on ingredients"),
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


# #Call launch function to execute

# In[19]:


iface.launch(share=True)


# In[ ]:




