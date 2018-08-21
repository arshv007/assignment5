
#Ques1
x=int(input('Enter Year:'))
if x%4==0:
    if x%100==0:
         if x%400==0:
             print(x,'is a leap year ')
         else:
             print(x,'is not a leap year ')
    else:
         print(x,'is a leap year ')
else:
     print(x,'is not a leap year ')

#Ques2
a=int(input('Enter Length:'))
b=int(input('Enter Breadth:'))
if(a>0 and b>0):
    if(a==b):
         print("Dimensions of Square")
    else:
        print("Dimensions of Rectangle")
else:
   print("Wrong Input")

#Ques3
a=int(input("Enter age 1:"))
b=int(input("Enter age 2:"))
c=int(input("Enter age 3:"))
if(a>=b and a>=c):
    print("Oldest age is:",a)
    if(b>=c):
      print("Youngest age is:",c)
    else:
      print("Youngest age is:",b)
      
elif(b>=a and b>=c):
    print("Oldest is:",b)
    if(a>=c):
      print("Youngest age is:",c)
    else:
      print("Youngest age is:",a)
      
else:
    print("Oldest age is:",c)
    if(a>=b):
      print("Youngest age is:",b)
    else:
      print("Youngest age is:",a)
    
#Ques4
age=int(input("Enter age:"))
sex=input("Enter Sex( M/F):")
status=input("Enter Marital Status (Y/N):")
if(sex=='F' or sex=='f'):
    print("Place of Service: URBAN AREA ONLY ")
elif(sex=='M' or sex=='m'):
    if(age>=20 and age<=40):
        print("Place of Service: ANYWHERE ")
    elif(age>40 and age<=60):
        print("Place of Service: URBAN AREA ONLY")
    else:
        print("ERROR")
else:
   print("ERROR")
   

#Ques5
x=int(input("Enter units:"))
y=int(input("Enter cost:"))
z=x*y
print('Amount:',z)
if(z>=1000):
    print('Amount after discount:',z-(z*(1/10)))
else:
    print("No Discount Under Purchase of 1000")

#Ques6
integers=[]
for i in range(10):
    value=int(input('Enter value:'))
    integers.append(value)
print('List:',integers)


#Ques7
"""
x=1
while x>0:
   print(x)
   x+=1
"""

#Ques8

x=[]
y=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digits:'))
    x.append(b)
print('List:',x)
for i in range(a):
    sq=x[i]*x[i]
    y.append(sq)
print('List of Squared element:',y)

#Ques9

l1=[]
l2=[]
l3=[]
l4=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    d=input('Enter values:')
    l1.append(d)
print('List:',l1)
for i in range(a):
    if str(l1[i]).isdigit():
        l2.append(l1[i])
    elif str(l1[i]).isalpha():
        l3.append(l1[i])
    else:
        l4.append(l1[i])
print('Int List:',l2)
print('String List:',l3)
print('Float List:',l4)


#Ques10

print("Prime numbers")

for i in range(1,101):
   if i > 1:
       for x in range(2,i):
           if (i % x) == 0:
               break
       else:
           print(i)


#Ques11
print('Pattern')
for i in range(0, 5,1):
    print("* "*i)

    
#Ques12
print()
l1=[]
l2=[]
a=int(input("Enter No of Values:"))
for i in range(a):
    b=int(input('Enter digit:'))
    l1.append(b)
print(l1)
search=int(input("Enter value to search:"))
l1.remove(search)
print(l1)      
         
         
             
         
