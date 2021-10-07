# 1°passo: instalar SpeechRecognition
# 2°passo:instalar PyAudio --> https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

# Aqui estou importando as bibliotecas necessárias para o código
import speech_recognition as sr
import os
import webbrowser

# criar reconhecedor de voz
rec = sr.Recognizer()

'''OBS: se haver mais de um microphone instalado no PC, veja na lista utilizando o print abaixo e indique o índice para o uso
do respectivo microphone. O print está comentado e para faze-lo funcionar, tire o comentário'''
#print(sr.Microphone().list_microphone_names())


# Estrutura do with abre e fecha o microphone
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Pode falar que ouvirei.")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")

    # Adicionei se acaso for abrir o browser, neste caso o Firefox
    if "abrir o navegador" in texto:
        os.system("start Firefox.exe")

    # Adicionei se acaso for abrir a rede social Instagram
    if "Abrir o Instagram" in texto:
        webbrowser.open("https://www.instagram.com/")

    # Para fechar o navegador
    if "fechar o navegador" in texto:
        os.system("taskkill /im Firefox.exe")

    # Para deligar o PC
    if "desligar o pc" in texto:
        os.system("shutdown /s /t 2")

    print("Capturado! Sua fala foi: " + texto)