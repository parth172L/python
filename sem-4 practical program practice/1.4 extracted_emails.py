# extracted emails

import re
def extract_emails(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Regex to find email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content)
    return emails

# Example usage:
emails = extract_emails('sample.txt')
print("Extracted Emails:", emails)