import csv
from gensim.models import Word2Vec
from alljobs import unique_jobTitles

similar_jobs_dict = {}

model = Word2Vec.load('jobs.model')

for pos, job in enumerate(unique_jobTitles):
    sim_jobs = model.wv.most_similar(job, topn=10)
    similar_jobs = [(s, score) for s, score in sim_jobs]
    similar_jobs_dict[job] = similar_jobs

# Write to CSV
with open('similar_jobs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    header_row = ['jobTitle']
    for _ in range(10):
        header_row.extend(['Similar Jobs', 'Score'])
    writer.writerow(header_row)

    for job, similar_jobs in similar_jobs_dict.items():
        row = [job]
        for sim_jobs, score in similar_jobs:
            row.extend([sim_jobs, score])
        writer.writerow(row)
print('result saved')
