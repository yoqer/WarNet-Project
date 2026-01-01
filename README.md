# Proyecto Experimental T4 WarNet: Dron Jammer de Espectro Completo


Web de estudio de experimentacion, no funcional.

http://maxxine.net/war/play_warnet_homepage.html


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





..   T4. Interconexion. ...



Archivo de Uso de App de Radar Estilo Arcade

El archivo que contiene la simulación de la interfaz de radar estilo arcade es el script de Python que se ejecuta en el Gateway Central:

Archivo: /home/ubuntu/WarNet-Project/gateway_ui/src/play_warnet_ui.py

Este archivo utiliza la librería Tkinter de Python para crear la ventana, el radar circular, los puntos de detección y los paneles laterales de estado, tal como se describió en el estudio técnico.

Para ejecutarlo (en un entorno Linux/Raspberry Pi con Python):

Bash

cd WarNet-Project/gateway_ui/src python3 play_warnet_ui.py 

2. Estado del Desarrollo del Proyecto WarNet

El proyecto WarNet es un diseño de arquitectura completo con código simulado para demostrar la lógica de la comunicación y la coordinación.




ANALISIS:

1-Componente

2-Estado de Desarrollo

3-Enlace con el Código

4-Elementos Faltantes (Implementación Real)



-Play WarNet UI (Radar)

Desarrollado (Simulación)

gateway_ui/src/play_warnet_ui.py

Conexión real a la red LoRaWAN (socket/serial) para recibir datos de telemetría en lugar de datos simulados.



-Gateway Central (Python)

Desarrollado (Lógica)

gateway_ui/src/play_warnet_ui.py

Módulo de traducción de voz a texto (ASR) y el LLM real (Amais) para traducir comandos a paquetes LoRaWAN.



-WarNet S3 (Control de Vuelo)

Desarrollado (Lógica)

warnet_s3_control/src/main.cpp

Implementación real de la librería de control de vuelo (ej. MultiWii portado) y las API de bajo nivel del ESP-IDF para el Jammer de Wi-Fi.





-WarNet C3 (Jammer/LoRaWAN)

Desarrollado (Lógica)

warnet_c3_jammer/src/main.cpp

Integración real de la librería LoRaWAN (LMIC) y la librería de bajo nivel para el Jammer de Bluetooth y el control del Módulo RF de Espectro Amplio (ej. CC1101).




-TinyML

Diseñado (Teórico)

Módulos de código en C++ (no incluidos)

Entrenamiento y despliegue de los modelos TinyML reales para el análisis de espectro en el ESP32-S3.




3. 
El código de la interfaz de radar (play_warnet_ui.py) está enlazado lógicamente con el resto del proyecto.

Lógica de Enlace: El script de Python simula la recepción de datos de los dispositivos (ID, distancia, estado de Jammer) que, en una implementación real, serían enviados por el WarNet C3 a través de LoRaWAN al Gateway Central.

Acción y Visualización: El estado de los indicadores en la UI (Rojo/Verde) refleja el estado de las acciones de Jammer que el código C++ del ESP32-C3 estaría ejecutando.









## 5. Licencia

Este proyecto se distribuye bajo la **Apache License 2.0**.

## 6. Referencias

*   **Estudio Técnico:** `technical_study_warnet_jammer.md`
*   **Diseño de Arquitectura:** `warnet_architecture_design.md`
*   **Paper ESPwn32:** [https://hal.science/hal-04183794/file/ESP32WOOT_CameraReady.pdf](https://hal.science/hal-04183794/file/ESP32WOOT_CameraReady.pdf)
