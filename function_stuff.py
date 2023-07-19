# FUNCTIONS ARE REPEATABLE CODE BLOCKS

def add_two_and_print(number):
    number = number + 2
    print(number)

add_two_and_print(34)

user_number = int(input("Enter your number: "))
add_two_and_print(user_number)


# FUNCTIONS CAN RETURN VALUES
def add_to_bill(bill, item, cost):
    bill = f"{bill}\n{item} {cost}"
    return bill

check = ""
check = add_to_bill(check, "apple", 1.23)
check = add_to_bill(check, "banana", 1.01)
check = add_to_bill(check, "grapes", 2.03)
print(check)
