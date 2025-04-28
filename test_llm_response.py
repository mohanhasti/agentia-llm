# if LLM detects a function call, it will return a response with the function call details.
res_function_call = Response(
    id="resp_680ec444bd548191a1e082e353b3c5640c92cfa0600093ab",
    created_at=1745798212.0,
    error=None,
    incomplete_details=None,
    instructions=None,
    metadata={},
    model="gpt-3.5-turbo-0125",
    object="response",
    output=[
        ResponseFunctionToolCall(
            arguments='{"expression":"1 * 3"}',
            call_id="call_2swLDavb9HNI4JKsjIEcVPYS",
            name="calculator_tool",
            type="function_call",
            id="fc_680ec44594948191b702131e69f7cd090c92cfa0600093ab",
            status="completed",
        )
    ],
    parallel_tool_calls=True,
    temperature=0.0,
    tool_choice="auto",
    tools=[
        FunctionTool(
            name="calculator_tool",
            parameters={
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A mathematical expression to evaluate. For example: 2 + 2, 3 * 4, etc.",
                    }
                },
                "required": ["expression"],
            },
            strict=True,
            type="function",
            description="A calculator tool that evaluates mathematical calculations like addition, subtraction, multiplication, or division.",
        )
    ],
    top_p=1.0,
    max_output_tokens=150,
    previous_response_id=None,
    reasoning=Reasoning(effort=None, generate_summary=None, summary=None),
    service_tier="default",
    status="completed",
    text=ResponseTextConfig(format=ResponseFormatText(type="text")),
    truncation="disabled",
    usage=ResponseUsage(
        input_tokens=79,
        input_tokens_details=InputTokensDetails(cached_tokens=0),
        output_tokens=19,
        output_tokens_details=OutputTokensDetails(reasoning_tokens=0),
        total_tokens=98,
    ),
    user=None,
    store=True,
)
# if LLM detects a text response, it will return a response with the text response details.
res_text = Response(
    id="resp_680ec347c8a48191ba8dbd9c6f5c8eb309c0f2f1449b8c01",
    created_at=1745797959.0,
    error=None,
    incomplete_details=None,
    instructions=None,
    metadata={},
    model="gpt-3.5-turbo-0125",
    object="response",
    output=[
        ResponseOutputMessage(
            id="msg_680ec34cae3c8191b78e8fbe49e6589a09c0f2f1449b8c01",
            content=[
                ResponseOutputText(
                    annotations=[],
                    text="Hello! How can I assist you today?",
                    type="output_text",
                )
            ],
            role="assistant",
            status="completed",
            type="message",
        )
    ],
    parallel_tool_calls=True,
    temperature=0.0,
    tool_choice="auto",
    tools=[
        FunctionTool(
            name="calculator_tool",
            parameters={
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A mathematical expression to evaluate. For example: 2 + 2, 3 * 4, etc.",
                    }
                },
                "required": ["expression"],
            },
            strict=True,
            type="function",
            description="A calculator tool that evaluates mathematical calculations like addition, subtraction, multiplication, or division.",
        )
    ],
    top_p=1.0,
    max_output_tokens=150,
    previous_response_id=None,
    reasoning=Reasoning(effort=None, generate_summary=None, summary=None),
    service_tier="default",
    status="completed",
    text=ResponseTextConfig(format=ResponseFormatText(type="text")),
    truncation="disabled",
    usage=ResponseUsage(
        input_tokens=75,
        input_tokens_details=InputTokensDetails(cached_tokens=0),
        output_tokens=11,
        output_tokens_details=OutputTokensDetails(reasoning_tokens=0),
        total_tokens=86,
    ),
    user=None,
    store=True,
)
