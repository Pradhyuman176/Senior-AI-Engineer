import pandas as pd

def build_trend(topics_by_date):
    all_topics = set()
    for topics in topics_by_date.values():
        all_topics.update(topics)

    dates = sorted(topics_by_date.keys())

    df = pd.DataFrame(
        0,
        index=sorted(list(all_topics)),
        columns=dates
    )

    for date, topics in topics_by_date.items():
        for topic in topics:
            df.loc[topic, date] += 1

    return df
