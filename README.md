
# Penyewaan Sepeda Dicoding Submission

This project represents the culmination of my journey through the "Belajar Analisis Data Dengan Python" course on Dicoding, where I've delved into the analysis and visualization of the bike sharing dataset. The accompanying notebook details my process, covering everything from Data Wrangling to Exploratory Data Analysis and Visualization. I also deploy this app in [here](https://penyewaansepedaapp.streamlit.app/).

In addition to the notebook, I've also developed a streamlined dashboard using Streamlit. You can access the dashboard by clicking the link provided in the right sidebar or directly here.

## 1. File Structures
```
.
├── dashboard
│   ├── dashboard.py
│   └── day_data.csv
├── data
│   ├── day.csv
|   └── hour.csv
├── screenshoots
|   ├── SS1.png
|   ├── SS2.png
|   └── SS3.png
├── README.md
├── notebook.ipynb
└── requirements.txt
```

## 2. Project work cycle
1. Data Wrangling: 
 - Gathering data
 - Assessing data
 - Cleaning data
2. Exploratory Data Analysis:
 - Defined business questions for data exploration
 - Create Data exploration
3. Data Visualization:
 - Create Data Visualization that answer business questions
4. Dashboard:
 - Set up the DataFrame which will be used
 - Make filter components on the dashboard
 - Complete the dashboard with various data visualizations

**Note: Numbers 1 to 3 are in the dicoding-collection-exercise and number 4 is in dashboard.**

## 3. Getting Started
### `notebook.ipynb`
1. Download this project.
2. Open your favorite IDE like Jupyter Notebook or Google Colaboratory (but in here I will use Google Colab).
3. Create a New Notebook.
4. Upload and select the file with .ipynb extension.
5. Connect to hosted runtime.
6. Lastly, run the code cells.

### `dashboard/dashboard.py`
1. Download this project.
2. Install the Streamlit in your terminal or command prompt using `pip install streamlit`. Install another libraries like pandas, numpy, scipy, matplotlib, and seaborn if you haven't.
3. Please note, don't move the csv file because it acts a data source. keep it in one folder as dashboard.py
4. Open your VSCode and run the file by clicking the terminal and write it `streamlit run dashboard.py`.
