import tkinter as tk
from tkinter import ttk
import math
import random
import time

# --- Configuración de la UI ---
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
RADAR_SIZE = 500
CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2
RADAR_RADIUS = RADAR_SIZE // 2
COLOR_BG = "#000000"  # Negro
COLOR_RADAR = "#00FF00"  # Verde Retro
COLOR_ACCENT = "#FF0000" # Rojo para Alerta

# --- Simulación de Dispositivos Detectados ---
# Formato: (ID, Nombre, Tipo, Distancia, Angulo, Estado_Jammer)
DEVICES = [
    ("D001", "Coche Clásico X", "AUTONOMOUS_CAR", 150, 45, "DETECTED"),
    ("D002", "Reloj Inteligente", "SMART_WATCH", 50, 180, "JAMMING_BT"),
    ("D003", "Drone Hostil", "DRONE", 200, 300, "JAMMING_WIFI"),
    ("D004", "Barco RC", "BOAT", 250, 90, "JAMMING_LORA"),
]

# --- Clase Principal de la UI ---
class PlayWarNetUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Play WarNet - Gateway Central")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(bg=COLOR_BG)
        
        self.create_widgets()
        self.update_radar()

    def create_widgets(self):
        # Marco Principal
        main_frame = tk.Frame(self, bg=COLOR_BG)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título Retro
        title_label = tk.Label(main_frame, text="PLAY WARNET", font=("Courier New", 24, "bold"), fg=COLOR_RADAR, bg=COLOR_BG)
        title_label.pack(pady=10)

        # Marco del Radar y Paneles
        content_frame = tk.Frame(main_frame, bg=COLOR_BG)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Panel Izquierdo (Mediciones)
        self.panel_left = self.create_panel(content_frame, "MEDICIONES Y ESTADO")
        self.panel_left.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Canvas del Radar
        self.radar_canvas = tk.Canvas(content_frame, width=RADAR_SIZE, height=RADAR_SIZE, bg=COLOR_BG, highlightthickness=0)
        self.radar_canvas.pack(side=tk.LEFT, padx=20, pady=10)
        self.draw_radar_base()

        # Panel Derecho (Acciones y Log)
        self.panel_right = self.create_panel(content_frame, "ACCIONES Y LOG")
        self.panel_right.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)
        
        # Simulación de la barra de escaneo
        self.scan_line = self.radar_canvas.create_line(CENTER_X, CENTER_Y, CENTER_X, CENTER_Y - RADAR_RADIUS, fill=COLOR_RADAR, width=2)
        self.angle = 0

    def create_panel(self, parent, title):
        panel = tk.Frame(parent, bg=COLOR_BG, width=200)
        
        title_label = tk.Label(panel, text=title, font=("Courier New", 14, "bold"), fg=COLOR_ACCENT, bg=COLOR_BG)
        title_label.pack(pady=5)
        
        # Contenedor para los indicadores (simulación de agujas y LEDs)
        self.indicators = {}
        for i, device in enumerate(DEVICES):
            frame = tk.Frame(panel, bg=COLOR_BG)
            frame.pack(fill=tk.X, pady=5, padx=5)
            
            # Etiqueta del dispositivo
            tk.Label(frame, text=f"{device[0]} - {device[1]}", font=("Courier New", 10), fg=COLOR_RADAR, bg=COLOR_BG).pack(side=tk.LEFT)
            
            # Indicador de Acción (LED)
            self.indicators[device[0]] = tk.Canvas(frame, width=15, height=15, bg=COLOR_BG, highlightthickness=0)
            self.indicators[device[0]].pack(side=tk.RIGHT)
            self.indicators[device[0]].create_oval(2, 2, 13, 13, fill=COLOR_RADAR if "JAMMING" in device[5] else COLOR_RADAR, tags="led")
            
        return panel

    def draw_radar_base(self):
        # Círculos concéntricos
        for i in range(1, 5):
            radius = RADAR_RADIUS * i / 4
            self.radar_canvas.create_oval(CENTER_X - radius, CENTER_Y - radius, CENTER_X + radius, CENTER_Y + radius, outline=COLOR_RADAR, dash=(4, 4), tags="grid")
        
        # Líneas de cuadrícula (Ejes)
        self.radar_canvas.create_line(CENTER_X, CENTER_Y - RADAR_RADIUS, CENTER_X, CENTER_Y + RADAR_RADIUS, fill=COLOR_RADAR, tags="grid")
        self.radar_canvas.create_line(CENTER_X - RADAR_RADIUS, CENTER_Y, CENTER_X + RADAR_RADIUS, CENTER_Y, fill=COLOR_RADAR, tags="grid")

    def update_radar(self):
        # Borrar detecciones anteriores
        self.radar_canvas.delete("detection")
        
        # Mover la línea de escaneo
        self.angle = (self.angle + 5) % 360
        rad = math.radians(self.angle)
        end_x = CENTER_X + RADAR_RADIUS * math.sin(rad)
        end_y = CENTER_Y - RADAR_RADIUS * math.cos(rad)
        self.radar_canvas.coords(self.scan_line, CENTER_X, CENTER_Y, end_x, end_y)
        
        # Dibujar detecciones
        for device in DEVICES:
            distance = device[3]
            angle = device[4]
            state = device[5]
            
            # Convertir coordenadas polares a cartesianas
            # Normalizar distancia al radio del radar
            norm_dist = distance * RADAR_RADIUS / 300 # 300 es la distancia máxima simulada
            
            angle_rad = math.radians(angle)
            x = CENTER_X + norm_dist * math.sin(angle_rad)
            y = CENTER_Y - norm_dist * math.cos(angle_rad)
            
            # Color basado en el estado
            color = COLOR_ACCENT if "JAMMING" in state else COLOR_RADAR
            
            # Dibujar el punto de detección
            self.radar_canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color, outline=COLOR_RADAR, tags="detection")
            
            # Actualizar indicador de estado
            if device[0] in self.indicators:
                led_color = COLOR_ACCENT if "JAMMING" in state else COLOR_RADAR
                self.indicators[device[0]].itemconfig("led", fill=led_color)
                
        # Simular movimiento de los dispositivos
        for i in range(len(DEVICES)):
            DEVICES[i] = (DEVICES[i][0], DEVICES[i][1], DEVICES[i][2], DEVICES[i][3] + random.randint(-2, 2), (DEVICES[i][4] + random.randint(-1, 1)) % 360, DEVICES[i][5])
            # Asegurar que la distancia se mantenga positiva
            if DEVICES[i][3] < 10:
                DEVICES[i] = (DEVICES[i][0], DEVICES[i][1], DEVICES[i][2], 10, DEVICES[i][4], DEVICES[i][5])

        # Repetir la actualización
        self.after(50, self.update_radar)

if __name__ == "__main__":
    app = PlayWarNetUI()
    app.mainloop()
