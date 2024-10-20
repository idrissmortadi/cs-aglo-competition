import os
import glob


def calculate_score_from_line(output_line):
    parts = output_line.split("-")
    graph_name = parts[0].split(" ")[0]

    d1 = set(map(int, parts[0].strip().split(" ")[1:]))
    d2 = set(map(int, parts[1].strip().split(" ")))

    intersection_size = len(d1.intersection(d2))
    total_vertices = max(max(d1), max(d2)) + 1

    score = (len(d1) + len(d2) + intersection_size) / total_vertices

    return graph_name, score


def process_latest_output_file(answer_dir):
    # Find the most recent answer file
    answer_files = glob.glob(os.path.join(answer_dir, "answers_*.txt"))
    if not answer_files:
        print("No answer files found.")
        return {}

    latest_file = max(answer_files, key=os.path.getctime)
    print(f"Processing file: {latest_file}")

    results = {}
    with open(latest_file, "r") as f:
        for line in f:
            graph_name, score = calculate_score_from_line(line)
            results[graph_name] = score

    return results


# Usage
answer_dir = "rep_answer"  # Adjust this path if necessary
scores = process_latest_output_file(answer_dir)

# Print results
for graph_name, score in scores.items():
    print(f"{graph_name}: Score = {score:.4f}")

# Calculate average score
if scores:
    average_score = sum(scores.values()) / len(scores)
    print(f"\nAverage Score: {average_score:.4f}")
else:
    print("\nNo scores calculated.")
