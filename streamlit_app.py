import streamlit as st
import difflib


def compute_error(sentence, answer):
    fix = []
    joined = []
    mistakes = 0
    for i, character in enumerate(difflib.ndiff(sentence, answer)):
        fix.append(character[0])
        joined.append(character[2])

        if character[0] == "+" or character[0] == "-":
            mistakes += 1
    error = mistakes / len(sentence) * 100
    return error, ''.join(joined), ''.join(fix)


st.title("Typing Driller")

example = """The classical view of a viral infection doesn't create much opportunity for social interaction. A single 
virus particle, or virion, encounters a target cell and breaks and enters. Once inside, it disassembles like a cat 
burglar unpacking tools and then executes its potentially deadly genetic program. """

with st.beta_expander("Passage and Hints", expanded=True):
    passage = st.text_area("Please insert a passage:")

    if passage != "" and passage[-1] != '.':
        st.error("Passage does not end with full-stop. Please input your passage again")

    sentences = passage.replace(". ", ".").split(".")[:-1]
    sentences = [sentence + '.' for sentence in sentences]

    hints = []
    for i, sentence in enumerate(sentences):
        hint = st.text_input(f"Sentence {i+1}: {sentence}")
        hints.append(hint)

st.text("When you are ready, hide the passage and hints!")

if st.checkbox("Ready?"):
    if passage == "":
        st.error("Please insert a passage.")
    else:
        st.text("Type original sentences:")

    for i, (hint, sentence) in enumerate(zip(hints, sentences)):
        answer = st.text_input(f"Hint: {hint}\n", key=str(i)+'hints')

        if st.checkbox("Answer", key=str(i)+answer):
            error, joined, fixed = compute_error(sentence, answer)
            st.text(f"Error: {error:.2f}%")
            st.text(f"Original: {sentence}")
            st.text(f"Answer: {answer}")
            st.text("Difference:")
            st.text(joined)
            st.text(fixed)
