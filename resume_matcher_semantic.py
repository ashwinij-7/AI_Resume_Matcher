import os
from sentence_transformers import SentenceTransformer, util
from utils import extract_text_from_pdf, extract_text_from_docx

# Load a pre-trained sentence embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_resume(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type: must be .pdf or .docx")

def calculate_similarity(resume_text, jd_text):
    # Encode both texts into embeddings
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)

    # Compute cosine similarity using semantic embeddings
    similarity_score = util.cos_sim(resume_embedding, jd_embedding).item()

    # Convert to percentage
    return round(similarity_score * 100, 2)