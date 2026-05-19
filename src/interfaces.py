from typing import Any, Protocol


class FleetSettings(Protocol):
    screen_width: int
    screen_height: int
    fleet_drop_speed: int
    fleet_direction: int


class BulletSettings(Protocol):
    bullet_allowed: int


class HasRect(Protocol):
    rect: Any


class KeyboardControlledShip(Protocol):
    moving_right: bool
    moving_left: bool
    rect: Any


class AlienFactory(Protocol):
    def __call__(self, screen: Any, settings: Any) -> Any:
        pass


class BulletFactory(Protocol):
    def __call__(self, screen: Any, settings: Any, ship: Any) -> Any:
        pass
