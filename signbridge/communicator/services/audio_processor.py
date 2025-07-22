from speech_to_sign import SpeechToSign
import threading


class AudioProcessor:
    def __init__(self):
        self.speech_processor = SpeechToSign()
        self.listening = False
        self.thread = None

    def start_listening(self):
        """Inicia el hilo de escucha de audio"""
        if not self.listening:
            self.listening = True
            self.thread = threading.Thread(
                target=self._listen_loop,
                daemon=True
            )
            self.thread.start()

    def _listen_loop(self):
        """Loop interno para procesamiento de audio"""
        while self.listening:
            self.speech_processor.listen_and_update()

    @property
    def last_phrase(self):
        """Última frase reconocida"""
        return self.speech_processor.last_recognized_phrase

    def stop_listening(self):
        """Detiene el procesamiento de audio"""
        self.listening = False
        if self.thread:
            self.thread.join()