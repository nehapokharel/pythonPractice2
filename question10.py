def snake_case(word):
    snake_case = [word[0].lower()]
    
    for letter in word[1:]:
        if letter == letter.upper():
            snake_case.append("_")
            snake_case.append(letter.lower())
        else:
            snake_case.append(letter)
    
    print(''.join(snake_case))


def kebab_case(word):
    kebab_case = [word[0].lower()]

    for letter in word[1:]:
        if letter == letter.upper():            
            kebab_case.append("-")
            kebab_case.append(letter.lower())
        else:
            kebab_case.append(letter)

    print(''.join(kebab_case))


snake_case('ThisIsCamelCased')
kebab_case('ThisIsCamelCased')