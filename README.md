# Proyecto Experimental WarNet: Dron Jammer de Espectro Completo

Este proyecto experimental implementa un sistema de contramedidas electrónicas móvil y autónomo, el **Dron WarNet**, coordinado por un **Gateway Central** con una interfaz de usuario de estilo retro arcade llamada **Play WarNet**.

## 1. Arquitectura del Sistema

El sistema se basa en la coordinación de dos microcontroladores ESP32 a bordo de un dron:

| Componente | Hardware | Función Clave | Framework |
| :--- | :--- | :--- | :--- |
| **Gateway Central** | Linux RT / RPi 500+ | Orquestación de comandos de voz (**"Amais"**), UI **Play WarNet**, y control de la red LoRaWAN. | Python (Tkinter) |
| **WarNet S3 Control** | ESP32-S3 | Control de Vuelo, Jammer Wi-Fi, TinyML (Análisis de Espectro). | Arduino |
| **WarNet C3 Jammer** | ESP32-C3 | Receptor LoRaWAN, Jammer Bluetooth, Escaneo de Espectro Amplio (con módulo RF externo). | Arduino |

## 2. Funcionalidades Clave

*   **Jammer Coordinado:** El S3 y el C3 trabajan juntos para saturar Wi-Fi y Bluetooth, y luego el C3 escanea y ataca el espectro completo (incluyendo celular y LoRaWAN) hasta que la señal objetivo desaparece.
*   **Control por Voz (LoRaWAN):** El Gateway Central traduce comandos de voz a paquetes LoRaWAN, que son la única forma de comunicación de control con el dron.
*   **Play WarNet UI:** Interfaz de usuario de estilo **Radar Retro Arcade** que muestra la geolocalización aproximada de las detecciones, el estado de los *jammers* y la efectividad de las acciones.

## 3. Estructura del Proyecto PlatformIO

```
/warnet_project
├── platformio.ini              # Configuración de los entornos de PlatformIO
├── /warnet_s3_control          # Código para el ESP32-S3 (Control de Vuelo/Jammer Wi-Fi)
├── /warnet_c3_jammer           # Código para el ESP32-C3 (LoRaWAN/Jammer Bluetooth/Escaneo RF)
└── /gateway_ui                 # Código Python para la UI Play WarNet
```

## 4. Despliegue y Ejecución

### 4.1. Ejecución de la UI Play WarNet

El Gateway Central ejecuta la UI para visualizar las acciones en tiempo real:

```bash
cd gateway_ui/src
python3 play_warnet_ui.py
```

### 4.2. Manual de Montaje

Consulte el documento **warnet_architecture_design.md** para el esquema de acople y montaje de las placas ESP32 y los módulos RF en el dron.

## 5. Licencia

Este proyecto se distribuye bajo la **Apache License 2.0**.

## 6. Referencias

*   **Estudio Técnico:** `technical_study_warnet_jammer.md`
*   **Diseño de Arquitectura:** `warnet_architecture_design.md`
*   **Paper ESPwn32:** [https://hal.science/hal-04183794/file/ESP32WOOT_CameraReady.pdf](https://hal.science/hal-04183794/file/ESP32WOOT_CameraReady.pdf)
