from sentence_transformers import SentenceTransformer, util
import csv
from word2vec_similarskills.allskills import unique_skills
# Load your SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define the threshold value
threshold = 0.8

skills_list_ = unique_skills[:1]
# skills_list_ = ['html','java']
merged_groups = {}
merge_threshold = 0.9


def get_embedding(skill):
    return model.encode(skill, convert_to_tensor=True)


# Function to group similar skills
def group_similar_skills(input_skill):
    similar_skills = []
    input_embedding = get_embedding(input_skill)
    for skill in unique_skills:  # Assuming unique_skills is your list of all skills
        similarity = util.pytorch_cos_sim(input_embedding, get_embedding(skill))
        if similarity > threshold:
            similar_skills.append(skill)
    return similar_skills


def merge_similar_groups(skill, similar_skills):
    for group, skills in merged_groups.items():
        group_embedding = get_embedding(skills[0])
        skill_embedding = get_embedding(skill)
        group_similarity = util.pytorch_cos_sim(skill_embedding, group_embedding)
        if group_similarity > merge_threshold:
            merged_groups[group].extend(similar_skills)
            return
    # If no suitable group is found, create a new group
    merged_groups[skill] = similar_skills


for input_skill in skills_list_:
    similar_skills = group_similar_skills(input_skill)
    merge_similar_groups(input_skill, similar_skills)

# Writing to CSV
file_name = 'merged_skills-v3.csv'

with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    for key, value in merged_groups.items():
        writer.writerow([key] + value)
print('written.')
