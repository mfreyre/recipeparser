from amounts import Amounts

def main():
    filename = raw_input("please enter filename: ")
    if filename == "":
        filename = "testrecipe.txt"
    f = open(filename, "r")
    contents = list(f)
    f.close()


    #conversion to csv occurs here:
    for line in contents:
        wordlist = line.split()
        print line
        amt_idx = int(raw_input("where does the amount break go? "))
        amt = " ".join(wordlist[:amt_idx])

        unit_idx = int(raw_input("where does the unit break go? "))
        unit = " ".join(wordlist[amt_idx:unit_idx])

        ingredient_idx = int(raw_input("where does the ingredient break go? "))
        ingredient = " ".join(wordlist[unit_idx:ingredient_idx])
        newline = ",".join([amt, unit, ingredient])
        print newline






if __name__ == "__main__":
    main()
