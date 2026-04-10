import time
import os
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from email_sender import send_email

INPUT_DIR = "/Users/moses/automation_input"
OUTPUT_DIR = "/Users/moses/automation_output"


class CSVHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"EVENT DETECTED: {event.src_path}")

        if event.src_path.endswith(".csv"):

            process_file(event.src_path)


def process_file(filepath):

    print(f"Processing file: {filepath}")

    # ⏳ wait for file write completion
    time.sleep(2)

    df = pd.read_csv(filepath)

    # -------------------------------
    # DATA CLEANING + ANALYTICS
    # -------------------------------

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle nulls
    df = df.fillna("Unknown")

    # Example transformation
    df["salary_band"] = df["salary"].apply(
        lambda x: "High" if x > 100000 else "Medium" if x > 70000 else "Low"
    )

    # Example aggregation
    summary = df.groupby("department")["salary"].mean().reset_index()
    print("Average salary by department:")
    print(summary)

    # Save cleaned file
    filename = os.path.basename(filepath).replace("joined", "cleaned")
    output_path = os.path.join(OUTPUT_DIR, filename)

    df.to_csv(output_path, index=False)

    print(f"Cleaned file saved: {output_path}")

    # Send email notification
    send_email(output_path)


# if __name__ == "__main__":
#
#     event_handler = CSVHandler()
#     observer = Observer()
#     observer.schedule(event_handler, INPUT_DIR, recursive=False)
#
#     print("Watching folder for new CSV files...")
#
#     observer.start()
#
#     try:
#         while True:
#             time.sleep(5)
#     except KeyboardInterrupt:
#         observer.stop()
#
#     observer.join()

def start_watcher():
    processed_files = set()

    def poll_existing_files():
        for file in os.listdir(INPUT_DIR):
            if file.endswith(".csv"):
                full_path = os.path.join(INPUT_DIR, file)
                if full_path not in processed_files:
                    processed_files.add(full_path)
                    print(f"📂 Found file via polling: {full_path}")
                    process_file(full_path)

    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, INPUT_DIR, recursive=False)

    print("Watching folder for new CSV files...")

    observer.start()

    try:
        while True:
            poll_existing_files()
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    start_watcher()