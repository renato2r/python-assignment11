import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load wind dataset
df = pldata.wind(return_type='pandas')

# Show the first and last 10 lines
print("📄 First 10 rows:")
print(df.head(10))
print("\n📄 Last 10 rows:")
print(df.tail(10))

# Convert 'strength' column to float
# Removes non-numeric characters and converts to float
df['strength'] = df['strength'].replace(r'[^\d\.]+', '', regex=True).astype(float)

# Create interactive scatter plot
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='💨 Wind Strength vs. Frequency by Direction',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'},
    template='plotly_dark'
)

# Save to HTML file
fig.write_html("wind.html")
print("✅ Plot saved as wind.html")

# Optional: show the plot in a browser window
# fig.show()
