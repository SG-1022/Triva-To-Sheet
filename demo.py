import streamlit as st
from Sheet import SheetIt


# This is an example website to show questions as if a trivia.
#
# BEFORE YOU RUN THIS, RUN main.py FOR SOME TIME,
# AND TO BE QUICK, CHANGE seconds TO -1
#
#
# To see the result, in the terminal, run
# 'pip install -r requirements.txt'
# if doesn't work, first run
# 'python -m venv venv'
#
# after that, run
# 'streamlit run demo.py'
# and click this link, then you will be taken to the website
# and the to close it,
# click on the terminal,
# then press Ctrl+C

sheet = SheetIt()

if "question" not in st.session_state:
    st.session_state["question"] = sheet.get_random_question()

question = st.session_state["question"]

st.title("Demo Quiz")

answer_to_text = lambda answer, letter: f"{letter}: {answer}"

answer_1 = answer_to_text(question["answer #1"], letter="a")
answer_2 = answer_to_text(question["answer #2"], letter="b")
answer_3 = answer_to_text(question["answer #3"], letter="c")
answer_4 = answer_to_text(question["answer #4"], letter="d")
correct_answer = question["answer"]

with st.form(key="Demo Form", enter_to_submit=True):
    st.subheader(question["question"])

    answer_chosen = st.radio("Answers:", key="answer #1", options=(answer_1, answer_2, answer_3, answer_4))


    submitted = st.form_submit_button()

if submitted and answer_chosen in (answer_1, answer_2, answer_3, answer_4):
    if answer_chosen.endswith(correct_answer):
        st.success(f"Correct! The correct answer is {correct_answer}")
        st.balloons()
    else:
        st.error(f"Incorrect. The correct answer is {correct_answer}")

if st.button("New Question"):
    new_question = sheet.get_random_question()
    st.session_state["question"] = new_question
    st.rerun()