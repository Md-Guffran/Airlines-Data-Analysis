import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Load the CSV
df = pd.read_csv('flights.csv')

# # Create a new 'date' column by combining 'year' and 'month'
# df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'].astype(str))

# # Sort by date
# df = df.sort_values('date')

# # Plot the trend
# plt.figure(figsize=(10, 6))
# plt.plot(df['date'], df['passengers'], marker='p')

# plt.title('Monthly Passenger Traffic Trend')
# plt.xlabel('Monthly and Yearly')
# plt.ylabel('Number of Passengers')
# plt.grid(True)
# plt.tight_layout()
# plt.show()


# plt.figure(figsize=(12,5))
# plt.plot(df['date'], df['passengers'],marker='o', color='blue')
# plt.title("montly passenger traffic trend")
# plt.xlabel('Date')
# plt.ylabel('Passengers')
# plt.grid(True)
# plt.tight_layout()
# plt.show

# yearly_df = df.groupby('year')['passengers'].sum().reset_index()

# plt.figure(figsize=(8,5))

# plt.bar(yearly_df['year'],yearly_df['passengers'],color='green')

# plt.title('Yearly Passenger Traffic  Trend')
# plt.xlabel('Year')
# plt.ylabel('Total Passenger')
# plt.grid(axis= 'y')
# plt.tight_layout()
# plt.show()
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'], format='%Y-%B')


# Sort by date
df = df.sort_values('date')
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['passengers'], marker='o', color='blue')

plt.title('Monthly Passenger Traffic Trend')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.grid(True)

# Format x-axis to show every 3rd month and rotate labels
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

monthly_traffic = df.groupby('date')['passengers'].sum().reset_index()

# Plot the trend
plt.figure(figsize=(12,10))
plt.plot(monthly_traffic['date'], monthly_traffic['passengers'], marker='o')
# plt.title('Overall Monthly Passenger Traffic Trend (All Airlines Combined)')
# plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
# plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Number of Passengers')
plt.grid(True)
plt.tight_layout()
plt.show()