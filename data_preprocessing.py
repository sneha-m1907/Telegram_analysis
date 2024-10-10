import pandas as pd 
import re
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

# Download the stopwords if not already done
import nltk 
nltk.data.path.append('C:\\nltk_data')
nltk.download('punkt')

nltk.download('stopwords')

# Load the scraped data
df = pd.read_csv('Investing_messages.csv')
print(f"Number of NaN values in 'text': {df['text'].isna().sum()}")

# Handle NaN values
df['text'] = df['text'].fillna('')   # Replace with your CSV file name

stop_words = set(stopwords.words('english'))

def clean_text(text):
    # Remove special characters and URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = text.lower()
    # Tokenize and remove stopwords
    text_tokens = word_tokenize(text)
    filtered_text = [word for word in text_tokens if word not in stop_words]
    return " ".join(filtered_text)


# Apply the clean_text function to the DataFrame
df['cleaned_message'] = df['text'].apply(clean_text)
df.to_csv('cleaned_messages.csv', index=False)
print("Cleaned messages saved to 'cleaned_messages.csv'.")
