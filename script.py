# Submit passage to drill
print("===== INPUT YOUR PASSAGE =====")
# passage = """The classical view of a viral infection doesn't create much opportunity for social interaction. A single virus particle, or virion, encounters a target cell and breaks and enters. Once inside, it disassembles like a cat burglar unpacking tools and then executes its potentially deadly genetic program."""
passage = input("Please input your passage:")
while passage[-1] != '.':
    passage = input("Passage does not end with full-stop. Please input your passage again:")

# Separates passage into sentences
# Ignore last element because split by . gives empty str at end
# Assume all sentence end with .
sentences = passage.replace(". ", ".").split(".")[:-1]
sentences = [sentence + '.' for sentence in sentences]


# Submit hints for sentence recall
print("\n===== INPUT YOUR HINTS =====")
hints = []
for i, sentence in enumerate(sentences):
    print(f"{i+1}.{sentence}")
    hint = input("Please input hints: ")
    hints.append(hint)


import os
max_error = 100
while max_error > 20:
    os.system('cls||clear')
    print("\n===== INPUT YOUR ANSWERS =====")
    max_error = 0
    # Submit answers for sentence recall based on hints
    answers = []
    for hint in hints:
        print("Hint:", hint)
        answer = input("Type original sentence: ")
        answers.append(answer)

    print("\n===== VIEW YOUR RESULTS =====")

    # Comparing sentences and answers to calculate error %
    import difflib
    for sentence, answer in zip(sentences, answers):
        fix = []
        joined = []
        mistakes = 0

        # character is formatted as "+ c" if there is an additional 'c' in the answer.
        # character is formatted as "- d" if there is a missing 'd' in the answer.
        # character is formatted as "  e" if the character 'e' is correct in the answer.
        for i, character in enumerate(difflib.ndiff(sentence, answer)):
            fix.append(character[0])
            joined.append(character[2])

            if character[0] == "+" or character[0] == "-":
                mistakes += 1

        error = mistakes / len(sentence) * 100
        max_error = max(max_error, error)
        print(f"Error: {error:.2f}%")
        print("Original:\t", sentence)
        print("Answer:\t\t", answer)
        print("Difference:")
        print("\t\t " + ''.join(joined))
        print("\t\t " + ''.join(fix))

    input("Press any key to continue:")



# import re
# tokens = re.findall(r"[\w']+|[.,!?;]", passage)
# print(tokens)