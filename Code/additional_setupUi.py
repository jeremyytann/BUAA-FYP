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
self.reload_world_thread = ReloadWorldThread(MainWindow=MainWindow)
self.reload_world_button.clicked.connect(self.reload_world_thread.start)

# --------------------------- PROP
# Generate Prop
self.generate_prop_thread = GeneratePropThread(MainWindow=MainWindow)
self.prop_generate_button.clicked.connect(self.generate_prop_thread.start)
# Get Prop List
self.get_prop_list_thread = GetPropListThread(MainWindow=MainWindow)
self.get_prop_list_thread.start()
# View Selected Prop
self.view_selected_prop_thread = ViewSelectedPropThread(MainWindow=MainWindow)
self.props_watch_button.clicked.connect(self.view_selected_prop_thread.start)
# Remove Selected Prop
self.remove_selected_prop_thread = RemoveSelectedPropThread(MainWindow=MainWindow)
self.props_remove_button.clicked.connect(self.remove_selected_prop_thread.start)
# Rotate Left Prop
self.prop_rotate_left_thread = PropRotateLeftThread(MainWindow=MainWindow)
self.props_rotate_left_button.clicked.connect(self.prop_rotate_left_thread.start)
# Rotate Right Prop
self.prop_rotate_right_thread = PropRotateRightThread(MainWindow=MainWindow)
self.props_rotate_right_button.clicked.connect(self.prop_rotate_right_thread.start)

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
# View Selected Vehicle
self.view_selected_vehicle_thread = ViewSelectedVehicleThread(MainWindow=MainWindow)
self.vehicle_watch_button.clicked.connect(self.view_selected_vehicle_thread.start)
# Remove Selected Vehicle
self.remove_selected_vehicle_thread = RemoveSelectedVehicleThread(MainWindow=MainWindow)
self.vehicle_remove_button.clicked.connect(self.remove_selected_vehicle_thread.start)

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
# View Selected Walker
self.view_selected_walker_thread = ViewSelectedWalkerThread(MainWindow=MainWindow)
self.walker_watch_button.clicked.connect(self.view_selected_walker_thread.start)
# Remove Selected Walker
self.remove_selected_walker_thread = RemoveSelectedWalkerThread(MainWindow=MainWindow)
self.walker_remove_button.clicked.connect(self.remove_selected_walker_thread.start)

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