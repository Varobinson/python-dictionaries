word = input('Tell me something!! \n>').lower()



def word_histogram(inp):
    word_num = {}
    word_count = inp.split(' ')
    for words in word_count:
        if words in word_num.keys():
            word_num[words] += 1
        else:
            word_num[words] = 1
    return word_num


 
final = word_histogram(word)
print(final)
