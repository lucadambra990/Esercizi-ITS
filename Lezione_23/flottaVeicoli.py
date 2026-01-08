from abc import ABC,abstractmethod

class Veichle:
    def __init__(self,plate_id:str,model:str,driver_name:str,registration_year:int,status:list[str]):
        self.plate_id=plate_id
        self.model=model
        self.driver_name=None
        self.registration_year=registration_year
        self.status=["available","rented","maintenance","cleaning","retired"]
    
    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def base_cleaning_time(self):
        pass

    @abstractmethod
    def wear_level(self):
        pass

    def info(self):
        return {
            "id":self.plate_id,
            "model":self.model,
            "driver_name":self.driver_name,
            "veichle_type":self.vehicle_type,
            "registration_year":self.registration_year,
            "status":self.status
        }
    
    def estimated_prep_time(self,factor:float = 1.0):
        return (self.base_cleaning_time() * factor) + self.wear_level
    
class Car(Veichle):
    def __init__(self, plate_id, model, driver_name, registration_year, status,doors:int,is_cabrio:bool):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.doors=doors
        self.is_cabrio=False

    def vehicle_type(self):
        return "car"
    
    def base_cleaning_time(self):
        return super().base_cleaning_time()
    
    def wear_level(self):
        return super().wear_level()
    
    def info(self):
        return super().info(self.doors,self.is_cabrio)

class Van(Veichle):
    def __init__(self, plate_id, model, driver_name, registration_year, status,max_load_kg:int,require_special_license:bool):
        super().__init__(plate_id, model, driver_name, registration_year, status)
        self.max_load_kg = max_load_kg
        self.require_special_license = False

    def vehicle_type(self):
        return "van"
    
    def base_cleaning_time(self):
        return super().base_cleaning_time()
    
    def wear_level(self):
        return super().wear_level()
    
    def info(self):
        return super().info(self.max_load_kg,self.require_special_license)
    
class FleetManager:
    def __init__(self):
        self.vehicles:dict[str,Veichle]={}

    def add(self,vehicle:Veichle)->bool:
        if vehicle in self.vehicles:
            return False
        else:
            self.vehicles["id"] = vehicle
            return True
        
    def get(self,plate_id:str)->Veichle:
        if plate_id in self.vehicles:
            return self.vehicles[plate_id]
        return None
    
    def update(self,plate_id:str,new_vehicle:Veichle)->None:
        pass

    def patch_status(self,plate_id:str,new_status:str)->None:
        pass

    def delete(self,plate_id:str)->bool:
        pass

    def list_all(self):
        pass