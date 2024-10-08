#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name:
    Names = name.readlines()

with open("./Input/letters/starting_letter.txt") as file:
    letter_Content = file.read()
    for name in Names:
        ProperName = name.strip()
        new_letter = letter_Content.replace(PLACEHOLDER, ProperName)
        with open(f"./Output/ReadyToSend/letter_for_{ProperName}.txt", mode="w") as letter:
            letter.write(new_letter)



