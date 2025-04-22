import streamlit as st
import datetime
import random
import os
import matplotlib.pyplot as plt

# --- Setup ---
st.set_page_config(page_title="Growth Mindset App", layout="centered")

# --- Sample Data ---
quotes = [
    "Mistakes are proof that you are trying.",
    "Challenges help me grow.",
    "Effort is the path to mastery.",
    "I can learn anything I put my mind to.",
    "Feedback helps me improve.",
    "Success comes from perseverance.",
    "I am a work in progress, and that’s okay."
]

challenges = [
    "Write down 3 things you did well today.",
    "Try something that scares you (a little).",
    "Ask for feedback from someone you trust.",
    "Reflect on a mistake and what you learned.",
    "Teach someone else something you know."
]

# --- Title and Quote ---
st.title("🌱 Growth Mindset App")
st.subheader("💬 Today's Growth Mindset Quote")
st.info(random.choice(quotes))

# --- Daily Check-In ---
st.subheader("🧠 How are you feeling today?")
mood = st.radio("Choose one:", ["Motivated", "Frustrated", "Curious", "Tired", "Excited"])
st.write(f"You're feeling: **{mood}**")

# --- Mindset Challenge ---
st.subheader("🧩 Growth Challenge of the Day")
st.success(random.choice(challenges))

# --- Journal Reflection ---
st.subheader("📓 Reflect on Your Day")
today = datetime.date.today()
reflection = st.text_area("What did you learn today?", height=150)
gratitude = st.text_area("What are you grateful for today?", height=100)

if st.button("Save Today's Entry"):
    with open("reflections.txt", "a") as f:
        f.write(f"{today}\nReflection: {reflection}\nGratitude: {gratitude}\n---\n")
    st.success("Your entry has been saved!")

# --- Download Journal ---
if os.path.exists("reflections.txt"):
    with open("reflections.txt", "r") as f:
        st.download_button("📁 Download Your Journal", f, file_name="growth_journal.txt")

# --- Goal Setting ---
st.subheader("🎯 Set & Track Your Goal")
goal = st.text_input("What's one area you'd like to improve?")
deadline = st.date_input("Set your goal deadline", today)
progress = st.slider("How far are you with your goal?", 0, 100)

if st.button("Save Goal"):
    with open("goals.txt", "a") as f:
        f.write(f"Goal: {goal} | Deadline: {deadline} | Progress: {progress}%\n")
    st.success("Goal saved!")

# --- Visualize Goal Progress ---
st.subheader("📊 Visual Progress Tracker")
fig, ax = plt.subplots()
ax.barh([goal], [progress], color="green")
ax.set_xlim(0, 100)
ax.set_xlabel("Progress (%)")
st.pyplot(fig)

# --- Streak Tracker (basic version) ---
st.subheader("🔥 Your Mindset Streak")
st.session_state['streak'] = st.session_state.get('streak', 0)
if st.button("✅ I completed today’s mindset tasks!"):
    st.session_state['streak'] += 1
st.write(f"Current Streak: **{st.session_state['streak']} days**")

st.markdown("---")
st.caption("Keep growing, one day at a time 🌟")
