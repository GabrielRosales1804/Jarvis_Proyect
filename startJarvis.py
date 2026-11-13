import sounddevice as sd
import numpy as np
import pyttsx3
import datetime
import time
import webbrowser
import os

# --- 1. Configuración de la Voz ---
engine = pyttsx3.init()
engine.setProperty('rate', 145) 

for voice in engine.getProperty('voices'):
    nombre_voz = voice.name.lower()
    id_voz = voice.id.lower()
    
    if 'es' in id_voz or 'spanish' in nombre_voz:
        if 'sabina' in nombre_voz or 'helena' in nombre_voz or 'laura' in nombre_voz:
            engine.setProperty('voice', voice.id)
            break

def obtener_saludo():
    hora = datetime.datetime.now().hour
    if 5 <= hora < 12:
        return "Buenos días"
    elif 12 <= hora < 19:
        return "Buenas tardes"
    else:
        return "Buenas noches"

def activar_sistema():
    mensaje = f"{obtener_saludo()}, señor. Activando área de trabajo."
    print(f"\n\n[Sistema]: {mensaje}")
    engine.say(mensaje)
    engine.runAndWait()
    
    print("[Sistema]: Abriendo YouTube Music...")
    webbrowser.open("https://music.youtube.com/playlist?list=PLDXXWXp2BUG5cbiQGnC04j5G3-cpE_doG")
    
    print("[Sistema]: Iniciando Visual Studio Community...")
    os.system("start devenv")

# --- 2. Configuración del Micrófono y Detección ---
UMBRAL_VOLUMEN = 15 
aplausos = 0
tiempo_ultimo_aplauso = 0
tiempo_ultima_actividad = time.time() 

# NUEVO: Este es nuestro "seguro" para apagar el micrófono a tiempo
sistema_activado = False 

TIEMPO_MAX_ENTRE_APLAUSOS = .5 
COOLDOWN_ECO = 0.3 
LIMITE_INACTIVIDAD = 120 

def detector_audio(indata, frames, time_info, status):
    global aplausos, tiempo_ultimo_aplauso, tiempo_ultima_actividad
    
    # NUEVO: Si el sistema ya se activó, ignoramos cualquier ruido nuevo
    if sistema_activado:
        return 
        
    volumen = np.linalg.norm(indata) * 10
    
    tiempo_restante = int(LIMITE_INACTIVIDAD - (time.time() - tiempo_ultima_actividad))
    print(f"\rEscuchando... Nivel: {volumen:05.2f} | Aplausos: {aplausos} | Tiempo restante: {tiempo_restante}s   ", end="")
    
    if volumen > UMBRAL_VOLUMEN:
        ahora = time.time()
        if (ahora - tiempo_ultimo_aplauso) > COOLDOWN_ECO:
            aplausos += 1
            tiempo_ultimo_aplauso = ahora
            tiempo_ultima_actividad = ahora 
            print(f"\n[!] ¡Aplauso detectado! Nivel: {volumen:.2f}")

print("Dispositivos de audio detectados:")
print(sd.query_devices())
print("\n--- INICIANDO PROTOCOLO ---")

# --- 3. Bucle Principal ---
try:
    with sd.InputStream(callback=detector_audio):
        while True:
            # Si el sistema ya se activó previamente, evitamos que el bucle siga evaluando
            if sistema_activado:
                break
                
            ahora = time.time()
            
            if aplausos == 2:
                # NUEVO: Bloqueamos el micrófono inmediatamente
                sistema_activado = True 
                
                # Ejecutamos las acciones
                activar_sistema()
                print("\n[Sistema]: Tareas completadas. Cerrando programa de escucha...")
                break 
                
            elif aplausos == 1 and (ahora - tiempo_ultimo_aplauso) > TIEMPO_MAX_ENTRE_APLAUSOS:
                print("\n[-] Tiempo agotado para el segundo aplauso. Reiniciando...")
                aplausos = 0
            
            if (ahora - tiempo_ultima_actividad) >= LIMITE_INACTIVIDAD:
                print("\n\n[Sistema]: Se han cumplido 2 minutos sin actividad. Apagando sistema de forma automática.")
                break 
                
            time.sleep(0.05)
            
except KeyboardInterrupt:
    print("\nApagando sistemas...")