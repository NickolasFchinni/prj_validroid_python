from dotenv import load_dotenv, dotenv_values 
import os
import requests

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def perguntar_ao_gemini(question):
  url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
  headers = {"Content-Type": "application/json"}
  body = {"contents": [{"parts": [{"text": question}]}]}

  print("Fazendo requisição para o Gemini responder a pergunta.")  

  response = requests.post(url, headers=headers, json=body)

  if response.status_code != 200:
    print("Erro ao consultar API do GEMINI, verifique se a chave da API no arquivo .env está correta.")

  return response.json()["candidates"][0]["content"]["parts"][0]["text"]

if __name__ == "__main__":
  print("Abrindo log da build do App.")
  with open("build_log.txt", "r") as log:
    logs = log.read()

  prompt_gemini = f"Esses são os últimos logs da buld mobile: \n{logs}\n Me diga o motivo do erro e como corrigir."

  resposta_gemini = perguntar_ao_gemini(prompt_gemini)

  print("Gerando arquivo com a resposta do Gemini.")
  with open("gemini_output.txt", "w") as out:
    out.write(resposta_gemini)

  print("Sugestão do Gemini gerada!")