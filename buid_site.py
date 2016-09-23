#!/usr/bin/env python

# Perhaps jinja2 is a more lightweigth solution
from jinja2 import Template

# Get the list of files (and title of the book) from the file "_book.yml"

# Create _site directory

# For each file:
	# Open and read it
	# Generate html string
	# Retrieve h1 and h2s (store the list of h1 and h2s for later)
	# Generate file and add html string to it

# For each html file generated
	# Read the file
	# Fill the navbar




# Our template. Could just as easily be stored in a separate file
template = """
<html>
<head>
<title>Template {{ title }}</title>
</head>
<body>
Body with {{ mystring }}.
</body>
</html>
"""

t = Template(template)
c = Context({"title": "title from code",
             "mystring":"string from code"})
print t.render(c)