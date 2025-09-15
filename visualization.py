import streamlit as st
import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

st.title("Text File Word Frequency Visualizer")

# 1. File uploader
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file:
    # 2. Read and clean text
    text = uploaded_file.read().decode("utf-8")
    words = re.findall(r"\b\w+\b", text.lower())   # extract words, case-insensitive
    freq = Counter(words)

    # Convert to DataFrame for easier display
    df = pd.DataFrame(freq.items(), columns=["Word", "Count"]).sort_values(
        by="Count", ascending=False
    )

    # --- Table ---
    st.subheader("Word Frequency Table")
    st.dataframe(df.reset_index(drop=True))

    # --- Histogram ---
    st.subheader("Histogram of Word Counts")
    fig_hist, ax_hist = plt.subplots()
    ax_hist.hist(df["Count"], bins=20)
    ax_hist.set_xlabel("Frequency")
    ax_hist.set_ylabel("Number of Words")
    ax_hist.set_title("Distribution of Word Frequencies")
    st.pyplot(fig_hist)

    # --- Pie Chart ---
    st.subheader("Pie Chart of Word Frequency")
    # Show only top N words to keep it readable
    top_n = st.slider("Number of top words to show in pie chart", 5, min(20, len(df)), 10)
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(
        df["Count"].head(top_n),
        labels=df["Word"].head(top_n),
        autopct="%1.1f%%",
        startangle=90,
    )
    ax_pie.axis("equal")
    st.pyplot(fig_pie)
