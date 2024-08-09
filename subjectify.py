from llm import generate


def subjectify(input_string: str) -> str:

    prompt = f"""return the general subject of the given text in one word or short phrase not more than five words.
    return only the word phrase, do not include output: or any other text except the word or short phrase.
    
    Examples:
    input: i can count all the good software abstractions ever written on two hands
    output: software abstractions
    input: I want every rich person in this country to see what Flavor Flav is doing and understand, THAT is what you are supposed to be doing with your excess wealth. Sponsor athletes, sponsor art, spend your money on things for the collective without looking for a ROI. The ROI is cultural.
    output: Flavor Fav wealth
    input: The sun is shining over the verdant hills of Africa.
    output: sunshine over African hills

    Now return the subject of the following text:
    {input_string}
   """

    subject, _ = generate(prompt=prompt, model="internlm2:latest",
                          num_predict=50, temperature=0.3, asJson=False)
    # if output: in subject, remove it
    subject = subject.replace("output:", "").strip()
    return subject
