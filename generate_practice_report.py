import os
import csv

def list_problems_by_topic(base_path, output_file="problem_list.csv"):
    rows = []
    total_problems = 0

    for topic in sorted(os.listdir(base_path)):
        if topic.startswith("."):
            continue

        topic_path = os.path.join(base_path, topic)
        if os.path.isdir(topic_path):
            for f in sorted(os.listdir(topic_path)):
                file_path = os.path.join(topic_path, f)
                if os.path.isfile(file_path):
                    topic_name = topic[2:].replace("_"," ").title()
                    problem_name = f[2:-3].replace("_"," ").title()
                    file_path = file_path.replace("/workspace/CodeTrek/","https://github.com/NaveenBasavaraj/CodeTrek/")
                    rows.append([problem_name, topic_name, file_path])
                    total_problems += 1

    # Write to CSV
    with open(output_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Problem Name", "Topic", "Link"])
        writer.writerows(rows)

        # Add total at the end
        writer.writerow(["Total Problems", total_problems])

    print(f"✅ Problem list saved to: {output_file}")

if __name__ == "__main__":
    repo_path = "/workspace/CodeTrek"
    list_problems_by_topic(repo_path)