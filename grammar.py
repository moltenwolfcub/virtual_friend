def pluralise(word):
    stay_same = ["sheep", "deer", "series", "species"]
    
    if word in stay_same:
        return(word)
        
    elif word[-1].lower() in ["s", "x", "z", "o"]:
        return(f"{word}es")

    elif word[-1].lower() == "f":
        return(f"{word[:1]}ves")

    elif word[-1].lower() == "y" and word[-2].lower() in "aeiou":
        return(f"{word}s")

    elif word[-1].lower() == "y" and word[-2].lower() not in "aeiou":
        return(f"{word[:-1]}ies")
    
    elif word[-1].lower() == "s" and word[-2].lower() == "u":
        return(f"{word[:-2]}i")
    
    elif word[-1].lower() == "s" and word[-2].lower() == "i":
        return(f"{word[:-2]}es")

    elif word[-1].lower() == "n" and word[-2].lower() == "o":
        return(f"{word[:-2]}a")
    
    else:
        return(f"{word}s")
