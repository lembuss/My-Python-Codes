# program performs a split on a sentence into individual words


def mysplit(strng):
    new = []
    splitword = []
    spaces = 0
    lngth = len(strng)

    for i in range(lngth):
        if ord(strng[i]) == 32:
            spaces +=1
        else:
            continue

    start = 0
    space = ''

    for i in range(spaces+1):
        new.insert(i, [])
        for j in range(start, lngth):
            if ord(strng[j]) == 32:
                start = j + 1
                break
            else:
                new[i].append(strng[j])
        
        inter = space.join(new[i])
        splitword.append(inter)

    return splitword

# code starts here
            
sentence = input("Enter sentence to be split: ")

print(mysplit(sentence))




