from itertools import zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Максим', 'Анна']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

res_generator = (el for el in zip_longest(tutors, klasses, fillvalue=None))
print(*res_generator)
print(*res_generator, "генератор исчерпал себя")
