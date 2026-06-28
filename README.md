# J.A.R.V.I.S. - Asistente de IA

Asistente virtual con inteligencia artificial, reconocimiento de voz y respuesta por voz en español.

## 🌐 Versión Web (Recomendada)

**https://jarvis-assistant.surge.sh**

Funciona en Chrome y Edge. Solo presiona INICIAR y habla.

## 📥 Descarga para Windows

**https://github.com/cristoforohuamalixd-droid/jarvis-assistant/releases/download/v1.0/Jarvis.exe**

Descarga el .exe y ejecútalo. No necesita instalar Python.

## 🐍 Versión Python (Código fuente)

```bash
git clone https://github.com/cristoforohuamalixd-droid/jarvis-assistant
cd jarvis-assistant
pip install -r requirements.txt
python main.py
```

## Comandos de voz
- "¿Qué hora es?" - Hora actual
- "¿Qué día es?" - Fecha actual
- "Busca [tema]" - Buscar en Google
- "Adiós" - Cerrar

## Tecnologías
- **IA**: Groq (Llama 3.3 70B)
- **Web**: Speech API + Groq API
- **Escritorio**: Python, edge-tts, pygame
