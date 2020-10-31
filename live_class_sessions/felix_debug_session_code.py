pins = (1, 2, 3, 4)
i = 0

while i < 5:
    user_attempt = int(input("What is your pin: "))
    if user_attempt in pins:
        print("Your pin exists!")
        break
    print("Please try again!")
    i += 1
