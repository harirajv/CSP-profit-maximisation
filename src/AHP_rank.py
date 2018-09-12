import copy
cspn =5 #Number of CSPs
prn =4 #Number of parameters
imp=[[1]*prn]*prn #Priority of parameters
para=["Performance","Availability", "Scalability", "Cost"]
sum_=[0]*prn
wt=[0]*prn
c=[]
rank=[0]*cspn
beg=0
end=100
mid=50
mid1=mid

def comp():
	a = copy.deepcopy(a1)
	for i in range(len(rank)):
		rank[i]=0
	for i in range(len(wt)):
		wt[i]=0
	
	max_=[-1]*prn
	for i in range(cspn):
		for j in range(prn):
			if(a[i][j]>max_[j]):
				max_[j]=a[i][j]    # assign max matrix

	for i in range(cspn):
		for j in range(prn):
			a[i][j]/=max_[j]     #Normalising values

	for j in range(prn):
		sum_[j]=sum(imp[j])

	for i in range(prn):
		for j in range(prn):
			wt[i]+=imp[i][j]/(sum_[j]*prn)    # Weight Vector
	#print("Weight Vector :")
	#print(wt)

	for i in range(cspn):
		for j in range(prn): 
			rank[i]+=a[i][j]*wt[j]     #Ranking values
	print("ranking values")
	print(rank)

def ranking():
	
	pos=0
	d=[]
	for i in range(len(rank)):
		max1_=-1
		for j in range(len(rank)):
			if(rank[j]>max1_):
				max1_=rank[j]
				pos=j
		d.append(pos+1)		
		rank[pos]=-2		
	print("Ranks after the change")
	print(d)
	for i in range(len(c)):
		if(c[i]!=d[i]):
			return 0
	return 1


print("Enter CSP Rating matrix" )
a1=[list(map(float,input().split())) for i in range(5)]    # Getting CSP Rating matrix

print("Enter relative importance of parameters")	
for i in range(prn-1):
	for j in range(i+1,prn):
		print(para[i]+" relative to "+para[j] )
		imp[i][j]=float(input())
		imp[j][i]=1/imp[i][j]              # Calculating important matrix

comp()
for i in range(len(rank)):
		max1_=-1
		for j in range(len(rank)):
			if(rank[j]>max1_):
				max1_=rank[j]
				pos=j
		c.append(pos+1)		
		rank[pos]=-2		
print("Initial Ranks")
print(c)               # Calculated the initial ranks separately and stored in c list

while(beg<end):
	print("Mid Value :"+str(mid1))
	temp=a1[max(c)-1][3]	
	a1[max(c)-1][3]*=1-(mid1/100)
	print(a1)
	comp()
	x=ranking()
	a1[max(c)-1][3]=temp
	if(x==1):
		beg=mid1
	else:	
		end=mid1
	
	mid=mid1	
	mid1=(beg+end)//2
	if(mid==mid1):
		break

print("The rating does not change for "+str(mid)+" decrease in the price rating")

