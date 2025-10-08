import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("📘 CORD-19 Data Explorer")
st.write("A simple Streamlit app to explore COVID-19 research papers.")

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("metadata_cleaned_sample.csv")
    return data

data = load_data()

# Show a sample
st.subheader("📋 Sample Data")
st.dataframe(data.head())

# Year filter
st.subheader("📅 Filter by Publication Year")
years = sorted(data['publish_time'].astype(str).str[:4].dropna().unique())

# Convert years safely to int
years_int = [int(y) for y in years if y.isdigit()]
if years_int:
    year_range = st.slider("Select year range", min(years_int), max(years_int), (2020, 2021))
    filtered_data = data[data['publish_time'].astype(str).str[:4].astype(int).between(year_range[0], year_range[1])]
else:
    st.warning("No valid year data found.")
    filtered_data = data

st.write(f"Showing data for years {year_range[0]}–{year_range[1]}" if years_int else "Showing all data")
st.dataframe(filtered_data.head())

# Visualization 1: Papers by year
st.subheader("📊 Publications Over Time")
year_counts = filtered_data['publish_time'].astype(str).str[:4].value_counts().sort_index()

if not year_counts.empty:
    fig1, ax1 = plt.subplots()
    year_counts.plot(kind='bar', ax=ax1)
    ax1.set_title("Number of Publications Over Time")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Number of Papers")
    st.pyplot(fig1)
else:
    st.info("No data available for year visualization.")

# Visualization 2: Top journals
st.subheader("🏛 Top Journals")
top_journals = filtered_data['journal'].value_counts().head(10)

if not top_journals.empty:
    fig2, ax2 = plt.subplots()
    top_journals.plot(kind='bar', ax=ax2)
    ax2.set_title("Top 10 Journals Publishing COVID-19 Research")
    ax2.set_xlabel("Journal")
    ax2.set_ylabel("Number of Papers")
    st.pyplot(fig2)
else:
    st.info("No journal data available.")

# Visualization 3: Word Cloud
st.subheader("☁ Common Words in Paper Titles")
titles = " ".join(filtered_data['title'].dropna().astype(str))

if titles.strip():
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.imshow(wordcloud, interpolation='bilinear')
    ax3.axis("off")
    st.pyplot(fig3)
else:
    st.info("No title data available for word cloud.")