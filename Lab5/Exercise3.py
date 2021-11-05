number = 4727
get = int(input("Please write a number: "))
while get != number:
    if get < number:
        print("You wrote a very small number.")
    else:
        print("You wrote a very big number.")
    get = int(input("Try an other number:"))
else:
  print("True, congratulations!")