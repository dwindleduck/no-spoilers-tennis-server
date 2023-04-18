from .base import *
import os
import dj_database_url



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "NDqwepoi>^%$&GohhhGGGfn12m00asvd9n813ib&*^2hi2!@3")


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = "RENDER" not in os.environ
DEBUG = False

ALLOWED_HOSTS = []


RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)



DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True
    )
}