import os

def count_problems_by_topic(base_path):
    problem_count = 0
    for topic in os.listdir(base_path):
        if topic.startswith("."):
            continue
        topic_path = os.path.join(base_path, topic)

        if os.path.isdir(topic_path):
            files = [f for f in os.listdir(topic_path) 
                    if os.path.isfile(os.path.join(topic_path, f)) and f.endswith(".py")]
            problem_count += len(files)
            print(f"{topic[2:]}: {len(files)} problem(s) solved")
    print(f"total problems solved: {problem_count}")
        

if __name__ == "__main__":
    repo_path = "/workspace/CodeTrek/navcodes"
    count_problems_by_topic(repo_path)
    
