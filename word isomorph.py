def find_pattern(word):
    chars = list(word)
    pattern = []
    for i, char1 in enumerate(chars):
        for j, char2 in enumerate(chars[i + 1 :]):
            if char1 == char2:
                distance = j + 1
                pattern.append(distance)
                break
        distance = 0
        if i == len(pattern):
            pattern.append(distance)
    return pattern


def repr_pattern(pattern):
    repr = []
    for num in pattern:
        if num == 0:
            s = "0"
            repr.append(s)
        else:
            s = "+" + str(num)
            repr.append(s)
    repr = " ".join(repr)
    return repr


word_pairs = []
with open("isomorph_input.txt") as f:
    f.readline()
    for line in f:
        word_pair = line.split()
        word_pairs.append(word_pair)

for word_pair in word_pairs:
    words = ", ".join(word_pair)
    if len(word_pair[0]) != len(word_pair[1]):
        print(f"{words} have different lengths")
    elif find_pattern(word_pair[0]) == find_pattern(word_pair[1]):
        pattern = repr_pattern(find_pattern(word_pair[0]))
        print(f"{words} are isomorphs with repetition pattern {pattern}")
    else:
        print(f"{words} are not isomorphs")
