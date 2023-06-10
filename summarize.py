import openai
import os 

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

class GPTSummarizer():
    def get_completion(prompt, task, temperature=0, model="gpt-3.5-turbo"):
        if task == "summary":
            prompt = f"Summarize the following text in a concise manner and with no repetition '{prompt}'"
        elif task == "prompt":
            pass

        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature, # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"], response.usage["total_tokens"]

