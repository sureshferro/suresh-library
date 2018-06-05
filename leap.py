# suresh-library
y=int(input("\n enter year"))
if(y%4==0):
	if(y%100==0):
		if(y%400==0):
			print("\nleap year")
		else:
			print("\n not leap year")
	else:
			print("\n leap year")
else:
	print("\n not leap year"
