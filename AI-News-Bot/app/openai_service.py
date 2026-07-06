from openai import OpenAI
from app.config import OPENAI_API_KEY

client=OpenAI(api_key=OPENAI_API_KEY)

def summarize(title):
    r=client.responses.create(
        model="gpt-5-mini",
        input=f"請用繁體中文以2句話摘要這則新聞標題：{title}"
    )
    return r.output_text
