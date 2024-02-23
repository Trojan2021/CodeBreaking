package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func encrypt(userInput string) {

}
func decrypt(userInput string) {
	sentence := userInput
	fmt.Print("Possible Decryptions:\n")
	for i := 1; i <= 25; i++ {
		newSentence := ""
		for _, x := range sentence {
			if x != ' ' {
				nextLetter := string((byte(unicode.ToLower(x))-97+1)%26 + 97)
				newSentence += nextLetter
			} else {
				newSentence += " "
			}
		}
		fmt.Printf("%d. %s\n", i, newSentence)
		sentence = newSentence
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	userChoice := "0"
	for !(userChoice == "1" || userChoice == "2") {
		fmt.Print("Would you like to encrypt or decrypt a shift cipher?\n1. Encrypt\n2. Decrypt\n> ")
		fmt.Scanln(&userChoice)
	}
	var userInput string
	fmt.Println("Please enter the enciphered message:")
	userInput, _ = reader.ReadString('\n')
	if userChoice == "1" {
		encrypt(userInput)
	}
	if userChoice == "2" {
		decrypt(userInput)
	}
}
