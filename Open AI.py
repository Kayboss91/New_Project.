
# set up the OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# define a function to generate a response
def generate_response (prompt):
    # set up the parameters for the API call
    model_engine = "davinci"
    prompt = prompt.strip()
    max_tokens = 50
    temperature = 0.5

    # generate the response using the OpenAI API
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    # return the generated text
    return response.choices[0].text.strip()

# prompt the user for input
user_input = input("What is your question? ")

# generate a response and print it to the console
response = generate_response(user_input)
print(response)
