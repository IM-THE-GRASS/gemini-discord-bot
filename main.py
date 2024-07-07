import google.generativeai as genai
API_KEY = "INPUT YOUR API KEY HERE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("who are you?")
print(response.text)
class ai:
    def __init__(self, model):
        self.model = model
    def generate(self, prompt):
        response = model.generate_content(str(prompt))
        return response.text