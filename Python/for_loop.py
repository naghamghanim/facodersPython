name=input("Enter student's name: " )
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

if(name in s1):
    s1_temp=s1[1:]
    summ=sum(s1_temp)
    print(name+" "+ str(summ))

elif (name in s2):
    s2_temp=s2[1:]
    summ=sum(s2_temp)
    print(name+" "+ str(summ))

elif (name in s3):
    s3_temp=s3[1:]
    summ=sum(s3_temp)
    print(name+" "+ str(summ))
else:
    print("Student is not recorded 0")
