def make_sentence(word, part_of_speech):
    if (part_of_speech == 0):
        return f"I am excited to add this {word} to my vast collection of them!"
    elif (part_of_speech == 1):
        return f"It's so nice outside today it makes me want to {word}!"
    elif (part_of_speech == 2):
        return f"Looking out my window, the sky is big and {word}!"

    return "Error"

word = input("Enter a noun or verb or adjective ")
number = int(input("Enter a number for part of speech "))
print(make_sentence(word, number))
    

