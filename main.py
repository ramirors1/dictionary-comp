#  create a new dictionary from a items in a list
# new_dict ={new_key:new_value for item in list}

#  create a new dictionary from existing dictionaries
# new_dict ={new_key:new_value for (key, value) in dict.items()}

#  create a new dictionary from existing dictionaries adding a condition at the end
# new_dict ={new_key:new_value for (key, value) in dict.items() if test}

#  [] = lists, {} = Dictionaries

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {name:random.randint(1, 100) for name in names}

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}