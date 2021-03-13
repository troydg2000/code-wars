def pig_it(text):
    sentence = []
    count = 0
    for i in text.split(" "):
        count+=1
        #j = list(i)
        j = i[1:]+i[0]
        
        if '?' in i: 
            j = j 
        elif '!' in i:
            j = j
        else: 
            j = j + "ay"
    
        sentence.append(j)
        if count < len(text.split(" ")):
            sentence.append(" ")
        else:
            sentence.append('')
    return ''.join(sentence)
