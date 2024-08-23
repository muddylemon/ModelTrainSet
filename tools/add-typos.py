from tools.llm import generate


def addTypos(input_string: str, additional_instructions: str = "") -> str:

    prompt = f"""
    Return the following passage exactly as written except introduce one or more subtle typos, misspellings or other mistakes.
    {additional_instructions}
    Now return the rewritten text for the following:

    {input_string}
   """.strip()

    rewritten, _ = generate(
        prompt=prompt, model="llama3:latest", temperature=0.8, asJson=False)
    rewritten = rewritten.replace("output:", "").strip()
    return rewritten
