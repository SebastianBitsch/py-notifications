# py-notifications

**Note: Only compatitble with OS X**

A small - very minimal - notification service for sending desktop notifications through the cli in python. 
When running jobs that take a few minutes, e.g. in a jupyter notebook, where you don't want to constantly check in on your code to see it it has finished, sending a notification when the job completes is usefull.

**No requirements**
- Uses the OS X built in osascript to construct the notification command - which is why it is only compatible with mac, the command is executed using the OS module.

## Usage 
An example of how to send a basic push notification with a title and some text - sent after 10 seconds.
  ```python
  from time import sleep
  from Notifications import notify

  sleep(10)
  notify("Took 10 seconds to run", title="Task done!")
  ```

## Output
<img width="378" alt="output-example" src="https://user-images.githubusercontent.com/72623007/164691363-ed6584bb-2645-4841-89e6-516891f5196f.png">
