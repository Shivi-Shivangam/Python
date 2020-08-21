# CLI Command Based App Launcher with NLTK Tokenizer
# TODO: Add Grammar Check

from os import system
from pyttsx3 import speak
from nltk.tokenize import word_tokenize as wt


def take_input(ask: str = "What can I do for you? ") -> [str]:
    """
    :param ask: str
    :return: [str]

    Asks user for input & returns a list of String Tokens
    """
    speak(ask)
    return wt(input(ask).lower())


def helper(error: str = None) -> None:
    """
    :param error: str
    :return: None

    Speaks & Prints the Helping String
    If error is Passed: Speaks & Prints about the Error
    """
    helper_string = """\t\tThis is a Simple Command-Based App Launcher
    \tYou have to Enter Commands to be Fulfilled
    \tUse Keywords like Run, Start, Launch, Execute, Open or Show to make a Request
    \tFor Example: Open Chrome Browser in Incognito Mode or, Launch Camera
    \t             Show Notifications or, Show Map
    \t[ Note: The Commands are Completely Case-Insensitive ]\n"""
    if error is not None:
        print(error)
        speak(error)
    print(helper_string)
    speak(helper_string)


def running(app: str) -> None:
    """
    :param app: str
    :return: None

    Speaks & Prints the Acknowledgement after Execution
    """
    text = f"{app} is Up & Running. Enjoy...!\n"
    if app == 'Task Manager':
        speak(text)
        print(text, end='')
        speak("[Note: You need to Close the Task Manager to Continue]")
        print("[Note: You need to Close the Task Manager to Continue]\n")
    else:
        speak(text)
        print(text)


intro_string = """\tWelcome to the Command-Based Application Launcher.
\t You can Type-in Commands to Launch Applications.
\t\t\tType Bye, Exit, Stop or Quit to Stop.
\t\t\t Type Help to know how to use it.\n"""

print(intro_string)
speak(intro_string)
command = take_input()

while ('exit' not in command) and ('quit' not in command) and ('stop' not in command) \
        and ('bye' not in command) and ('nothing' not in command):
    # Helper
    if 'help' in command:
        helper()
    # Base Run Command Check
    elif ('run' in command) or ('start' in command) or ('launch' in command) \
            or ('execute' in command) or ('open' in command) or ('show' in command):
        # Browser
        if ('browser' in command) or ('chrome' in command) or ('edge' in command) \
                or (('internet' in command and 'explorer' in command) or 'ie' in command):
            # Ask for Browser Name, if ont specified in Command
            if ('chrome' not in command) and ('edge' not in command) \
                    and (('internet' not in command and 'explorer' not in command) and 'ie' not in command):
                command = take_input("Which Browser would you like to use? "
                                     "(Press Enter for Default: Microsoft Edge): ")
            if ('internet' in command and 'explorer' in command) or 'ie' in command:
                system("start iexplore google.com")
                running("Internet Explorer")
            elif 'chrome' in command:
                # Ask if the user need Incognito/Private Browsing
                if 'incognito' not in command or 'private' not in command:
                    command = take_input("Do you want Incognito Private Chrome? ")
                if 'incognito' in command or 'private' in command or 'yes' in command or 'yeah' in command:
                    system("start chrome -incognito")
                    running("Incognito Chrome")
                else:
                    system("start chrome google.com")
                    running("Chrome Browser")
            elif 'edge' in command:
                # Ask if the user need Incognito/Private Browsing
                if 'incognito' not in command or 'private' not in command:
                    command = take_input("Do you want Incognito Private Microsoft Edge? ")
                if 'incognito' in command or 'private' in command or 'yes' in command or 'yeah' in command:
                    system("start msedge -inPrivate")
                    running("Incognito Edge")
                else:
                    system("start msedge google.com")
                    running("Edge Browser")
            # Default
            else:
                system("start msedge google.com")
                running("Edge Browser")

        # Media Player
        elif ('player' in command) or ('windows' in command and 'mediaplayer' in command) \
                or ('vlc' in command) or ('groove' in command):
            # Ask for Media Player Name, if ont specified in Command
            if ('windows' not in command and 'mediaplayer' not in command) \
                    and ('vlc' not in command) and ('groove' not in command):
                command = take_input("Which Media Player would you like to use?"
                                     "(Press Enter for Default: Windows Media Player): ")
            if 'vlc' in command:
                system("start vlc")
                running("VLC")
            elif 'groove' in command:
                system("start mswindowsmusic:")
                running("Groove")
            # Default
            else:
                system("start wmplayer")
                running("Windows Media Player")

        # Text Editor
        elif ('text' in command and 'editor' in command) or ('text' in command and 'processor' in command)\
                or ('microsoft' in command and 'word' in command) or ('word' in command) \
                or ('notepad' in command) or ('onenote' in command) or ('sublime' in command):
            # Ask for Text Editors Name, if ont specified in Command
            if ('microsoft' not in command and 'word' not in command) and ('word' not in command) \
                    and ('notepad' not in command) and ('onenote' not in command) and ('sublime' not in command):
                command = take_input("Which Text Editor would you like to use?"
                                     "(Press Enter for Default: Notepad): ")
            if ('word' in command) or ('microsoft' in command and 'word' in command):
                system("start winword")
                running("Microsoft Word")
            elif 'onenote' in command:
                system("start onenote")
                running("Microsoft OneNote")
            elif 'sublime' in command:
                system("start sublime_text")
                running("Sublime Text")
            # Default
            else:
                system("start notepad")
                running("Notepad")

        # Antivirus
        elif ('antivirus' in command) or ('windows' in command and 'defender' in command) or ('bitdefender' in command):
            # Ask for Antivirus Name, if ont specified in Command
            if ('windows' not in command and 'defender' not in command) and ('bitdefender' not in command):
                command = take_input("Which Antivirus would you like to use?"
                                     "(Press Enter for Default: Windows Defender): ")
            if 'bitdefender' in command:
                system("start seccenter")
                running("Bit-Defender")
            else:
                system("start windowsdefender:")
                running("Windows Defender")

        # PowerPoint
        elif ('power' in command and 'point' in command) or 'presentation' in command or 'ppt' in command:
            system("start powerpnt")
            running("Microsoft PowerPoint")

        # Excel
        elif 'excel' in command or 'spreadsheet' in command:
            system("start excel")
            running("Microsoft Excel")

        # File Explorer
        elif 'explorer' in command or ('file' in command and 'explorer' in command):
            system("start explorer")
            running("File Explorer")

        # Task Manager
        elif ('task' in command and 'manager' in command) or 'taskmanager' in command:
            running("Task Manager")
            system("taskmgr")

        # Alarm & Clock
        elif 'alarm' in command or 'clock' in command:
            system("start ms-clock:")
            running("Alarm")

        # Calculator
        elif 'calculator' in command:
            system("start calculator:")
            running("Calculator")

        # Calendar
        elif 'calendar' in command:
            system("start outlookcal:")
            running("Calendar")

        # Camera
        elif 'camera' in command:
            system("start microsoft.windows.camera::")
            running("Camera")

        # Action Center / Notification Panel
        elif ('action' in command and 'center' in command) or 'notification' in command or 'notifications' in command:
            system("start ms-actioncenter:")
            running("Action Center")

        # News
        elif 'news' in command:
            system("start bingnews:")
            running("News")

        # Paint/Paint3D
        elif 'paint' in command:
            system("start ms-paint:")
            running("Paint")

        # Photos
        elif 'photo' in command or 'pic' in command:
            system("start ms-photos:")
            running("Photo")

        # Settings
        elif 'setting' in command or 'settings' in command:
            system("start ms-settings:")
            running("Setting")

        # Weather
        elif 'weather' in command:
            system("start bingweather:")
            running("Weather")

        # Xbox
        elif 'xbox' in command:
            system("start xbox:")
            running("Xbox")

        # Map
        elif 'map' in command:
            system("start bingmaps:")
            running("Map")

        # Mail
        elif 'mail' in command or 'email' in command:
            system("start outlookmail:")
            running("Mail")

        # Unknown Command Handling
        else:
            helper("Either the Request is Invalid or It can't  be Executed.\nFollow these Guidelines:")
    # Invalid Command Handling
    else:
        helper("Invalid Command. Follow these Guidelines:")
    command = take_input()
else:
    speak("Thanks for Using the Program.\nGood Bye and Have a Nice Day!!")
    print("Thanks for Using the Program.\nGood Bye & Have a Nice Day!!")
