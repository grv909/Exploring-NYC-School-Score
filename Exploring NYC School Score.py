#!/usr/bin/env python
# coding: utf-8

# 
# # Project : Exploring NYC Public School Test Result Scores
# 

# ![schoolbus.jpg](attachment:schoolbus.jpg)
# Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a maximum score of 800 points. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.
# 
# Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend. 
# 
# 
# We will be answering three key questions about New York City (NYC) public school SAT performance.

# # Importing Libraries and Reading the Dataset

# Now, we will import the necessary Python libraries and read the project dataset into a Pandas DataFrame.
# Steps:
# 
# 1.Import the pandas library as pd. <br>
# 2. Read the dataset ('schools.csv') into the DataFrame 'schools'.

# In[1]:


# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()


# # Finding schools with the best math scores

# #### Objective:
# 
# Next, we will create a DataFrame named best_math_schools containing the "school_name" and "average_math" scores for schools where the results are at least 80% of the maximum possible score. We will sort the DataFrame by "average_math" in descending order.
# 
# #### Steps:
# 
# 1. Create a boolean mask for schools with average math scores >= 80% of the maximum possible score.
# 2. Select relevant columns ("school_name" and "average_math") and apply the filter.
# 3. Sort the resulting DataFrame by "average_math" in descending order.

# In[2]:


best_math_schools = schools[["school_name","average_math"]][schools["average_math"]>=0.8*800].sort_values(by="average_math",ascending=False)
best_math_schools.head()


# # Identifying the top 10 performing schools

# #### Objective:
# 
# Now, we will create a DataFrame named top_10_schools containing school names and a column named "total_SAT" with results sorted by "total_SAT" in descending order. We aim to identify the top 10 performing schools based on scores across the three SAT sections.
# #### Steps:
# 1. Create a DataFrame 'top_10_schools' with school names and a "total_SAT" column.
# 2. Identify the top 10 performing schools based on scores across SAT sections.
# 3. Sort the DataFrame by "total_SAT" in descending order.

# In[3]:


schools["total_SAT"] = schools["average_math"]+schools["average_reading"]+schools["average_writing"]
top_10_schools = schools[["school_name","total_SAT"]].sort_values(by="total_SAT",ascending=False).head(10)
top_10_schools


# # Locating the NYC borough with the largest standard deviation in SAT performance

# #### Objective:
# 
# In this step, we will find the NYC borough with the largest standard deviation for "total_SAT." We'll create a DataFrame named largest_std_dev with "borough" as the index and columns: "num_schools" for the number of schools in the borough, "average_SAT" for the mean of "total_SAT," and "std_SAT" for the standard deviation of "total_SAT." All numeric values will be rounded to two decimal places.
# 
# #### Steps:
# 
# 1. Group the data by "borough" and calculate statistics (count, mean, std) for "total_SAT."
# 2. Identify the borough with the largest standard deviation.
# 3. Create a DataFrame 'largest_std_dev' with required columns and rounded numeric values.

# In[4]:


# 1. Group the data by "borough" and find the number of schools, mean, and standard deviation of "total_SAT"
grouped_stats = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"])


# In[5]:


# 2. Find the NYC borough with the largest standard deviation
largest_std_borough = grouped_stats["std"].idxmax()


# In[6]:


# 3. Subset for the row where "std" is equal to the largest value for that column across the DataFrame
largest_std_dev = grouped_stats[grouped_stats.index == largest_std_borough]


# In[7]:


# 4. Rename columns
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})


# In[8]:


# 5. Display the resulting DataFrame with rounded values
largest_std_dev = largest_std_dev.round(2)
largest_std_dev

