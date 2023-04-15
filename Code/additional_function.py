# to add in the UI_MainWindow

# --------------------------- CARLA STATUS
# Refresh Carla Status
def get_carla_status(self, MainWindow):
    self.refresh_carla_status_thread.start()
    
# --------------------------- MAP
# Load Map
def load_map(self, MainWindow):
        self.load_map_thread.start()