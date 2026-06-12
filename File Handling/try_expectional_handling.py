try:
    num = str(input("Enter a number: "))
    print(num)
except ValueError:
    print("Please enter a valid integer.")
# except:
#     print("An unexpected error occurred.")