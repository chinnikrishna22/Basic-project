import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = [] 

    for length in pwlength:
        password = ""
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
    return pword


def replaceWithUppercaseLetter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
    return pword


def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    
    print("Generating " + str(num_passwords) + " passwords")
    
    password_lengths = []

    print("Minimum length of password should be 3")

    for i in range(num_passwords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length < 3:
            length = 3
        password_lengths.append(length)
    
    passwords = generatePassword(password_lengths)

    for i in range(num_passwords):
        print("Password #" + str(i+1) + " = " + passwords[i])

if __name__ == "__main__":
    main()
