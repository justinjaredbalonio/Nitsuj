student_scores = {
	"Justin": [90,92,94],
	"Juliana": [90,95,97],
	"Balonio": [95,98,97]  #Iterable

}


#justin_grades = student_scores['Justin']

#print(justin_grades)

#for grade in justin_grades:
	#print(grade)

student_grades = [student_scores ['Justin'],
student_scores['Juliana'],
student_scores['Balonio']
]


for student, grades in student_scores.items():
	print(student)
	for grade in grades:
		print(grade)


