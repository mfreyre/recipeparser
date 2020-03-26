from amounts import Amounts

def main():
    filename = raw_input("please enter filename: ")
    if filename == "":
        filename = "testrecipe.txt"
    f = open(filename, "r")
    contents = list(f)
    f.close()

    recipe_csv = open("recipe.csv", "w+")

    #conversion to csv occurs here:
    for line in contents:
        wordlist = line.split()
        print line
        newline = guessAtSolution(wordlist)
        print "i have a guess, and my guess is " + newline
        ok = raw_input("was that right? Y/N ")
        if ok != "Y":
            newline = getUserInputSolution(wordlist)

        recipe_csv.write(newline + "\n")

    recipe_csv.close()

def getUserInputSolution(wordlist):
    amt_idx = int(raw_input("where does the amount break go? "))

    amt = " ".join(wordlist[:amt_idx])

    unit_idx = int(raw_input("where does the unit break go? "))
    unit = " ".join(wordlist[amt_idx:unit_idx])

    ingredient_idx = int(raw_input("where does the ingredient break go? "))
    ingredient = " ".join(wordlist[unit_idx:ingredient_idx])
    newline = ",".join([amt, unit, ingredient])
    print newline
    return newline

def guessAtSolution(wordlist):
    # get all words with numbers in it:
    idx = 0
    amt_words = []
    while (wordlist[idx][0].isdigit()):
        amt_words.append(wordlist[idx])
        idx += 1
    amt = " ".join(amt_words)

    unit = wordlist[idx]
    idx += 1
    ingredient = " ".join(wordlist[idx:len(wordlist)])

    return ",".join([amt, unit, ingredient])









if __name__ == "__main__":
    main()
