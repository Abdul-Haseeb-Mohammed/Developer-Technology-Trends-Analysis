# Technology & Demographics Survey Dashboard

## Overview
This project involves creating an interactive **Looker Studio dashboard** to visualize insights from a technology and demographics survey. The dashboard highlights current technology usage, future technology trends, and demographic distributions among survey respondents.

The project uses **Python** for data preparation and transformation before uploading the processed data to **Looker Studio** for visualization.

---

## Project Workflow

### 1. Data Preparation
Two Python scripts were used to clean and summarize the survey data:

1. **prepare_survey_data.py**  
   - Processes raw survey data to generate summarized information for the dashboard panels.  
   - Creates `survey_top10_all_panels.csv` used for most visualizations (except word cloud and demographics 2x2 page).  

2. **Survey_data_country_standardized.py**  
   - Standardizes country names in the dataset.  
   - Produces `survey_data_updated.csv`, which is used for the Word Cloud panel.  

You can download the standardized dataset here:  
👉 [survey-data-updated.csv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/HLOosvsPgIwt5dgOOh1RSg/survey-data-updated.csv)
---

### 2. Dashboard Design
The dashboard is organized into three sections, each using a **2x2 rectangle layout**:

#### Current Technology Usage
- **Panel 1:** Top 10 Languages Used (Stacked Bar)  
- **Panel 2:** Top 10 Databases Used (Stacked Column)  
- **Panel 3:** Top 10 Platforms Used (Word Cloud)  
- **Panel 4:** Top 10 Web Frameworks Used (Scatter Bubble)  

#### Future Technology Trends
- **Panel 1:** Top 10 Languages Desired Next Year (Stacked Bar)  
- **Panel 2:** Top 10 Databases Desired Next Year (Stacked Column)  
- **Panel 3:** Top 10 Desired Platforms (Tree Map)  
- **Panel 4:** Top 10 Desired Web Frameworks (Scatter Bubble)  

#### Demographics
- **Panel 1:** Respondents by Age (Pie Chart)  
- **Panel 2:** Respondent Count by Country (Map Chart)  
- **Panel 3:** Respondent Distribution by Education Level (Line Bar Chart)  
- **Panel 4:** Respondent Count by Age, Classified by Education Level (Stacked Bar Chart)  

**Note:** Word Cloud visualization was implemented using **Vega/Vega-Lite** from the Community Visualizations in Looker Studio.

---

## Tools & Technologies
- **Python:** Data cleaning, summarization, and preprocessing  
- **Looker Studio:** Dashboard creation and visualization  
- **Pandas/Numpy:** Data manipulation and aggregation  
- **Vega/Vega-Lite:** Custom visualization for Word Cloud  

---

## Data Files
- `survey_top10_all_panels.csv` – Summarized data for most panels  
- `survey_data_updated.csv` – Standardized data used for Word Cloud panel  

---

## Dashboard Link
You can view the interactive dashboard here:  
👉 [Technology & Demographics Survey Dashboard](https://lookerstudio.google.com/reporting/e4624702-0d58-4c52-9bf6-943168a5ecf1)

---

## Steps to Reproduce
1. Run `prepare_survey_data.py` to generate summarized data for dashboard panels.  
2. Run `Survey_data_country_standardized.py` to standardize country names for the Word Cloud.  
3. Upload the processed CSV files to Looker Studio.  
4. Create the dashboard panels using the specified visualization types.  

---

## Outcome
The final dashboard provides clear, interactive insights into:  
- Current technology usage  
- Technology adoption trends for the next year  
- Demographic patterns across survey respondents  

This project demonstrates **end-to-end data processing and visualization** skills, combining Python data pipelines with interactive dashboard design in Looker Studio.
