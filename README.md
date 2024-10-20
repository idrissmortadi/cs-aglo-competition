# Graph Dominating Set Algorithm Evaluator

## 🎯 Project Overview

This project is part of an advanced algorithm competition for CS 3A INFO students at CentraleSupélec. It focuses on evaluating algorithms that calculate two dominating sets (D1 and D2) in graphs while minimizing their sizes and intersection.

## 🧩 Key Components

1. **Dominating Set Algorithm**: Implemented in `dominant.py`, this algorithm finds two dominating sets D1 and D2 for a given graph.

2. **Score Calculator**: Located in `calculate_latest_scores.py`, this script evaluates the performance of the dominating set algorithm by calculating scores based on the latest output file.

## 🔧 How It Works

1. The `dominant.py` script processes input graphs and generates dominating sets.
2. Results are saved in the `rep_answer` directory with timestamps.
3. The `calculate_latest_scores.py` script finds the most recent output file and calculates scores.

## 🧮 Score Calculation

The score for each graph is calculated as: (|D1| + |D2| + |D1 ∩ D2|) / |V|
Where:
- |D1| is the size of the first dominating set
- |D2| is the size of the second dominating set
- |D1 ∩ D2| is the size of the intersection between D1 and D2
- |V| is the total number of vertices in the graph

A lower score indicates better performance.

## 🚀 Usage

1. Run the dominating set algorithm:
   ```
   python dominant.py [input_dir] [output_dir]
   ```
   Where `[input_dir]` contains the input graph files and `[output_dir]` is where the results will be saved.

2. Calculate scores for the latest output:
   ```
   python calculate_latest_scores.py
   ```
   This will automatically find the most recent output file in the `rep_answer` directory and calculate scores.

## 📋 Requirements

- Python 3.x
- NetworkX library

## 📜 Competition Rules

1. Only participants with CentraleSupélec email addresses are accepted.
2. The execution time limit is 20 seconds.
3. The algorithm must be deterministic.
4. Random functions can only be used to arbitrarily choose a node or edge in the graph.
5. It's forbidden to run the algorithm multiple times and return the best solution.
6. Algorithms based on linear programming are not accepted.
7. Installing external libraries or loading code from modules you haven't coded yourself is prohibited.
8. The NetworkX library is available, but using its `min_weighted_dominating_set` function is forbidden.

