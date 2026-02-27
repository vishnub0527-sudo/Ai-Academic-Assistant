from litellm import completion
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "groq/llama-3.1-8b-instant"

def generate_answer(context, question):

    response = completion(
        model=MODEL_NAME,
        api_key=os.getenv("GROQ_API_KEY"),   # 🔥 IMPORTANT
        messages=[
            {"role": "system", "content": f"Use the following context:\n{context}"},
            {"role": "user", "content": question}
        ],
        max_tokens=500,
    )

    return response["choices"][0]["message"]["content"]