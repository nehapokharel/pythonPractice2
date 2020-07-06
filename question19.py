def check_parentheses(braces):
    brackets=['()','{}','[]']
    while any(x in braces for x in brackets):
        for br in brackets:
            braces = braces.replace(br,'')
    return not braces

b= input("Enter braces ")
x = check_parentheses(b)
if x:
    print("Valid")
else:
    print("Invalid")
