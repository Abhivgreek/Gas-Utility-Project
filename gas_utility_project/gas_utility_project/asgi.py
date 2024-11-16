# gas_utility_project/asgi.py

import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'gas_utility_project' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gas_utility_project.settings')

application = get_asgi_application()