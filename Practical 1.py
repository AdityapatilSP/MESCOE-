input("Enter Employee Name : ")
input("Enter Employee ID : ")
B = float(input("Basic pay :"))
HRA = int(B*10)/100
print("HRA : ",HRA)
TA = int(B*5)/100
print("TA :",TA)
GS = int(B+HRA+TA)
print("Gross Salary :",GS)
T = int(GS*2)/100
print("Tax :" ,T)
NS = int(GS - T)
print("Net Salary :", NS)
