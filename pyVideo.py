from gtts import gTTS
from moviepy import *
import os

# Texto a convertir en audio
text = "Hello, world! Welcome to AI-powered video creation."
language = 'en'

# Crear el audio con gTTS
tts = gTTS(text=text, lang=language, slow=False)
audio_path = "hello_world.mp3"
tts.save(audio_path)

# Crear un clip de imagen como fondo (puedes usar una imagen tuya)
image_path = "background.jpg"  # Asegúrate de tener una imagen en la misma carpeta
if not os.path.exists(image_path):  
    # Si no tienes una imagen, usa un color sólido como fondo
    video_clip = ColorClip(size=(1280, 720), color=(0, 0, 255), duration=5)  # Fondo azul
else:
    video_clip = ImageClip(image_path).with_duration(5)  # 5 segundos de duración

# Cargar el audio
audio_clip = AudioFileClip(audio_path)

# Ajustar duración del video a la del audio
video_clip = video_clip.with_audio(audio_clip)

# Exportar el video final
output_video = "hello_world.mp4"
video_clip.write_videofile(output_video, fps=24, codec="libx264", audio_codec="aac")

print("✅ Video generado exitosamente:", output_video)
