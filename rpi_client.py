import socket
import time
import board
import digitalio
import busio
import adafruit_lis3dh #if not install do [sudo pip3 install adafruit-circuitpython-lis3dh] to install library


class Accelerometer:
    def __init__(self) -> None:
        pass

    def read_axis(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        int1 = digitalio.DigitalInOut(board.D6)             # interrupt connected to GPIO6
        lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
        x, y, z = lis3dh.acceleration #update to code
        return (x + "," + y+ "," + z); #update
        # return lis3dh.acceleration


class ControllerClient:
    def __init__(self, server_address, port):
        self.server_address = server_address
        self.port = port

    def send_command(self, command):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.server_address, self.port))
        client.sendall(bytes(command, "utf-8"))
        response = client.recv(1024).decode("utf-8")
        client.close()
        return response


def main():
    SERVER_IP = "localhost"
    SERVER_PORT = 5554

    # Setup
    accelerometer_object = Accelerometer()
    connection = ControllerClient(SERVER_IP, SERVER_PORT)

    while True:
        samples = accelerometer_object.read_axis()
        response = connection.send_command(samples)
        if response is not None:
            print(response)


if __name__ == "__main__":
    main()
