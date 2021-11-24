from django.apps import AppConfig


class AuthenticateConfig(AppConfig):
    name = 'login'


class PreviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'preview'
