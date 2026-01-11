import pyttsx3
import speech_recognition as sr

class VoiceEngine:
    def __init__(self):
        """
        Initialize the Text-to-Speech engine.
        """
        self.engine = pyttsx3.init()
        
        # Configure voice properties (Optional: Select a specific voice)
        voices = self.engine.getProperty('voices')
        # Usually 0 is male, 1 is female on Windows
        self.engine.setProperty('voice', voices[0].id) 
        self.engine.setProperty('rate', 170) # Speed of speech

    def speak(self, text):
        """
        Convert text to speech.
        """
        if not text:
            return
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """
        Listen to microphone input and return string text.
        Returns: 
            str: The recognized text, or None if failed/timed out.
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.0  # Wait a second of silence determining end of phrase
            r.energy_threshold = 300 # Adjust accordingly to ambient noise
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                return None

        try:
            print("Recognizing...")
            # Using google for better accuracy. 
            # Note: For strict offline, one would need PocketSphinx or Vosk, 
            # but Google is standard for 'beginner-friendly' accurate Python assistants.
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Network error.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
