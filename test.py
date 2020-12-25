from os import environ
from dotenv import load_dotenv

load_dotenv()

json = environ.get("JSON_SORT_KEYS")
print(json)