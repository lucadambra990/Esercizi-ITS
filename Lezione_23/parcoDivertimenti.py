from abc import ABC,abstractmethod

class Ride(ABC):
    def __init__(self,id:str,name:str,min_height_cm:int)->None:
        self.id=id
        self.name=name
        self.min_height_cm=min_height_cm
    
    @abstractmethod
    def category(self):
        pass

    @abstractmethod
    def base_wait(self):
        pass

    def info(self)->dict:
        return {"id":self.id,
                    "name":self.name,
                        "min_height":self.min_height_cm,
                            "category":self.category(),
                                "time":self.base_wait()}
        
    def wait_time(self,crowd_factor:float=1.0):
        return round(self.base_wait() * crowd_factor,2)


class RollerCoaster(Ride):
    def __init__(self, id, name, min_height_cm,inversions:int):
        super().__init__(id, name, min_height_cm)
        self.inversions=inversions
    
    def category(self):
        return "roller_coaster"
    
    def base_wait(self):
        return super().base_wait()
    
    def info(self):
        info_inv = super().info()
        info_inv["inversions"] = self.inversions
        return info_inv
    
class Carousel(Ride):
    def __init__(self, id, name, min_height_cm,animals:list[str]):
        super().__init__(id, name, min_height_cm)
        self.animals=animals

    def category(self):
        return "family"
    
    def base_wait(self):
        return super().base_wait()
    
    def info(self):
        info_animals = super().info()
        info_animals["animals"] = self.animals

class Park:
    def __init__(self,rides:dict[str,Ride] = {}):
        self.rides = rides

    def add(self,ride):
        self.rides[ride.id]=ride

    def get(self,ride_id:str) -> Ride:
        if ride_id in self.rides:
            return self.rides[ride_id]
        return None
    
    def list_all(self) -> list[Ride]:
        return list(self.rides.values())

    