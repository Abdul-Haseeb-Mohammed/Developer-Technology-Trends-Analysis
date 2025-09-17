import pandas as pd
import pycountry

# Load your CSV
df = pd.read_csv("survey_data_updated.csv")

# Manual mapping for non-standard or tricky country names
manual_country_mapping = {
    "congo, republic of the...": "Congo",
    "venezuela, bolivarian republic of...": "Venezuela",
    "iran, islamic republic of...": "Iran",
    "hong kong (s.a.r.)": "Hong Kong",
    "united kingdom of great britain and northern ireland": "United Kingdom",
    "united republic of tanzania": "Tanzania",
    "viet nam": "Vietnam",
    "republic of korea": "South Korea",
    "syrian arab republic": "Syria",
    "democratic republic of the congo": "Congo, Democratic Republic",
    "côte d'ivoire": "Ivory Coast",
    "republic of moldova": "Moldova",
    "brunei darussalam": "Brunei",
    "nomadic": "Unknown"  # No country; mark as Unknown
}

# Function to standardize country names
def standardize_country(name):
    name_clean = str(name).strip().lower()
    if name_clean in manual_country_mapping:
        return manual_country_mapping[name_clean]
    try:
        country = pycountry.countries.search_fuzzy(name)[0]
        return country.name
    except:
        return name  # Keep original if not found

# Apply the function
df['Country_Clean'] = df['Country'].apply(standardize_country)

# Save cleaned CSV
df.to_csv("survey_data_cleaned.csv", index=False)

print("Country column fully cleaned and standardized for Looker Studio.")
