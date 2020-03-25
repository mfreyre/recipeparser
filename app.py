def main():
    filename = raw_input("please enter filename: ")
    print filename
    f = open(filename, "r")
    contents = list(f)
    f.close()
    for line in contents:
        print line




if __name__ == "__main__":
    main()
