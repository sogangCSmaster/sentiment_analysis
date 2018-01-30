from textblob import TextBlob
from googletrans import Translator

translator = Translator()
a = "나는 너가 정말 좋아."
print(a)
b = translator.translate(a)
b = b.text
#The polarity score is a float within the range [-1.0, 1.0].
analysis = TextBlob(b)
print("극성 감성 분석은 [-1.0, 1.0] 사이의 소수 입니다.")
print("극성 감성 분석 결과 : ", analysis.sentiment.polarity)
if analysis.sentiment.polarity < 0:
    print("분석 결과 : 부정")
