import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Настройки OpenAI
MODEL_NAME = "gpt-3.5-turbo"
MAX_TOKENS = 1000
TEMPERATURE = 0.7