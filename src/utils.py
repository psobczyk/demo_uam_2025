import re

def count_words_in_text(text: str) -> int:
    return len(text.split())


def count_chars_in_text(text: str) -> int:
    # Remove spacesand count the characters
    return len(text)


def clean_text(text):
    # Remove lines with just page numbers or formatting
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        # Skip empty lines, lines with just numbers or short formatting lines
        if line.strip() and not re.match(r'^\d+$', line.strip()) and len(line.strip()) > 1:
            cleaned_lines.append(line)
            
    cleaned_text = ' '.join(cleaned_lines)
    
    # Remove special characters and extra whitespace
    cleaned_text = re.sub(r'[^\w\s\-—,.!?:;\"\'()]', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    return cleaned_text

