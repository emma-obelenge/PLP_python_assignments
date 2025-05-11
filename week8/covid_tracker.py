# covid_tracker.py
# COVID-19 Global Data Tracker

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Optional: Improve plot style
sns.set(style="darkgrid")
plt.rcParams['figure.figsize'] = (12, 6)

# 2. Load the datasets
covid_death_file_path = os.path.join(os.path.dirname(__file__), "COVID DEATHS.csv")
covid_vaccination_file_path = os.path.join(os.path.dirname(__file__), "COVID_VACCINATIONS.csv")

# Check if the files exist
if not os.path.exists(covid_death_file_path) or not os.path.exists(covid_vaccination_file_path):
    raise FileNotFoundError("One or both of the dataset files are missing. Please check the file paths.")
# Load datasets
print("Loading datasets...")
deaths = pd.read_csv(covid_death_file_path, encoding='latin1')
vaccinations = pd.read_csv(covid_vaccination_file_path, encoding='latin1')

# 3. Data Exploration
print("\nDeaths dataset columns:", deaths.columns.tolist())
print("\nSample Deaths Data:\n", deaths.head())
print("\nVaccinations dataset columns:", vaccinations.columns.tolist())
print("\nSample Vaccinations Data:\n", vaccinations.head())

# Check for missing values
print("\nMissing values in Deaths dataset:\n", deaths.isnull().sum())
print("\nMissing values in Vaccinations dataset:\n", vaccinations.isnull().sum())

# 4. Data Cleaning
deaths["date"] = pd.to_datetime(deaths["date"])
vaccinations["date"] = pd.to_datetime(vaccinations["date"])

# Filter selected countries
countries = ["India", "United States", "Kenya", "Nigeria", "Brazil"]
deaths = deaths[deaths["location"].isin(countries)]
vaccinations = vaccinations[vaccinations["location"].isin(countries)]

# Fill missing values
deaths["total_cases"].fillna(0, inplace=True)
deaths["total_deaths"].fillna(0, inplace=True)
vaccinations["total_vaccinations"].fillna(0, inplace=True)
vaccinations["people_vaccinated_per_hundred"].fillna(0, inplace=True)

# 5. EDA: Total Cases and Deaths Over Time
for country in countries:
    subset = deaths[deaths["location"] == country]
    plt.plot(subset["date"], subset["total_cases"], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.tight_layout()
plt.show()

for country in countries:
    subset = deaths[deaths["location"] == country]
    plt.plot(subset["date"], subset["total_deaths"], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.tight_layout()
plt.show()

# 6. Death Rate
deaths["death_rate"] = deaths["total_deaths"] / deaths["total_cases"]
death_rates = deaths.groupby("location")["death_rate"].max().reset_index()

sns.barplot(x="location", y="death_rate", data=death_rates)
plt.title("Max Death Rate by Country")
plt.ylabel("Death Rate (Max)")
plt.tight_layout()
plt.show()

# 7. Vaccination Progress
for country in countries:
    subset = vaccinations[vaccinations["location"] == country]
    plt.plot(subset["date"], subset["total_vaccinations"], label=country)
plt.title("Total Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.tight_layout()
plt.show()

# People vaccinated per hundred (latest date)
latest_vax = vaccinations.sort_values("date").groupby("location").tail(1)
sns.barplot(x="location", y="people_vaccinated_per_hundred", data=latest_vax)
plt.title("People Vaccinated Per Hundred (Latest)")
plt.ylabel("Percent Vaccinated")
plt.tight_layout()
plt.show()

# 8. Summary
print("\n--- Insights Summary ---")
print("1. The US and India had the highest number of cases overall.")
print("2. Brazil shows a higher death rate compared to others.")
print("3. Kenya and Nigeria had lower case counts and vaccine coverage.")
print("4. The US led in vaccination rollout, followed by India.")
print("5. Early death rates were higher before vaccines became widely available.")
