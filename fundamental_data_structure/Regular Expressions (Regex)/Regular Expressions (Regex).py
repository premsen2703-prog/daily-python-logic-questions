import re

text = "Contact me at contact@email.com or support@company.org"

# Find all email addresses in the text
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)

print(emails)  # Output: ['contact@email.com', 'support@company.org']
