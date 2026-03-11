import os
from pathlib import Path


def get_files_info(working_directory, directory="."):
    try:    
        working_dir_abs = os.path.abspath(working_directory)
        
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        
        if os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
            pass
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
            
        
        
        stat_return = []
        
        dir_path = Path(target_dir)
        

        for item in dir_path.iterdir():
            stats = item.stat()
            stat_return.append(f"- {item.name}: file_size={stats.st_size} bytes, is_dir={item.is_dir()}")

        
        return '\n'.join(stat_return)
    except Exception as e:
        return f"Error: {e}"
    