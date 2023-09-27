import json
from itertools import chain
# import timeit
with open('skills.json', 'r') as file:
    data = json.load(file)

skills_list = data


def clean_string(s):
    return s.replace('.', '').replace('(', '').replace(')', '').replace('-', ' ').replace(',', ' ').replace('-', ' ').replace('   ', ' ')


# Apply the function to each element in the nested lists
cleaned_skills_list = [[clean_string(skill) for skill in sub_list] for sub_list in skills_list]

flat_skills_li = list(chain.from_iterable(cleaned_skills_list))

flat_skills_list = flat_skills_li
unique_skills = []
for allflat in flat_skills_list:
    if allflat not in unique_skills:
        unique_skills.append(allflat)
# for pos, skill in enumerate(flat_skills_list):
#     print(pos, skill)
# print(len(flat_skills_list))
print(len(unique_skills))


# with open('jobs.json', 'r') as file2:
#     jobs = json.load(file2)
#
# print(len(jobs))
