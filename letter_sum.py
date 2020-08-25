word = input('Pick a word any word!! \n>').lower()

def letter_histogram(inp):
    new_dict = {}
    for letters in inp:
        if letters in new_dict:
          new_dict[letters] += 1
        else:
          new_dict[letters] = 1
    
    for key in new_dict:
        if new_dict[key] >= 1:
            print({f'{key} : {new_dict[key]}'})
            
        
letter_histogram(word)

