import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("A simple app to explore COVID-19 research papers metadata")

# Load data
data = pd.read_csv("metadata_cleaned_sample.csv")

# Year filter
years = sorted(data["publish_time"].dropna().astype(str).str[:4].unique())
year_range = st.slider("Select year range", int(min(years)), int(max(years)), (2020, 2021))

# Filter out rows with missing or invalid years before applying the slider
data["year"] = pd.to_numeric(data["publish_time"].astype(str).str[:4], errors="coerce")
filtered = data[data["year"].between(*year_range, inclusive="both")]

# Show data sample
st.subheader("Sample of Data")
st.write(filtered.head())

# Publication count
st.subheader("Publications by Year")
year_counts = filtered["publish_time"].astype(str).str[:4].value_counts().sort_index()
st.bar_chart(year_counts)

# Word cloud of titles
st.subheader("Word Cloud of Titles")
text = " ".join(filtered["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
st.image(wordcloud.to_array())
