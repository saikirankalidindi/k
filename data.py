from pymongo import MongoClient
from pprint import pprint
# MongoDB's connection information
mongodb_url = "mongodb://appanalystdu:jacetHipw!lsO*wabs1cNodvuc@192.168.1.107:27027/"
database_name = "resumes"
collection_name = "coarthatechnosolutionsIN"

# Connect to the MongoDB database with authentication
client = MongoClient(mongodb_url)
db = client[database_name]
collection = db[collection_name]

# Find documents with non-empty "skills" arrays
documents_with_skills = collection.aggregate([{'$match': {'resume.professionalQualification.skills': { '$exists': 'true', '$ne': [] }}},{'$project': {'_id': 0,'skills': {'$cond': {'if': {'$and': [{ '$isArray': '$resume.professionalQualification.skills.text' },{ '$ne': ['$resume.professionalQualification.skills.text', []] }]},'then': {'$map': {'input': '$resume.professionalQualification.skills.text','as': 'skill','in': { '$toLower': '$$skill' }}},'else': []}}}}])

# Initialize a list to store skills
skills_list = []
for skills_ in documents_with_skills:

    skills_list.append(dict(skills_)['skills'])

import json

with open('skills.json', 'w') as file:
    json.dump(skills_list, file)

print('data')


