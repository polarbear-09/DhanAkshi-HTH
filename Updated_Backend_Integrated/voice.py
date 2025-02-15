import speech_recognition as sr
import pyttsx3
from gpt_integration import generate_financial_advice, generate_emotional_support_message

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 160)  # Adjust speaking speed
        self.engine.setProperty("voice", self.get_female_voice())  # Use a more natural voice

    def get_female_voice(self):
        """
        Selects a female voice if available.
        """
        voices = self.engine.getProperty("voices")
        for voice in voices:
            if "female" in voice.name.lower():
                return voice.id
        return voices[0].id  # Default to first voice if no female voice found

    def speak(self, text):
        """
        Converts text to speech and speaks it out loud.
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """
        Captures voice input and converts it to text.
        """
        with sr.Microphone() as source:
            print("🎤 Listening... Speak now.")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio)
                print(f"🗣️ You said: {text}")
                return text.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I didn't catch that. Can you repeat?")
                return None
            except sr.RequestError:
                self.speak("Speech service is currently unavailable.")
                return None
            except Exception as e:
                self.speak("An error occurred while processing your speech.")
                return None

    def process_voice_command(self, command):
        """
        Processes voice commands related to financial advice or emotional support.
        """
        if command is None:
            return "I couldn't understand. Try again."

        if any(word in command for word in ["advice", "finance", "money", "spending"]):
            response = generate_financial_advice(command)
        elif any(word in command for word in ["stress", "anxious", "worry", "emotional"]):
            response = generate_emotional_support_message("stressed")
        elif any(word in command for word in ["save", "savings", "budget"]):
            response = generate_financial_advice(f"Give me saving tips for {command}")
        else:
            response = "I'm not sure how to respond. Try asking about financial advice or emotional support."

        print(f"🤖 AI Response: {response}")
        self.speak(response)
        return response

if __name__ == "__main__":
    assistant = VoiceAssistant()

    while True:
        user_input = assistant.listen()
        if user_input in ["exit", "quit", "stop"]:
            assistant.speak("Goodbye! Take care of your finances. 💰")
            break
        assistant.process_voice_command(user_input)
