from gensim.models import Word2Vec

model = Word2Vec.load('word2vec.model')

sim_skills = model.wv.most_similar('java',topn=5)

similar_skills = [skill for skill, _ in sim_skills]

print(similar_skills)




