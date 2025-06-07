import random
def generate_secret_code():
    """
    Generates a secret code based on settings in config.py.
    Duplicates are allowed as per the original example.
    Returns a list of strings (digits).
    """
    num = []
    for i in range(4):
        number = str(random.randint(0,9))
        num.append(number)
    return num
    pass


def calculate_feedback(secret_code, player_guess):

    """
    Calculates the number of bulls and cows for a given guess.
    - secret_code: The list of strings representing the secret code.
    - player_guess: The list of strings representing the player's guess.
    Returns a tuple: (bulls, cows)
    """

    bulls = 0
    cows = 0

    secret = list(secret_code)
    guess = list(player_guess)

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
            secret[i] = guess[i] = "-"  

    for i in range(4):
        if guess[i] != "-":
            if guess[i] in secret:
                cows += 1
                index = secret.index(guess[i])
                secret[index] = "-" 
    return bulls, cows