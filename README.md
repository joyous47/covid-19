# 🦠 CORD-19 Dataset Analysis App

[cite_start]This is a Streamlit application designed for an interactive analysis of the COVID-19 Open Research Dataset (CORD-19)[cite: 1, 3, 4]. [cite_start]The app provides an overview of the dataset, data visualizations, a data explorer for filtering research papers, and access to the raw data[cite: 1].

The project is structured into three main Python scripts:
* [cite_start]`clean_data.py`: Preprocesses the raw `metadata.csv` file to handle missing values and malformed data, saving the cleaned data to `metadata_cleaned.csv`[cite: 2].
* `visualizations.py`: Generates and saves static visualization charts as PNG files.
* [cite_start]`app.py`: The main Streamlit application that loads the cleaned data and displays the analysis and visualizations[cite: 1].

---

### 📋 Prerequisites

Before you run the application, ensure you have the following installed:

* Python 3.7+
* pip (Python package installer)

---

### ⚙️ Installation and Setup

1.  **Clone the repository or download the files.**

2.  **Install the required Python libraries.**
    Open your terminal and run the following command:

    ```bash
    pip install streamlit pandas matplotlib seaborn
    ```

---

### ▶️ How to Run the App

Follow these steps in order to run the application correctly:

1.  **Clean the data.**
    First, you need to run the data cleaning script to prepare the dataset. [cite_start]This script handles data cleaning tasks such as fixing malformed dates and filling missing values in key columns like 'title', 'abstract', 'authors', and 'journal'[cite: 2].

    ```bash
    python clean_data.py
    ```
    [cite_start]This will generate a new file, `metadata_cleaned.csv`, which the other scripts will use[cite: 2, 4, 5, 6].

2.  **Generate the visualizations.**
    [cite_start]Next, run the visualizations script[cite: 1]. This script will create an `images/` directory and save all the required plot images inside it. [cite_start]The Streamlit application will load these images to display the charts[cite: 1].

    ```bash
    python visualizations.py
    ```

3.  **Launch the Streamlit app.**
    [cite_start]Finally, you can start the interactive web application[cite: 1].

    ```bash
    streamlit run app.py
    ```
    [cite_start]The application will automatically open in your default web browser[cite: 1].

---

### 📊 Application Features

[cite_start]The application is divided into several tabs for a seamless user experience[cite: 1]:

* [cite_start]**Overview**: Provides high-level metrics about the dataset, such as the total number of papers, unique authors, and unique journals[cite: 1].
* [cite_start]**Visualizations**: Displays key insights through charts, including publications per year, top journals, and top authors[cite: 1].
* [cite_start]**Data Explorer**: An interactive section that allows users to filter the dataset by publication year and journal[cite: 1].
* [cite_start]**Raw Data**: Shows the first 1000 rows of the dataset and provides a button to download the full `metadata_cleaned.csv` file[cite: 1].

---

### 🧑‍💻 Developed By

Joy
* [cite_start]GitHub: [https://github.com/joyous47](https://github.com/joyous47) [cite: 1]

---

### 📄 Data Source

[cite_start]The dataset used in this analysis is the COVID-19 Open Research Dataset (CORD-19), sourced from Semantic Scholar[cite: 1].# covid-19
