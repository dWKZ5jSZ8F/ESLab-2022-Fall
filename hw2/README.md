# HW2: Socket Programming and Data Visualization
## Description
In this project, we use **B-L4S5I-IOT01A** discovery board as an IOT node sensor device. With BSP driver libraries, we retrieve the sensor values and transmit to the host server via TCP sockets. The data is then being visualized. The project is built in Mbed OS environment.

## How to run 
1. Import program `mbed-os-example-sockets` (url: https://github.com/ARMmbed/mbed-os-example-sockets.git) into Mbed Studio.

2. Import `BSP_B-L475E-IOT01` (url: https://os.mbed.com/teams/ST/code/BSP_B-L475E-IOT01/) driver library for the sensors.

3. Apply some modifications and fixes:
    - Replace the files below with `fix-patches`.
    ```
    ~\mbed-os\targets\TARGET_STM\TARGET_STM32L4\PeripheralNames.h
    ~\mbed-os\targets\TARGET_STM\TARGET_STM32L4\STM32Cube_FW\CMSIS\stm32l4s5xx.h
    ~\BSP_B-L475E-IOT01\Drivers\BSP\B-L475E-IOT01\stm32l475e_iot01_qspi.c
    ```
    - Change `Target["printf_lib"]` to `"std"` in `~\mbed-os\targets\targets.json`

4. Replace `~\source\main.cpp` and `~\mbed_app.json`:
    - Change `config["hostname"]["value"]` to your host IP (you can get it using `ipconfig` in local machine cmd) in `~\mbed_app.json`.
    - Change `target_overrides["*"]["nsapi.default-wifi-ssid"]` and `target_overrides["*"]["nsapi.default-wifi-password"]` to your local wifi network same as your local machine.

5. Run `socket-server.py` to setup your host and listening for any client.

6. Build and compile your Mbed program and complete the transmission of sensor data through the TCP socket.

## Results
As the figures below show, the sensor values recorded by the **B-L4S5I-IOT01A** board is visualized into plots by using python library `matplotlib`.

![results](https://user-images.githubusercontent.com/57944276/198839221-e44d33e7-fb7e-430b-945e-5b4db0f9db29.png)
