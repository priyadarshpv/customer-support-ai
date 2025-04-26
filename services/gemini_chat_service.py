import google.generativeai as genai

class GeminiChatService:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text.strip()

