# Introduction
In this study, we investigate the effectiveness of various types of features in predicting Semantic Text Similarity (STS) through Multi-Layer Perceptrons (MLPs), Support Vector Regressors (SVRs), and Random Forest Reggressors (RFRs). We evaluate Lexical features, Syntactic features, and purely String-related features, to examine their relative contributions to the STS prediction performance of the models.

# Methodology

## Feature Extraction

## Model Training and Testing

# Results
As we mentioned before, we evaluated the various feature types using three distinct models: Multi-Layer Perceptron (MLP), Support Vector Regressor (SVR), and Random Forest Reggressor (RFR). The features analyzed are the previosly mentioned Lexical, Syntactic and Strings (each individually), as well as an Unrestricted (Lexical + Syntactic + Strings) set, and an additional FeatureSelection set extracted from Unrestricted. For MLP and SVR the FeatureSelection set is calculated based on the Pearson correlation of each individual feature with the Gold Standard, while for the RFR it is based on the feature importance calculated by the Random Forest algorithm.

Each of the training sets' performance is quantified by the Pearson correlation of the model predictions with the Gold Standard, with higher values indicating stronger predictive relevance. These results inform us about which feature types and models are most suitable for the STS task. They are summarized in the following table:

| Features           | MLP         | SVR         | RFR         |
|--------------------|-------------|-------------|-------------|
| Lexical            | 0.606827    | 0.681158    | 0.728462    |
| Syntactic          | 0.666410    | 0.658254    | 0.660777    |
| Strings            | 0.674307    | 0.676096    | 0.684635    |
| Unrestricted       | 0.652460    | 0.743904    | **0.757023**|
| FeatureSelection   | 0.743657    | 0.741766    | 0.744606    |

### Feature Selection

Top 10 feature correlations:
    - lemmas_wn_aug_overlap: 0.7233182098358424
    - normal_char_2gram: 0.7215526758966642
    - lemmas_char_2gram: 0.6901581750008041
    - sw_char_2gram: 0.6876105592190485
    - sw_gst_5: 0.6666336863967723
    - lemmas_gst_5: 0.6661478233635988
    - wsd_wn_aug_overlap: 0.6586188923309088
    - normal_char_3gram: 0.6514041862188327
    - lemmas_char_3gram: 0.6478882891792085
    - sw_char_3gram: 0.643363404655336

Top 10 feature importances:
    - lemmas_wn_aug_overlap: 0.4325020377546965
    - normal_char_2gram: 0.16297134111640896
    - chunk_sim_s: 0.0412800853629427
    - lemmas_weighted_overlap: 0.02753037523823193
    - normal_char_5gram: 0.01989175950164162
    - wsd_wn_aug_overlap: 0.016492690513259033
    - wsd_lin_similarity: 0.014270287965658636
    - sw_gst_5: 0.014165231257718914
    - lemmas_resnik_similarity: 0.010444430980915709
    - wsd_resnik_similarity: 0.010332560312099703



# Conclusion
