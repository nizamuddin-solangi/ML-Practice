import voice
import commands
import time

def main():
    """
    Main loop for Jarvis AI Assistant.
    """
    jarvis = voice.VoiceEngine()
    
    # Startup greeting
    jarvis.speak("Initializing Jarvis. Systems are online. How can I help you?")

    while True:
        # Listen for user input
        command = jarvis.listen()
        
        if command:
            # Process the command
            response = commands.process_command(command)
            
            # Check for exit signal
            if response == "EXIT":
                jarvis.speak("Shutting down services. Goodbye, sir.")
                break
            
            # Intelligent Response Handling:
            # If the command was not understood, only speak if "Jarvis" was explicitly addressed.
            # This prevents the assistant from nagging on every unrecognized background noise.
            if response == "I am not sure how to do that yet.":
                if "jarvis" in command:
                    jarvis.speak(response)
            else:
                # Valid command executed
                jarvis.speak(response)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
