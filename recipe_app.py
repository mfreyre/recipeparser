from amounts import Amounts
import sys, getopt

def main(argv):
    opts, args = getopt.getopt(argv, "i:")
    for opt, arg in opts:
        if opt  == "-i":
            filename = arg

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
        if ok not in ["Y", "y"]:
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
    while (wordlist[idx][0].isdigit() or wordlist[idx].lower() in Amounts.number_words):
        amt_words.append(wordlist[idx])
        idx += 1
    amt = " ".join(amt_words)

    unit = wordlist[idx]
    idx += 1
    ingredient = " ".join(wordlist[idx:len(wordlist)])

    return ",".join([ingredient, amt, unit])









if __name__ == "__main__":
    main(sys.argv[1:])
