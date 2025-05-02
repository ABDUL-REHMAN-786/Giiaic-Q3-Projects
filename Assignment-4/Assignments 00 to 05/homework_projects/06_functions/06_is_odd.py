# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

for num in range(10, 20):
    if num % 2 == 0:
        print(f"{num} even")
    else:
        print(f"{num} odd")
# # Note: This code snippet iterates through numbers from 10 to 19 and prints whether each number is even or odd.
# # The modulo operator (%) is used to determine if a number is even (remainder 0) or odd (remainder 1).