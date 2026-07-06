from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
LINE_CHANNEL_ACCESS_TOKEN=os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
LINE_USER_ID=os.getenv("LINE_USER_ID")
