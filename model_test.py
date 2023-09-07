from gensim.models import Word2Vec

model = Word2Vec.load('word2vec2.model')

sim_skills = model.wv.most_similar('python', topn=10)
similar_skills = []
# similar_skills = [skill for skill, _ in sim_skills]
for skills_tuple in sim_skills:
    skill = skills_tuple[0]
    score = str(skills_tuple[1])
    skills_ = skill+'|'+score
    similar_skills.append(skills_)
print(similar_skills)




