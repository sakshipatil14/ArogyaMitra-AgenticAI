from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("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"))

def aromi_chat(message):

    prompt = f"""
    You are AROMI, an AI fitness and wellness coach.

    Help users with:
    - workout advice
    - travel fitness tips
    - motivation
    - healthy habits

    User message: {message}
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content