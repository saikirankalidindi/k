from gensim.models import Word2Vec
from allskills import flat_skills_list
model = Word2Vec.load('word2vec2.model')

sim_skills = model.wv.most_similar('data science', topn=10)

similar_skills = [skill for skill, _ in sim_skills]

# for skill in similar_skills:
#     simi_skill = model.wv.most_similar(skill, topn=10)
#     print(simi_skill)

print(similar_skills)

