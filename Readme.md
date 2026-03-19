📊** Applied Statistics & Exploratory Data Analysis Project**

(Originally done in 2021 — republished to preserve and showcase foundational work)

📝** Project Note**

This project was originally completed in 2021 as part of my learning in Applied Statistics and Analysis.

I am publishing it here to:

Preserve my early work

Track my learning journey

Showcase strong fundamentals in statistics and data analysis

Even though this is an old project, the concepts used here are timeless and highly relevant in real-world data science.

🎯 Project Overview

This project covers:

Probability fundamentals

Binomial & Poisson distributions

Exploratory Data Analysis (EDA)

Feature engineering

Hypothesis testing

Data-driven business recommendations

📌 Key Concepts Used

🔹 1. Joint Probability

Joint probability measures the likelihood of two events happening together.

Example:

Probability that a person planned to purchase and actually purchased

🔹 2. Conditional Probability

Conditional probability tells us:

What is the probability of event A happening given that event B has already happened?

Formula:

P(A | B) = P(A ∩ B) / P(B)

🔹 3. Binomial Distribution

Used when:

Fixed number of trials (n)

Only two outcomes (success/failure)

Probability remains constant

Example:

Number of defective items in a batch

🔹 4. Poisson Distribution

Used when:

Events occur randomly over time or space

We count occurrences in an interval

Example:

Number of customers arriving in a store

Number of cars sold per week

🔹 5. Exploratory Data Analysis (EDA)

EDA is used to:

Understand data patterns

Detect outliers

Identify relationships between variables

🔹 6. Feature Engineering

New features created:

Age of team

Win Rate

Championship Rate

These helped in better performance analysis.

🔹 7. Hypothesis Testing

Used to make statistical decisions.

Methods used:

Z-test

T-test

Proportion test

📊 Part 1: Probability & Distributions
✔ Key Results

Joint Probability = 0.2

Conditional Probability = 0.8

Binomial Distribution:

P(X ≤ 2) = 0.9885

P(X ≥ 3) = 0.0115

👉 Insight: Defects are very rare

Poisson Distribution:

P(X ≥ 1) = 0.9502

P(2 ≤ X < 5) = 0.6161

👉 Insight: Events occur frequently but within a range

📊 Part 2: Basketball Dataset Analysis
🔧 Data Processing Steps

Cleaned missing values

Converted object types to numeric

Extracted year from text fields

Created new performance metrics

🏆 Top Performing Teams

Team 1

Team 2

Team 3

Team 4

Team 5

👉 High win rate + strong consistency

📉 Low Performing Teams

Team 61

Team 60

Team 55

👉 Low win rate → not ideal for investment

📈 Key Insights

Strong relationship between games played and wins

Win rate is a strong indicator of performance

Older teams tend to perform better, but not always

Some young teams show strong potential

🎯 Business Recommendation
Best teams to approach:

Team 1

Team 2

Team 3

Team 4

Team 5

High potential team:

Team 21 (young + good performance)

📊 Part 3: Startup Data Analysis
🔧 Data Preprocessing

Removed missing values

Converted funding values into numeric format

Removed outliers

📉 Hypothesis Testing Results
1️⃣ Funding vs Company Success

p-value ≈ 0.19

👉 No significant relationship
👉 More funding does NOT guarantee success

2️⃣ Winners vs Contestants

p-value ≈ 0.037

👉 Significant difference exists
👉 Winners are more likely to stay operational

🚀 Final Learnings

Probability helps in decision-making under uncertainty

Statistical distributions model real-world scenarios

EDA is critical before applying ML models

Data-driven insights are more reliable than assumptions

Strong fundamentals are key to becoming a good data scientist
