# Introduction
In this study, we investigate the effectiveness of various types of features in predicting Semantic Text Similarity (STS) through Multi-Layer Perceptrons (MLPs) and Support Vector Regressors (SVRs). We evaluate lexical features, syntactic features, and purely string-related features, to examine their relative contributions to the STS prediction performance of the models.

# Methodology

## Feature Extraction

## Model Training and Testing

# Results
We evaluated the various feature types using three distinct models: a Multi-Layer Perceptron (MLP), a Support Vector Regressor (SVR) and a Random Forest Reggressor (RFR). The features analyzed are the previosly mentioned Lexical, Syntactic and Strings (each individually), as well as an Unrestricted (Lexical + Syntactic + Strings) set, and an additional FeatureSelection set extracted from Unrestricted. For MLP and SVR the FeatureSelection set is calculated based on the Pearson correlation of each individual feature with the Gold Standard, while for the RFR it is based on the feature importance calculated by the Random Forest algorithm.

Each of the training sets' performance is quantified by the Pearson correlation of the model predictions with the Gold Standard, with higher values indicating stronger predictive relevance. These results inform us about which feature types and models are most suitable for the STS task. They are summarized in the following table:

| Features           | MLP         | SVR         | RFR         |
|--------------------|-------------|-------------|-------------|
| Lexical            | 0.606827    | 0.681158    | 0.728462    |
| Syntactic          | 0.666410    | 0.658254    | 0.660777    |
| Strings            | 0.674307    | 0.676096    | 0.684635    |
| Unrestricted       | 0.652460    | 0.743904    | **0.757023**|
| FeatureSelection   | 0.743657    | 0.744606    | 0.744606    |





# Conclusion
