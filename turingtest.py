import random

def human_response(question):
    responses = {
        "how are you?" : "I'm fine, just a bit tired and feelin sleepy.", 
        "What are ur hobbies?" : "I enjoy playing basketball, painting, and watching netflix.",
        "What is 3+5?" : "It's 8, duh!"
    }
    return responses.get(question.lower(), "Hmm, I haven't thought about that.")

def ai_response(question):
    responses = {
        "how are you": "I am functioning within normal parameters.",
        "What are your hobbies?" : "I do not possess hobbies.",
        "What is 3+5?" : "The result is 8."
    }
    return responses.get(question.lower(), "Unable to process input.")

def turing_test():
    agent = random.choice(["human","ai"])

    question = input("Judge: Ask a question:  ")

    if agent == "human":
        answer = human_response(question)
    else: 
        answer = ai_response(question)

    print("\nResponse:" , answer)
    guess = input("\nIs it Human or AI? ").lower()

    if guess == agent:
        print("Correct Guess!")
    else:
        print("Wrong guess! :(")

turing_test()