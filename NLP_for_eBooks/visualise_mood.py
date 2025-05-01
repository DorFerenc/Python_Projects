import glob
import streamlit as st
import plotly.express as px
import nltk

nltk.download("vader_lexicon")

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

negativity = []
positivity = []
for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
    scores = analyzer.polarity_scores(content)
    negativity.append(scores["neg"])
    positivity.append(scores["pos"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

# Check
print("Loaded files:", filepaths)
print("Dates:", dates)
print("Positivity:", positivity)
print("Negativity:", negativity)


st.title("Diary Tone")

st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,
                     labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity,
                     labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_figure)

# To run enter the project directorie and run this command: 'streamlit run visualise_mood.py'