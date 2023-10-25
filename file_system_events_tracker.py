import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/ronav/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created")
    
    def on_modified(self,event):
        print(f"Hey, {event.src_path} has been created")

    def on_moved(self,event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self,event):
        print(f"Oops! Someone Deleted {event.src_path}!")

observer = Observer() 
fileSystemEvenHandler = FileEventHandler()   
observer.schedule(fileSystemEvenHandler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()    
