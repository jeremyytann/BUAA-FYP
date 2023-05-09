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

        client.reload_world()
        
        world = client.get_world()
        map_name = world.get_map().name
        
        print(map_name)
    except RuntimeError:
        print('CARLA Simulator not detected')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
"""

class ReloadWorldThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def get_carla_status(self, MainWindow):
    self.refresh_carla_status_thread.start()
    
  def run(self):
        with open("reload_world_script.py", "w") as f:
          f.write(script_code)

        try:
          self.MainWindow.ui.current_map_label.setText("加载中...")
          result = subprocess.run(["python", "reload_world_script.py"], capture_output=True, text=True)
          output = result.stdout.strip()
          
          if "CARLA Simulator not detected" in output:
            self.MainWindow.ui.carla_status_label.setText("未连接")
            self.MainWindow.ui.current_map_label.setText("None")
            self.MainWindow.ui.map_list_widget.clear()
            
            self.refresh_carla_status_thread = RefreshCarlaStatusThread(MainWindow=self.MainWindow)
            self.get_carla_status(self.MainWindow)
          else:
            self.MainWindow.ui.current_map_label.setText(output)
        except KeyboardInterrupt:
            pass
        finally:
            os.remove("reload_world_script.py")