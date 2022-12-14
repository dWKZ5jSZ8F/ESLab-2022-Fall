# HW7: Mbed-DSP programming 
## Description
In this homework, we use **CMSIS-DSP** framework for ARM CORTEX based microcontroller to perform digital signal processing on input sensor values. In this instance, I implemented a lowpass FIR filter on input accelerometer, gyroscope, temperature, humidity and pressure values.  

## How to run 
1. Build a new program in Mbed Studio.
2. Import `mbed-dsp` (url: https://os.mbed.com/teams/mbed-official/code/mbed-dsp/) for FIR filter function and `BSP_B-L475E-IOT01` (url: https://os.mbed.com/teams/ST/code/BSP_B-L475E-IOT01/) driver library for the 3D accelerator sensors.
3. Replace the file under `~\mbed-dsp\cmsis_dsp\TransformFunctions\arm_bitreversal2.S` directory and `~\main.cpp`.
4. Build and compile the program.
5. Modify the parameters in the `visualize.py` for the visualization of the output.

## Results
![result](https://user-images.githubusercontent.com/57944276/203071820-4d9a3f5d-4d5f-4a56-be8e-920afc96cfcd.png)
