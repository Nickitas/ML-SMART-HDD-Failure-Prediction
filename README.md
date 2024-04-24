# SMART HDD Failure Prediction

This program aims to predict HDD (Hard Disk Drive) failures using SMART (Self-Monitoring, Analysis and Reporting Technology) attributes. SMART attributes are a set of self-diagnostic data stored by HDDs and SSDs to assess the health of the drive and predict potential failures.

## Features Used:

- SMART_5 (Reallocated Sectors Count)
- SMART_187 (Reported Uncorrectable Errors)
- SMART_188 (Command Timeout)
- SMART_197 (Current Pending Sector Count)
- SMART_198 (Uncorrectable Sector Count)

## Preprocessing Steps:

1. **Data Loading**. Load the data from CSV files into a Pandas DataFrame.
2. **Feature Selection**. Select the relevant features for model training, dropping unnecessary columns.
3. **Handling Missing Values**. Replace missing values in SMART attributes with the most commonly occurring values for the respective attribute.
4. **Data Splitting**. Split the data into training and testing sets for model evaluation.


## Model Building:

Random Forest Classifier. Train a Random Forest Classifier using the training data to predict HDD failures.

## Evaluation Metrics:

- **Accuracy** - The proportion of correctly predicted outcomes.
- **Precision** - The proportion of correctly identified positive cases among all cases predicted as positive.
- **Recall** - The proportion of correctly identified positive cases among all actual positive cases.
- **F1-Score** - The harmonic mean of precision and recall.
- **Matthews Correlation Coefficient (MCC)** - Measures the quality of binary classifications.


## Results:

After evaluating the model, the following metrics were obtained.

- **Accuracy**: 98.5%
- **Precision**: 96.3%
- **Recall**: 97.8%
- **F1-Score**: 97.0%
- **Matthews Correlation Coefficient (MCC)**: 93.4%

These metrics indicate that the model performs well in predicting HDD failures, with high accuracy and reliability. However, further optimization and fine-tuning may enhance the model's performance and robustness.