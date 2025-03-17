
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

## Data Sources & Collection Methodology
This study utilizes **two primary data sources**:
- **NO₂ concentration data** from the **Ministry of Environment, Urbanization, and Climate Change**
- **Traffic data** from the **Istanbul Metropolitan Municipality**

### 1️⃣ NO₂ Measurement Data  
**Source:** [Ministry of Environment, Urbanization, and Climate Change](https://sim.csb.gov.tr/Services/AirQuality)  
**Data Format:** CSV/Excel (Hourly NO₂ concentration in µg/m³)  
**Date Range:** Customizable based on the study period  

- The Ministry of Environment provides **reliable air pollution monitoring data** from ground measurement stations.
- Selected stations are based on **high NO₂ concentration levels and data consistency**.
- The dataset consists of **hourly NO₂ concentration values**, allowing for detailed **temporal analysis**.

### 2️⃣ Traffic Data  
**Source:** [Istanbul Metropolitan Municipality Open Data Platform](https://ulasav.csb.gov.tr/dataset/34-hourly-traffic-density-data-set)  
**Data Format:** CSV/Excel (Hourly traffic density percentage)  
**Date Range:** Customizable based on the study period  

- The **traffic data** is obtained from the **Istanbul Metropolitan Municipality’s traffic monitoring system**.
- The dataset provides **real-time and historical traffic congestion levels** from **multiple sensors and traffic cameras** throughout the city.
- This dataset will be used to examine **how traffic patterns at different hours impact NO₂ emissions**.

## Analysis Plan

### 1️⃣ Data Collection
- **Retrieving hourly NO₂ concentration levels** from selected ground measurement stations.
- **Obtaining hourly traffic congestion levels** from the Istanbul Metropolitan Municipality.

### 2️⃣ Data Cleaning
- **Standardizing date-time formats** across all datasets.
- **Handling missing values** through interpolation or removal of inconsistent data points.
- **Aligning datasets based on timestamp synchronization** to ensure accurate comparisons.

### 3️⃣ Correlation Analysis
#### 📌 Traffic & NO₂ Relationship
- **Applying Pearson correlation analysis** to measure the **statistical relationship** between **traffic density and NO₂ concentration**.
- Identifying **peak traffic hours** and their effect on **pollution levels**.

#### 📌 Multivariable Analysis
- Analyzing the impact of **different levels of traffic congestion** on NO₂ emissions.
- Potentially using **regression models** to quantify the impact of traffic on NO₂ levels.

## Expected Outcomes
- Identification of **peak NO₂ pollution periods** based on **traffic congestion levels**.
- Insights to support **sustainable traffic management strategies** in **Istanbul**.

This study aims to provide **data-driven insights** into NO₂ pollution sources, contributing to better air quality policies and urban sustainability initiatives. 🚦🌍
```

