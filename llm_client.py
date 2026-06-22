from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client=Groq()

def generate_response(prompt:str):
    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        response_format={"type": "json_object"},
        messages=[
            {
                "role":"user",
                "content": prompt
        }]
    )
    return response.choices[0].message.content