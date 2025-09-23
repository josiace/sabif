import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tuto.settings')

application = get_wsgi_application()

# Appel du script de création admin
try:
    from .startup import create_admin
    create_admin()
except Exception as e:
    print(f"⚠️ Erreur lors de la création du superutilisateur : {e}")
