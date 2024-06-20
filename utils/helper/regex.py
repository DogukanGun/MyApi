import re


def find_number_in_sentence(sentence):
    # Define the regex pattern for finding numbers
    pattern = r'\d+'
    # Search for the pattern in the sentence
    match = re.search(pattern, sentence)
    if match:
        return match.group()
    else:
        return None


def extract_hashes(text):
    """
    Extracts 66-character transaction or block hashes (with '0x' prefix) from the given text.

    Parameters:
    text (str): The input text containing transaction or block hashes.

    Returns:
    list: A list of extracted 64-character hexadecimal hashes.
    """
    # Define the regex pattern for a 64-character hexadecimal string
    pattern = r'\b0x[0-9a-fA-F]{64}\b'

    # Find all matches in the text
    matches = re.findall(pattern, text)

    return matches