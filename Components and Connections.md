# Components Used:

1. ESP8266 NodeMCu
2. L298N Motor Driver
3. DC geared motor x4
4. 11.1V Li-Ion battery

# Wiring Details:

## _Connection between NodeMCU and L298N:_

1. Motordrive IN1 - D2
2. Motordrive In2 - D3
3. Motordrive Enable1 - D1
4. Motordrive IN3 - D5
5. Motordrive IN4 - D6
6. Motordrive Enable2 - D7

## _Power Connections:_

1. Connect battery positive terminal to L298 +12 pin.
2. Connect battery negative to motordrive gnd.
3. Connect NodeMCU gnd to motordrive gnd.
4. Connect NodeMCU Vin to motordrive +5V out pin.

## _Motor Connection:_

Two motors are connected to the OUT1 and OUT2 pins.
The two other motors are connected to the OUT3 and OUT4 pins.
