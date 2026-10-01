import os

# Check required files
required_files = [
    "index.html",
    "style.css",
    "script.js"
]

for file in required_files:
    assert os.path.exists(file), f"{file} does not exist"

# Read files
with open("index.html", "r", encoding="utf-8") as file:
    html = file.read().lower()

with open("style.css", "r", encoding="utf-8") as file:
    css = file.read()

with open("script.js", "r", encoding="utf-8") as file:
    js = file.read()

# HTML tests
required_html = [
    "<html",
    "<form",
    'id="name"',
    'id="email"',
    'id="roll"',
    'id="course"',
    'id="phone"',
    'type="submit"',
    'style.css',
    'script.js'
]

for element in required_html:
    assert element in html, f"Missing HTML element: {element}"

# CSS test
assert len(css.strip()) > 0, "CSS file is empty"

# JavaScript test
assert "addEventListener" in js, "JavaScript event listener missing"
assert "registrationForm" in js, "Form JavaScript functionality missing"

print("====================================")
print("All tests passed successfully!")
print("HTML: PASS")
print("CSS: PASS")
print("JavaScript: PASS")
print("====================================")