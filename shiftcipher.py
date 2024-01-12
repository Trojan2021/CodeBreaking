import random

# guraw hfgju raguv atfjr erybb xvat
# thenj ustwh enthi ngswe reloo king
# then just when things were looking


def encrypt(user_input: str) -> None:
    rand = random.randint(1, 25)
    new_sentence = ""
    for x in user_input:
        if not x == " ":
            next_letter = chr(
                (ord(x.lower()) - 97 + rand) % 26 + 97
            )  # get the next letter
            new_sentence += next_letter
        else:
            new_sentence += " "
    print(f"\nYour encrypted string is {new_sentence}\n")


def decrypt(user_input: str) -> None:
    sentence = user_input
    print("Possible decryptions:\n")
    for i in range(25):
        new_sentence = ""
        for x in sentence:
            if not x == " ":
                next_letter = chr(
                    (ord(x.lower()) - 97 + 1) % 26 + 97
                )  # get the next letter
                new_sentence += next_letter
            else:
                new_sentence += " "
        print(new_sentence)
        sentence = new_sentence


if __name__ == "__main__":
    user_choice = 0
    while not (user_choice == "1" or user_choice == "2"):
        user_choice = input(
            "Would you like to encrypt or decrypt a shift cipher?\n1. Encrypt\n2. Decrypt\n> "
        )
    user_input = input("Please enter the text that you would like to use\n:")
    if user_choice == "1":
        encrypt(user_input)
    else:
        decrypt(user_input)
