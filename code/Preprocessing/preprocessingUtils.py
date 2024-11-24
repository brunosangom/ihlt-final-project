import pandas as pd
import nltk
import string
import ast
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

class TextPreprocessor:
    def __init__(self):
        # Initialize stopwords and lemmatizer
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()


    def load_dataset(self, path):
        dataset_df = pd.read_csv(path)

        # Turn the 2 first columns from strings to actual lists of strings
        dataset_df.iloc[:, :2] = dataset_df.iloc[:, :2].map(ast.literal_eval)

        return dataset_df

    def remove_punctuation(self, df):
        """Remove punctuation from words in both columns of a DataFrame"""
        punctuation_removed_df = df.copy()
        
        punctuation_removed_df.iloc[:, 0] = punctuation_removed_df.iloc[:, 0].apply(
            lambda sentence: [word.strip(string.punctuation) for word in sentence]
        )
        punctuation_removed_df.iloc[:, 1] = punctuation_removed_df.iloc[:, 1].apply(
            lambda sentence: [word.strip(string.punctuation) for word in sentence]
        )
        
        return punctuation_removed_df

    def remove_empty_strings(self, df):
        """Remove empty strings from both columns of a DataFrame"""
        empty_strings_removed_df = df.copy()
        
        empty_strings_removed_df.iloc[:, 0] = empty_strings_removed_df.iloc[:, 0].apply(
            lambda sentence: [word for word in sentence if word]
        )
        empty_strings_removed_df.iloc[:, 1] = empty_strings_removed_df.iloc[:, 1].apply(
            lambda sentence: [word for word in sentence if word]
        )
        
        return empty_strings_removed_df

    def convert_to_lowercase(self, df):
        """Convert words to lowercase in both columns of a DataFrame"""
        lowercase_df = df.copy()
        
        lowercase_df.iloc[:, 0] = lowercase_df.iloc[:, 0].apply(
            lambda sentence: [word.lower() for word in sentence]
        )
        lowercase_df.iloc[:, 1] = lowercase_df.iloc[:, 1].apply(
            lambda sentence: [word.lower() for word in sentence]
        )
        
        return lowercase_df

    def remove_stopwords(self, df):
        """Remove stopwords from both columns of a DataFrame"""
        stopwords_removed_df = df.copy()
        
        stopwords_removed_df.iloc[:, 0] = stopwords_removed_df.iloc[:, 0].apply(
            lambda sentence: [word for word in sentence if word not in self.stop_words]
        )
        stopwords_removed_df.iloc[:, 1] = stopwords_removed_df.iloc[:, 1].apply(
            lambda sentence: [word for word in sentence if word not in self.stop_words]
        )
        
        return stopwords_removed_df

    def lemmatize(self, df):
        """Apply lemmatization to words in both columns of a DataFrame"""
        lemmatized_df = df.copy()
        
        lemmatized_df.iloc[:, 0] = lemmatized_df.iloc[:, 0].apply(
            lambda sentence: [self.lemmatizer.lemmatize(word) for word in sentence]
        )
        lemmatized_df.iloc[:, 1] = lemmatized_df.iloc[:, 1].apply(
            lambda sentence: [self.lemmatizer.lemmatize(word) for word in sentence]
        )
        
        return lemmatized_df