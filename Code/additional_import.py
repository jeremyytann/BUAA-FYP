# to add in the import list

# --------------------------- CARLA STATUS
from carla_status.refresh_carla_status import RefreshCarlaStatusThread

# --------------------------- MAP
from world_map.load_map import LoadMapThread

# --------------------------- VEHICLE
from vehicle.generate_vehicles import GenerateVehiclesThread
from vehicle.remove_all_vehicles import RemoveAllVehiclesThread
from vehicle.get_vehicle_list import GetVehicleListThread

# --------------------------- WALKER
from walker.generate_walkers import GenerateWalkersThread
from walker.remove_all_walkers import RemoveAllWalkersThread
from walker.get_walker_list import GetWalkerListThread

# --------------------------- WEATHER
from weather.fog_none import FogNoneThread
from weather.fog_light import FogLightThread
from weather.fog_heavy import FogHeavyThread
from weather.rain_none import RainNoneThread
from weather.rain_light import RainLightThread
from weather.rain_heavy import RainHeavyThread
from weather.time_morning import TimeMorningThread
from weather.time_noon import TimeNoonThread
from weather.time_evening import TimeEveningThread
from weather.time_night import TimeNightThread