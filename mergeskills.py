import csv
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from word2vec_similarskills.allskills import unique_skills

# Load your Word2Vec model
model = Word2Vec.load('word2vec2.model')

# Define the threshold value
threshold = 0.8

skills_list_ = unique_skills
# skills_list_ = ['html','java']
# Create a dictionary to store merged groups
merged_groups = {}

# Define a threshold for merging
merge_threshold = 0.9


# Function to group similar skills
def group_similar_skills(input_skill):
    similar_skills = []
    input_vector = model.wv[input_skill]
    for skill in model.wv.key_to_index:
        similarity = cosine_similarity([input_vector], [model.wv[skill]])[0][0]
        if similarity > threshold:
            similar_skills.append(skill)
    return similar_skills


# Function to merge similar skills groups
def merge_similar_groups(skill, similar_skills):
    for group, skills in merged_groups.items():
        group_similarity = cosine_similarity([model.wv[skill]], [model.wv[skills[0]]])[0][0]
        if group_similarity > merge_threshold:
            merged_groups[group].extend(similar_skills)
            return
    # If no suitable group is found, create a new group
    merged_groups[skill] = similar_skills


for input_skill in skills_list_:
    similar_skills = group_similar_skills(input_skill)
    merge_similar_groups(input_skill, similar_skills)

print(merged_groups)

# file_name = 'merged_skills-v3.csv'

# Writing to CSV
# with open(file_name, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     for key, value in merged_groups.items():
#         writer.writerow([key] + value)
# print('written.')
