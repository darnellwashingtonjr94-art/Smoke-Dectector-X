import subprocess
import time

class WifiManager:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def is_connected(self):
        try:
            output = subprocess.check_output(["iwgetid", "-r"]).decode("utf-8").strip()
            return output == self.ssid
        except subprocess.CalledProcessError:
            return False

    def reconnect(self):
        print(f"Attempting to reconnect to {self.ssid}...")
        subprocess.run(["nmcli", "dev", "wifi", "connect", self.ssid, "password", self.password])
        time.sleep(5)
        return self.is_connected()
