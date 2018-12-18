lower=int(input())
upper=int(input())
if(upper<=1000000 and lower<=1000000):
	for i in range(lower,upper):
		if(i%2!=0):
			print(i )
