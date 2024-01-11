cipher = input("Please enter the cipher text to be solved. Spaces will be ignored: ")
sentence = cipher

# This program was designed to work on a shift cipher. It will try all 25 combinations
# This is an example of what can be entered into the program
# guraw hfgju raguv atfjr erybb xvat
# thenj ustwh enthi ngswe reloo king
# then just when things were looking

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
