from sentence_transformers import SentenceTransformer, util
import torch
model_name = 'paraphrase-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

skills = ['python', 'django', 'flask', 'natural language processing', 'scikit learn', 'python django', 'machine learning', 'cyberark', 'computer vision', 'linux administration', 'deep learning']

skill_embeddings = model.encode(skills, convert_to_tensor=True)


def find_similar_skills(input_skill, skills, model, top_k=5):

    input_embedding = model.encode(input_skill, convert_to_tensor=True)

    # Calculate cosine similarity
    cos_scores = util.pytorch_cos_sim(input_embedding, skill_embeddings)[0]

    # Get top-k similar skills
    top_results = torch.topk(cos_scores, k=top_k)

    similar_skills = [(skills[i], cos_scores[i].item()) for i in top_results.indices]
    return similar_skills


input_skill = 'Data analysis with Python'
similar_skills = find_similar_skills(input_skill, skills, model)

for skill, score in similar_skills:
    print(f'input skill: ({input_skill}) | Similar skill: ({skill}) | Similarity Score: ({score})')
