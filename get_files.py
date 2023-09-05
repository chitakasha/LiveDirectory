import os

def get_files(directory):
    """
    Returns a list of all files in the specified directory and its subdirectories.

    Args:
        directory (str): The directory to search for files.

    Returns:
        A list of file paths (str).
    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)
    return files