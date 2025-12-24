import json
from review_agent import extract_topic
from topic_store import TopicStore
from trend_engine import build_trend

# Load data
with open("data/reviews.json", "r") as f:
    reviews_by_date = json.load(f)

topic_store = TopicStore()
topics_by_date = {}

for date, reviews in reviews_by_date.items():
    topics_by_date[date] = []

    for review in reviews:
        raw_topic = extract_topic(review)
        final_topic = topic_store.add_or_merge(raw_topic)
        topics_by_date[date].append(final_topic)

trend_df = build_trend(topics_by_date)

trend_df.to_csv("output/trend_report.csv")
print(trend_df)
