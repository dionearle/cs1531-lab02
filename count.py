'''
 Exercise 3:
 Given a paragraph of text,
 1. count the number of times each character occurs in the text,
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''

def count_char(text):

    char_occurs = {}
    for i in text:
        if i in char_occurs:
            char_occurs[i] += 1
        else:
            char_occurs.update({i:1})

    for j in char_occurs:
        print(f"{j} {char_occurs[j]}")

def count_char_insensitive(text):

    text = text.lower()
    char_occurs = {}
    for i in text:
        if i in char_occurs:
            char_occurs[i] += 1
        else:
            char_occurs.update({i:1})

    for j in char_occurs:
        print(f"{j} {char_occurs[j]}")


def count_char_ordered(text):

    text = text.lower()
    char_occurs = {}
    for i in text:
        if i in char_occurs:
            char_occurs[i] += 1
        else:
            char_occurs.update({i:1})

    new_dict = sorted(char_occurs.items(), key=lambda x: x[1])
    new_dict = new_dict[::-1]
    length = len(new_dict)

    p = 0
    while (p < length):
        print(f"{new_dict[p][0]} {new_dict[p][1]}")
        p += 1

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
#count_char(text2)
#count_char_insensitive(text2)
count_char_ordered(text2)
