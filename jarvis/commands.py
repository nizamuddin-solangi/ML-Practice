import system_control

def process_command(command):
    """
    Parses the command string and executes the corresponding action.
    Returns:
        str: Response text for the assistant to speak.
    """
    if not command:
        return "I didn't catch that."

    # Browser Control
    if "open chrome" in command:
        system_control.open_chrome()
        return "Opening Chrome, sir."
    
    elif "close chrome" in command:
        system_control.close_chrome()
        return "Closing Chrome."

    elif "search google for" in command:
        query = command.replace("search google for", "").strip()
        if query:
            system_control.google_search(query)
            return f"Searching Google for {query}."
        else:
            return "What should I search for on Google?"

    # Typing
    elif "type" in command:
        text = command.replace("type", "").strip()
        if text:
            system_control.type_text(text)
            return "Typing now."
        else:
            return "What should I type?"

    # Media Control
    elif "play music" in command:
        system_control.play_pause_music()
        return "Playing music."
    
    elif "increase volume" in command or "volume up" in command:
        system_control.volume_control("increase")
        return "Increasing volume."
    
    elif "decrease volume" in command or "volume down" in command:
        system_control.volume_control("decrease")
        return "Decreasing volume."
    
    elif "mute" in command:
        system_control.volume_control("mute")
        return "Muting audio."

    # System Power
    elif "shutdown" in command and "pc" in command:
        system_control.system_power("shutdown")
        return "Shutting down the system in 10 seconds. Goodbye, sir."
    
    elif "restart" in command and "pc" in command:
        system_control.system_power("restart")
        return "Restarting the system in 10 seconds."

    # Conversation / Extras
    elif "hello" in command:
        return "Hello! How can I help you today?"
    
    elif "exit" in command or "stop" in command:
        return "EXIT" # Signal to stop the main loop
    
    else:
        return "I am not sure how to do that yet."
