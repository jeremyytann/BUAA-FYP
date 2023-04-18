# to add in the setupUi

# --------------------------- CARLA STATUS
# Refresh Carla Status
self.refresh_carla_status_thread = RefreshCarlaStatusThread(MainWindow=MainWindow)
self.get_carla_status(MainWindow)
self.carla_status_refresh_button.clicked.connect(self.get_carla_status)

# --------------------------- MAP
# Load Map
self.load_map_thread = LoadMapThread(MainWindow=MainWindow)
self.load_map_button.clicked.connect(self.load_map)

# --------------------------- VEHICLE
# Generate Vehicles
self.generate_vehicles_thread = GenerateVehiclesThread(MainWindow=MainWindow)
self.generate_vehicles_button.clicked.connect(self.generate_vehicles)
# Get Vehicle List
self.get_vehicle_list_thread = GetVehicleListThread(MainWindow=MainWindow)
# Remove All Vehicles
self.remove_all_vehicles_thread = RemoveAllVehiclesThread(MainWindow=MainWindow)
self.remove_all_vehicles_button.clicked.connect(self.remove_all_vehicles)