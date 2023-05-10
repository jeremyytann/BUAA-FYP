import subprocess
import os
from PyQt6.QtCore import QThread

prop_name = ""

script_code = """
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

spectator = world.get_spectator()
spectator_transform = spectator.get_transform()

prop_distance = 3 
prop_location = spectator_transform.location + (spectator_transform.get_forward_vector() * prop_distance)

prop_location.z = 0

prop_blueprint = world.get_blueprint_library().find('{prop_name}')

prop_transform = carla.Transform(prop_location)

prop_actor = world.spawn_actor(prop_blueprint, prop_transform)

print(str(prop_actor.id) + "-" + prop_actor.type_id)
"""

class GeneratePropThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    global prop_name
    selected_props = self.MainWindow.ui.props_list_widget.selectedItems()
    
    if len(selected_props) > 0:
      for selected_prop in selected_props:
        prop_name = selected_prop.text()
    
      script_code_formatted = script_code.format(prop_name=prop_name)
    
      with open("generate_prop_script.py", "w") as f:
        f.write(script_code_formatted)

      try:
        result = subprocess.run(["python", "generate_prop_script.py"], capture_output=True, text=True)
        output = result.stdout.strip()
        
        self.MainWindow.ui.existing_props_list_widget.addItem(output)
      except KeyboardInterrupt:
        pass