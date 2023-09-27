from itertools import chain
from stopremove import cleaned_skills_list

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
