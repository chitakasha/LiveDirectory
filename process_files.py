def process_files(files):
    """
    Processes a list of files by counting the number of words in each file.

    Args:
        files (list): A list of file paths (str).

    Returns:
        A list of tuples, where each tuple contains the file path (str) and the word count (int).
    """
    results = []
    for file in files:
        with open(file, "r") as f:
            text = f.read()
            word_count = len(text.split())
            results.append((file, word_count))
    return results