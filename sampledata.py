import csv
from itertools import chain
from sentence_transformers import SentenceTransformer, util
from gensim.models import Word2Vec
from allskills import unique_skills
from alljobs import unique_jobTitles
from timeit import timeit
model = SentenceTransformer('all-mpnet-base-v2')
vec_model = Word2Vec.load('word2vec.model')

skills_list = unique_skills

start = timeit()
def get_most_similar_skill(input_skill, skills_list, threshold):
    input_embedding = model.encode(input_skill, convert_to_tensor=True)

    most_similar_skills = []
    for skill in skills_list:
        skill_embedding = model.encode(skill, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(input_embedding, skill_embedding)[0][0].item()

        if similarity >= threshold:
            most_similar_skills.append((skill, similarity))

    return most_similar_skills


threshold = 0.7
total_skills = []
tp = []
matched = []
input_skills = ['data scientist']  # "data scientist", "senior software developer", "devops admin"
for input_skill in input_skills:
    similar_skills = get_most_similar_skill(input_skill, skills_list, threshold)
    print(similar_skills)

    for key_skill, _ in similar_skills:
        required_skills = vec_model.wv.most_similar(key_skill,topn=10)
        total_skills.extend([sk for sk, _ in required_skills])
    print(total_skills)
    top_skills = [[input_skill]]+[total_skills]
    print(top_skills)
    tp = list(chain.from_iterable(top_skills))
    matched.append(tp)

with open('requiredSkills.csv1','a',newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['job title', 'matched skills'])

    writer.writerows(matched)
end = timeit()
print('data written.')
print(end-start)
