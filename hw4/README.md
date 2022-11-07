# HW4: Mbed BLE programming - Peripheral in mbed-os (stm32) and Central in Python (RPi)
## Description
In this project, we use **B-L4S5I-IOT01A** discovery board as an BLE peripheral device with **Raspberry Pi 3** connected to a Linux host as a BLE central device to retrieve sensor values from the peripheral. Also, the peripheral provides a service that return specific data whenever its button is pressed ro released. An `EventQueue` object is used to schedule occuring events such that sensor values are returned every 1000ms and button data are returned on event.

## How to run 
### BLE peripheral (GATT server)
1. Import files from Github repo `mbed-os-example-ble/BLE_GattServer_AddService/` (url: https://github.com/ARMmbed/mbed-os-example-ble) into Mbed Studio.
2. Import `BSP_B-L475E-IOT01` (url: https://os.mbed.com/teams/ST/code/BSP_B-L475E-IOT01/) driver library for the magnetometer sensors.
3. Replace or add files under`~\source\` directory and `~\mbed_app.json`.
4. Build and compile the program. (Check if the baud rate in the terminal is synchronized, in this case 115200, such that the output would not be corrupted.)

### BLE central (GATT client)
1. Connect RPi3 to Linux host and log in.
2. Run `ble_scan_connect.py` and connect to device named **HR/M/Button** with the same MAC address as output in Mbed Studio terminal.
3. You could choose between **Heartrate/magneto** (0x180d) or **Button** (0xa000) service.

## Results
### Sequence chart
![](https://i.imgur.com/jNSfzH4.png)

### Demo
The figures below shows the demo results of this project.
