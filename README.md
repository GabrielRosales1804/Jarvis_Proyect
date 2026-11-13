# Proyect Jarvis
# Área de Trabajo Activada por Aplausos (Clap-Activated Workspace)

Un script automatizado en Python que utiliza reconocimiento de audio para preparar tu entorno de desarrollo con un doble aplauso. Al detectarlo, el sistema te saluda por voz según la hora del día, abre tu lista de reproducción favorita en YouTube Music y lanza tu IDE.

[Read this in English below]

##  Características
*   Detección de doble aplauso: Utiliza el micrófono para medir los picos de volumen e identificar un patrón de dos aplausos rápidos.
*   Saludo por voz contextual: Te da los "Buenos días", "Buenas tardes" o "Buenas noches" dependiendo de la hora.
*   Auto-ejecución de entorno: Abre automáticamente YouTube Music y el entorno de desarrollo.
*   Ahorro de recursos: El micrófono se apaga automáticamente si no detecta actividad en 2 minutos o justo después de activarse el sistema.

## Requisitos
Necesitarás Python 3.x y las siguientes librerías instaladas:

pip install sounddevice numpy pyttsx3

Nota para usuarios de Arch Linux: Para que pyttsx3 funcione correctamente en distribuciones Linux, es posible que necesites instalar un motor de síntesis de voz del sistema como espeak o espeak-ng (sudo pacman -S espeak-ng). Además, sounddevice puede requerir portaudio (sudo pacman -S portaudio).

## Uso
1. Ejecuta el script desde tu terminal: python main.py
2. Da dos aplausos fuertes y rápidos.
3. El sistema te saludará y preparará tu entorno.

##  Personalización (Nota sobre Arch Linux / Windows)
El script incluye el comando os.system("start devenv"), el cual lanza Visual Studio Community en Windows. 
Si estás ejecutando esto en Arch Linux, deberás modificar la línea 40 para tu IDE preferido en Linux (por ejemplo, VS Code, Rider o Neovim).
*   Para VS Code: os.system("code")
*   Para JetBrains Rider: os.system("rider")

También puedes cambiar la lista de reproducción modificando la URL en la función activar_sistema().

________________________________________________________________________

#  Clap-Activated Workspace

An automated Python script that uses audio recognition to set up your development environment with a double clap. Upon detection, the system greets you via text-to-speech based on the time of day, opens your favorite YouTube Music playlist, and launches your IDE.

##  Features
*   Double Clap Detection: Uses the microphone to measure volume peaks and identify a quick two-clap pattern.
*   Contextual Voice Greeting: Greets you with "Good morning", "Good afternoon", or "Good evening" depending on the time.
*   Environment Auto-Launch: Automatically opens YouTube Music and your development environment.
*   Resource Saving: The microphone automatically shuts down if no activity is detected for 2 minutes or immediately after the system is triggered.

##  Requirements
You will need Python 3.x and the following libraries installed:

pip install sounddevice numpy pyttsx3

Note for Arch Linux users: For pyttsx3 to work properly on Linux distributions, you may need to install a system speech synthesis engine like espeak or espeak-ng (sudo pacman -S espeak-ng). Additionally, sounddevice might require portaudio (sudo pacman -S portaudio).

## Usage
1. Run the script from your terminal: python main.py
2. Give two loud, quick claps.
3. The system will greet you and set up your environment.

##  Customization (Note on Arch Linux / Windows)
The script currently uses os.system("start devenv"), which launches Visual Studio Community on Windows. 
Since you are using Arch Linux, you should modify line 40 to launch your preferred Linux IDE (like VS Code, Rider, or Neovim).
*   For VS Code: os.system("code")
*   For JetBrains Rider: os.system("rider")

You can also change the playlist by modifying the URL in the activar_sistema() function.
