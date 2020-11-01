import sqlite3 as sq
id_num=0
while id_num != -1:
	try:
		id_num=input("Please enter an ID number: ")
		try:
			bridge=sq.connect('pets.db')
			b=bridge.cursor()
			b.execute('SELECT * FROM person WHERE id=?', id_num)
			person_row=b.fetchone()
			print(person_row[1],person_row[2],"is", person_row[3], "years old.")
			b.execute('SELECT pet.name,pet.breed,pet.age,pet.dead FROM pet INNER JOIN person_pet ON person_pet.pet_id=pet.id INNER JOIN person ON person.id=person_pet.person_id WHERE person.id=?', id_num)
			pp_row=b.fetchall()
	
			if len(pp_row)==1:
				if (pp_row[0][3]==0):
					print(person_row[1],person_row[2], "owns", pp_row[0][0], "who is a", pp_row[0][1],", and is", pp_row[0][2], "years old")
				elif (pp_row[0][3]==1):
					print(person_row[1],person_row[2], "owned", pp_row[0][0], "who is a", pp_row[0][1],", and tragically passed at the age of", pp_row[0][2])
			elif len(pp_row)==2:
				if (pp_row[0][3]==0):
					print(person_row[1],person_row[2], "owns", pp_row[0][0], "who is a", pp_row[0][1],", and is", pp_row[0][2], "years old")
					if (pp_row[1][3]==0):
						print("and owns", pp_row[1][0], "who is a", pp_row[1][1],", and is", pp_row[1][2], "years old")
					else:
						print("and owned", pp_row[1][0], "who was a", pp_row[1][1],", and tragically passed at the age of", pp_row[1][2])
				elif (pp_row[0][3]==1):
					print(person_row[1],person_row[2], "owned", pp_row[0][0], "who is a", pp_row[0][1],", and tragically passed at the age of", pp_row[0][2])
					if (pp_row[1][3]==0):
						print("and owns", pp_row[1][0], "who is a", pp_row[1][1],", and is", pp_row[1][2], "years old")
					else:
						print("and owned", pp_row[1][0], "who was a", pp_row[1][1],", and tragically passed at the age of", pp_row[1][2])
		except TypeError:
			print("No entry exists for that person, please enter another value")	
	except sq.ProgrammingError:
		exit()
	
	