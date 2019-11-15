def isfunny(word):
    word = input('Enter one word: ')
    revword = word[::-1]
    length = len(word)
    for i in range(length):
        w = abs(ord(word[i] - word[i-1]))
        rw = abs(ord(revword[i] - revword[i-1]))
        if  w != rw :
            print('Not funny')
            break
        else:
            print('Funny')
    
