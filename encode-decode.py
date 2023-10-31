"""
Created By: Phoenix Cushman & Kyle Jeter
Date: 10/25/2023
Project: Lab 6: Software Engineering
"""
#import libraries
def encode(password_str): #This function takes in a string containing an integer based password, encodes it by adding 3 to each digit, and returns the resulting encoded string.
    return_str = ""
    for i in password_str:
        return_str += str(int(i) + 3)[-1] #We index into the last character in the new str digit because some digits when added with 3 result in a two digit number. (ex: 9 + 3 = 12). We don't want the tens place digit so we only index into the ones place digit.
    return return_str

def decode(encoded_str):
    return_str = ""
    nums = {0:7, 1:8, 2:9, 3:0, 4:1, 5:2, 6:3, 7:4, 8:5, 9:6, }
    for i in encoded_str:
        return_str += str(nums[int(i)])
    return return_str


def main():
    loop_ctrl_bool = True
    while(loop_ctrl_bool):
        #Print the Menu options
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option_str = str(input("Please enter an option: ")) #Take in the user menu option number string
        if (option_str == "1"): #1. Encode Option
            password_str = str(input("Please enter your password to encode: "))
            encoded_str = encode(password_str)
            print(f"Your password has been encoded and stored!\n")
        elif (option_str == "2"): #2. Decode Option
            print(f"The encoded password is {encoded_str}, and the original password is {decode(encoded_str)}.")
        elif (option_str == "3"): #3. Quit Option
            loop_ctrl_bool = False #Set the control boolean value to false and continue to the next loop iteration to exit
            continue
    return	

if __name__=='__main__':
    main()