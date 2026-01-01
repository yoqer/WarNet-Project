# Manual de Acople y Montaje del Dron WarNet

## Autor: Manus AI
## Fecha: 8 de Diciembre de 2025

---

## 1. Introducción

Este manual detalla el acople de los componentes electrónicos para el Dron Experimental WarNet, un sistema de contramedidas electrónicas móvil. La arquitectura se basa en la coordinación de dos microcontroladores ESP32 (S3 y C3).

## 2. Componentes Requeridos

| Componente | Cantidad | Notas |
| :--- | :--- | :--- |
| **Controlador Principal** | 1 | ESP32-S3 Development Board |
| **Módulo de Comunicación** | 1 | ESP32-C3 Development Board |
| **Módulo LoRaWAN** | 1 | Basado en SX1276/SX1278 (868/915 MHz) |
| **Módulo RF de Amplio Espectro** | 1 | Basado en CC1101 (para escaneo de espectro) |
| **Sensores** | 1 | IMU MPU-6050 (Acelerómetro + Giroscopio) |
| **Motores** | 4 | Motores Brushless con ESCs (Controladores Electrónicos de Velocidad) |
| **Batería** | 1 | Batería LiPo (ej. 3S o 4S) |
| **Chasis** | 1 | Chasis de Dron (ej. F450 o similar) |

## 3. Esquema de Conexión

### 3.1. Conexión del ESP32-S3 (Control de Vuelo)

El ESP32-S3 actúa como el controlador de vuelo.

| Componente | Pines del ESP32-S3 | Función |
| :--- | :--- | :--- |
| **Motor 1 (PWM)** | GPIO 1 | Control de Velocidad |
| **Motor 2 (PWM)** | GPIO 2 | Control de Velocidad |
| **Motor 3 (PWM)** | GPIO 3 | Control de Velocidad |
| **Motor 4 (PWM)** | GPIO 4 | Control de Velocidad |
| **IMU (SDA)** | GPIO 8 | Bus I2C |
| **IMU (SCL)** | GPIO 9 | Bus I2C |

### 3.2. Conexión del ESP32-C3 (Comunicación y Jammer)

El ESP32-C3 actúa como el nodo de comunicación y el orquestador del Jammer.

| Componente | Pines del ESP32-C3 | Función |
| :--- | :--- | :--- |
| **LoRaWAN (SCK)** | GPIO 10 | Bus SPI |
| **LoRaWAN (MISO)** | GPIO 11 | Bus SPI |
| **LoRaWAN (MOSI)** | GPIO 12 | Bus SPI |
| **LoRaWAN (CS)** | GPIO 13 | Chip Select |
| **Módulo RF (SCK)** | GPIO 18 | Bus SPI |
| **Módulo RF (MISO)** | GPIO 19 | Bus SPI |
| **Módulo RF (MOSI)** | GPIO 20 | Bus SPI |
| **Módulo RF (CS)** | GPIO 21 | Chip Select |

### 3.3. Conexión de Coordinación (ESP32-S3 y ESP32-C3)

La comunicación entre los dos ESP32 se realiza a través de SPI.

| Pin del ESP32-S3 | Pin del ESP32-C3 | Función |
| :--- | :--- | :--- |
| **GPIO 14 (SCK)** | GPIO 14 (SCK) | Reloj SPI |
| **GPIO 15 (MISO)** | GPIO 15 (MISO)** | Datos de S3 a C3 |
| **GPIO 16 (MOSI)** | GPIO 16 (MOSI)** | Datos de C3 a S3 |
| **GPIO 17 (CS)** | GPIO 17 (CS) | Chip Select |

**Nota:** El ESP32-S3 debe configurarse como **SPI Master** y el ESP32-C3 como **SPI Slave** para esta comunicación.

## 4. Pasos de Montaje

1.  **Montaje del Chasis:** Fije los 4 motores y los ESCs al chasis del dron.
2.  **Cableado de Potencia:** Conecte los ESCs a la batería LiPo a través de una placa de distribución de energía (PDB).
3.  **Montaje del ESP32-S3:** Fije el ESP32-S3 al centro del chasis. Conecte los pines PWM a los ESCs y el IMU al bus I2C.
4.  **Montaje del ESP32-C3:** Fije el ESP32-C3 cerca del S3. Conecte los módulos LoRaWAN y RF al bus SPI.
5.  **Cableado de Coordinación:** Conecte los pines SPI entre el S3 y el C3.
6.  **Prueba de Firmware:** Cargue el firmware de PlatformIO en cada placa y realice pruebas de comunicación y control de vuelo.

## 5. Consideraciones de Seguridad

*   **Pruebas de Vuelo:** Realice las primeras pruebas de vuelo sin hélices.
*   **Pruebas de Jammer:** Las pruebas de Jammer deben realizarse en un entorno controlado y legalmente permitido.

---
**Fin del Manual de Montaje**
