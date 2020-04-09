from medicines.models import medicine


def resister_medicine():
	name=input("Name: ")
	start_date=input("Start_date: ")
	consumption_counter=input("Count: ")
	new_ob=medicine(name=name,start_date=start_date,consumption_counter=consumption_counter)
	new_ob.save()

x=0
print('Do you want to add medicine ?')
x = int(input())

while(x==1):
	resister_medicine()
	print("Added")
	
	x = int(input("Again?: "))