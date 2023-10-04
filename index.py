from google_play_scraper import Sort, reviews_all, app, reviews
from collections import defaultdict
from datetime import datetime

import csv, json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

result= reviews_all(
    'kr.co.burgerkinghybrid', #post API req 부분.
    lang='ko', # defaults to 'en'
    sort=Sort.NEWEST,
    filter_score_with=None,# defaults to None(means all score)
)

for item in result:
  item['at'] = item['at'].strftime('%Y-%m-%d %H:%M:%S')

for item in result:
  if item['repliedAt']!=None:
    item['repliedAt'] = item['repliedAt'].strftime('%Y-%m-%d %H:%M:%S')

for item in result:
  content = item['content']
  # Split the content into words based on some criteria (e.g., space)
  words = content.split()  # Split by space, you can adjust the criteria
  updated_content = ' '.join(words)
  item['content'] = updated_content

df = pd.DataFrame(result)

# Convert the 'Date' column to a datetime object
df['at'] = pd.to_datetime(df['at'])

# Group the data by month and calculate the mean score for each month
monthly_data = df.resample('M', on='at').mean()

# Create the line graph
plt.figure(figsize=(10, 6))

# Plot the data
plt.plot(monthly_data.index, monthly_data['score'], marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Average Score')
plt.title('Average Score by Month')

# Display the x-axis months nicely
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()