from abc import ABC, abstractmethod


class Ride(ABC):
    def __init__(self, id: int, name: str, min_height_cm: int) -> None:
        self.id = id
        self.name = name
        self.min_height_cm = min_height_cm

    @abstractmethod
    def category(self) -> str:
        pass

    @abstractmethod
    def base_wait(self) -> int:
        pass

    def info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "min_height": self.min_height_cm,
            "category": self.category(),
            "base_wait": self.base_wait()
        }

    def wait_time(self, crowd_factor: float = 1.0) -> float:
        return round(self.base_wait() * crowd_factor, 2)


class RollerCoaster(Ride):
    def __init__(self, id: int, name: str, min_height_cm: int, inversions: int):
        super().__init__(id, name, min_height_cm)
        self.inversions = inversions

    def category(self) -> str:
        return "roller_coaster"

    def base_wait(self) -> int:
        return 30 + self.inversions * 5

    def info(self) -> dict:
        data = super().info()
        data["inversions"] = self.inversions
        return data


class Carousel(Ride):
    def __init__(self, id: int, name: str, min_height_cm: int, animals: list[str]):
        super().__init__(id, name, min_height_cm)
        self.animals = animals

    def category(self) -> str:
        return "family"

    def base_wait(self) -> int:
        return 10

    def info(self) -> dict:
        data = super().info()
        data["animals"] = self.animals
        return data


class Park:
    def __init__(self):
        self.rides: dict[int, Ride] = {}

    def add(self, ride: Ride) -> None:
        self.rides[ride.id] = ride

    def get(self, ride_id: int) -> Ride | None:
        return self.rides.get(ride_id)

    def list_all(self) -> list[Ride]:
        return [ride.info() for ride in self.rides.values()]
