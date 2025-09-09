# Find Largest Files Script

This Python script finds and displays the largest files in a given directory. It is useful for quickly identifying files that are taking up the most disk space.

## Features

- Recursively searches through all subdirectories.
- Displays file sizes in a human-readable format (B, KB, MB, GB, TB).
- Allows you to specify how many of the largest files to display (default is 10).

## Usage

1. **Clone or Download** this repository.

2. **Run the script** from the command line:

   ```
   python find_largest_files.py /path/to/directory -n 15
   ```

   - Replace `/path/to/directory` with the directory you want to search.
   - The `-n` option lets you specify how many files to display (optional, default is 10).

## Example Output

```
          Size  File
----------------------------------------------------------------------
    1.25 GB  /home/user/Videos/movie.mp4
  650.00 MB  /home/user/Downloads/installer.iso
  430.50 MB  /home/user/Music/song.flac
```

## Requirements

- Python 3.x

No additional Python packages are required.

## License

This project is licensed under the MIT License.
