import matplotlib.pyplot as plt
import os
import json
import math


def average_value(array):
    return sum(array) / len(array)


def sko(array, exp_value):
    D = 0

    for i in array:
        D += (i - exp_value) ** 2

    return math.sqrt(D / len(array))


def split_dict(dictionary):
    key_list = list(dictionary.keys())
    value_list = list(dictionary.values())
    return key_list, value_list


# Method which sorting dictionary by values
def dictionary_sorting(dictionary):
    sorted_values = sorted(dictionary.values(), reverse=True)
    sorted_dict = {}

    for i in sorted_values:
        for k in dictionary.keys():
            if dictionary[k] == i:
                sorted_dict[k] = dictionary[k]
                break

    return sorted_dict


# FOR SKILLS
def proccessing_skills():
    skills_dict = {}

    for jsObj in os.listdir(r'C:\Users\bulat\PycharmProjects\HHru_parsing\docs\vacancies'):

        with open(rf'C:\Users\bulat\PycharmProjects\HHru_parsing\docs\vacancies\{jsObj}', encoding='utf-8') as file:
            src = file.read()
            src = json.loads(src)

        skills_arr = []

        try:
            for skill in src['key_skills']:
                skills_arr.append(skill['name'].upper())

            for skill in skills_arr:
                if skill not in skills_dict:
                    skills_dict[f'{skill}'] = 0
                if skill in skills_dict:
                    skills_dict[f'{skill}'] += 1

        except KeyError:
            pass

    sorted_skills = dictionary_sorting(skills_dict)

    first_16_skills = {}

    for i, (key, value) in enumerate(sorted_skills.items()):
        first_16_skills[key] = value
        if i == 15:
            break

    return first_16_skills


# FOR SALARY
def proccessing_salary():
    without_xp = []
    one_three = []
    three_six = []
    more_six = []

    for jsObj in os.listdir(r'C:\Users\bulat\PycharmProjects\HHru_parsing\docs\vacancies'):
        with open(rf'C:\Users\bulat\PycharmProjects\HHru_parsing\docs\vacancies\{jsObj}', encoding='utf-8') as file:
            src = file.read()
            src = json.loads(src)

        experience_mapping = {
            'Нет опыта' : without_xp,
            'От 1 года до 3 лет' : one_three,
            'От 3 до 6 лет' : three_six,
            'Более 6 лет' : more_six
        }

        try:
            experience_name = src['experience']['name']
            salary_currency = src['salary']['currency']
            salary_from = src['salary']['from']
            salary_to = src['salary']['to']

            if salary_currency == 'RUR' and salary_to != 'null' and salary_to != None:
                average_salary = (salary_to + salary_from) / 2
                if experience_name in experience_mapping and average_salary > 10000:
                    experience_mapping[experience_name].append(average_salary)
            elif salary_currency == 'RUR' and (salary_to == 'null' or salary_to == None):
                if experience_name in experience_mapping:
                    experience_mapping[experience_name].append(salary_from)
        except (TypeError, KeyError):
            pass

    return experience_mapping


def BigProccessing(type = str()):
    output_dict = {}

    for jsObj in os.listdir(r'C:\Users\bulat\PycharmProjects\HHru_parsing\docs\vacancies'):

        with open(rf'C:\Users\bulat\PycharmProjects\HHru_parsing\docs\vacancies\{jsObj}', encoding='utf-8') as file:
            src = file.read()
            src = json.loads(src)

        try:
            if type == 'metro':
                source = src['address']['metro']['station_name']
            elif type == 'experience' or type == 'xp':
                source = src['experience']['name']
            else:
                return '[INFO] Произошла ошибка, попробуйте заново!'
        except TypeError:
            pass

        try:
            if source not in output_dict:
                output_dict[f'{source}'] = 0
            if source in output_dict:
                output_dict[f'{source}'] += 1
        except (KeyError, TypeError):
            pass

        sorted_dict = dictionary_sorting(output_dict)

    return sorted_dict


metro_dict = BigProccessing(type='metro')


# График по востребованности скиллов
skills_dict = proccessing_skills()
skill_name, skill_value = split_dict(skills_dict)
plt.bar(skill_name, skill_value)
plt.xlabel("Название самых распространенных скиллов")
plt.xticks(rotation=90)
plt.ylabel("Кол-во раз встречающихся в вакансиях")
plt.title("Самые востребованные навыки для DevOps")
plt.show()


# Круговая диаграмма по востребованности опыта в DevOps
xp_dict = BigProccessing(type='xp')
labels, values = split_dict(xp_dict)
fig1, ax = plt.subplots()
ax.pie(values, labels=labels, autopct='%1.1f%%')
ax.axis("equal")
plt.show()


# Зарплаты
salary_dict = proccessing_salary()
for key in salary_dict:
    print(f"Средняя зарплата для DevOps специалиста {key} ", average_value(salary_dict[key]),
          f"Среднеквадратичное отклонения для зарплаты DevOps специалиста {key} ", sko(salary_dict[key],average_value(salary_dict[key])))