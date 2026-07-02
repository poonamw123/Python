def ChkVowel(ch):
    if ch in ( "a", "e" , "i", "o", "u", "A", "E", "I", "O", "U"):
        return True
    
    else:
        return False
    
def main():
    Value = input("Enter a character : ")
    
    Ret = ChkVowel(Value)
    
    if Ret:
        print("it is a vowel")
        
    else:
        print("it is a Consonant")
        
if __name__ == "__main__":
    main()