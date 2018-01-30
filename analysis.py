from textblob import TextBlob
from googletrans import Translator

translator = Translator()
a = "오픈소스를 활용한 간단한 감성분석 엔진입니다."
print(a)
engString = translator.translate(a)
engString = engString.text
print(engString)
analysis = TextBlob(engString)
print(analysis.sentiment.polarity)
if analysis.sentiment.polarity >= 0:
    print("분석결과 : 긍정 POSITIVE")
elif analysis.sentiment.polarity < 0:
    print("분석 결과 : 부정 NEGATIVE")
