import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit

# --- Load the Uploaded CSV File ---
df = pd.read_csv('sample.csv')

# --- Print column names to inspect ---
print("Columns in the loaded DataFrame:")
print(df.columns)

# --- Prepare the Data ---
# Update the column names below based on the print output above
df = df[['Monthly Production Date', 'Monthly Oil']].rename(columns={'Monthly Production Date': 'date', 'Monthly Oil': 'rate'}) # Adjusted names based on a common pattern; update as necessary
df['date'] = pd.to_datetime(df['date'])
df = df.dropna().sort_values('date').reset_index(drop=True)

# --- Calculate Time in Months from Start ---
df['months'] = (df['date'] - df['date'].min()).dt.days / 30.44

# --- Define Hyperbolic Decline Function ---
def hyperbolic_decline(t, D, b, q_i):
    return q_i / np.power(1 + b * D * t, 1 / b)

q_i_fixed = df['rate'].max()

def decline_with_fixed_qi(t, D, b):
    return hyperbolic_decline(t, D, b, q_i_fixed)

# --- Fit the Hyperbolic Curve ---
time_data = df['months'].values
rate_data = df['rate'].values
initial_bounds = ([0, 0], [1, 2])
popt, _ = curve_fit(decline_with_fixed_qi, time_data, rate_data, bounds=initial_bounds, maxfev=10000)
D_fitted, b_fitted = popt

print(f"\n📈 Fitted Parameters:")
print(f"  q_i (fixed) = {q_i_fixed:.2f}")
print(f"  D (decline rate) = {D_fitted:.4f}")
print(f"  b (hyperbolic factor) = {b_fitted:.4f}")

# --- Forecast Production on the 1st of Each Month ---
num_months = len(df) + 12  # forecast 12 months beyond actual data
start_date = df['date'].min()
forecast_dates = pd.date_range(start=start_date, periods=num_months, freq='MS')  # Month Start

# Convert dates to "months since start"
forecast_months = (forecast_dates - start_date) / pd.Timedelta(days=30.44)
forecast_months = forecast_months.astype(float)

# Forecasted production rates
forecast_rates = decline_with_fixed_qi(forecast_months, D_fitted, b_fitted)

# Optional: Create DataFrame for forecast
forecast_df = pd.DataFrame({
    'date': forecast_dates,
    'forecast_rate': forecast_rates
})

# --- Plot ---
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['date'], y=df['rate'], mode='markers+lines', name='Actual Production'))
fig.add_trace(go.Scatter(x=forecast_dates, y=forecast_rates, mode='lines', name='Hyperbolic Forecast'))
fig.update_layout(
    title="📉 Hyperbolic Decline Curve Forecast (Monthly-Aligned)",
    xaxis_title="Date",
    yaxis_title="Oil Production Rate"
)
fig.show()
