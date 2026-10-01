import os

file_name = "index.html"

# Check 1: HTML file exists
assert os.path.exists(file_name), "index.html does not exist"

# Read HTML file
with open(file_name, "r", encoding="utf-8") as file:
    html = file.read().lower()

# Required elements
required_elements = [
    "<html",
    "<form",
    'id="name"',
    'id="email"',
    'id="roll"',
    'id="course"',
    'type="submit"',
]

# Check required elements
for element in required_elements:
    assert element in html, f"Missing required element: {element}"

print("All HTML tests passed successfully!")