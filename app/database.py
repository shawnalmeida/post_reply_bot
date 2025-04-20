from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["social_replies"]
collection = db["replies"]

def save_to_db(platform: str, post_text: str, generated_reply: str):
    collection.insert_one({
        "platform": platform,
        "post_text": post_text,
        "generated_reply": generated_reply,
        "timestamp": datetime.utcnow()
    })