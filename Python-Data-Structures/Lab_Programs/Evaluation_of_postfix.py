def evaluate_postfix(expression):
    stack=[]

    for token in expression.split():

        if token.isdigit():
            stack.append(int(token))

        else: 
            a=stack.pop()
            b=stack.pop()

            if token == '+':
                stack.append(a+b)
            elif token == '-':
                stack.append(a-b)
            elif token == '*':
                stack.append(a*b)
            elif token =='/':
                stack.append(a/b)

    return stack.pop()

expression = "3 2 + 5 2 *"

result=evaluate_postfix(expression)

print("Postfix Expression:",expression)
print("Result:",result)
