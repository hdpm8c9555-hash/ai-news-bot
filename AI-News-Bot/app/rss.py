import feedparser

RSS='https://news.google.com/rss/search?q=artificial+intelligence'

def get_news(limit=5):
    feed=feedparser.parse(RSS)
    return [{"title":e.title,"link":e.link} for e in feed.entries[:limit]]
