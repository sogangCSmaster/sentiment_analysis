# sentiment_analysis
sentiment_analysis using textblob

## details
Korean sentiment analysis using textblob

textblob module을 이용한 한국어 감성분석 (used polarity, 극성 탐지 이용)

## dependencies
- python3
  - textblob (pip3 install textblob)
  - googletrans (pip3 install googletrans)

### 설명
코드는 정말 간단합니다. textblob모듈에 있는 sentiment.polarity 객체를 이용하면 극성탐지를 이용한 긍부정이 나옵니다.

다만 영어만 지원이 되기 때문에 googletrans모듈을 이용하여 한국어를 영어로 먼저 번역을 합니다.
