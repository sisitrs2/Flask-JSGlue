# Version 1.0.0 - 21.8.2024
## Overview

This fork of Flask-JSGlue (0.3.1) was created to update the dependencies to work with newer versions of Flask, Jinja2, and Werkzeug. The original functionality has been retained with minimal changes to ensure compatibility with updated libraries.

## Updated Import Statements:
Replaced the deprecated import from jinja2 import Markup with from markupsafe import Markup to ensure compatibility with Jinja2 3.1.0 and later.
Compatibility Adjustments:
Adjusted the package to be compatible with Flask 3.0.x, Jinja2 3.1.x, and Werkzeug 3.x.

These changes are focused solely on maintaining compatibility with newer versions of Flask and its dependencies. No additional features have been added, and the core functionality remains the same.
