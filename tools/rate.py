from tools.llm import generate

default_rating_system = """
Instructions:
Rate the content on a scale of 1 to 10
Content considered excellent and near perfect should be awarded 10
Content that is poorly written, full of mistakes and poorly communicate their message should be awarded 1
Your criteria is readability, communication effectiveness and literary style.
"""


def rate(input_string: str, additional_instructions: str = default_rating_system) -> str:

    prompt = f"""
Rate the following input fairly. Consider the input carefully before rendering a decision
{additional_instructions}


return your rating as a JSON object in this schema:

    [{
        "content": "Original content, truncated to no more than 500 characters...",
        "reason": "Detail your reasoning for your rating in a short paragraph.",
        "rating": 5
    }]


Now return the rating for the following content:

    {input_string}
""".strip()

    rating, _ = generate(
        prompt=prompt, model="llama3:latest", temperature=0.8, asJson=True)

    # rating should be in correct schema
    if

    return rating
