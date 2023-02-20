def main():
    numStore = int(input("Enter an integer to convert to another base: "))
    baseStore = int(input("Select a base (2) (6) (8): "))
    if baseStore == 2:
            print(bin(numStore))
    if baseStore == 6:
            print(hex(numStore))
    if baseStore == 8:
            print(oct(numStore))
    
        
      

if __name__ == "__main__":
    main()


 