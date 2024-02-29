List =[]
n = int(input("Enter a number of Elements"))

for i in range(0, n):
    element = int(input())
    List.append(element)
print(List)
print("The max number is:",max(List))
print("The min number is:",min(List))
print("The sum of number is:",sum(List))
print("The average of  number is:",sum(List)/len(List))
