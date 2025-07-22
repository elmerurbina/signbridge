from speech_to_sign import SpeechToSign

speech_to_sign = SpeechToSign()

def recognize_speech():
    if speech_to_sign.listen_and_update():
        return {
            "phrase": speech_to_sign.last_recognized_phrase,
            "success": True
        }
    return {
        "phrase": "",
        "success": False
    }
