# CORD-19 Data Analysis

This project is part of my data analysis assignment.  
It focuses on exploring the CORD-19 metadata dataset using Python and Pandas.  
The main goal is to load the data, clean it, do some analysis, and visualize basic insights about COVID-19 research papers.

---

## 🧠 What I did
- Loaded the metadata.csv file using pandas  
- Checked the structure, data types, and missing values  
- Looked at some basic statistics for the numeric columns  
- (Next steps will include cleaning, analysis, and visualizations)

---

## ⚙ How to Run
1. Make sure you have Python installed on your computer  
2. Install pandas if you don’t already have it:
   ```bash
   pip install pandas
  3.	Download the metadata.csv file from the official CORD-19 dataset
	4.	Put the file in the same folder as cord19_analysis.py
	5.	Run the script in your terminal:py cord19_analysis.py
 Note :



The metadata.csv file from the CORD-19 dataset is too large to upload here.
Please download it separately and put it in the same directory as the Python file before running it.

##  Part 3: Data Analysis and Visualization
In this part, I analyzed the cleaned CORD-19 dataset to find trends in COVID-19 research papers.
- Counted papers by publication year  
- Identified top journals publishing COVID-19 research  
- Found frequent words in paper titles  
- Created visualizations (bar charts and a word cloud) using Matplotlib and WordCloud  

The charts help show how research activity changed over time and which journals contributed the most.
## 🧩 Part 4: Streamlit Web App

For this part, I built a simple Streamlit app to explore the cleaned CORD-19 dataset.  
It lets users filter papers by publication year, see data samples, and view visualizations like bar charts and a word cloud.

### 🧠 What the app does
- Filters publications by selected year range  
- Displays a preview of the dataset  
- Shows a bar chart of papers published per year  
- Generates a word cloud from paper titles  

### ⚙ How to run the app
1. Install Streamlit (if you don’t already have it):
   ```bash
   pip install streamlit
2.  run app with :
  streamlit run app.py
3.Open the local link (http://localhost:8501) that appears in your terminal.
