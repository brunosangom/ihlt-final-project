# Introduction
In this study, we investigate the effectiveness of various types of features in predicting Semantic Text Similarity (STS) through Multi-Layer Perceptrons (MLPs), Support Vector Regressors (SVRs), and Random Forest Reggressors (RFRs). We evaluate Lexical features, Syntactic features, and purely String-related features, to examine their relative contributions to the STS prediction performance of the models.

# Methodology  
The common preprocessing pipeline involves removing punctuation and converting all text to lowercase.  

For specific Lexical and String feature extraction, additional preprocessing steps are applied, obtaining various different types of pairs of sentences:

- Stopwords are removed.  
- Text is converted to lowercase.  
- Only for Lexical, a Word Sense Disambiguation approach is used: each word is replaced with its most common synonym (based on the most frequent synset). If no synset exists for a word, it remains unchanged.  

## Feature Extraction
- **Lexical**:
    - *Jaccard distance*: Measures the dissimilarity between two sets by calculating the size of their intersection divided by the size of their union.
    - *Containment measure*: Focuses on the proportion of the smaller set that overlaps with the larger set, emphasizing partial matches.
    - *Pairwise Word Similarity (Lin & Resnik)*: Measure of the semantic similarity between words of the sentences, based on their Information Content (IC) and the WordNet hierarchy.
      - *Lin similarity*: Based on the IC of the least common subsumer of two concepts, normalized by their IC.
      - *Resnik similarity*: Based on the IC of the most informative shared ancestor.
    - *WordNet augmented word overlap*: Enhances word overlap measures by incorporating semantic relationships derived from the WordNet lexical database.
    - *Weighted word overlap*: Extends basic word overlap measures by assigning different weights to words based on their importance or frequency.
    - *Greedy lemma aligning overlap*: Aligns words or lemmas in a greedy manner to maximize the overlap between two texts, considering synonyms or lemmatized forms.

- **Syntactic**:
    - *N-grams overlap removing function words*:  
    Function words (e.g., prepositions, conjunctions, articles) carry less meaning and can introduce noise. Removing them enhances semantic similarity estimates. Part-of-Speech (POS) tagging, essential for identifying grammatical roles, is used to filter out these function words. The overlap of n-grams (for n=1, 2, 3) is computed between the two sentences after removing function words.

    - *Syntactic roles similarity**:  
    Semantic similarity can be measured by comparing words or phrases with the same syntactic roles across sentences. Using the Stanza library (Stanford NLP Group, 2006), syntactic roles like predicates (p), objects (o), and subjects (s) are grouped into "chunks." Similarity between chunks is calculated using Lin similarity for the lemmas of the words in each chunk. The final similarity score includes four measures: the similarity of predicates, objects, subjects, and the overall sentence similarity (average of the three).

    - *Syntactic dependencies overlap*:  
    Dependency relations between words in a sentence (edges connecting governing words and dependents) are analyzed for overlap. The weighted dependency relation coverage (wdrc) is computed for each sentence relative to the other. As this measure is asymmetric, the overall similarity is the harmonic mean of $\text{wdrc}(S_1, S_2)$ and $\text{wdrc}(S_2, S_1)$.

- **Strings**:
    - *Character n-grams*:  
    This method captures sequences of characters (e.g., 3-grams, 4-grams) from a sentence to compare its structure. By using TF-IDF vectorization and cosine similarity, it measures how similar two strings are based on their character sequences, regardless of word choice. 

    - *Greedy String Tiling (GST)*:  
    GST identifies matching substrings (tiles) between two strings and computes similarity based on their overlap. It focuses on partial matches, measuring how much of one string appears in another. A length threshold (e.g., 5 or 10 characters) ensures that only significant matches contribute to the final similarity score. This method is useful for detecting partial or reordered matches.

## Model Training and Testing

Three distinct models were trained to predict semantic similarity:

- Multi-Layer Perceptron (MLP)
- Support Vector Regressor (SVR)
- Random Forest Regressor (RFR)

The features analyzed are the previosly mentioned Lexical, Syntactic and Strings (each individually), as well as an Unrestricted (Lexical + Syntactic + Strings) set, and an additional FeatureSelection set extracted from Unrestricted. For MLP and SVR the FeatureSelection set is calculated based on the Pearson correlation of each individual feature with the Gold Standard, while for the RFR it is based on the feature importance calculated by the Random Forest algorithm.

# Results
Each of the training sets' performance is quantified by the Pearson correlation of the Gold Standard with the model predictions on the test set, with higher values indicating stronger predictive relevance. These results inform us about which feature types and models are most suitable for the STS task. They are summarized in the following table:

| Features           | MLP         | SVR         | RFR         |
|--------------------|-------------|-------------|-------------|
| Lexical            | 0.606827    | 0.681158    | 0.728462    |
| Syntactic          | 0.666410    | 0.658254    | 0.660777    |
| Strings            | 0.674307    | 0.676096    | 0.684635    |
| Unrestricted       | 0.652460    | 0.743904    | **0.757023**|
| FeatureSelection   | 0.743657    | 0.741766    | 0.744606    |

From these results, we make the following observations:
- The best score was achieved by the RFR model with the Unrestricted feature set, with a Pearson correlation of **0.757023**
- When considering feature types individually, the Syntactic features seem to be slightly less informative than the Lexical and Strings, suggesting that the similarity between texts is more related to the words themselves than to their roles in a sentence.
- The SVR and RFR significantly improve their scores when using all the feature types together (Unrestricted), indicating that there is information that can be inferred from the combination of the different feature types. The MLP does not increase when trained on Unrestricted, but we suspect this might be an issue with overfitting, since the validation score improved for this run. This could be fixed with further experimentation on larger architecture configurations and different training parameters.
- Generally, the FeatureSelection set achieves consistent results, showing that most of the information is encoded in a minority of the features. It also seems to substantially paliate the training issue that the MLP model had with the Unrestricted features, by removing noise and focusing on impactful features.
- The RFR has consistently better performance than the MLP and SVR, which are mostly close except for some inconsistencies of MLP. 

### Top Features
In addition to the overall results, we also extracted feature-specific results (the ones used for FeatureSelection), that allow us to study which are the most important features and the characteristics they share.

The next table displays the top 10 features according to Pearson correlation with the Gold Standard:

| Feature                | Correlation Score |
|------------------------|-------------------|
| lemmas_wn_aug_overlap  | 0.7233           |
| normal_char_2gram      | 0.7216           |
| lemmas_char_2gram      | 0.6902           |
| sw_char_2gram          | 0.6876           |
| sw_gst_5               | 0.6666           |
| lemmas_gst_5           | 0.6661           |
| wsd_wn_aug_overlap     | 0.6586           |
| normal_char_3gram      | 0.6514           |
| lemmas_char_3gram      | 0.6479           |
| sw_char_3gram          | 0.6434           |

We can observe that only 3 types of features appear on the list:
- *WordNet-Augmented Word Overlap:* For the Lemmatized and the Word Sense Disambiguation sentences. It seems to be the feature that best captures the lexical information of the words in sentences.
- *Character n-grams:* For the Normal, no-Stopwords, and Lemmatized sentences, with values 2 and 3 for n. The comparison of character distributions between sentences appears to be very relevant to STS.
- *Greedy String Tiling:* For the no-Stopwords and Lemmatized sentences, both with minimum tile length of 5 characters. The proportion of string tiles that align between sentences also seems to encode great part of their similarity.

Out of these 3 features, 1 is Lexical and the other 2 are Strings features.

The next table displays the top 10 features according to the Feature Importance assigned by the RFR algorithm:

| Feature                | Importance Score |
|------------------------|------------------|
| lemmas_wn_aug_overlap  | 0.4325          |
| normal_char_2gram      | 0.1630          |
| chunk_sim_s            | 0.0413          |
| lemmas_weighted_overlap| 0.0275          |
| normal_char_5gram      | 0.0199          |
| wsd_wn_aug_overlap     | 0.0165          |
| wsd_lin_similarity     | 0.0143          |
| sw_gst_5               | 0.0142          |
| lemmas_resnik_similarity| 0.0104         |
| wsd_resnik_similarity  | 0.0103          |

We observe that there are 4 common features among the 2 tables: ``lemmas_wn_aug_overlap``, ``normal_char_2gram``, ``wsd_wn_aug_overlap``, and ``sw_gst_5``, which reinforces the relevance of these features when identifying paraphrases. It is especially remarkable that the top 2 features hold a substantially greater importance score than the rest (x10 and x4, respectively, when compared to the 3rd most important feature), which indicates that these features encode most of the information necessary to predict the similarity between sentence-pairs.

The rest of the features that appear on the second table include Chunk Similarity of Subjects, Weighted Word Overlap, and Pairwise Word Similarity (with the Lin and Resnik similarity measures). Out of the 6 features that appear on this list, 3 are Lexical, 1 Syntactic and 2 Strings-related.

# Conclusion
In conclusion, the analysis reveals that combining various feature types (Lexical, Syntactic, and Strings) consistently provides substantial improvements over applying them on their own, especially when using the SVR and RFR predictors. The MLP, however, showed limited performance, likely due to insufficient generalization capability of the architectures used for the experiment. Feature selection significantly reduced noise, leading to more consistent performance across models.

The results of our comprehensive study demonstrate that the Random Forest Regressor (RFR) with the Unrestricted feature set (containing Lexical, Syntactic and String-based features) yields the best performance in predicting Semantic Text Similarity, with a Pearson correlation of **0.757023** with the Gold Standard.

Finally, some specific features, notably *WordNet-Augmented Word Overlap* and *Character n-grams*, were identified as most influential in predicting similarity, highlighting the importance of Lexical and String-related features. Overall, the study emphasizes the value of feature combination and selection in enhancing STS prediction accuracy.