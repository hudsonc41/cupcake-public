from random import choice


def encode(g):
    k = r = 0
    digits = list(g)
    for digit in digits:
        digit = int(digit)
        d = (3 * digit + 7) % 10
        r = r + 2 ** (3 * d + 2) + (k * 8**d)
        k += 1
    return r


def match(gcode, scode):
    b = c = ""
    for k in range(10):
        p = int(gcode / (8**k)) % 8
        q = int(scode / (8**k)) % 8
        r = p - q
        s = (2 * r) + (3 * q)
        if s > 11 and s > (2 * r):
            if s == 3 * p:
                b += "B"
            else:
                c += "C"
    return b + c


def generate_candidates():
    candidates = []
    for char in list("0123456789"):
        for i in range(100, 1000):
            str_num = char + str(i)
            num_digits = list(str(str_num))
            if len(set(num_digits)) == 4:
                candidates.append(str_num)
    return candidates


def reduce_candidates(score):
    new_candidates = []
    for candidate in candidates:
        candidate_code = encode(candidate)
        candidate_score = match(guess_code, candidate_code)
        if candidate_score == score:
            new_candidates.append(candidate)
    return new_candidates


candidates = generate_candidates()
answer_code = 12748856
guesses = 0
guess = choice(candidates)
guess_code = encode(guess)
while len(candidates) > 1:
    guesses += 1
    guess_code = encode(guess)
    score = match(guess_code, answer_code)
    candidates = reduce_candidates(score)
    print(
        f"Guess {guesses} {guess} gives {score} Candidates remaining: {len(candidates)}"
    )
    if len(candidates) % 2 != 0:
        middle_element_i = int((len(candidates) + 1) / 2 - 1)
    else:
        middle_element_i = int(len(candidates) / 2)
    guess = candidates[middle_element_i]
print(f"Solution: {guess}")

print(f'hi {encode("9862")}')
print(match(941099524, 939547652))
