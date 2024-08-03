from google.cloud import speech_v1
import os
from dotenv import load_dotenv

load_dotenv()

language_code = os.getenv('language_code')
audio_file_path = os.getenv('file_path')
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

def process_audio(audio_file_path):
    speech_client = speech_v1.SpeechClient()

    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
    # import pdb; pdb.set_trace()
    audio = speech_v1.RecognitionAudio(content=content)
    config = speech_v1.RecognitionConfig(
        encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )

    response = speech_client.recognize(config=config, audio=audio)

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

def process_audio_process(response):
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))




if __name__ == "__main__":
    processed_audio = process_audio(audio_file_path)
    # process_audio_process(processed_audio)
