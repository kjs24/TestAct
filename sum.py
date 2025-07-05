# summarize.py
import os
from openai import OpenAI
from openai import ChatCompletion

def load_input(path="input.txt"):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def call_llm(prompt: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",    # 또는 원하는 모델명
        messages=[{"role": "system", "content": "You are a concise summarizer."},
                  {"role": "user",   "content": prompt}],
        temperature=0.3,
        max_tokens=200
    )
    return response.choices[0].message.content

def save_summary(text: str, path="summary.txt"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    original = load_input()
    summary  = call_llm(original)
    save_summary(summary)
    print(" summary.txt 파일 생성 완료")
