from gensim.models import Word2Vec


model = Word2Vec.load('jobs.model')

sim_jobs = model.wv.most_similar('frontend developer', topn=10)

similar_jobs = [job for job, _ in sim_jobs]

# for skill in similar_skills:
#     simi_skill = model.wv.most_similar(skill, topn=10)
#     print(simi_skill)

print(similar_jobs)
