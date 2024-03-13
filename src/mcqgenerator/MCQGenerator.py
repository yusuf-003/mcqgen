import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging

# importing the neccessary packages from langchain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

#Load environment variable from the .env file
load_dotenv()
key = os.getenv("OPEN_API_KEY")

llm = ChatOpenAI(openai_api_key=key,model_name="gpt-3.5-turbo", temperature=0.3)
