import os

def notify(text, *args, **kwargs):
    """
    Display a global notification, usefull when waiting for a long block of code to execute.
    
    Parameters
    ----------
    text: str, required
        The main body of text to be displayed in the notification

    title: str, optional
        The title of the notification

    subtitle: str, optional
        The subtitle of the notification, written between the title and text
    """ 

    defaultKwargs = { 'title': "Task completed", 'subtitle': "" }
    kwargs = { **defaultKwargs, **kwargs }
    
    os.system("""osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "Submarine"'""".format(text,kwargs['title'],kwargs['subtitle']))
