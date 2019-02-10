from django.apps import AppConfig

from mzdriver.servo_control import SERVO_CONTROL


class MyAppConfig(AppConfig):
    name = 'mzdriver'
    verbose_name = "MZ Driver"

    def ready(self):
        SERVO_CONTROL.setup()
