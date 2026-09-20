import streamlit as st
from huggingface_hub import InferenceClient

st.title("MCQ Generator")

topic = st.text_input("Enter the topic")

number = st.number_input(
    "Number of questions",
    min_value=1,
    max_value=10,
    value=5
)

difficulty = st.selectbox(
    "Select difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.button("Generate MCQs"):

    if topic == "":
        st.warning("Please enter a topic.")

    else:

        prompt = f"""
        Generate {number} multiple choice questions
        about {topic}.

        Difficulty level: {difficulty}

        Each question must contain:
        - Question
        - Four options: A, B, C, D
        - Correct answer

        Use this format:

        Question 1:
        A.
        B.
        C.
        D.
        Answer:

        Generate exactly {number} questions.
        """

        try:

            client = InferenceClient(
                api_key=st.secrets["Access_Token"]
            )

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=2000
            )

            result = response.choices[0].message.content

            st.subheader("Generated Questions")

            st.write(result)

        except Exception as e:

            st.error("Error generating questions")
            st.write(e)