from pathlib import Path
import streamlit as st
from PIL import Image

# PATH SETTINGS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cdw()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile_pic.jpg"

# GENERAL SETTINGS
PAGE_TITLE = "Welcome to my Universe"
PAGE_ICON = ":random:"
NAME = "Vuong Thieu Luan"
DESCRIPTION = """
Associates Data Analysis and Data Scientist, assisting enterprises by supporting data-driven decision-making"""
EMAIL = "luan1668@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/luan2003/",
    "Github": "https://github.com/Darkred69"
    }
PROJECTS = {
    "Testing for now" : "🏆Testing"
}

st.set_page_config(page_title = PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Welcome to my Universe!")


# Load CSS, PDF, and profile pic
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


# HERO SECTION
col1, col2 = st.columns(2, gap="small")

with col1:
    # Convert PosixPath object to string
    st.image(str(profile_pic), width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download resume",
        data = PDFbyte,
        file_name= resume_file.name,
        mime = "application/octet-stream",
    )
    st.write("📧",EMAIL)


# -- SOCIAL LINKS --------------------------------
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# -- Experiences and Qualifications --------------------------------
st.write("#")
st.subheader("EXPERIENCE AND QUALIFICATIONS")
st.write("""
        - ✔️ DAAD Scholarship in Germany 
        - ✔️ Datacamp Data Scientist Certification
        - ✔️ MindX Data Analyst Course
        - ✔️ 3-month internship at SSI in stock and market analysis for brokers
         """)

# -- SKILLS

st.write("#")
st.subheader("SKILLS")
st.write("""
        - 🧑‍💻Python (pandas, numpy, scipy, sklearn, matplotlib, seaborn)
        - 🗄️SQL (SQL Server, MySQL)
        - 📊Data Visualization (Power BI)
        - 📈Data Analysis (Descriptive statistics, inferential statistics, time series analysis, ELT analysis)
        - 📚Data Science (Data cleaning, data preprocessing, feature engineering, model training, model evaluation, model deployment)
        """)

# --- PROJECTS ---
st.write('\n')
st.subheader("PROJECTS")
st.write("---")

st.write("🚧", "**California Housing Analysis**")
st.write(
    """
- ► Data Preprocessing by clearing all Null Values and handle text and categorical attributes
- ► Data visualization using histogram, scatterplot, and heatmap
- ► Use stratified sampling to sample but keep the original proportions
- ► Feature Combination by creating a CombinedAttributesAdder pipeline
- ► Parameter Tuning using Grid Search and RandomizedSearch on RandomForest
- ► Model Analysis using Cross Validation technique for Decision Tree, SVR, RandomForest, and Linear Regression
"""
)

st.write("- 🔗[Project's Link](https://github.com/Darkred69/California-Housing-Analysis)")



# --- Project 2
st.write('\n')
st.write("🚧", "**Sales Project**")
st.write(
    """
- ► Exploratory Data Analysis with SQL
- ► Data Preprocessing and Cleaning by Fix Data type, drop unnecessary columns and fix duplicates values
- ► Data Visualization using Power BI
"""
)
st.write("- 🔗[Project's Link]( https://github.com/Darkred69/Sales-project)")


# --- Project 3
st.write('\n')
st.write("🚧", "**Sales Insight Analysis**")
st.write(
    """
- ► Data Exploration using SQL
- ► ETL using DAX in PowerBI
- ► Build a Report in PowerBI
"""
)
st.write("- 🔗[Project's Link](https://github.com/Darkred69/Sales-Insight-Analysis)")

# # --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
