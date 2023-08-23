from gensim.models import Word2Vec


model = Word2Vec.load('finetunedV1.model')

sim_skills = model.wv.most_similar('documentation', topn=5)

similar_skills = [skill for skill, _ in sim_skills]

print(similar_skills)
