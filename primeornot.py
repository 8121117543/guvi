try:
	n=int(input())
	flag=0
	for i in range(2,int(n/2)+1):
		if n%i ==0:
			flag=1
			break
	if flag==0:
		print('yes')
	else :
		print('no')
except:
	print('invalid')
