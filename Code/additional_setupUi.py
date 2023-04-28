# to add in the setupUi

# --------------------------- CARLA STATUS
# Refresh Carla Status
self.refresh_carla_status_thread = RefreshCarlaStatusThread(MainWindow=MainWindow)
self.refresh_carla_status_thread.start()
self.carla_status_refresh_button.clicked.connect(self.refresh_carla_status_thread.start)

# --------------------------- MAP
# Load Map
self.load_map_thread = LoadMapThread(MainWindow=MainWindow)
self.load_map_button.clicked.connect(self.load_map_thread.start)

# --------------------------- VEHICLE
# Generate Vehicles
self.generate_vehicles_thread = GenerateVehiclesThread(MainWindow=MainWindow)
self.generate_vehicles_button.clicked.connect(self.generate_vehicles)
# Get Vehicle List
self.get_vehicle_list_thread = GetVehicleListThread(MainWindow=MainWindow)
self.get_vehicle_list_thread.start()
# Remove All Vehicles
self.remove_all_vehicles_thread = RemoveAllVehiclesThread(MainWindow=MainWindow)
self.remove_all_vehicles_button.clicked.connect(self.remove_all_vehicles)

# --------------------------- WALKER
# Generate Walkers
self.generate_walkers_thread = GenerateWalkersThread(MainWindow=MainWindow)
self.generate_walkers_button.clicked.connect(self.generate_walkers)
# Get Vehicle List
self.get_walker_list_thread = GetWalkerListThread(MainWindow=MainWindow)
self.get_walker_list_thread.start()
# Remove All Walkers
self.remove_all_walkers_thread = RemoveAllWalkersThread(MainWindow=MainWindow)
self.remove_all_walkers_button.clicked.connect(self.remove_all_walkers)

# --------------------------- WEATHER
# Fog None
self.fog_none_thread = FogNoneThread(MainWindow=MainWindow)
self.fog_none_button.clicked.connect(self.fog_none_thread.start)
# Fog Light
self.fog_light_thread = FogLightThread(MainWindow=MainWindow)
self.fog_light_button.clicked.connect(self.fog_light_thread.start)
# Fog Heavy
self.fog_heavy_thread = FogHeavyThread(MainWindow=MainWindow)
self.fog_heavy_button.clicked.connect(self.fog_heavy_thread.start)
# Rain None
self.rain_none_thread = RainNoneThread(MainWindow=MainWindow)
self.rain_none_button.clicked.connect(self.rain_none_thread.start)
# Rain Light
self.rain_light_thread = RainLightThread(MainWindow=MainWindow)
self.rain_light_button.clicked.connect(self.rain_light_thread.start)
# Rain Heavy
self.rain_heavy_thread = RainHeavyThread(MainWindow=MainWindow)
self.rain_heavy_button.clicked.connect(self.rain_heavy_thread.start)
# Time Morning
self.time_morning_thread = TimeMorningThread(MainWindow=MainWindow)
self.time_morning_button.clicked.connect(self.time_morning_thread.start)
# Time Noon
self.time_noon_thread = TimeNoonThread(MainWindow=MainWindow)
self.time_noon_button.clicked.connect(self.time_noon_thread.start)
# Time Evening
self.time_evening_thread = TimeEveningThread(MainWindow=MainWindow)
self.time_evening_button.clicked.connect(self.time_evening_thread.start)
# Time Night
self.time_night_thread = TimeNightThread(MainWindow=MainWindow)
self.time_night_button.clicked.connect(self.time_night_thread.start)

# Manual Weather
self.manual_weather_thread = ManualWeatherThread(MainWindow=MainWindow)
self.manual_weather_button.clicked.connect(self.manual_weather_thread.start)