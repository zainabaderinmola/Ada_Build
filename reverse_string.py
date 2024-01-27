def reverse_string(input):
    answer = ""
    # Your code goes here
    for i in input:
        answer = i + answer
    #  End of your code
    return answer

input = 'hello'

reverse_string(input)

# # Tests below, do not change
# assert reverse_string("hello") == "olleh", "Cannot reverse 'hello'"
# assert reverse_string("") == "", "When given an empty string it returns an empty string, but doesn't"
# assert reverse_string("racecar") == "racecar", "Cannot reverse 'racecar'"
# assert reverse_string("12345") == "54321", "Cannot reverse 12345"

# # If the program gets here, the code works!
# print("Your solution works!")