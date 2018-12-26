import random

WORDS = (
                "treehouse",
                "python",
                "learner",
)

def prompt_for_words(chalenge):
    gueses = set()
    print("what words can you find in a word {}".format(chalenge))
    print("(Enter Q to quit)")
    while True:
        guess = input("{} words> ".format(len(gueses)))
        if guess.upper() == 'Q':
            break
        gueses.add(guess.lower())
    return gueses

challenge_word = random.choice(WORDS)

def output_results(results):
    for word in results:
        print("* " + word)


player_1_words = prompt_for_words(challenge_word)
player_2_words = prompt_for_words(challenge_word)

print("Player 1 Resulds:")
player_1_unique = player_1_words - player_2_words
print("{} gueses, {} unique".format(len(player_1_words), len(player_1_words - player_1_unique)))
output_results(player_1_unique)
print("-" * 10)
player_2_unique = player_2_words - player_1_words
print("{} gueses, {} unique".format(len(player_2_words), len(player_2_words - player_2_unique)))
output_results(player_2_unique)

print("Shared gueses")
shared_words= player_1_words.intersection(player_2_words)
output_results(shared_words)
