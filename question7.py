info_list  = [('krish', 'sapkota', 23), ('neha', 'pokharel', 22), ('sujan', 'k.c', 22), ('zyan', 'malla', None), ('sisu', 'malla', 24)]

age = [x[2] for x in info_list]
total_age = 0

for i in range(len(age)):
    if age[i] == None:
        age[i] = 0
    total_age +=age[i] 
print(total_age)