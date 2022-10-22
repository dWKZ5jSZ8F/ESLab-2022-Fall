from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner
import bluepy.btle as btle

devices = list(Scanner().scan(5.0))

for i, device in enumerate(devices):
    print(f"{i}: {device.addr} {device.addrType} {device.rssi}")
    for (adtype, desc, value) in device.getScanData():
    	print(f"{desc} = {value}")

num = int(input('Connect to index: '))
print(f"Connecting to device {num}: {devices[num].addr}")
dev = Peripheral(devices[num].addr, devices[num].addrType)

try:
    ch = dev.getCharacteristics(uuid=UUID(0xfff4))[0]
    ch.write(input("Write something: ").encode('utf-8'), withResponse=True)
    cccd = ch.getHandle() + 1
    dev.writeCharacteristic(cccd, b"\x01\x00")
    print("Receive something, waiting")
    while True:
        if dev.waitForNotifications(5.0):
            print("Exit with received notification.")
            break
finally:
    dev.disconnect()

