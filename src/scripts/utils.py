import sys
import os

def add_src_to_path():
    src_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    # Add the parent directory to sys.path
    if src_folder_path not in sys.path:
        sys.path.append(src_folder_path)
