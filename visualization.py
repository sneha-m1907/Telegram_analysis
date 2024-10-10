import pandas as pd 
import matplotlib.pyplot as plt 

# Load the sentiment data
df = pd.read_csv('sentiment_messages.csv')

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Plot sentiment over time
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['sentiment'], label='Sentiment', color='blue')
plt.xlabel('Date')
plt.ylabel('Sentiment')
plt.title('Sentiment over Time for Stock-Related Discussions')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
