from app.rss import get_news
from app.openai_service import summarize
from app.line_service import push

msg="🤖 AI Daily News\n\n"

for n in get_news(3):
    msg+=f"📰 {n['title']}\n"
    msg+=summarize(n['title'])
    msg+="\n\n"

push(msg)
print(msg)
