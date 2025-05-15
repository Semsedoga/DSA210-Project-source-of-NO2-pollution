
# ANALYZING NO₂ POLLUTION SOURCES IN ISTANBUL

## Project Overview
Air pollution is a critical environmental issue of our decade, and nitrogen dioxide (NO₂) is a chemical compound that belongs to the nitrogen oxides (NOx) group of extremely reactive gases. NO₂ is primarily emitted by vehicular traffic and industrial activities, making it a significant urban pollutant.

This study aims to analyze the impact of **traffic volume** on NO₂ emissions in Istanbul by collecting data from ground measurement stations in specific districts. The NO₂ concentration data will be sourced from the **Ministry of Environment, Urbanization, and Climate Change**, while **traffic data** will be obtained from the **Istanbul Metropolitan Municipality**.

By analyzing NO₂ concentration levels at different times of the day with varying traffic densities, this project aims to identify correlations between **traffic volume and pollution levels**. Based on the findings, the **primary sources of NO₂ emissions** will be determined.

## Motivation
Air pollution, particularly NO₂ emissions from traffic, is a major concern in urban areas like **Istanbul**, where **high traffic congestion** significantly affects air quality. Understanding the relationship between **traffic volume and NO₂ levels** can help pinpoint key pollution sources and support the development of **sustainable traffic management strategies**.

## Research Question
**How does traffic volume influence NO₂ concentration levels in Istanbul across different times of the day?**

### Hypothesis  
- **Higher traffic volume leads to increased NO₂ concentration levels**, with peak pollution occurring during **rush hours**.
- The NO₂ level during **rush hours (07:00–09:00 and 17:00–19:00)** is significantly higher than during **night hours (01:00–03:00)** in Istanbul.
- The average NO₂ level on **weekdays** is significantly higher than on **weekends** in Istanbul.


## Data Sources & Collection Methodology
This study utilizes **two primary data sources**:
- **NO₂ concentration data** from the **Ministry of Environment, Urbanization, and Climate Change**
- **Traffic data** from the **Istanbul Metropolitan Municipality**

### NO₂ Measurement Data  
**Source:** [Ministry of Environment, Urbanization, and Climate Change](https://sim.csb.gov.tr/Services/AirQuality)  
**Data Format:** CSV/Excel (Hourly NO₂ concentration in µg/m³)  
**Date Range:** Customizable based on the study period  

- The Ministry of Environment provides **reliable air pollution monitoring data** from ground measurement stations.
- Selected stations are based on **high NO₂ concentration levels and data consistency**.
- The dataset consists of **hourly NO₂ concentration values**, allowing for detailed **temporal analysis**.

### Traffic Data  
**Source:** [Istanbul Metropolitan Municipality Open Data Platform](https://ulasav.csb.gov.tr/dataset/34-hourly-traffic-density-data-set)  
**Data Format:** CSV/Excel (Hourly traffic density percentage)  
**Date Range:** Customizable based on the study period  

- The **traffic data** is obtained from the **Istanbul Metropolitan Municipality’s traffic monitoring system**.
- The dataset provides **real-time and historical traffic congestion levels** from **multiple sensors and traffic cameras** throughout the city.
- This dataset will be used to examine **how traffic patterns at different hours impact NO₂ emissions**.

## Analysis Plan

### Data Collection
- **Retrieving hourly NO₂ concentration levels** from selected ground measurement stations.
- **Obtaining hourly traffic congestion levels** from the Istanbul Metropolitan Municipality.

### Data Cleaning
- **Standardizing date-time formats** across all datasets.
- **Handling missing values** through interpolation or removal of inconsistent data points.
- **Aligning datasets based on timestamp synchronization** to ensure accurate comparisons.

### Correlation Analysis
#### Traffic & NO₂ Relationship
- **Applying Pearson correlation analysis** to measure the **statistical relationship** between **traffic density and NO₂ concentration**.
- Identifying **peak traffic hours** and their effect on **pollution levels**.

#### Multivariable Analysis
- Analyzing the impact of **different levels of traffic congestion** on NO₂ emissions.
- Potentially using **regression models** to quantify the impact of traffic on NO₂ levels.

## Expected Outcomes
- Identification of **peak NO₂ pollution periods** based on **traffic congestion levels**.
- Insights to support **sustainable traffic management strategies** in **Istanbul**.

This study aims to provide **data-driven insights** into NO₂ pollution sources, contributing to better air quality policies and urban sustainability initiatives. 

## Exploratory Data Analysis & Hypothesis Testing

###  Dataset Overview
This analysis focuses on hourly NO₂ (nitrogen dioxide) measurements from two air quality monitoring stations in **Kağıthane** and **Üsküdar**, Istanbul. The data spans from January to May 2024 and was obtained from the [Istanbul Metropolitan Municipality Open Data Portal](https://data.ibb.gov.tr/).

Üsküdar and Kağıthane were selected because of their low data loss and the fact that they are located on different sides of Istanbul, offering a geographical contrast between the Asian and European parts of the city.

---

### Data Cleaning Process

The original dataset contained hourly NO₂ measurements from air quality monitoring stations in Istanbul. The data cleaning steps were as follows:

1. **Datetime Parsing:**  
   The `Tarih` (timestamp) column was converted to `datetime` format to enable proper time-based analysis.

2. **Handling Missing Values:**  
   Some rows had missing NO₂ values for either Kağıthane or Üsküdar. These rows were:
   - **Retained** if at least one station had a valid value (for comparisons involving one location only).
   - **Dropped** from specific comparisons (like hypothesis testing) when both values were required to be present.

3. **Feature Engineering:**  
   To support time-based analysis, the following columns were created:
   - `Hour`: Extracted from timestamp to group data by hour of day
   - `Month`: Used to observe monthly trends
   - `Weekday/Weekend Indicator`: Used to compare pollution levels on weekdays vs weekends

4. **No Outlier Removal:**  
   Since high NO₂ values may correspond to real pollution peaks (e.g., during traffic congestion), no outlier removal was applied to preserve data integrity.

---

### Exploratory Data Analysis (EDA)

#### 1. Time Series Overview
- The NO₂ concentration fluctuates throughout the day, with notable peaks during certain periods.
- A visible difference in overall NO₂ behavior can be observed between the two monitoring locations, representing different parts of Istanbul.

#### 2. Hourly Trends
- **Rush hour periods** correlate with increased NO₂ levels in both regions.
- The increase is more prominent in areas with heavier traffic density.

#### 3. Monthly Averages
- NO₂ levels rise gradually from January to March, peaking in April.
- A decrease is observed starting May, potentially due to seasonal variation.

#### 4. Weekday vs Weekend
- Both regions exhibit higher NO₂ levels on **weekdays**, which supports the traffic-related pollution hypothesis.

---

### Hypothesis Testing Results

| Hypothesis | p-value | Statistically Significant? |
|------------|---------|-----------------------------|
| Weekdays vs Weekends | 2.78e-35 (Kağıthane), 3.39e-02 (Üsküdar) | ✅ Yes |
| Rush Hours vs Night Hours | 2.30e-07 (Kağıthane), 1.11e-04 (Üsküdar) | ✅ Yes |

All tests support the hypothesis that **traffic volume significantly affects NO₂ pollution** in Istanbul.

---

### Summary
These findings highlight the relationship between traffic activity and air quality in Istanbul:
- NO₂ pollution increases during peak traffic hours.
- Weekday pollution levels are significantly higher than weekend levels.
- This indicates a strong correlation between human activity (especially traffic) and air pollution.

The next step will be applying **machine learning techniques** to further explore and model pollution behavior.

---
## 📊 Final Conclusion – Understanding NO₂ Pollution Through Time, Traffic & Prediction Models

This project explored the relationship between time-related traffic patterns and NO₂ air pollution levels in Istanbul using real-world data from two districts: **Kağıthane** (European side) and **Üsküdar** (Asian side).

---

### ✅ Key Insights from Exploratory Analysis

- **Rush hour peaks** (07:00–09:00 & 17:00–19:00) are consistently associated with elevated NO₂ levels.
- **Kağıthane** consistently reports **higher NO₂ concentrations** than Üsküdar, likely due to higher population density and traffic flow.
- **Weekday NO₂ levels** are higher than those on weekends, reflecting workday commuting behavior.
- **Monthly trends** show seasonal variation, with a rise during winter-spring and a decline in May.

All of these patterns were statistically confirmed using **independent hypothesis tests**.  
The t-test results clearly support the idea that **traffic activity strongly influences urban NO₂ pollution**.

---

### 🤖 Machine Learning Perspective – Random Forest Modeling

To move beyond correlation and assess **predictive capability**, we applied **Random Forest Regression** models using:

- `Hour of day`  
- `Weekend indicator`  
- `Rush hour flag`  

Separate models were trained for **Kağıthane** and **Üsküdar**.

- The **R² scores** showed that time-based variables explain a **moderate portion of the variance** in NO₂ concentrations.
- Model performance was **visually validated** using scatter plots and hourly average comparisons between predicted and actual values.
- **Kağıthane's model** performed slightly better than Üsküdar’s, aligning with its more pronounced hourly fluctuations.

---

### 📈 Visual Summary of Analysis

The following plots were used to explore, validate, and communicate key insights:

1. **Combined Hourly Trends** – Direct comparison of NO₂ at both stations  
2. **Barplots by Hour & Traffic Flag** – Understand rush vs non-rush hour impact  
3. **Monthly Trends** – Identify long-term and seasonal variation  
4. **Weekday vs Weekend Comparison** – Effect of weekly routines  
5. **Rush Hour vs Other Hours** – Isolate the influence of traffic intensity
6. **NO₂ Summary – Kağıthane by Traffic Period** - Summarize the mean, standard deviation, and sample size of NO₂ levels during rush and non-rush hours to highlight traffic-related pollution differences.
7. **NO₂ Summary – Kağıthane by Traffic Period** - Summarize the mean, standard deviation, and sample size of NO₂ levels during rush and non-rush hours to highlight traffic-related pollution differences.
8. **Random Forest Predicted vs Actual NO₂** – Evaluate model effectiveness  
9. **Hourly Average Prediction Match** – Daily trend alignment

Each visualization played a distinct role in connecting **pollution behavior** to **human activity patterns**.

---

### 🌍 Policy Implications & Urban Planning

The results can directly inform:

- **Environmental policy**: regulating vehicle use in peak hours
- **Public health**: issuing air quality warnings during rush periods
- **Urban mobility planning**: redesigning traffic flow to reduce emissions

By identifying **when** and **where** pollution spikes occur, data-driven decisions can be made to **protect urban populations**.

---

### 🔬 Recommendations for Future Work

- Include additional variables: **temperature**, **humidity**, **wind speed**, and **traffic volume**
- Use advanced models: **XGBoost**, **LSTM**, or **hybrid architectures**
- Extend analysis to **more districts** and **longer time periods**
- Develop **interactive dashboards** for real-time NO₂ prediction and public access

---

### 📌 Final Takeaway

Even with a limited set of time-based indicators, this project has shown that:

> 🛣 **Traffic patterns explain a significant portion of urban NO₂ variability**.

With better data and smarter models, we can build systems that both **monitor and mitigate pollution**, contributing to **a healthier and more sustainable Istanbul**.


