# power_consumption

# PowerPulse: Household Energy Usage Forecast

## Project Overview
The rise of smart meters and IoT devices has made household power consumption data available at high resolution.  
This project uses **synthetic power consumption data** to analyze and forecast household energy usage using Python, SQL, Power BI, and Streamlit.

---

## Objectives
- Simulate household power usage dataset.
- Clean, preprocess, and store data in PostgreSQL.
- Build Power BI dashboards for insights.
- Develop a Streamlit app for interactive exploration.
- Apply machine learning for forecasting power usage.

---

## Tools & Technologies
- **Python (Pandas, NumPy, Matplotlib, Scikit-learn)**
- **PostgreSQL (SQL for storage & queries)**
- **Power BI (Dashboard & Reports)**
- **Streamlit (Interactive Web App)**

---

## Dataset
Synthetic dataset generated with following features:
- `Date` – Calendar date  
- `Time` – Time of recording (hourly)  
- `Global_active_power` – Household active power (kW)  
- `Global_reactive_power` – Reactive power (kVAR)  
- `Voltage` – Supply voltage (V)  
- `Global_intensity` – Current intensity (A)  
- `Sub_metering_1, Sub_metering_2, Sub_metering_3` – Energy usage by different appliances  

File: **household_power.csv**

---

## Business Use Cases
1. **Peak Load Identification** – Identify high-consumption periods.  
2. **Appliance Monitoring** – Understand usage patterns of sub-metered appliances.  
3. **Anomaly Detection** – Detect abnormal usage (potential faults).  
4. **Energy Forecasting** – Predict next day/hour consumption.  

---

## SQL Queries Examples

### 1. Daily Average Consumption
```sql
SELECT date, AVG(global_active_power) AS avg_power
FROM household_power
GROUP BY date
ORDER BY date;

