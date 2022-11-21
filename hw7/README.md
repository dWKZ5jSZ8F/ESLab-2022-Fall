# HW7: Mbed-DSP programming 
## Description
In this homework, we use **CMSIS-DSP* framework for ARM CORTEX based microcontroller to perform digital signal processing on input sensor values. In this instance, I implemented a lowpass FIR filter on input 3D accelerators values.  

## How to run 
1. Build a new program in Mbed Studio.
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
