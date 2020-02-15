def print_lol(the_list, indent, level=0):
    for each in the_list:
        if isinstance(each, list):
            print_lol(each, indent, level+1)
        else:
            if  indent:
                for tabnum in range(level):
                    print("\t", end="")
            print(each)
