from enum import Enum


class VehicleSize(Enum):
    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2
    
class Vehicle:
    def __init__(self, vehicle_size, plate_no, spot_size):
        self.vehicle_size = vehicle_size
        self.plate_no = plate_no
        self.spot_size = spot_size
        self.spots_taken = []
    
    def clear_spots(self):
        pass
        # TODO


class Car(Vehicle):
    def __init__(self, plate_no):
        super().__init__(VehicleSize.COMPACT, plate_no, 1)
    
    
        
        