from django.apps import AppConfig


class AppConfig(AppConfig):
    pass


class CustomAppConfig(AppConfig):
    """
    This class may be use to setup configuration for scalable components
    and tools
    """
    name = 'custom'
