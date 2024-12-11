# Introduction
In this study, we investigate the effectiveness of various types of features in predicting Semantic Text Similarity (STS) through Multi-Layer Perceptrons (MLPs) and Support Vector Regressors (SVRs). We evaluate lexical features, syntactic features, and purely string-related features, to examine their relative contributions to the STS prediction performance of the models.

# Methodology

## Feature Extraction

## Model Training and Testing

# Results
The table presents the correlation results for the various feature types, evaluated using two distinct models: a Multi-Layer Perceptron (MLP) and a Support Vector Regressor (SVR). The features analyzed are Lexical, Syntactic, Strings, Unrestricted (Lexical + Syntactic + Strings), and FeatureSelection (selecting top features from Unrestricted). Each feature's performance is quantified by its Pearson correlation with the Gold Standard, with higher values indicating stronger predictive relevance. These results inform us about which feature types and models are most suitable for the STS task.

| Features           | MLP         | SVR         |
|--------------------|-------------|-------------|
| Lexical            | 0.681449    | 0.681158    |
| Syntactic          | 0.674589    | 0.637858    |
| Strings            | 0.672253    | 0.676096    |
| Unrestricted       | 0.736438    | 0.748999    |
| FeatureSelection   | 0.735535    | 0.742852    |


# Conclusion
