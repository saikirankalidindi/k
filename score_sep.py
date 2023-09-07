import csv
from gensim.models import Word2Vec
from allskills import flat_skills_list

similar_skills_dict = {}

model = Word2Vec.load('word2vec2.model')

for pos, skill in enumerate(flat_skills_list):
    sim_skills = model.wv.most_similar(skill, topn=10)
    similar_skills = [(s, score) for s, score in sim_skills]
    similar_skills_dict[skill] = similar_skills

# Write to CSV
with open('similar_skills.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    header_row = ['Skill']
    for _ in range(10):
        header_row.extend(['Similar Skill', 'Score'])
    writer.writerow(header_row)

    for skill, similar_skills in similar_skills_dict.items():
        row = [skill]
        for sim_skill, score in similar_skills:
            row.extend([sim_skill, score])
        writer.writerow(row)
