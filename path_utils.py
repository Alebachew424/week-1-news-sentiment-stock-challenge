import os

def get_project_root():
    # Assumes script is inside 'scripts' folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    return project_root

def get_data_path(*relative_path_parts):
    """
    Constructs an absolute data path relative to the project root.
    Usage:
        get_data_path('Data', 'Data', 'raw_analyst_ratings', 'raw_analyst_ratings.csv')
    """
    project_root = get_project_root()
    return os.path.join(project_root, *relative_path_parts)