# to add in the UI_MainWindow

# --------------------------- CARLA STATUS
# Refresh Carla Status
def get_carla_status(self, MainWindow):
    self.refresh_carla_status_thread.start()
    
# --------------------------- MAP
# Load Map
def load_map(self, MainWindow):
    self.load_map_thread.start()
    
# --------------------------- CAR
# Generate Vehicles
def generate_vehicles(self, MainWindow):
    self.generate_vehicles_thread.start()

# Remove All Vehicles
def remove_all_vehicles(self, MainWindow):
    self.remove_all_vehicles_thread.start()