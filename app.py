### Health Management APP
from dotenv import load_dotenv

load_dotenv() ## load all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))





## Function to load Goofle Gemini Pro Vision Api and get response

def get_gemini_response(input,image,prompt):
    model=genai.GenerativeModel('gemini-1.5-pro')
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # check if a file has been uploaded
    if uploaded_file is not None:
        # read the files into bytes
        bytes_data=uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type": uploaded_file.type, #Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
##initialize our streamlit app   

input_prompt="""
You are an expert in nutritionist where you need to see the food from the image
               and calculate the total calories, also provide the etails of every food items with calories
               is below format
               
               1. Item1- no of calories
               2. Item2- no of calories
               ----
               ----

"""

st.set_page_config(page_title="AI Nutritionist App")

st.header("AI Nutritionist App")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file=st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded image.",use_column_width=True)


submit=st.button("Tell me the total calories")

  ## If Submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)



    
