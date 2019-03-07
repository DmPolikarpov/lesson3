import csv

content = [
        	{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
       		{'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        	{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
   		  ]

with open('list_dict.csv', 'w', encoding='utf-8') as list_dict:
	fields = ['name', 'age', 'job']
	writer = csv.DictWriter(list_dict, fields, delimiter = ';')
	writer.writeheader()
	for i in content:
		writer.writerow(i)
