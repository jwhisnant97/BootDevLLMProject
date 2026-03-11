from pathlib import Path
import time
import os

# Create a Path object for your directory
directory = Path('.')

for file_path in directory.iterdir():
    if file_path:  # Ensure it's not a subdirectory
        # Get metadata
        stats = file_path.stat()
        
        print(f"- {file_path.name}: file_size={stats.st_size}, is_dir={os.path.isdir(file_path.name)}")
