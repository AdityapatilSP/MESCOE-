English = int(input("Enter English marks :"))
Maths = int(input("Enter Maths marks :"))
Chemistry = int(input("Enter Chemistry marks :"))
Physics = int(input("Enter Physics marks :"))
BEE = int(input("Enter BEE marks :"))

if English > 40:
    print("Passed in English ")
else : print("Fail")
if Maths > 40:
    print("Passed in Maths ")
else : print("Fail")
if Chemistry > 40:
    print("Passed in Chemistry ")
else: print("Fail")
if Physics > 40:
    print("Passed in Physics")
else: print("Fail")
if BEE > 40:
    print("Passed in BEE")
else : print("Fail")

Aggregate = ((int(English) + int(Maths) + int(Chemistry) + int(Physics) + int(BEE)) / 500)*(100)
print("The Aggregate is : ", Aggregate)


if Aggregate > 75:
    print("The grade is Distinction ")
elif Aggregate >= 60:
    print("The grade is First Division")
elif Aggregate >= 50:
    print("The grade is Second Division")
