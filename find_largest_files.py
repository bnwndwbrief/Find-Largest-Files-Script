import os
import argparse

def find_largest_files(directory, top_n=10):
    file_sizes = []
    for root, _, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                size = os.path.getsize(file_path)
                file_sizes.append((size, file_path))
            except OSError:
                continue

    file_sizes.sort(reverse=True)
    return file_sizes[:top_n]

def human_readable_size(size, decimal_places=2):
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024:
            return f"{size:.{decimal_places}f} {unit}"
        size /= 1024
    return f"{size:.{decimal_places}f} PB"

def main():
    parser = argparse.ArgumentParser(description="Find and display the largest files in a directory.")
    parser.add_argument("directory", help="Directory to search")
    parser.add_argument("-n", "--number", type=int, default=10, help="Number of files to display (default: 10)")
    args = parser.parse_args()

    largest_files = find_largest_files(args.directory, args.number)
    print(f"{'Size':>15}  {'File'}")
    print("-" * 70)
    for size, path in largest_files:
        print(f"{human_readable_size(size):>15}  {path}")

if __name__ == "__main__":
    main()
