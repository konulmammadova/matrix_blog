from django.apps import AppConfig


class MatrixAppConfig(AppConfig):
    name = 'matrix_app'
    verbose_name = 'Matrix'

    def ready(self):
        import matrix_app.signals


