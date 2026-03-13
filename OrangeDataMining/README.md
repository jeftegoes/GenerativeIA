# Orange Data Mining <!-- omit in toc -->

- [1. Widgets](#1-widgets)
  - [1.1. Data Table](#11-data-table)
  - [1.2. Select Columns](#12-select-columns)
  - [1.3. Correlations](#13-correlations)
  - [1.4. Distributions](#14-distributions)
  - [1.5. Box Plot](#15-box-plot)
  - [1.6. Scatter Plot](#16-scatter-plot)

# 1. Widgets

- These widgets are commonly used in **exploratory data analysis (EDA)** to understand the dataset before applying machine learning.

## 1.1. Data Table

- **Summary**
  - Displays the dataset in a spreadsheet-like format where you can view all rows and columns.
- **What it is used for**
  - Inspect raw data
  - Check missing values
  - Verify that the dataset loaded correctly
- **Simple use-case**
  - After loading a **Fake News dataset**, you open **Data Table** to confirm columns such as:
  - `title`
  - `text`
  - `label (fake/real)`
- This helps verify that the dataset structure is correct before training a model.

## 1.2. Select Columns

- **Summary**
  - Allows you to **choose which columns will be features, targets, or metadata** for the machine learning model.
- **What it is used for**
  - Define the **target variable**
  - Remove irrelevant columns
  - Organize attributes for modeling
- **Simple use-case**
  - In a **fake news classifier**:
    - `text` -> Feature
    - `label` -> Target (Fake / Real)
    - `id` -> Meta attribute
- This prepares the dataset for training a classifier.

## 1.3. Correlations

- **Summary**
  - Shows the **correlation between numerical variables**, indicating how strongly they are related.
- **What it is used for**
  - Detect relationships between variables
  - Identify redundant features
  - Feature selection
- **Simple use-case**
  - In a **financial dataset**, you might analyze:
    - `income`
    - `loan_amount`
    - `credit_score`
- If `income` and `loan_amount` are highly correlated, the model may not need both.

## 1.4. Distributions

- **Summary:**
  - Displays the **distribution of values for a variable**, often using histograms.
- **What it is used for:**
  - Understand how values are spread
  - Detect skewed data
  - Compare distributions across classes
- **Simple use-case:**
  - In a **spam detection dataset**, you might check the distribution of:
    - `message_length`
- You may discover that **spam messages are generally longer** than normal ones.

## 1.5. Box Plot

- **Summary**
  - Shows **median, quartiles, and outliers** of a dataset.
- **What it is used for**
  - Compare groups
  - Detect outliers
  - Understand variability
- **Simple use-case:**
  - In a **student performance dataset**, you compare:
    - `exam_score` grouped by `study_method`
- The box plot may show that **students using method A have a higher median score**.

## 1.6. Scatter Plot

- **Summary:**
  - Displays the **relationship between two numerical variables** using points on a graph.
- **What it is used for:**
  - Detect patterns.
  - Identify clusters.
  - Observe correlations visually.
- **Simple use-case:**
  - In a **customer dataset**, you plot:
    - `age` vs `annual_spending`
- You may identify **customer segments**, such as:
  - young high spenders
  - older low spenders
