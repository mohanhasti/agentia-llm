tools = [
    {
        "type": "function",
        "name": "calculator_tool",
        "description": "A calculator tool that evaluates mathematical calculations like addition, subtraction, multiplication, or division.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A mathematical expression to evaluate. For example: 2 + 2, 3 * 4, etc.",
                },
            },
            "required": ["expression"],
        },
    }
]

