import schedule
import time
import os

def run_updater():
    print("Running Knowledge Update....")
    result=os.system("python update_knowledge.py")
    if result==0:
        print("Update Finished Successfully!")
    else:
        print("Update Failed!")


print("Scheduler Started! Press Ctrl+C to Stop.")
print("This will run update_knowledge.py every 2 minutes (for testing).\n")

while True:
    schedule.run_pending()
    time.sleep(10)