# سنقوم بتخزين المدخل بمتغير ، المدخل هو 88

mark = input('Enter the mark : ')
mark=float(mark)
# ابدا بكتابة الكود هنا

if mark < 50:
    print('Failed')
elif mark >= 50 and mark < 75:
    print ('Accepted')
elif mark >=75 and mark < 85:
    print('Good')
elif mark >=85 and mark < 90:
     print('Very Good')
else:
     print('Excellent')
