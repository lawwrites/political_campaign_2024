#Load in libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 
from datetime import datetime
from collections import Counter
import re
from wordcloud import WordCloud, STOPWORDS
import spacy
from spacy.matcher import Matcher #will use to train the model off patterns
from spacy.pipeline import EntityRuler
from random import choice


def print_docstring(func):
    def wrapper(*args, **kwargs):
        return func(func, *args, **kwargs)
    return wrapper


def load_data(file='data/fuel-econ.csv'):
   df = pd.read_csv(file)
   
   return df
   
 
@print_docstring   