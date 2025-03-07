<!-- Interfaces and variants -->

The TLEx501B sensor is available in three different interface configurations: IIF, PWM, and SPC/HSM. All three also include the SSC interface.
Only with the SSC communication protocol all registers of the DSP are available (see [TLx5012B manual](https://www.infineon.com/dgdl/Infineon-Angle_Sensor_TLE5012B-UM-v01_02-en-UM-v01_02-EN.pdf?fileId=5546d46146d18cb40146ec2eeae4633b)
for further information). The purpose of the interfaces is to support a wide variety of different tasks, from ultra low power use replacing ordinary Hall-effect switches up to high performance use cases. This flexibility allows us to utilize the full range of functions, even if we don't have the perfectly matching sensor type.

The following table summarizes the settings for each interface configuration:

| Type             | E1000                       | E3005                       | E5000                        | E5020                       | E9000                       |
|:-----------------|:----------------------------|:----------------------------|:-----------------------------|:----------------------------|:----------------------------|
| Interface        | IIF (Incremental Interface) | HSM (Hall-Switch-Mode)      | PWM (Pulse-Width-Modulation) | PWM (Pulse-Width-Modulation)| SPC (Short-PWM-Code)        |
|                  | SSC as push-pull output     | SSC as push-pull output     | SSC as push-pull output      | SSC as push-pull output     | SSC as push-pull output     |
|                  | IFA/B/C as push-pull output | IFA/B/C as push-pull output | IFA as push-pull output      | IFA as open-drain output    | IFA as open-drain output    |
| Auto calibration | mode 1                      | mode 1                      | disabled                     | mode 2                      | disabled                    |
| Prediction       | disabled                    | enabled                     | enabled                      | disabled                    | disabled                    |
| Spike filter     | disabled                    | disabled                    | enabled                      | enabled                     | enabled                     |
| Absolute count   | enabled                     |                             |                              |                             |                             |
| Hysteresis       | 0.703°                      | 0.703°                      | disabled                     | disabled                    | disabled                    |
| Resolution       | 12bit mode, 0.088°          |                             | PWM frequency is 244 Hz      | PWM frequency is 1953 Hz    | SPC unit time is 3 μs       |
| Update rate      | 42.7 μs                     | 42.7 μs                     | 85.4 μs                      | 42.7 μs                     | 85.4 μs                     |
| Usage            | BLDC motor commutation      | replacement of three Hall   | steering angle and actuator  | steering angle and actuator | steering angle and actuator |
|                  |                             | switches for BLDC motor     | position sensing             | position sensing            | position sensing            |
|                  |                             | commutation                 |                              |                             |                             |

