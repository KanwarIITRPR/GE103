eng = int(input("Enter the marks that you obtained in English: "))
hindi = int(input("Enter the marks that you obtained in Hindi: "))
math = int(input("Enter the marks that you obtained in Mathematics: "))
sci = int(input("Enter the marks that you obtained in Science: "))
sst = int(input("Enter the marks that you obtained in Social Studies: "))

avg_marks = (eng + hindi + math + sci + sst)/5

if avg_marks >= 90:
    print("You secured grade A.")
elif avg_marks >= 80:
    print("You secured grade B.")
elif avg_marks >= 70:
    print("You secured grade C.")
elif avg_marks >= 60:
    print("You secured grade D.")
else:
    print("You secured grade F.")