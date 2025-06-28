import streamlit as st

def iq_test():
    st.header("🧠 Welcome to EduTrack - IQ Test\n")

    questions = [
        {"q": "What comes next in the sequence? 2, 4, 8, 16, ?", "a": "32", "explanation": "Each number is multiplied by 2."},
        {"q": "Which word doesn't belong? Apple, Banana, Carrot, Mango", "a": "carrot", "explanation": "Carrot is a vegetable; the others are fruits."},
        {"q": "If ALL CATS are ANIMALS and SOME ANIMALS are PETS, can we say ALL CATS are PETS?", "a": "no", "explanation": "No, not all animals are necessarily pets."},
        {"q": "Find the odd one out: 3, 5, 7, 9, 11", "a": "9", "explanation": "All are prime numbers except 9."},
        {"q": "What is the missing number? 1, 4, 9, 16, ?, 36", "a": "25", "explanation": "These are squares of 1, 2, 3, 4, 5, 6."},
        {"q": "If you rearrange the letters “CIFAIPC” you get the name of a:", "a": "pacific", "explanation": "It's an anagram."},
        {"q": "Which number is the odd one out? 121, 144, 169, 196, 225, 242", "a": "242", "explanation": "All others are perfect squares."},
        {"q": "A clock shows 3:15. What is the angle between the hour and minute hands? (in degrees)", "a": "7.5", "explanation": "Hour hand moves 0.5° per minute. At 3:15, it's 7.5° past 3."},
        {"q": "If it takes 5 machines 5 minutes to make 5 widgets, how long for 100 machines to make 100 widgets?", "a": "5 minutes", "explanation": "Each machine makes 1 widget in 5 minutes."},
        {"q": "Which number logically replaces the question mark? 6 → 36, 7 → 49, 8 → ?", "a": "64", "explanation": "Each number is squared."},
        {"q": "What comes next? J, F, M, A, M, J, ?", "a": "j", "explanation": "First letters of months: January to July."},
        {"q": "You see a boat filled with people. It hasn't sunk, but when you look again you don't see a single person. Why?", "a": "all were married", "explanation": "Single is a play on words."},
        {"q": "Which number is missing? 2, 6, 12, 20, ?", "a": "30", "explanation": "Add 4, 6, 8, 10..."},
        {"q": "If TWO is written as 420, and TEN is 520, what is ONE?", "a": "320", "explanation": "T=100, W=200, O=100, etc. (Pattern-based logic)"},
        {"q": "What is the next number in the series? 1, 1, 2, 3, 5, ?", "a": "8", "explanation": "Fibonacci sequence: each number is the sum of the two preceding ones."},
        {"q": "If you have a cube with a side length of 3 cm, what is its volume?", "a": "27", "explanation": "Volume = side³ = 3³ = 27."},
        {"q": "A farmer has 17 sheep and all but 9 die. How many are left?", "a": "9", "explanation": "All but 9 means 9 are still alive."},
        {"q": "What is the next letter in this sequence? A, C, E, G, ?", "a": "i", "explanation": "Every second letter in the alphabet."},
        {"q": "A man has 53 socks in his drawer: 21 identical blue, 15 identical black, and 17 identical red. How many socks must he take out to ensure he has a pair of the same color?", "a": "4", "explanation": "Worst case: 1 of each color. The 4th guarantees a pair."},
    ]

    with st.form("iq_form"):
        user_answers = []
        for i, q in enumerate(questions, 1):
            ans = st.text_input(f"Q{i}: {q['q']}", key=f"q{i}")
            user_answers.append(ans)
        submitted = st.form_submit_button("Submit")

        if submitted:
            score = 0
            for i, q in enumerate(questions):
                user_ans = user_answers[i].strip().lower()
                correct_ans = q['a'].strip().lower()
                st.write(f"**Q{i+1}: {q['q']}**")
                if user_ans == correct_ans:
                    st.success("✅ Correct!")
                    score += 1
                else:
                    st.error(f"❌ Incorrect! Correct Answer: {q['a']}")
                    st.info(f"Explanation: {q['explanation']}")
                st.write("---")

            percent = (score / len(questions)) * 100
            if percent >= 80:
                level = "Genius Thinker"
            elif percent >= 60:
                level = "Advanced Thinker"
            elif percent >= 40:
                level = "Moderate Thinker"
            else:
                level = "Beginner Thinker"
            st.balloons()
            st.write(f"🎉 You answered {score} out of {len(questions)} questions correctly!")
            st.write(f"\n✅ IQ Score: {percent:.2f}%")
            st.write(f"🧠 Level: {level}\n")

            # Store answers in session state for analysis
            st.session_state["iq_answers"] = user_answers
            st.session_state["iq_score"] = percent  # percent should be out of 100
            st.session_state["iq_level"] = level

            return percent, level
        




if __name__ == "__main__":
    iq_test()
