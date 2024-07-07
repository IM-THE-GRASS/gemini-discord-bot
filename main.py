import google.generativeai as genai
API_KEY = "INPUT YOUR API KEY HERE"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("who are you?")
print(response.text)