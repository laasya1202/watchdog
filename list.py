import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
source="/Users/sushma/Downloads"
destination="/Users/sushma/Desktop/list"
directory={
    "imagefiles":[".jpg",".jpeg",".png"],
    "documentfiles":[".ppt",".pdf",".txt"]
}
class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)
        for i,j in directory.items():
            if extension in j:
                filename=os.path.basename(event.src_path)
                path1=source + "/" + filename
                path2=destination + "/" + i
                path3=destination + "/" + i + "/" + filename
                if os.path.exists(destination+"/"+i):
                    if os.path.exists(path2):
                        print("Moving your files...")
                        time.sleep(1)
                        shutil.move(path1,path3)
                    else:
                        os.makedirs(path2)
                        print("Moving your files...")
                        shutil.move(path1,path3)
                        time.sleep(1)
event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,source,recursive=True)
observer.start()
while True:
    time.sleep(2)
    print("Your module is running.")

