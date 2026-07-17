'''n=int(input("enter a size:"))
for i in range(n):
      for j in range(i+1):
             print(j+1,end=" ")
      print()
      '''
'''n=int(input("enter a number:"))
num=1
for i in range(n):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()'''

'''n=int(input("Enter a size:"))
for i in range(n):
    for j in range(i+1):
        print(i*j,end=" ")
    print()'''
'''n=int(input("Enter a size:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()'''
'''n=int(input("Enter a size:"))
c=65
for i in range(n):
    for j in range(i+1):
        print(chr(c),end=" ")
        c+=1
    print()'''

#List comprehension
'''l=[1,2,3,4,5,56,6,7]
res=[i+10 for i in l]
print(res)'''
#index* index value
#List comprehension
'''l=[1,2,3,4,5,56,6,7]
res=[i*l[i] for i in range(len(l))]
print(res)'''
#cube-List comprehension
l=[1,2,3,4,5,56,6,7]
res=[i if i%2==0  else 0 for i in l ]
print(res)


    
            

      
      
