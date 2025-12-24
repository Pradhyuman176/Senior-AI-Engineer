from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")
SIMILARITY_THRESHOLD = 0.85

class TopicStore:
    def __init__(self):
        self.topics = []

    def add_or_merge(self, topic_name):
        new_embedding = model.encode(topic_name, normalize_embeddings=True)

        for topic in self.topics:
            similarity = cosine_similarity(
                [new_embedding],
                [topic["embedding"]]
            )[0][0]

            if similarity >= SIMILARITY_THRESHOLD:
                return topic["name"]

        self.topics.append({
            "name": topic_name,
            "embedding": new_embedding
        })
        return topic_name
