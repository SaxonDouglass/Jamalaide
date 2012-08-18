DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',               # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/home/finn/projects/jamalaide/jamalaide/db', # Or path to database file if using sqlite3.
        'USER': '',                                           # Not used with sqlite3.
        'PASSWORD': '',                                       # Not used with sqlite3.
        'HOST': '',                                           # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                           # Set to empty string for default. Not used with sqlite3.
    }
}

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/finn/projects/jamalaide/jamalaide/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/finn/projects/jamalaide/jamalaide/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/finn/projects/jamalaide/jamalaide/site-static/',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qph2xfv4=r7k)+28wy^lf0#xr%b_hf^x6^-o5zh@%)=faf#&amp;(h'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/finn/projects/jamalaide/jamalaide/templates'
)
