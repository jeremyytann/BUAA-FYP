import subprocess
import os
from PyQt6.QtCore import QThread

script_code = f"""
import time
import os
import carla
from numpy import random

def main():
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(5)
        world = client.get_world()
        world_map = world.get_map()
        available_maps = client.get_available_maps()
        
        blueprint_library = world.get_blueprint_library()
        static_props = blueprint_library.filter('static.prop.*')
        
        output = 'CARLA Simulator connected' + '-' + world_map.name + ','
        
        for map_name in available_maps:
            output += map_name + ' '
            
        output += ','
        
        for static_prop in static_props:
          if "helmet" in static_prop.id:
            output = output
          else:
            output += static_prop.id + ' '
        
        print(output)
    except RuntimeError:
        print('CARLA Simulator not detected')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
"""

class RefreshCarlaStatusThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    with open("refresh_carla_status_script.py", "w") as f:
      f.write(script_code)

    try:
      self.MainWindow.ui.carla_status_label.setText("刷新中...")
      result = subprocess.run(["python", "refresh_carla_status_script.py"], capture_output=True, text=True)
      output = result.stdout.strip()
      
      if "CARLA Simulator connected" in output:
        outputs = output.split(',')
        map_name = outputs[0].split('-')[1]
        available_maps = outputs[1].split(' ')
        static_props = outputs[2].split(' ')
        
        self.MainWindow.ui.map_list_widget.clear()
        self.MainWindow.ui.props_list_widget.clear()
        
        for map in available_maps:
            self.MainWindow.ui.map_list_widget.addItem(map)
            
        for static_prop in static_props:
            self.MainWindow.ui.props_list_widget.addItem(static_prop)
        
        self.MainWindow.ui.carla_status_label.setText("已连接")
        self.MainWindow.ui.current_map_label.setText(map_name)
      elif "CARLA Simulator not detected" in output:
        self.MainWindow.ui.carla_status_label.setText("未连接")
        self.MainWindow.ui.current_map_label.setText("None")
        self.MainWindow.ui.map_list_widget.clear()
        self.MainWindow.ui.props_list_widget.clear()
    except KeyboardInterrupt:
      pass
    finally:
      os.remove("refresh_carla_status_script.py")