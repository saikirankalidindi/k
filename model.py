from gensim.models import Word2Vec
from data import skills_list
from stopremove import cleaned_skills_list

print('loading dataset')
tokenized_corpus = cleaned_skills_list

print('training the model......')

model = Word2Vec(sentences=tokenized_corpus,
                 vector_size=300,
                 window=6,
                 min_count=1,
                 sg=1,
                 negative=1,
                 epochs=5,
                 workers=4)


similar_words = model.wv.most_similar('python')

print(similar_words)

model.save("word2vec2.model")
