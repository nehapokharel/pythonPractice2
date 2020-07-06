class FindSumZero():

    def __init__(self, value):
        self.value = value

    def sum_zero(self, array_list, n):   
        self.array_list = array_list
        self.n = n
        for i in range(0, self.n-2): 
        
            for j in range(i+1, self.n-1): 
            
                for k in range(j+1, self.n): 
                
                    if (self.array_list[i] + self.array_list[j] + self.array_list[k] == 0): 
                        print(self.array_list[i], self.array_list[j], self.array_list[k]) 
                        self.value = True
        
        if (self.value == False): 
            print(" do not exist ") 
  

arr = [0, -1, 2, -3, 1] 
n = len(arr) 
x = FindSumZero(True)
x.sum_zero(arr, n) 