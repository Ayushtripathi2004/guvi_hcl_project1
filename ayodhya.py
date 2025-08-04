import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Loading Excel data
df = pd.read_excel("ayodhya_tourist_bookings_final.xlsx")

# Data Cleaning
df.dropna(inplace=True)  # Remove rows with missing values
df['BookingCost'] = pd.to_numeric(df['BookingCost'], errors='coerce')  # Ensure cost is numeric
df['Type'] = df['Type'].str.strip().str.title()  # Clean trip types (remove spaces, proper case)
df['Destination'] = df['Destination'].str.strip().str.title()  # Clean destination names
df.dropna(inplace=True)  # Drop rows with NaNs after conversions

st.title("🧳 Travel Booking Dashboard")

# KPIs
total_bookings = df['BookingID'].count()
avg_cost = df['BookingCost'].mean()

# KPI Cards
st.metric("Total Bookings", total_bookings)
st.metric("Average Booking Cost", f"₹{avg_cost:,.2f}")

# Bar Chart
st.subheader("📍 Bookings by Destination")
dest_counts = df['Destination'].value_counts()
st.bar_chart(dest_counts)

# Pie Chart
st.subheader("🎯 Trip Type Distribution")
type_counts = df['Type'].value_counts()
fig, ax = plt.subplots()
ax.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')
ax.axis("equal")
st.pyplot(fig)
