import whisper


def speech_recognition(model='base'):
    whisper_model = whisper.load_model(model)
    result = whisper_model.transcribe("data/RADIO TAPOK - Потрошитель_(bombmusic.ru).mp3", fp16=False)

    with open(f'transcription_{model}.txt', 'w') as file:
        file.write(result['text'])


def main():
    models = {1: 'tiny', 2: 'base', 3: 'small', 4: 'medium', 5: 'large'}

    for k, v in models.items():
        print(f'{k}: {v}')

    model = int(input("Enter the appropriate number of the selected model: "))

    if model not in models.keys():
        raise KeyError('[!] This model unsupported, please choice another models...')

    print(f'[+] You choice model: {model}, waiting...')

    speech_recognition(models[model])


if __name__ == '__main__':
    main()
