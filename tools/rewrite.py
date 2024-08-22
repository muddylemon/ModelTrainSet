from tools.llm import generate


def rewrite(input_string: str, additional_instructions: str = "") -> str:

    prompt = f"""
    Rewrite the following passage in your own words.
    Cover all the main points but do not include any of the original text.
    Use clear and professional language.
    {additional_instructions}
    Now return the rewritten text for the following:

    {input_string}
   """.strip()

    rewritten, _ = generate(
        prompt=prompt, model="llama3:latest", temperature=0.8, asJson=False)
    rewritten = rewritten.replace("output:", "").strip()
    return rewritten
