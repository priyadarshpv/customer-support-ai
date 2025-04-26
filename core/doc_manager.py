
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class DocumentManager:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.sections = {}
        self.embeddings = []

    def add_sections(self, doc_name, sections):
        for heading, content in sections.items():
            combined = f"{doc_name} - {heading}: {content}"
            self.sections[heading] = combined
        self.embeddings = self.model.encode(list(self.sections.values()), convert_to_tensor=True)

    def search(self, query, top_k=3):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        similarities = cosine_similarity([query_embedding], self.embeddings)[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        return [list(self.sections.values())[i] for i in top_indices]
