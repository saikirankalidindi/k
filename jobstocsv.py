import csv
from sentence_transformers import SentenceTransformer, util
from sbertmodel import jobs_dict

model_name = 'all-mpnet-base-v2'
model = SentenceTransformer(model_name)


skills_dict = jobs_dict

with open('similar_jobs_v3.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(['Skills'])

    for key, value in skills_dict.items():
        encoded_key = model.encode([key], convert_to_tensor=True)
        encoded_value = model.encode(value, convert_to_tensor=True)

        similarities = util.pytorch_cos_sim(encoded_key, encoded_value)

        row_data = [key] + [item for pair in zip(value, similarities[0].tolist()) for item in pair]
        writer.writerow(row_data)

print("Results saved")
