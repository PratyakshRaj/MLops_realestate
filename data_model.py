from pydantic import BaseModel

class realestate(BaseModel):
    type : str
    amenities : str
    postcode : str
    Area : str
    living_area : float 
    surface_of_garden_for_houses : float 	
    Building_height	: float
    proprerty_average_height : float	
    number_of_floors : float	
    perimeter : float	
    age_in_years : float