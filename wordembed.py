from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from word2vec_similarskills.allskills import flat_skills_list
# Load your Word2Vec model
model = Word2Vec.load('word2vec2.model')

# Define the threshold value
threshold = 0.8

skills_list_ = flat_skills_list[:10]

# Function to group similar skills
def group_similar_skills(input_skill):
    similar_skills = []
    input_vector = model.wv[input_skill]
    for skill in model.wv.key_to_index:
        similarity = cosine_similarity([input_vector], [model.wv[skill]])[0][0]
        if similarity > threshold:
            similar_skills.append(skill)
    return similar_skills


# Example usage
for input_skill in skills_list_:
    similar_skills = group_similar_skills(input_skill)
    # print(input_skill)
    print(f'input skill :{input_skill} simiarskills group :{similar_skills}')

