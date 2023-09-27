from sentence_transformers import SentenceTransformer, util
import numpy as np
from stopremove import cleaned_skills_list
from itertools import chain
from allskills import unique_skills

jobs_dict = {}
# Step 3: Load Pre-trained SBERT Model
model = SentenceTransformer('all-MiniLM-L6-v2')

job_titles = cleaned_skills_list
encoded_titles = np.array([model.encode(' '.join(title)) for title in job_titles])


# Step 5: Define Similarity Function
def get_similar_titles(input_title, encoded_titles, top_k=5):
    input_vector = model.encode(input_title)
    similarity_scores = util.pytorch_cos_sim(input_vector, encoded_titles)[0]
    similar_indices = similarity_scores.argsort()[-top_k-1:-1]
    similar_titles = [job_titles[i] for i in similar_indices]
    return similar_titles


for aJobTitle in unique_skills[:10]:
    # Step 6: Use the Function
    input_title = aJobTitle
    similar_titles = get_similar_titles(input_title, encoded_titles)

    # Remove duplicates using set and convert it back to a list
    similar_titles = list(set(chain.from_iterable(similar_titles)))

    jobs_dict[input_title] = similar_titles


print(jobs_dict)


