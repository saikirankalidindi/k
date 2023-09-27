from mergeskills import merged_groups
from sentence_transformers import SentenceTransformer, util

model_name = 'paraphrase-MiniLM-L6-v2'
model = SentenceTransformer(model_name)
list_skills = []
for group, skills in merged_groups.items():
    list_skills = [group]+skills
# print(list_skills)

    input_skills = list_skills
    encoded_skills = model.encode(input_skills, convert_to_tensor=True)

    similarities = util.pytorch_cos_sim(encoded_skills, encoded_skills)

    for i, skill in enumerate(input_skills):
        similar_skills = [(input_skills[j], similarities[i][j]) for j in range(len(input_skills))]
        for similar_skill, score in similar_skills:
            print(skill, ':', similar_skill, ':', score)
