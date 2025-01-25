from flask.cli import load_dotenv
from pymongo import MongoClient

import os

load_dotenv()  # Load environment variables from .env file

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client['clarity-mentorship']
contacts_collection = db['contacts']
