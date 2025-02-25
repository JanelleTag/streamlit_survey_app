import streamlit as st
import csv
import os

# Check if the CSV file exists and create it if it does not
file_name = 'survey_responses.csv'
if not os.path.isfile(file_name):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            "First Name", "Last Name", "Age", "City", "Occupation",
            "Three Things", "Word Connection", "Dream Job", "Job Value", "Problem Solving",
            "Cultural Impact", "Subject Interest", "Perfect Work Life", "Greatest Strength",
            "Preferred Company", "Enjoyable Activity", "Learning Interest", "Curiosity",
            "Good At", "Work Preference", "Creative vs Helping", "Top Values",
            "Ideal Work Environment", "Money No Object", "Future Success"
        ])

# Title for your app
st.title("Discover Your Path Survey")

# Creating a simple form
with st.form("survey_form"):
    st.write("Please answer the following questions to help us understand your interests and aspirations:")

    # Personal Information Section
    st.subheader("Please provide your personal information:")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    city = st.text_input("City")
    occupation = st.text_input("Occupation or what best represents you if not employed")

    # Section Header: Character
    st.subheader("This section measures your character:")
    three_things = st.text_input("1. What are 3 things you enjoy doing in your free time that make you lose track of time?")
    word_connection = st.radio("2. Which of these words connect most with you?", ('Creativity', 'Helping others', 'Freedom', 'Stability'))
    dream_job = st.text_input("3. If you could wake up tomorrow and have any job in the world, what would it be?")
    job_value = st.radio("4. What do you value most in a job: the benefits or the work itself?", ('The benefits', 'The work itself'))

    # Additional sections and questions follow the same pattern...
    problem_solving = st.radio("5. When you have problems, how do you solve them?", ('Break them down into steps', 'Seek advice from others', 'Trust my instincts', 'Research to understand the problem'))
    cultural_impact = st.text_input("6. How does your culture affect the way you work and get along with others?")
    subject_interest = st.radio(
        "7. Which of these subjects would you enjoy learning more about?",
        ('Marketing and branding (like working in advertising)', 'Psychology and understanding people (like being a counselor)', 'Technology and gadgets (like being a tech support specialist)', 'Business and finance (like working as a financial advisor)'))
    perfect_work_life = st.text_input("8. If you could create your perfect work life, what would it be like?")
    greatest_strength = st.radio("9. What is your greatest strength?", ('Creativity', 'Talking to people', 'Solving puzzles', 'Being organized'))
    preferred_company = st.radio(
        "10. What kind of people do you enjoy being around?",
        ('Dreamers', 'Friendly folks', 'Self-starters', 'Focused achievers'))
    enjoyable_activity = st.radio(
        "11. Which of these activities sounds most enjoyable to you right now?",
        ('Starting a fun project', 'Helping someone', 'Learning a new hobby', 'Sorting things out'))
    learning_interest = st.text_input("12. What’s something you’ve always wanted to learn or try but haven’t had the chance to yet?")
    curiosity = st.text_input("13. What do you feel most curious about, and why?")
    good_at = st.text_input("14. Have you ever done something that made you realize you were really good at it? What was it?")
    work_preference = st.radio("15. Do you like to work alone or with others?", ('Alone', 'With others'))
    creative_helping = st.text_input("16. If you had to choose between helping people or being creative every day, which would you choose?")
    top_values = st.text_input("17. What are the top 3 values or principles that matter most to you in life?")
    ideal_work_env = st.text_input("18. When you think of your ideal work environment, what does it look like?")
    money_no_object = st.text_input("19. If money was no object, how would you spend your time?")
    future_success = st.text_input("20. What do you hope people will say about your future success?")

    # Submission button
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Save data to CSV file
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                first_name, last_name, age, city, occupation,
                three_things, word_connection, dream_job, job_value, problem_solving,
                cultural_impact, subject_interest, perfect_work_life, greatest_strength,
                preferred_company, enjoyable_activity, learning_interest, curiosity,
                good_at, work_preference, creative_helping, top_values,
                ideal_work_env, money_no_object, future_success
            ])
        st.write("Thank you for participating!")
