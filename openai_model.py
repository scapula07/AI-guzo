import os
from dotenv import load_dotenv

#   import KeyBERT and OpenAI
import openai
from keybert import KeyLLM
from keybert.llm import OpenAI

#   get API key
load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

#   create the LLM
openai_client = openai.OpenAI(api_key=openai_key)
llm = OpenAI(openai_client)


# input('enter what you need to help your business')

#   load in KeyLLM
keyword_extractor = KeyLLM(llm)

def keywords(input_text):
    keywords = keyword_extractor.extract_keywords(input_text)
    print(keywords)