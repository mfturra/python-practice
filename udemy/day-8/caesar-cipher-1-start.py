alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    # print(alphabet[shift])
    
    # create indices var to store text index vals
    text_indices = []

    # cycle through chars in text
    for char in text:
        # for each char, locate it in alphabet
        if char in alphabet:
            
            # store index val of char in text_indices
            text_indices.append(alphabet.index(char))
            print(f"These are the text_indices before shift: {text_indices}")

            # shift text_indices by shift value
            for item in text_indices:
                shifted_indices = []
                shifted_indices.append(item + shift)
            print(f"These are the shifted_indices: {shifted_indices}")
    
    # look for chars in text_indices 
    # for char in text_indices:




    # # loop through individual letters in text
    # for letter in text:
    #     # output current letter in text
    #     print(f"\nThe current letter is {letter}")

    #     # locate current letter index in alphabet
    #     new_letter_index = alphabet.index([letter])
    #     print(new_letter_index)

        # # loop through elements in alphabet
        # for i in alphabet:
        #     # if letter is found in alphabet 
        #     if letter in alphabet:
        #         # store 

        #         print(f"This letter was found in the alphabet: {letter+shift}\n")
            # new_text =+ alphabet[letter][shift]
            # put letters in new variable

            # store found letter in new_text 
            # new_text = []
            # new_text[letter]
            # print("The new_text variable is: {new_text}")
        # print(f"This is the current letter: {new_text}")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# plain_text = str(input("Please input the text that you'd like to encode"))
# shift = str(input("Please input the shift that you'd like to use to encode the message"))

encrypt(text=text, shift=shift)