def checkIfItsPrime(number):
    denominator = 1
    max_number_of_nice_numbers = 2
    current_number_of_nice_numbers = 0

    number_given_was_prime = False

    while denominator <= number:

        remainder = number % denominator
        if remainder == 0:
            current_number_of_nice_numbers += 1

        if current_number_of_nice_numbers > max_number_of_nice_numbers:
            number_given_was_prime = False
            break
        elif current_number_of_nice_numbers <= max_number_of_nice_numbers:
            number_given_was_prime = True

        denominator = denominator + 1

    print("Done with loop")
    if number_given_was_prime == True:
        print("The number you gave was prime")
    elif number_given_was_prime == False:
        print("The number given was NOT prime")

while True:
    User_Answer = input("Do you want a prime number: ")

    if User_Answer == "no":
        print("You said no. I will now exit")
        break
    elif User_Answer == "yes":
        print("You said yes")
        number = int(input("Give me a number and I'll check if its prime: "))
        checkIfItsPrime(number)
    else:
        print("Say yes or no")
