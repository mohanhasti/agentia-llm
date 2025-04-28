#calculator tool
def calculator_tool(expression):
    try:
        result = eval(expression)
        return f"The result of the expression '{expression}' is: {result}"
    except Exception as e:
        return f"Error: {str(e)}. Please provide a valid mathematical expression."