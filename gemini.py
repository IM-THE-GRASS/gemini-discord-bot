import google.generativeai as genai
import config
api_key = config.get_config("api_key")
model = config.get_config("model")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model)
class gemini:
    def __init__(self):
        pass
    def generate(self, prompt):
        response = model.generate_content(str(prompt))
        return response.text

