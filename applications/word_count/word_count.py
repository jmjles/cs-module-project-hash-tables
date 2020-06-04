def word_count(s):
    # Your code here
    if s == '':
        return {}

    ignore = [':',';',',','.','-','+','=','/', '\\','|','[',']','{','}','(',')','*','^','&','"']

    for symbole in ignore:
        s = s.replace(symbole,"")

    special = ['\r', '\n', '\t']
    
    for symbole in special:
        s = s.replace(symbole," ")

    words = {}
    string = s.lower().split(" ")

    

    
        
    for s in string:
        if words.get(s) is not None:
            words[s] += 1
        elif s == "":
            continue
        else:
            words[s] = 1
    return words


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("a a\ra\na\ta \t\r\n"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
