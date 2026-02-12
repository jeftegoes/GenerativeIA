# Classification - Alghoritms (models) <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Introduction](#1-introduction)
- [2. Study Case](#2-study-case)
  - [2.1. Dataset](#21-dataset)
  - [2.2. Training](#22-training)
- [3. Alghoritms (models)](#3-alghoritms-models)
  - [3.1. Naive Bayes](#31-naive-bayes)
    - [3.1.1. How It Works (Simple Steps)](#311-how-it-works-simple-steps)
    - [3.1.2. Example Uses](#312-example-uses)
    - [3.1.3. Use case result](#313-use-case-result)
    - [3.1.4. Key Idea](#314-key-idea)
  - [3.2. Decision trees](#32-decision-trees)
    - [3.2.1. How Decision Tree Differs from Naive Bayes](#321-how-decision-tree-differs-from-naive-bayes)
    - [3.2.2. How the Tree is Built](#322-how-the-tree-is-built)
    - [3.2.3. Structure of a Decision Tree](#323-structure-of-a-decision-tree)
    - [3.2.4. Key Idea](#324-key-idea)
    - [3.2.5. Advantages of Decision Trees](#325-advantages-of-decision-trees)
    - [3.2.6. Use case result](#326-use-case-result)
  - [3.3. Rule-Based](#33-rule-based)
    - [3.3.1. How It Works (Simple Steps)](#331-how-it-works-simple-steps)
    - [3.3.2. Key Idea](#332-key-idea)
    - [3.3.3. Use case result](#333-use-case-result)
  - [3.4. kNN](#34-knn)
    - [3.4.1. Use case result](#341-use-case-result)
  - [3.5. SVN](#35-svn)
    - [3.5.1. Use case result](#351-use-case-result)
  - [3.6. Logistic regression](#36-logistic-regression)
    - [3.6.1. Use case result](#361-use-case-result)

# 1. Introduction

- Assigns data into **predefined categories**.
- Requires **labeled historical data** (supervised learning).
- **Example**
  - Predicting whether a customer will churn or not.
- Scales well to high-dimensional data where human visualization is impossible.
- **Used in**
  - Fraud detection.
  - Customer retention.
  - Credit risk analysis.

# 2. Study Case

## 2.1. Dataset

| Credit history | Debts | Properties | Income              | Risk     |
| -------------- | ----- | ---------- | ------------------- | -------- |
| Bad            | High  | None       | < 15.000            | High     |
| Unknown        | High  | None       | >= 15.000 <= 35.000 | High     |
| Unknown        | Low   | None       | >= 15.000 <= 35.000 | Moderate |
| Unknown        | Low   | None       | < 15.000            | High     |
| Unknown        | Low   | None       | > 35.000            | Low      |
| Unknown        | Low   | Good       | > 35.000            | Low      |
| Bad            | Low   | None       | < 15.000            | High     |
| Bad            | Low   | Good       | > 35.000            | Moderate |
| Good           | Low   | None       | > 35.000            | Low      |
| Good           | High  | Good       | > 35.000            | Low      |
| Good           | High  | None       | < 15.000            | High     |
| Good           | High  | None       | >= 15.000 <= 35.000 | Moderate |
| Good           | High  | None       | > 35.000            | Low      |
| Bad            | High  | None       | >= 15.000 <= 35.000 | High     |

## 2.2. Training

| Credit history | Debts | Properties | Income              |
| -------------- | ----- | ---------- | ------------------- |
| Bad            | High  | Good       | < 15.000            |
| Unknown        | High  | Good       | < 15.000            |
| Unknown        | Low   | None       | > 35.000            |
| Good           | High  | Good       | >= 15.000 <= 35.000 |

# 3. Alghoritms (models)

## 3.1. Naive Bayes

- **Naive Bayes** is a **machine learning classification algorithm based on probability and statistics**.
  - It uses **historical data** to calculate how likely something belongs to a certain class.
  - The algorithm applies **Bayes' Theorem** and assumes that all features are **independent** of each other.
  - This simplifying assumption is why it is called _"naive"_.

### 3.1.1. How It Works (Simple Steps)

1. **Learn from Past Data**
   - Count how often each class appears.
   - Calculate how often each feature appears within each class.
2. **Build a Probability Model**
   - Convert these counts into probabilities.
3. **Classify New Data**
   - For a new example, multiply the probabilities of its features for each class.
4. **Choose the Most Probable Class**
   - The class with the highest probability becomes the prediction.

### 3.1.2. Example Uses

- Predicting **loan risk** (high, moderate, low).
- Detecting **spam emails**.
- Predicting if a customer will **buy a product**.
- Classifying **text or images**.

### 3.1.3. Use case result

| Risk (Prior)        | Credit History: Good (5) | Credit History: Unknown (5) | Credit History: Bad (4) | Debts: High (7) | Debts: Low (7) | Properties: None (11) | Properties: Good (3) | Income <15000 (3) | Income >=15000 <=35000 (4) | Income >35000 (7) |
| ------------------- | ------------------------ | --------------------------- | ----------------------- | --------------- | -------------- | --------------------- | -------------------- | ----------------- | -------------------------- | ----------------- |
| **High (6/14)**     | 1/6                      | 2/6                         | 3/6                     | 4/6             | 2/6            | 6/6                   | 0                    | 3/6               | 2/6                        | 1/6               |
| **Moderate (3/14)** | 1/3                      | 1/3                         | 1/3                     | 1/3             | 2/3            | 2/3                   | 1/3                  | 0                 | 2/3                        | 1/3               |
| **Low (5/14)**      | 3/5                      | 2/5                         | 0                       | 2/5             | 3/5            | 3/5                   | 2/5                  | 0                 | 0                          | 5/5               |

### 3.1.4. Key Idea

- **Naive Bayes**
  - Is a classification algorithm that uses **probability** to predict the class of new data based on patterns learned from historical data.
  - It assumes that all features are **independent** of each other (the "naive" assumption), and it calculates how likely each class is by multiplying the probabilities of the observed features.

## 3.2. Decision trees

- A **Decision Tree** is a machine learning algorithm used for **classification and prediction**.
- In this example, it is used to predict the **risk of giving a loan** (_High, Moderate, or Low_) based on customer data.

### 3.2.1. How Decision Tree Differs from Naive Bayes

- **Naive Bayes:** builds a **probability table**.
- **Decision Tree:** builds a **tree structure** that looks like a flowchart.
- Instead of calculating probabilities for prediction, Decision Trees make decisions by **following paths in the tree**.

### 3.2.2. How the Tree is Built

- The algorithm analyzes the historical dataset and performs mathematical calculations to decide:
  - Which feature should be at the **top** (most important).
  - How to split the data into branches.
- **The main calculations used are**
  - **Entropy** → Measures disorder or uncertainty in the data.
  - **Information Gain** → Measures how useful a feature is for classification.
- The **most significant features appear near the top** of the tree.
- Some features may **not appear at all** if they are not relevant for prediction.

### 3.2.3. Structure of a Decision Tree

- **Root Node:** First decision (e.g., Income).
- **Branches:** Possible values of that feature.
- **Internal Nodes:** Additional decisions (e.g., Credit History).
- **Leaf Nodes:** Final classification (High, Moderate, Low risk).

### 3.2.4. Key Idea

- **Decision Trees**
  - Learn patterns from historical data.
  - Create a **set of decision rules**.
  - Classify new data by simply **following the path** in the tree.

### 3.2.5. Advantages of Decision Trees

- Easy to understand and visualize.
- Works like human decision-making.
- Automatically ignores irrelevant features.
- No probability calculations needed during prediction.

### 3.2.6. Use case result

![Decision Tree Result](/Images/DecisionTree.png)

## 3.3. Rule-Based

- **Rule-Based Learning** is a **machine learning classification approach** that creates a set of **IF–THEN rules** from historical data to make predictions.
- Instead of using probability tables (Naive Bayes) or a tree structure (Decision Tree), this method learns **explicit logical rules** that are easy to interpret.

### 3.3.1. How It Works (Simple Steps)

1. **Learn from Past Data**
   - The algorithm receives a historical dataset (e.g., credit history, debts, properties, income).
   - It analyzes patterns and relationships between features and the final class (risk).
2. **Generate Rules**
   - After mathematical analysis, the model creates rules such as:
     - **IF** Income ≥ 35 AND Credit History = Good → **Risk = Low**
     - **IF** Income ≥ 35 AND Credit History = Unknown → **Risk = Low**
3. **Create a Default Rule**
   - A fallback rule is defined for cases where no other rule applies:
     - **DEFAULT → Risk = High**
4. **Classify New Data**
   - For a new customer, the system checks each rule in order.
   - The first rule that matches the data is applied.
   - If none match, the **default rule** is used.

### 3.3.2. Key Idea

- **Rule-Based Learning**
  - Converts data into **human-readable rules**.
  - Applies rules sequentially to classify new cases.
  - May ignore irrelevant features if they are not useful for decision-making.

### 3.3.3. Use case result

| Rule                                             | Result      |
| ------------------------------------------------ | ----------- |
| If Income >= 35.000 and Credit history = Good    | Risk = Low  |
| If Income >= 35.000 and Credit history = Unknown | Risk = Low  |
| Default                                          | Risk = High |

## 3.4. kNN

### 3.4.1. Use case result

## 3.5. SVN

### 3.5.1. Use case result

## 3.6. Logistic regression

### 3.6.1. Use case result
