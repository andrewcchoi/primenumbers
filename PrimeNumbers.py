
for i in range(2,30):
    counter = 0
    n = 2
    while n < i:
        if i % n == 0:
            print(str(i) + " is not a prime number")
            counter = 1
            break
        n += 1
if counter == 0:
    print(str(i) + " is a prime number.")
