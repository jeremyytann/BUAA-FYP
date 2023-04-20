# to add in the UI_MainWindow

# --------------------------- CARLA STATUS
# Refresh Carla Status
def get_carla_status(self, MainWindow):
    self.refresh_carla_status_thread.start()
    
# --------------------------- MAP
# Load Map
def load_map(self, MainWindow):
    self.load_map_thread.start()
    
# --------------------------- VEHICLE
# Generate Vehicles
def generate_vehicles(self, MainWindow):
    self.generate_vehicles_thread.start()
    self.get_vehicle_list_thread.start()

# Remove All Vehicles
def remove_all_vehicles(self, MainWindow):
    if self.generate_vehicles_thread.isRunning():
      self.generate_vehicles_thread.terminate()
      
    self.remove_all_vehicles_thread.start()
    
# --------------------------- WALKER
# Generate Walkers
def generate_walkers(self, MainWindow):
    self.generate_walkers_thread.start()
    self.get_walker_list_thread.start()

# Remove All Walkers  
def remove_all_walkers(self, MainWindow):
    if self.generate_walkers_thread.isRunning():
      self.generate_walkers_thread.terminate()
    
    self.remove_all_walkers_thread.start()