def calculator():
    print(" Welcome to My Calculator ")
    
    try:
        num1 = float(input("Enter first number: "))
        op = input("Choose operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return " Cannot divide by zero!"
        else:
            return " Invalid operator!"
        
        return f" Result: {result}"

    except ValueError:
        return " Please enter valid numbers!"

print(calculator())
        
        