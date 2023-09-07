from gensim.models import Word2Vec

from allskills import flat_skills_list

similar_skills_dict = {}

model = Word2Vec.load('word2vec2.model')

for pos, skill in enumerate(flat_skills_list):

    sim_skills = model.wv.most_similar(skill, topn=10)

    similar_skills = [skill+f'({_})' for skill, _ in sim_skills]

    similar_skills_dict[skill] = similar_skills

print(similar_skills_dict)
