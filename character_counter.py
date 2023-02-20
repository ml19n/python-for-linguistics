def main():
    #open and read file as string
    with open("lorem.txt") as file:
        text = list(file.read())
    #loop through string to count character frequencies and print them
    for char in text:
        char_freq_pair = char + " " + str(text.count(char))
        print(char_freq_pair)    

if __name__ == "__main__":
    main()






