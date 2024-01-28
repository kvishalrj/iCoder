### project/wsgi.py

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iCoder.settings')

application = get_wsgi_application()

# vercel config

app = application # add this line.
