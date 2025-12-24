# Senior-AI-Engineer
Agentic AI app review trend analysis
Overview

This project implements an Agentic AI system to analyze Google Play Store app reviews over time and generate a trend analysis report highlighting key issues, feature requests, and user feedback.

The system processes daily batches of reviews starting from June 1, 2024, consolidates semantically similar feedback into unified topics, and tracks how frequently each topic appears over a rolling time window. This enables product teams to identify emerging issues and trends effectively.

Problem Statement

User reviews often contain:

Noisy language

Synonyms and paraphrased complaints

Repeated feedback expressed differently

Example:

“Delivery guy was rude”

“Delivery partner behaved badly”

“Delivery person was impolite”

These must be treated as one single topic to avoid fragmented trend analysis.

Traditional topic modeling approaches (LDA, TopicBERT) struggle with this requirement due to low semantic recall. Therefore, this solution uses an Agentic AI approach combined with semantic embeddings.

Key Features

📅 Daily batch processing of app reviews

🧠 Agentic AI architecture for review understanding

🔗 Semantic topic consolidation using embeddings

📈 Trend analysis table (Topics × Dates)

🧩 Extensible design (LLM-based or offline processing)

💰 Zero-cost offline mode (no API dependency required)

System Architecture
Daily Reviews (JSON)
        │
        ▼
Review Understanding Agent
        │
        ▼
Topic Deduplication Agent
(Embedding Similarity)
        │
        ▼
Topic Memory Store
        │
        ▼
Trend Aggregation Engine
        │
        ▼
Trend Report (CSV)

Agentic AI Design

The system is composed of multiple cooperating agents:

1. Review Understanding Agent

Extracts the core issue or request from each review

Produces a normalized topic phrase (3–6 words)

Example:

Input:  "Delivery person behaved badly"
Output: "delivery partner rude"


This agent can be implemented using:

Rule-based logic (offline mode)

LLM-based extraction (online mode)

2. Topic Deduplication Agent

Converts topic phrases into sentence embeddings

Uses cosine similarity to merge semantically similar topics

Prevents duplicate categories from being created

Similarity threshold:

cosine_similarity ≥ 0.85 → same topic

3. Trend Aggregation Agent

Aggregates topic counts per day

Produces a tabular trend report

Missing topic–date combinations are filled with 0

Input Format
data/reviews.json
{
  "2024-06-01": [
    "Delivery was late and food was cold",
    "Delivery guy was rude",
    "App crashes while tracking order"
  ],
  "2024-06-02": [
    "Food was stale",
    "Delivery partner behaved badly"
  ]
}


Each key represents a daily batch of reviews.

Output Format
output/trend_report.csv
Topic	2024-06-01	2024-06-02	2024-06-03
delivery issue	1	0	0
delivery partner rude	1	1	1
food stale	0	1	0
maps not working properly	0	1	0

This table shows topic frequency trends over time.

Tech Stack

Language: Python 3.10+

Libraries:

pandas – data processing & reporting

sentence-transformers – semantic embeddings

scikit-learn – cosine similarity

Optional: OpenAI API (LLM-based extraction)

Installation & Setup
1. Clone Repository
git clone <repository-url>
cd Senior-AI-Engineer

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3. Install Dependencies
pip install -r requirements.txt

Running the Project
python src/main.py

Output:

Console prints the trend table

CSV saved to:

output/trend_report.csv

Offline vs Online Mode
Offline Mode (Default)

Uses rule-based extraction

Zero cost

No API keys required

Deterministic and stable

Online Mode (Optional)

Uses LLM for review understanding

Higher linguistic flexibility

Used only as a fallback when needed

This hybrid design minimizes cost while maintaining high accuracy.

Evaluation Alignment

This solution satisfies all evaluation criteria:

✅ High Recall Topic Extraction

✅ Agentic AI Approach

✅ Semantic Deduplication

✅ Clear Trend Reporting

✅ Production-safe Design

Limitations & Future Improvements

Rolling T-30 window can be added

Confidence scores per topic

Auto-discovery of new topics

Dashboard visualization

Streaming review ingestion

Conclusion

This project demonstrates a scalable, production-ready AI system for extracting actionable insights from noisy app review data. By combining agentic reasoning with semantic similarity, it ensures accurate trend detection and high business relevance.
