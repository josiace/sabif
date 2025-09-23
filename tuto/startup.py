import os
from django.contrib.auth import get_user_model

def create_admin():
    User = get_user_model()
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "prince")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "afletounoudouprince5@gmail.com")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "afletounoudouprince5@gmail")

    if not User.objects.filter(username=username).exists():
        print("✅ Création du superutilisateur...")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print("ℹ️ Superutilisateur déjà présent.")
