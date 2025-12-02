
def count_lines(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return sum(1 for _ in f)

if __name__ == "__main__":
    path = input("Enter path to text file: ").strip() 
    n = count_lines(path)
    print(f"Number of lines: {n}")
        
