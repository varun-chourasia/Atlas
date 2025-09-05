import requests

def ask_ollama(prompt):
    response = requests.post(
        "https://localhost:11434/api.generate",
        json={"model":"llama3.2", "prompt": prompt}
    )

    return response.json()['response']