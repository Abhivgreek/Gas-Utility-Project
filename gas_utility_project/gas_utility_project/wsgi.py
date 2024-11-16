# gas_utility_project/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'gas_utility_project' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gas_utility_project.settings')

application = get_wsgi_application()
