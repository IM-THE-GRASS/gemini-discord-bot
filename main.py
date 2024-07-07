import google.generativeai as genai
import json
config_file = open("config.json")
config = json.loads(config_file.read())
config_file.close
api_key = config["api_key"]
model =config["model"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model)
class gemini:
    def __init__(self):
        pass
    def generate(self, prompt):
        response = model.generate_content(str(prompt))
        return response.text
ai = gemini()
print(ai.generate("hi"))
