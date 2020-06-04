def no_dups(s):
    # Your code here
    if s == "":
        return s
    string = s.split(" ")
    cashe = {}

    i = 0
    while i < len(string):
        if cashe.get(string[i]) is not None:
            del string[i]
            i -= 1
        else:
            cashe[string[i]] = string[i]
        i += 1

    result = " ".join(string)

    # str(string).replace(',', '').replace("'","").replace("[","").replace("]","")
    
    return result



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
