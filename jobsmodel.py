from gensim.models import Word2Vec
from cleanedjobslist import cleaned_jobs_list

tokenized_corpus = cleaned_jobs_list


model = Word2Vec(sentences=tokenized_corpus,
                 vector_size=300,
                 window=6,
                 min_count=1,
                 sg=1,
                 negative=1,
                 epochs=5,
                 workers=4)


# # similar_words = model.wv.most_similar('python')
#
# print(similar_words)

model.save("jobs.model")

print('model build')
