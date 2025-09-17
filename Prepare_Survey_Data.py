import pandas as pd

# Load your CSV file
df = pd.read_csv("survey_data_updated.csv")

# Columns to process with corresponding panel names
columns_to_panels = {
    'LanguageHaveWorkedWith': 'Top 10 Languages Used',
    'DatabaseHaveWorkedWith': 'Top 10 Databases Used',
    'PlatformHaveWorkedWith': 'Top 10 Platforms Used',
    'WebframeHaveWorkedWith': 'Top 10 Web Frameworks Used',
    'LanguageWantToWorkWith': 'Top 10 Languages Desired Next Year',
    'DatabaseWantToWorkWith': 'Top 10 Databases Desired Next Year',
    'PlatformWantToWorkWith': 'Top 10 Desired Platforms',
    'WebframeWantToWorkWith': 'Top 10 Desired Web Frameworks'
}

# Function to explode, count top 10 and add panel column
def explode_count_panel(df, column, panel_name):
    df[column] = df[column].str.split(';')
    exploded = df.explode(column)
    exploded[column] = exploded[column].str.strip()
    
    
    top_counts = exploded[column].value_counts().head(10).reset_index()
    top_counts.columns = ['Item', 'Count']
    top_counts['Panel'] = panel_name
    return top_counts

# Combine all panels into one DataFrame
all_panels_df = pd.DataFrame()

for col, panel in columns_to_panels.items():
    panel_df = explode_count_panel(df, col, panel)
    all_panels_df = pd.concat([all_panels_df, panel_df], ignore_index=True)

# Save combined CSV
all_panels_df.to_csv("survey_top10_all_panels.csv", index=False)
print("Combined CSV for all panels saved as 'survey_top10_all_panels.csv'")
