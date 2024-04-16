from openai import OpenAI 
import streamlit as st 

f  = open(r'C:\Users\alenp\Downloads\Innmoatics\code reviever\openai_key.txt')
key = f.read()
client = OpenAI(api_key = key )


# Streamlit UI
st.title("Python Code Review Tool")

# User input
code = st.text_area("Enter your Python code here:")
system_prompt = "The following Python code has been submitted for review:"

if st.button("Review Code"):


    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": "You are a helpful AI Assistant. Given a Python code snippet, you will review it for potential bugs and suggest fixes."},
            {"role": "user", "content": code}
        ]
    )

    # Display corrected code
    corrected_code = response.choices[0].message.content
    st.markdown("<h3 style='color:green;font-size:20px;'>Review</h3>", unsafe_allow_html=True)
    st.write(response.choices[0].message.content)