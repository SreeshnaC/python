n=int(input("Enter the no.of elements"))
num_list=[]
for i in range(n):
    a=int(input("enter the numbers:"))
    num_list.append(a)
print("Entered list:",num_list)
sqr_list=[x**2 for x in num_list]
print("squared list:",sqr_list)
