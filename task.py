import speech_recognition as sr
from macos_speech import Synthesizer

r = sr.Recognizer()
speaker = Synthesizer()

def recognize_command(audio):
    try:
        command = r.recognize_google(audio, language='ru-RU')
        return command.lower()
    except sr.UnknownValueError:
        return None


def process_command(command):
    if command.startswith('создать заголовок'):
        title = command.split('заголовок', 1)[1].strip()
        html_content = f"<h3>{title}</h3>"
        with open('output.html', 'w') as f:
            f.write(html_content)
        speak('HTML страница с заголовком создана.')
    elif command.startswith('создать абзац'):
        text = command.split('абзац', 1)[1].strip()
        html_content = f"<p>{text}</p>"
        with open('output.html', 'w') as f:
            f.write(html_content)
        speak('HTML страница с абзацем создана.')
    elif command == 'прочесть':
        try:
            with open('output.html', 'r') as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            speak('HTML страница не создана.')
    elif command == 'сохранить':
        try:
            with open('output.html', 'r') as f:
                content = f.read()
                with open('output.html', 'w') as f:
                    f.write(content)
                speak('Текст сохранен как HTML.')
        except FileNotFoundError:
            speak('HTML страница не создана.')
    elif command == 'текст':
        try:
            with open('output.html', 'r') as f:
                content = f.read()
                with open('output.txt', 'w') as f:
                    f.write(content)
                speak('Текст сохранен как обычный текст.')
        except FileNotFoundError:
            speak('HTML страница не создана.')
    else:
        speak('Не распознана команда.')



def speak(text):
    print(text)
    speaker.say(text)

def main():
    with sr.Microphone() as source:
        print('Голосовой ассистент запущен.')
        while True:
            print('Слушаю...')
            audio = r.listen(source)

            command = recognize_command(audio)
            if command:
                process_command(command)
            else:
                print('Не распознана команда.')

if __name__ == '__main__':
    main()
