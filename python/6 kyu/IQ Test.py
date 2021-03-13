def iq_test(numbers):
    number = [int(i) for i in numbers.split(" ")]
     
    even = 0 
    odd = 0
    for i in number:
        
        if (i % 2) == 0:
            even = even + 1
        else:
            odd = odd +1
     
    if odd > even:
        even_nos = [number.index(num) +1 for num in number if num % 2 == 0] 
        return even_nos[0]
    else:
        even_nos = [number.index(num) +1 for num in number if num % 2 != 0] 
        return even_nos[0]
