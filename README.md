# 🛢️ Decline Curve Analysis on Sample Oil Production Data

This repository contains a Jupyter Notebook that performs **Decline Curve Analysis (DCA)** using a **hyperbolic decline model** on historical oil production data. The goal is to forecast future production trends and visualize the results interactively.

---

## 📂 Contents

- `oil_decline_analysis.ipynb` – Main notebook performing the analysis  
- `sample.csv` – Sample dataset with historical oil production and dates

---

## 📊 Project Overview

**Decline Curve Analysis (DCA)** is a widely-used method in petroleum engineering to estimate future oil and gas production based on historical data. This notebook:

- Applies a **hyperbolic decline curve** model  
- Fixes the **initial production rate (qᵢ)** as the peak value  
- Estimates the **decline rate (D)** and **hyperbolic factor (b)** via curve fitting  
- Forecasts future production and visualizes it alongside historical data

**Model equation**:

\[
q(t) = \frac{q_i}{(1 + bDt)^{1/b}}
\]

---

## 🧰 Tools & Libraries Used

- `pandas` – for data manipulation  
- `numpy` – for numerical calculations  
- `scipy.optimize.curve_fit` – for curve fitting  
- `plotly.graph_objects` – for interactive visualization

---

## 📌 Dataset

The file `sample.csv` includes:

- **Monthly Production Date** – Monthly timestamp of production  
- **Monthly Oil** – Oil production value for the corresponding month

---

## 🔧 Features & Functionality

- ✅ Clean and preprocess time-series oil production data  
- ✅ Convert date to "months since production started"  
- ✅ Fit hyperbolic decline model using curve fitting  
- ✅ Forecast production for 12 months beyond actual data  
- ✅ Plot historical and predicted production rates interactively

---
