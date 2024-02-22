English = int(input("Enter English marks :"))
Maths = int(input("Enter Maths marks :"))
Chemistry = int(input("Enter Chemistry marks :"))
Physics = int(input("Enter Physics marks :"))
BEE = int(input("Enter BEE marks :"))


if (English >= 40 and Maths >=40 and Chemistry >= 40 and Physics >=40 and BEE >=40):
    print("Passed")
    Aggregate = ((int(English) + int(Maths) + int(Chemistry) + int(Physics) + int(BEE)) / 500)*(100)
    print("The Aggregate is : ", Aggregate)
    if Aggregate > 75:
        print("The grade is Distinction ")
    elif Aggregate >= 60:
        print("The grade is First Division")
    elif Aggregate >= 50:
        print("The grade is Second Division")
    elif Aggregate >= 40:
        print("The grade is third Division ")
else : print("Failed")
