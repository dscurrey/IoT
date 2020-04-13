import socket, traceback

host = '192.168.137.207'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))

while(True):
    try:
        message, address = s.recvfrom(1024)
        #print(str(type(message)))
        message = str(message)
        sensors = message.split(",")
        print("Gyro:\t{}, {}, {}, {}".format(sensors[5].strip(","),sensors[6].strip(","),sensors[7].strip(","),sensors[8].strip(",")))
        print('----------------------------')
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exec()
        
# Format of Message:
# Timestamp(sec), sensorid(Accelero), x, y, z, sensorid(Gyro), x, y, z, sensorid(Magneto), x, y, z
