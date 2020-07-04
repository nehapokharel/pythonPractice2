def is_prime(number):
    if number > 1:  
        for i in range(2,number):  
            if (number % i) == 0:  
                return False 
                break  
            else:  
                return True
                break               
    else:  
        return False

num = int(input('Enter number: '))
z = is_prime(num)
print(z)