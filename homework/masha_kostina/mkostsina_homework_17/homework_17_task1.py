import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="Full path to the directory with logs")
    parser.add_argument("-t", "--text", required=True, help="Text to search for")
    parser.add_argument("-f", "--first", action="store_true", help="Stop after the first match found")
    return parser.parse_args()

def build_words(line:str, search_text:str, context_words: int = 5) -> str:
    words = line.strip().split()
    result = []
    for ids, word in enumerate(words):
        if search_text in word:
            start = max(0, ids - context_words)
            end = min(len(words), ids + context_words + 1)
            res = " ".join(words[start:end])
            result.append(res)
    return "\n ".join(result)

def analyze_logs():
    args = parse_arguments()
    folder = args.directory
    search_text = args.text
    show_first_only = args.first
    
    if not os.path.isdir(folder):
        print(f"Ошибка: '{folder}' не является папкой или не существует")
        return
    
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    
    matches_found = 0
    
    for filename in files:
        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                for line_number, line in enumerate(f, start=1):
                    if search_text in line:
                        res = build_words(line, search_text)
                        print(f"[{filepath}] (line {line_number})")
                        print(f"  -> {res}")
                        matches_found += 1
                        if show_first_only:
                            return

    if matches_found == 0:
        print("Совпадений не найдено.")

if __name__ == "__main__":
    analyze_logs()
