# CLI Command Based App Launcher
# TODO: Add Word Check

from os import system

intro_string = """\tWelcome to the Command-Based Application Launcher
\t You can Type-in Commands to Launch Applications
\t\t\tType Bye\\Exit\\Stop\\Quit to Stop
\t\t\tType Help to know How to Use it\n"""
help_string = """\t\t\tThis is a Simple Command-Based App Launcher
\t\t\tYou have to Enter Commands\\Requests to be Fulfilled
\t\t\tUse Keywords like Run, Start, Launch, Execute, Open or Show to make a Request
\t\t\tFor Example: Open Chrome Browser in Incognito Mode or Launch Camera
\t\t\t             Show Notifications or Show Map
\t\t\t[ Note: The Commands are Completely Case-Insensitive ]"""

print(intro_string)
command = input("What can I do for You? ").lower()

while 'exit' not in command and 'quit' not in command and 'stop' not in command and 'bye' not in command and 'nothing' not in command:
    # Helper
    if 'help' in command:
        print(help_string)
    # Base Run Command Check
    elif 'run' in command or 'start' in command or 'launch' in command or 'execute' in command or 'open' in command or 'show' in command:
        # Browser
        if 'browser' in command or ('chrome' in command) or ('edge' in command) or ('internet explorer' in command or 'ie' in command):
            if 'chrome' not in command and 'edge' not in command and ('internet explorer' not in command and 'ie' not in command):
                command = input("Which Browser would you like to use?(Press Enter for Default: Microsoft Edge): ").lower()
            if 'internet explorer' in command or 'ie' in command:
                system("start iexplore google.com")
            elif 'chrome' in command:
                if 'incognito' not in command or 'private' not in command:
                    command = input("Do you want Incognito/Private Chrome? ").lower()
                if 'incognito' in command or 'private' in command or 'yes' in command or 'yeah' in command:
                    system("start chrome -incognito")
                else:
                    system("start chrome google.com")
            elif 'edge' in command:
                if 'incognito' not in command or 'private' not in command:
                    command = input("Do you want Incognito/Private Microsoft Edge? ").lower()
                if 'incognito' in command or 'private' in command or 'yes' in command or 'yeah' in command:
                    system("start msedge -inPrivate")
                else:
                    system("start msedge google.com")
            else:
                system("start msedge google.com")
        # Media Player
        elif 'player' in command or 'windows media player' in command or 'vlc' in command or 'groove' in command:
            if 'windows media player' not in command and 'vlc' not in command and 'groove' not in command:
                command = input("Which Media Player would you like to use?(Press Enter for Default: Windows Media Player): ").lower()
            if 'vlc' in command:
                system("start vlc")
            elif 'groove' in command:
                system("start mswindowsmusic:")
            else:
                system("start wmplayer")
        # Text Editor
        elif 'text editor' in command or 'word processor' in command or 'microsoft word' in command or 'notepad' in command or 'onenote' in command or 'sublime' in command:
            if 'microsoft word' not in command and 'notepad' not in command and 'onenote' not in command and 'sublime' not in command:
                command = input("Which Text Editor would you like to use?(Press Enter for Default: Notepad): ").lower()
            if 'microsoft word' in command:
                system("start winword")
            elif 'onenote' in command:
                system("start onenote")
            elif 'sublime' in command:
                system("start sublime_text")
            else:
                system("start notepad")
        # Antivirus
        elif 'antivirus' in command or 'windows defender' in command or 'bitdefender' in command:
            if 'windows defender' not in command and 'bitdefender' not in command:
                command = input("Which Antivirus would you like to use?(Press Enter for Default: Windows Defender): ").lower()
            if 'bitdefender' in command:
                system("start seccenter")
            else:
                system("start windowsdefender:")
        # PowerPoint
        elif 'power point' in command or 'presentation' in command:
            system("start powerpnt")
        # Excel
        elif 'excel' in command or 'spreadsheet' in command:
            system("start excel")
        # File Explorer
        elif 'explorer' in command or 'file explorer' in command:
            system("start explorer")
        # Task Manager
        elif 'task manager' in command or 'taskmanager' in command:
            system("taskmgr")
        # Alarm & Clock
        elif 'alarm' in command or 'clock' in command:
            system("start ms-clock:")
        # Calculator
        elif 'calculator' in command:
            system("start calculator:")
        # Calendar
        elif 'calendar' in command:
            system("start outlookcal:")
        # Camera
        elif 'camera' in command:
            system("start microsoft.windows.camera::")
        # Action Center / Notification Panel
        elif 'action center' in command or 'notification' in command:
            system("start ms-actioncenter:")
        # News
        elif 'news' in command:
            system("start bingnews:")
        # Paint/Paint3D
        elif 'paint' in command:
            system("start ms-paint:")
        # Photos
        elif 'photo' in command or 'pic' in command:
            system("start ms-photos:")
        # Settings
        elif 'setting' in command:
            system("start ms-settings:")
        # Weather
        elif 'weather' in command:
            system("start bingweather:")
        # Xbox
        elif 'xbox' in command:
            system("start xbox:")
        # Map
        elif 'map' in command:
            system("start bingmaps:")
        # Mail
        elif 'mail' in command:
            system("start outlookmail:")
        # Unknown Command Handling
        else:
            print("Either the Request is Invalid or It can't  be Execute.\nUse these Guidelines:\n", help_string)
    # Invalid Command Handling
    else:
        print("Invalid Command. Use these Guidelines:\n", help_string)
    command = input("\nWhat can I do for You? ").lower()
else:
    print("OK Bye!!")
