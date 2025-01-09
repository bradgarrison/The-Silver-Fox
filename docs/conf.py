# File: docs/conf.py

extensions = [
   "multiproject",
   # Your other extensions.
   "sphinx.ext.intersphinx",
   ...
]

# Define the projects that will share this configuration file.
multiproject_projects = {
    "user": {},
    "dev": {
        # Set a custom path.
        "path": "dev",
    },
}

# Common options.
html_theme = "sphinx_rtd_theme"
