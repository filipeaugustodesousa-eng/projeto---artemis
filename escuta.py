import sounddevice as sd
import whisper
import scipy.io.wavfile as wav

model = whisper.load_model("base")

def ouvir_felipe():

    print("Ouvindo...")

    samplerate = 16000
    duration = 5

    audio = sd.rec(int(duration * samplerate),
                   samplerate=samplerate,
                   channels=1)

    sd.wait()

    wav.write("entrada.wav", samplerate, audio)

    result = model.transcribe("entrada.wav", language="pt")

    texto = result["text"].lower()

    print("Você disse:", texto)

    return texto