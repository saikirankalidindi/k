from gensim.models import Word2Vec
from data import skills_list
print('getting data from skills list')
# Prepare your tokenized corpus
tokenized_corpus = skills_list
print('model is training.....')
# Initialize and train the Word2Vec model with different parameters
model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=150,   # Trying a smaller vector size
    window=6,          # Further adjust window size
    min_count=15,      # Another min_count value
    sg=1,              # Skip-gram model
    epochs=200,        # Even more epochs
    workers=4
)

# Save the third round of fine-tuned model
model.save("word2vec.model")


