import os
import json
from PIL import Image

import google.generativeai as genai

# working directory path
working_dir = os.path.dirname(os.path.abspath(__file__))

# path of config_data file
config_file_path = os.path.join(working_dir, "config.json")

# loading the GOOGLE_API_KEY
if os.path.exists(config_file_path):
    with open(config_file_path, "r") as f:
        config_data = json.load(f)
    GOOGLE_API_KEY = config_data.get("GOOGLE_API_KEY", "")
else:
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")

# configuring google.generativeai with API key
genai.configure(api_key=GOOGLE_API_KEY)


def load_gemini_pro_model(model_name="gemini-3.6-flash"):
    gemini_model = genai.GenerativeModel(model_name)
    return gemini_model


# get response from Gemini multimodal model - image/text to text
def gemini_pro_vision_response(prompt, image, model_name="gemini-3.6-flash"):
    gemini_vision_model = genai.GenerativeModel(model_name)
    response = gemini_vision_model.generate_content([prompt, image])
    result = response.text
    return result


# get response from embeddings model - text to embeddings
def embeddings_model_response(input_text):
    embedding_model = "models/gemini-embedding-001"
    embedding = genai.embed_content(model=embedding_model,
                                    content=input_text,
                                    task_type="retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding_list


# get response from Gemini model - text to text
def gemini_pro_response(user_prompt, model_name="gemini-3.6-flash"):
    gemini_model = genai.GenerativeModel(model_name)
    response = gemini_model.generate_content(user_prompt)
    result = response.text
    return result
