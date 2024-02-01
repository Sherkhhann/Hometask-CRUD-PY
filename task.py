list_of_dict=[]
while True:
	print("""
		c - > create
		g - > get
		u - > update
		d - > delete
		e - > exit""")
	a=input("What do you choose? - > ")
	if a == "e":
		break
	if a == "c":
		create_dict={
	"username": input("Input your username: "),
	"task": input("What are you going to do? "),
	"due_date": input("When are you going to do it?"),
	"time": input("Last question :) What tiime?")}
		list_of_dict.append(create_dict)
		
	if a == "g":
		for i in list_of_dict:
			for key, value in i.items():
				print(value, end=" ")
			print()
	if a == "u":
		user_input = input("Which user? ")
		user_change_input = input("Update user to - >")
		task_change_input = input("Update task to - >")
		due_date_change_input = input("Update day to - >")
		time_change_input = input("Update time to - >")
		for j in list_of_dict:
			if user_input in j.values():
				j.update({
				"username": user_change_input, 
				"task": task_change_input, 
				"due_date": due_date_change_input, 
				"time": time_change_input})
	if a == "d":
		user_delete = input("Delete which user?")
		for d in list_of_dict:
			if user_delete in d.values():
				list_of_dict.remove(d)