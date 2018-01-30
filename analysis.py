from textblob import TextBlob
from googletrans import Translator
import time
import sys

a = sys.argv[1]

translator = Translator()

engString = translator.translate(a,src='ko')
engString = engString.text
analysis = TextBlob(engString)
posneg = analysis.sentiment.polarity

if posneg >= 0:
    print("POSITIVE")
elif posneg < 0:
    print("NEGATIVE")
