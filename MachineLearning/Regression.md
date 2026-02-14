# Regression - Alghoritms (models) <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Introduction](#1-introduction)
- [2. Classification vs Regression](#2-classification-vs-regression)
- [3. How Regression Works](#3-how-regression-works)
- [4. Examples of Regression Applications](#4-examples-of-regression-applications)
- [5. Key Idea](#5-key-idea)

# 1. Introduction

- **Regression** is a type of machine learning used to **predict numerical values**.
- While **classification** predicts categories (e.g., High, Medium, Low risk), **regression predicts numbers** such as prices, sales, probabilities, or measurements.

# 2. Classification vs Regression

- **Classification -> predicts classes (labels)**
  - **Example:** Loan risk = High / Medium / Low.
- **Regression -> predicts continuous values (numbers)**
  - **Example:** Sales = 52,000 units.

# 3. How Regression Works

- Regression models learn the relationship between:
  - **X (independent variables)** -> input features.
  - **Y (dependent variable)** -> the numeric value we want to predict.
- The algorithm finds patterns in past data to estimate **Y based on X**.

# 4. Examples of Regression Applications

- Predicting **sales** based on advertising costs.
- Predicting **wind speed** using temperature, humidity, and air pressure.
- Estimating the **dollar price** based on economic factors.
- Predicting the **probability of patient survival**.
- Calculating **investment risk** from customer financial behavior.
- Defining a **new credit card limit** based on past spending.
- Predicting **product prices** or future values.
- In all these cases, the output (**Y**) is a **number**, not a category.

# 5. Key Idea

- Regression is used when the goal is to **estimate a measurable value** rather than assign a label.
- Regression predicts **how much** or **how many**, while classification predicts **which category**.
