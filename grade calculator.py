print("Enter points from 5 different classes this semester:")

classone = int(input("Class one:"))
classtwo = int(input("Class two:"))
classthree = int(input("Class three:"))
classfour = int(input("Class four:"))
classfive = int(input("Class five:"))

total = classone + classtwo+ classthree + classfour + classfive
average = total/5

if average >= 95 and average <= 100:
    print("A+")
elif average >= 90:
    print("A")
elif average >= 85:
    print("B+")
elif average >= 80:
    print("B")
elif average >= 75:
    print("C+")
elif average >= 70:
    print("C")
elif average >= 65:
    print("D+")
elif average >= 60:
    print("D")
else:
    print("F")
