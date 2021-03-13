def Convert(string): 
    li = list(string.split(" ")) 
    return li 

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

def spin_words(sentence):
    # Find how many spaces in string
    a = int(sentence.count(' '))
    
    # convert to list
    sentence_list = Convert (sentence)
    
    # initialize variables
    New_sentence = []
    count = 0
    
    #swap if less than 5 and add space if less than spaces total
    for i in sentence_list:
        if len(i) >= 5:
            New_sentence.append(i[::-1])
        else:
            New_sentence.append(i)
        count = count + 1
        
        if count <= a:
            New_sentence.append(" ")
        else:
            New_sentence.append("")
    
    New_sentence = listToString(New_sentence)
    
    # return string        
    return New_sentence   
    return None
