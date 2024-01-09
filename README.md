# Exploring-NYC-School-Score
# NYC Schools SAT Performance Analysis

## Overview

This project aims to analyze SAT performance in New York City (NYC) schools using Python and the Pandas library. The analysis focuses on identifying top-performing schools and assessing the variability in SAT scores across different NYC boroughs.

## Project Structure

### 1. Importing Libraries and Reading the Dataset

#### Objective:
Import necessary Python libraries and read the project dataset into a Pandas DataFrame.

#### Steps:
1.1. Import the pandas library as `pd`.
1.2. Read the dataset ('schools.csv') into the DataFrame 'schools'.

### 2. Identifying Top Math-Performing Schools

#### Objective:
Create a DataFrame named `best_math_schools` containing the "school_name" and "average_math" scores for schools where the results are at least 80% of the maximum possible score. Sort the DataFrame by "average_math" in descending order.

#### Steps:
2.1. Create a boolean mask for schools with average math scores >= 80% of the maximum possible score.
2.2. Select relevant columns ("school_name" and "average_math") and apply the filter.
2.3. Sort the resulting DataFrame by "average_math" in descending order.

### 3. Top 10 Performing Schools Across SAT Sections

#### Objective:
Create a DataFrame named `top_10_schools` containing school names and a column named "total_SAT" with results sorted by "total_SAT" in descending order. Identify the top 10 performing schools based on scores across the three SAT sections.

#### Steps:
3.1. Create a DataFrame 'top_10_schools' with school names and a "total_SAT" column.
3.2. Identify the top 10 performing schools based on scores across SAT sections.
3.3. Sort the DataFrame by "total_SAT" in descending order.

### 4. Locating Borough with Largest SAT Standard Deviation

#### Objective:
Find the NYC borough with the largest standard deviation for "total_SAT." Create a DataFrame named `largest_std_dev` with "borough" as the index and columns: "num_schools" for the number of schools in the borough, "average_SAT" for the mean of "total_SAT," and "std_SAT" for the standard deviation of "total_SAT." All numeric values will be rounded to two decimal places.

#### Steps:
4.1. Group the data by "borough" and calculate statistics (count, mean, std) for "total_SAT."
4.2. Identify the borough with the largest standard deviation.
4.3. Create a DataFrame 'largest_std_dev' with required columns and rounded numeric values.

## Usage

1. Clone the repository: `git clone https://github.com/your-username/nyc-schools-sat-analysis.git`
2. Navigate to the project directory: `cd nyc-schools-sat-analysis`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the Jupyter notebook: `jupyter notebook`

## Requirements

- Python 3.x
- Jupyter Notebook
- Pandas library

Feel free to explore and customize the project according to your needs. Happy coding!
