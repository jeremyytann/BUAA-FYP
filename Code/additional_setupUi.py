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