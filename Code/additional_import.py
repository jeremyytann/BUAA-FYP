# to add in the import list

# --------------------------- CARLA STATUS
from carla_status.refresh_carla_status import RefreshCarlaStatusThread

# --------------------------- MAP
from world_map.load_map import LoadMapThread
from world_map.reload_world import ReloadWorldThread

# --------------------------- PROP
from prop.generate_prop import GeneratePropThread
from prop.get_prop_list import GetPropListThread
from prop.view_selected_prop import ViewSelectedPropThread
from prop.remove_selected_prop import RemoveSelectedPropThread
from prop.prop_rotate_left import PropRotateLeftThread
from prop.prop_rotate_right import PropRotateRightThread

# --------------------------- VEHICLE
from vehicle.generate_vehicles import GenerateVehiclesThread
from vehicle.remove_all_vehicles import RemoveAllVehiclesThread
from vehicle.get_vehicle_list import GetVehicleListThread
from vehicle.view_selected_vehicle import ViewSelectedVehicleThread
from vehicle.remove_selected_vehicle import RemoveSelectedVehicleThread

# --------------------------- WALKER
from walker.generate_walkers import GenerateWalkersThread
from walker.remove_all_walkers import RemoveAllWalkersThread
from walker.get_walker_list import GetWalkerListThread
from walker.view_selected_walker import ViewSelectedWalkerThread
from walker.remove_selected_walker import RemoveSelectedWalkerThread

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
from weather.manual_weather import ManualWeatherThread