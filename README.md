# Query-Evaluation-on-Relational-Data
This project implements a query evaluation system for two relational tables, R and S, stored in CSV files (R.csv and S.csv). The goal is to implement query operators and evaluate queries on a small database using Python. The project is divided into three parts, each addressing a specific query task.

# Part 1: Group-by with Aggregation
The first part computes aggregation results (sum, min, max) over a specified attribute in a table using a modified merge sort algorithm. The input consists of a CSV file, a group-by attribute, an aggregation attribute, and the desired aggregation function (sum, min, or max). The output is written to O1.csv in the form of tuples (x, y), where x is the group-by attribute value, and y is the result of the aggregation function applied to the values of the aggregation attribute for each group.

- Code file: part1.py
- Input: CSV file (R.csv or S.csv), group-by attribute, aggregation attribute, aggregation function.
- Output: Aggregated results in O1.csv.

# Part 2: Merge Join
The second part performs a natural join between the tables R and S on the common attribute A. The schema for R is (A, B, C), and for S it is (D, A, E). The join is implemented using the merge-join algorithm, and the output is a table with the schema (A, B, C, D, E) written to O2.csv.

- Code file: part2.py
- Input: R.csv, S.csv.
- Output: Join result in O2.csv.

# Part 3: Composite Query
The third part evaluates a composite query: sum(E) for A where R.C = 7, after performing a natural join between R and S. The result is grouped by S.A and the sum of E is calculated for each group where the condition R.C = 7 holds. The result is written to O3.csv.

- Code file: part3.py
- Input: R.csv, S.csv.
- Output: Query result in O3.csv.

# Instructions
  1. Part 1: Run part1.py with command-line arguments specifying the input file, group-by attribute, aggregation attribute, and aggregation function. Example: python part1.py R.csv 1 2 max

  2. Part 2: Run part2.py to execute the natural join between R.csv and S.csv. Example: python part2.py

  3. Part 3: Run part3.py to execute the composite query. Example: python part3.py

# Notes
- The input CSV files must be sorted by the join key (attribute A).
- No external libraries (such as Pandas) are used to process the CSV files.
- The project is implemented in Python, ensuring it runs efficiently even for large datasets.
