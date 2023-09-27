from pymongo import MongoClient

# MongoDB's connection information
mongodb_url = "mongodb://appuseradmindu:ci0cconr[nNowU*yagVo!heug3@192.168.1.107:27027/"
database_name = "resumes"
collection_name = "coarthatechnosolutionsIN"

# Connect to the MongoDB database with authentication
client = MongoClient(mongodb_url)
db = client[database_name]
collection = db[collection_name]

# Find documents with non-empty "skills" arrays
documents_with_jobTitles = collection.aggregate([{'$match': {'resume.professionalExperience.jobTitle.text': {'$exists': 'true', '$ne': ''}}}, {'$project': {'_id': 0, 'resume.professionalExperience.jobTitle.text': 1}}, {'$project': {'jobTitles': {'$map': {'input': '$resume.professionalExperience.jobTitle.text', 'as': 'title', 'in': {'$toLower': '$$title'}}}}}])

# Initialize a list to store skills
jobs_list = []
for skills_ in documents_with_jobTitles:

    jobs_list.append(dict(skills_)['jobTitles'])

print(len(jobs_list))

# import json
#
# with open('jobs.json', 'w') as file:
#     json.dump(jobs_list, file)
#
# print('data')