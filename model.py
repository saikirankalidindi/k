from gensim.models import Word2Vec
from data import skills_list

print('loading dataset')
#Prepare your tokenized corpus
tokenized_corpus = skills_list
print('training the model......')
# Initialize and train the Word2Vec model
model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=150,   # Trying a smaller vector size
    window=6,          # Further adjust window size
    min_count=15,      # Another min_count value
    sg=1,              # Skip-gram model
    epochs=200,        # Even more epochs
    workers=4
)

# Get the vector representation of a word
vector = model.wv['word']

# # Find similar words
# similar_words = model.wv.most_similar('python')

# print(similar_words)

# Save the model
model.save("word2vec.model")





