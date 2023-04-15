import subprocess
import os
from PyQt6.QtCore import QThread
from carla_status.refresh_carla_status import RefreshCarlaStatusThread

map_name = ""

script_code = """
import carla

def main():
    try:
        client = carla.Client('localhost', 2000)
        client.set_timeout(5)

        world = client.load_world('{map_name}')
        print('{map_name}')
    except RuntimeError:
        print('CARLA Simulator not detected')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
"""

class LoadMapThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def get_carla_status(self, MainWindow):
    self.refresh_carla_status_thread.start()
    
  def run(self):
    global map_name
    selected_maps = self.MainWindow.ui.map_list_widget.selectedItems()
    
    if len(selected_maps) > 0:
        for selected_map in selected_maps:
            map_name = selected_map.text()
        
        script_code_formatted = script_code.format(map_name=map_name)
        
        with open("load_map_script.py", "w") as f:
          f.write(script_code_formatted)

        try:
          self.MainWindow.ui.current_map_label.setText("加载中...")
          result = subprocess.run(["python", "load_map_script.py"], capture_output=True, text=True)
          output = result.stdout.strip()
          
          if "CARLA Simulator not detected" in output:
            self.MainWindow.ui.carla_status_label.setText("未连接")
            self.MainWindow.ui.current_map_label.setText("None")
            self.MainWindow.ui.map_list_widget.clear()
            
            self.refresh_carla_status_thread = RefreshCarlaStatusThread(MainWindow=self.MainWindow)
            self.get_carla_status(self.MainWindow)
          else:
            self.MainWindow.ui.current_map_label.setText(map_name)
        except KeyboardInterrupt:
            pass
        finally:
            os.remove("load_map_script.py")