n = float(input("Please, input an integer: "))
sum = float
ave = float
if (n%2 ==1):
    sum = ((n+1)/2)**2
    ave = (n)*((n-1)/2)+1
else:
    sum = (n/2)**2
    ave = (1+n)*(n/2)+1
print("The sum of odd numbers starting from 1 up to and including N:", sum)
print("The average of even numbers starting from 1 up to and including N:", ave)