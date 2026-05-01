input_string = ""
index = 0

def S():
    global index

    if index < len(input_string) and input_string[index] == 'a':
        index += 1  
        if S():     
            if index < len(input_string) and input_string[index] == 'b':
                index += 1  
                return True
            else:
                return False
        return False

    return True

input_string = input("Enter string: ")
index = 0

if S() and index == len(input_string):
    print("String Accepted")
else:
    print("String Rejected")