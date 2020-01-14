
class CarControls:
    __slots__ = ['gear', 'steering', 'throttle', 'braking']

    def __init__(self, gear, steering, throttle, braking):
        self.gear = gear
        self.steering = steering
        self.throttle = throttle
        self.braking = braking

    def to_list(self):
        return [self.gear, self.steering, self.throttle, self.braking]


class CarControlUpdates:
    __slots__ = ['d_gear', 'd_steering', 'd_throttle', 'd_braking', 'supervisor']

    def __init__(self, gear, steering, throttle, braking, supervisor: bool):
        self.d_gear = gear
        self.d_steering = steering
        self.d_throttle = throttle
        self.d_braking = braking
        self.supervisor = supervisor

    def to_list(self):
        return [self.d_gear, self.d_steering, self.d_throttle, self.d_braking]

    def to_dict(self):
        return {element: getattr(self, element, 0) for element in self.__slots__}
