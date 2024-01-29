#   imports
import numpy as np
import pandas as pd
from os import path
import sys
from flask import Flask

#   import NLP
import yake
yake_extractor = yake.KeywordExtractor()

def keywords(input_text):
    if len(input_text) > 240:
        result = "Input too long, please try again"
    else:
        keywords = yake_extractor.extract_keywords(input_text)

        # keywords_df = pd.DataFrame(keywords, columns=['term', 'score'])
        # keywords_df = keywords_df.sort_values(by='score') # The lower the score the more relevant the keyword is
        # result = keywords_df[0][0:5]

        result = keywords
    return result