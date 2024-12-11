# IHLT: Semantic Text Similarity Final Project

## Summary

This project studies the use of various feature types and prediction models to estimate the similarity between sentence pairs.

A comprehensive discussion of the methodology used and analysis of the obtained results can be found at [`discussion.md`](./discussion.md).

## Project Structure

- [`Datasets/`](./Datasets/) contains the STS datasets used for the project
- [`Features/`](./Features/) contains the feature extraction notebooks, as well as their resulting training and testing sets
  - [`lexicalFeatureExtraction.ipynb`](./Features/lexicalFeatureExtraction.ipynb) contains the code for extracting the **Lexical** features
  - [`stringFeatureExtraction.ipynb`](./Features/stringFeatureExtraction.ipynb) contains the code for extracting the purely **String**-related features
  - [`syntacticFeatureExtraction.ipynb`](./Features/syntacticFeatureExtraction.ipynb) contains the code for extracting the **Syntactic** features
- [`Models/`](./Models/) contains the notebooks where the machine learning models are trained and tested
  - [`MLP.ipynb`](./Models/MLP.ipynb) contains the code for training and testing **Multi-Layer Perceptron** models on the different types of features
  - [`RFR.ipynb`](./Models/RFR.ipynb) contains the code for training and testing **Random Forest Regressor** models on the different types of features
  - [`SVR.ipynb`](./Models/SVR.ipynb) contains the code for training and testing **Support Vector Machine** models on the different types of features
- [`Preprocessing/`](./Preprocessing/) contains files involving the preprocessing of the datasets for easier manipulation
  - [`loadDatasets.ipynb`](./Preprocessing/loadDatasets.ipynb) contains the code for tokenizing the raw datasets and compiling them together
  - [`preprocessingUtils.py`](./Preprocessing/preprocessingUtils.py) contains helper functions to automate common preprocessing steps
  - [`STS_test.csv`](./Preprocessing/STS_test.csv) contains the compiled and tokenized testing sentence pairs
  - [`STS_train.csv`](./Preprocessing/STS_train.csv) contains the compiled and tokenized training sentence pairs
