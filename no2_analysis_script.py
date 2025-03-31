

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load the cleaned dataset
df = pd.read_excel("temizlenmis_no2_verisi.xlsx")
df["Tarih"] = pd.to_datetime(df["Tarih"])
df["Saat"] = df["Tarih"].dt.hour
df["Gün"] = df["Tarih"].dt.day_name()
df["HaftaSonu"] = df["Gün"].isin(["Saturday", "Sunday"])
df["Ay"] = df["Tarih"].dt.to_period("M").astype(str)

# --- EDA ---

# 1. Time Series Plot (Both stations)

plt.figure(figsize=(12, 4))
plt.plot(df["Tarih"], df["Kağıthane"], color="darkorange")
plt.title("Hourly NO₂ Levels - Kağıthane")
plt.xlabel("Date")
plt.ylabel("NO₂ (µg/m³)")
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 4))
plt.plot(df["Tarih"], df["Üsküdar"], color="seagreen")
plt.title("Hourly NO₂ Levels - Üsküdar")
plt.xlabel("Date")
plt.ylabel("NO₂ (µg/m³)")
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Hourly Averages
hourly = df.groupby("Saat")[["Kağıthane", "Üsküdar"]].mean().reset_index()
hourly["Traffic"] = hourly["Saat"].apply(lambda x: "Rush Hour" if x in [7,8,17,18,19] else "Other")

# Barplot - Istanbul Overview (Kağıthane)
plt.figure(figsize=(10,4))
sns.barplot(data=hourly, x="Saat", y="Kağıthane", hue="Traffic")
plt.title("Kağıthane - Hourly NO₂ Levels")
plt.tight_layout()
plt.savefig("hourly_kağıthane.png")
plt.close()

# Barplot - Istanbul Overview (Üsküdar)
plt.figure(figsize=(10,4))
sns.barplot(data=hourly, x="Saat", y="Üsküdar", hue="Traffic")
plt.title("Üsküdar - Hourly NO₂ Levels")
plt.tight_layout()
plt.savefig("hourly_uskudar.png")
plt.close()

# 3. Monthly Averages
monthly = df.groupby("Ay")[["Kağıthane", "Üsküdar"]].mean().reset_index()
plt.figure(figsize=(10,4))
sns.lineplot(data=monthly, x="Ay", y="Kağıthane", marker="o", label="Kağıthane")
sns.lineplot(data=monthly, x="Ay", y="Üsküdar", marker="o", label="Üsküdar")
plt.title("Monthly Average NO₂ - Istanbul")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_avg_istanbul.png")
plt.close()

# 4. Weekday vs Weekend
weekday = df.groupby("HaftaSonu")[["Kağıthane", "Üsküdar"]].mean().reset_index()
weekday["Label"] = weekday["HaftaSonu"].replace({True: "Weekend", False: "Weekday"})
wk = weekday.melt(id_vars="Label", value_vars=["Kağıthane", "Üsküdar"], var_name="Station", value_name="NO2")

plt.figure(figsize=(6,4))
sns.barplot(data=wk, x="Label", y="NO2", hue="Station")
plt.title("Weekday vs Weekend NO₂ Levels - Istanbul")
plt.tight_layout()
plt.savefig("weekday_weekend_istanbul.png")
plt.close()

# --- Hypothesis Testing ---
results = []

# Rush Hour vs Night (Kağıthane)
rush_k = df[df["Saat"].isin([7,8,17,18,19])]["Kağıthane"].dropna()
night_k = df[df["Saat"].isin([1,2,3])]["Kağıthane"].dropna()
p_k = ttest_ind(rush_k, night_k, equal_var=False).pvalue
results.append(("Rush Hours vs Night Hours (Kağıthane)", p_k))

# Rush Hour vs Night (Üsküdar)
rush_u = df[df["Saat"].isin([7,8,17,18,19])]["Üsküdar"].dropna()
night_u = df[df["Saat"].isin([1,2,3])]["Üsküdar"].dropna()
p_u = ttest_ind(rush_u, night_u, equal_var=False).pvalue
results.append(("Rush Hours vs Night Hours (Üsküdar)", p_u))

# Weekday vs Weekend (Kağıthane)
p_wk_k = ttest_ind(df[df["HaftaSonu"]==False]["Kağıthane"].dropna(),
                   df[df["HaftaSonu"]==True]["Kağıthane"].dropna(), equal_var=False).pvalue
results.append(("Weekday vs Weekend (Kağıthane)", p_wk_k))

# Weekday vs Weekend (Üsküdar)
p_wk_u = ttest_ind(df[df["HaftaSonu"]==False]["Üsküdar"].dropna(),
                   df[df["HaftaSonu"]==True]["Üsküdar"].dropna(), equal_var=False).pvalue
results.append(("Weekday vs Weekend (Üsküdar)", p_wk_u))

# Print Results
print("Hypothesis Testing Results (Istanbul NO₂ Analysis):")
for name, pval in results:
    print(f"{name}: p = {pval:.4e} → {'Significant' if pval < 0.05 else 'Not Significant'}")
