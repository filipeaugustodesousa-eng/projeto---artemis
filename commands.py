import os

def executar(comando):
    comando = comando.lower()

    if "youtube" in comando:
        os.system("start https://youtube.com")
        return "Abrindo YouTube"

    elif "google" in comando:
        os.system("start https://google.com")
        return "Abrindo Google"

    elif "bloco de notas" in comando:
        os.system("notepad")
        return "Abrindo bloco de notas"

    elif "vscode" in comando:
        os.system("code")
        return "Abrindo Visual Studio Code"

    return None