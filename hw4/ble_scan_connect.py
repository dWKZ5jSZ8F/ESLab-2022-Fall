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
        if cHandle == 13:
            print(f"Heart rate: {int.from_bytes(data, 'big')}")
        elif cHandle == 19:
            print(f"MagnetoX: {int.from_bytes(data, 'big')}")
        elif cHandle == 25:
            print(f"MagnetoY: {int.from_bytes(data, 'big')}")
        elif cHandle == 31:
            print(f"MagnetoZ: {int.from_bytes(data, 'big')}")
        else:
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
    print("(180d for HeartRate/Magneto, a000 for Button")
    target_svc = int("0x" + str(input("Target service: ")), 16)
    if target_svc == 0x180d:
        op = 'H'
        print("HeartRate/Magneto Service")
        svc = dev.getServiceByUUID(UUID(target_svc))
        # for chars in svc.getCharacteristics():
        #    print(str(chars), ": ", str(chars.uuid))
        ch = dev.getCharacteristics(uuid=UUID(0x2a37))[0]
        chX = dev.getCharacteristics(uuid=UUID(0x1235))[0]
        chY = dev.getCharacteristics(uuid=UUID(0x1241))[0]
        chZ = dev.getCharacteristics(uuid=UUID(0x1247))[0]
        cccd0 = ch.getHandle() + 1
        cccd1 = chX.getHandle() + 1
        cccd2 = chY.getHandle() + 1
        cccd3 = chZ.getHandle() + 1
        dev.writeCharacteristic(cccd0, b"\x01\x00")
        dev.writeCharacteristic(cccd1, b"\x01\x00")
        dev.writeCharacteristic(cccd2, b"\x01\x00")
        dev.writeCharacteristic(cccd3, b"\x01\x00")
    elif target_svc == 0xa000:
        op = 'B'
        print("Button Service")
        svc = dev.getServiceByUUID(UUID(target_svc))
        # for chars in svc.getCharacteristics():
        #     print(str(chars), ": ", str(chars.uuid))
        # target_ch = int("0x" + str(input("Target characteristic: ")), 16)
        ch = dev.getCharacteristics(uuid=UUID(0xa001))[0]
        # print("Characteristic properties: ", ch.propertiesToString())
        cccd = ch.getHandle() + 1
        dev.writeCharacteristic(cccd, b"\x01\x00")
    # cccd = ch.getDescriptors(forUUID=UUID(0x2902))[0]
    # cccd.write(b"\x00\x01",True)
    print("Waiting to receive notification(s)...")
    count = 0
    while True:
        if dev.waitForNotifications(50.0):
            if op == 'H':
                count += 1
                if count >= 100:
                    print("Simulation done.")
                    break
            elif op == 'B':
                continue
        else:
            print("No notifications received.")
            break

finally:
    dev.disconnect()
