grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}


def students_names(Class_name):
    if(Class_name=="grade_one"):
        list1=list(grade_one.keys())
    elif(Class_name=="grade_two"):
        list1=list(grade_two.keys())
    else :
        list1=list(grade_three.keys())
    return list1

def student_score(Std_name,grade):
    x=0
    sum=0
    if(grade=="grade_one"):
        list2=grade_one.get(Std_name)
        L=len(list2)
        x=0
        sum=0
        while(x<L):
            sum+=list2[x]
            x=x+1

    elif(grade=="grade_two"):
        list2=grade_two.get(Std_name)
        L=len(list2)
        while(x<L):
            sum+=list2[x]
            x=x+1
    elif(grade=="grade_three"):
        list2=grade_three.get(Std_name)
        L=len(list2)
        x=0
        sum=0
        while(x<L):
            sum+=list2[x]
            x=x+1
    else:
        print("The grade is not exist")
    return sum


while True:
    x=  input("Choose one: students_names, student_score, students_count \n")
    if(x=="Done"):
        break
    elif(x=='students_names'):
        ClassName=input("Choose the Class: grade_one, grade_two, grade_three \n ")
        print(students_names(ClassName))
    elif(x=='student_score'):
        stdName=input("Enter the name of the student \n")
        gradeName=input("Enter the grade \n")
        print(student_score(stdName,gradeName))
    elif(x=='student_count'):
        gradeName2= input("Enter the grade \n")
