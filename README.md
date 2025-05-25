# Decline-Curve-Analysis-on-Sample-data
This repository contains a Jupyter Notebook that performs decline curve analysis (DCA) using a hyperbolic model on historical oil production data. It demonstrates how to forecast future production based on past trends and visualize the results interactively.

📂 Contents
oil_decline_analysis.ipynb – Main notebook performing the analysis.

sample.csv – Sample dataset with historical oil production and dates.

README.md – Project documentation and overview.

📊 Project Overview
Decline Curve Analysis is a key technique in reservoir engineering and production forecasting. This notebook focuses on modeling oil production decline using a hyperbolic decline curve, with the initial production rate (qᵢ) fixed and the decline rate (D) and hyperbolic factor (b) estimated from data.

🧰 Tools & Libraries Used
The project uses the following Python libraries:

pandas – Data manipulation and preprocessing

numpy – Numerical computations

scipy.optimize.curve_fit – Non-linear curve fitting to estimate decline parameters

plotly.graph_objects – Interactive plotting for visualizing actual and forecasted production trends

📌 Dataset
The dataset sample.csv contains two columns:

Monthly Production Date – The date of the production record (monthly)

Monthly Oil – Oil production value for the corresponding month

🔧 Features & Functionality
Preprocessing of time series data into monthly intervals since production start.

Implementation of the Hyperbolic Decline Model:

𝑞
(
𝑡
)
=
𝑞
𝑖
(
1
+
𝑏
𝐷
𝑡
)
1
/
𝑏
q(t)= 
(1+bDt) 
1/b
 
q 
i
​
 
​
 
with qᵢ fixed at the max production rate.

Parameter fitting using curve_fit to obtain optimal D and b.

Forecasting of production for 12 future months.

Visualization of actual vs. predicted values using interactive Plotly charts.
