A = int(input())
B = int(input())

# Validate the inputs
if 0 < A < 10 and 0 < B < 10:
    print(A + B)
else:
    print("Invalid Input: Numbers should be between 0 and 10")
