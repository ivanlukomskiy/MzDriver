import logging

from mzdriver.servo_control import SERVO_CONTROL

log = logging.getLogger(__name__)


class DriverState:
    vy = 0

    def set_vy(self, value):
        try:
            fv = float(value)
            self.vy = 100 if fv >= 100 else -100 if fv <= -100 else fv
            SERVO_CONTROL.set(self.vy)
            log.info("VY set to {}".format(fv))
        except ValueError:
            log.error("Failed to set VY")


HOLDER = DriverState()
