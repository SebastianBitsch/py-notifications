import os

def notify(body:str = "Your code has finished running", title:str = "Task completed", substitle:str = ""):
    """
    Display a global notification, useful when waiting for a long block of code to execute.
    
    Parameters
    ----------
    body: str, optional
        The main body of body to be displayed in the notification

    title: str, optional
        The title of the notification

    subtitle: str, optional
        The subtitle of the notification, written between the title and body
    """
    os.system(f"""osascript -e 'display notification "{body}" with title "{title}" subtitle "{substitle}" sound name "Submarine"'""")
