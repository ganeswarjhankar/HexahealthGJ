import random

strings = ["https://www.hexahealth.com/marketing/lasik-bangalore",
           "https://www.hexahealth.com/campaigns/liver-transplant", "string3", "string4", "string5", "string6",
           "string7", "string8", "string9",
           "string10", "string11", "https://www.hexahealth.com/"]

# Generate 10 random indices between 0 and 11 (inclusive)
indices = [random.randint(0, len(strings)-1) for _ in range(10)]

# Create a new list to store the 10 unique random strings
random_strings = []

# Use a set to keep track of the strings that have been added
added_strings = set()

# Iterate over the list of indices
for index in indices:
  # Retrieve the corresponding string from the original list
  s = strings[index]
  # If the string has not already been added to the new list, add it
  if s not in added_strings:
    random_strings.append(s)
    added_strings.add(s)

# Print the list of unique random strings
print(random_strings)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By