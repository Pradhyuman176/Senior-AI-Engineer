import re

def extract_topic(review: str) -> str:
    review = review.lower()

    rules = {
        "delivery partner rude": [
            "rude", "impolite", "behaved badly", "shouted"
        ],
        "delivery issue": [
            "late", "delay", "not delivered", "delivery issue"
        ],
        "food stale": [
            "stale", "cold food", "bad taste"
        ],
        "maps not working properly": [
            "map", "location", "tracking", "gps"
        ],
        "instamart open all night": [
            "instamart", "open all night", "24 hours"
        ],
        "bring back 10 minute bolt delivery": [
            "10 minute", "bolt delivery"
        ],
        "app crash": [
            "crash", "stuck", "not opening"
        ]
    }

    for topic, keywords in rules.items():
        for kw in keywords:
            if kw in review:
                return topic

    return "general feedback"
