from bluepy.btle import DefaultDelegate, Scanner, Peripheral, UUID

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

    def handleNotification(self, cHandle, data):
            print(f"Received: {int.from_bytes(data, 'big')}")

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(5.0)
n = 0
addr = []

for dev in devices:
    print("%d: Device %s (%s), RSSI = %d dB" % (n, dev.addr, dev.addrType, dev.rssi))
    addr.append(dev.addr)
    n += 1
    for (adtype, desc, value) in dev.getScanData():
        print("%s = %s" % (desc, value))

num = int(input('Connect to device: '))
print("Connecting to device %s: %s" % (num, addr[num]))
dev = Peripheral(addr[num], 'random')
dev.setDelegate(ScanDelegate())
print("Services:")
for svc in dev.services:
    print(str(svc), ": ", str(svc.uuid))

try:
    target_svc = int("0x" + str(input("Target service: ")), 16)
    svc = dev.getServiceByUUID(UUID(target_svc))
    for chars in svc.getCharacteristics():
        print(str(chars), ": ", str(chars.uuid))
    target_ch = int("0x" + str(input("Target characteristic: ")), 16)
    ch = dev.getCharacteristics(uuid=UUID(target_ch))[0]
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

