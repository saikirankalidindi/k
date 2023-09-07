from itertools import chain
from stopremove import cleaned_skills_list

flat_skills_li = list(chain.from_iterable(cleaned_skills_list))

flat_skills_list = flat_skills_li

# for pos, skill in enumerate(flat_skills_list):
#     print(pos, skill)
# print(len(flat_skills_list))
