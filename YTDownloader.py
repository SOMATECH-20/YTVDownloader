import pytube
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

print("Welcome to our YouTube Downloader! Our application is capable of downloading videos up to 720p resolution. Please note that as we are currently in a development environment, you may encounter errors while using our software. We value your feedback and welcome any comments or concerns you may have while using our application.")

root = Tk()
root.withdraw() # Hide the main window


while True:
    u_input = input("\n\n\tPress C to choose where to download the video\n")
    if u_input.lower() == "c":

        save_path = askdirectory(title='Select Folder') # Show the file dialog

        if not save_path:
            print("No folder selected")
            quit() # Exit
        else:
            if not os.path.exists(save_path):
                os.makedirs(save_path)


        def on_progress(stream, chunk, bytes_remaining):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage = int(bytes_downloaded / total_size * 100)
            print(f"\rProgress: {percentage}%", end="")

        while True:
            try:
                url = input("Enter the URL of the video you want to download: ")
                yt = pytube.YouTube(url)
                yt.register_on_progress_callback(on_progress)
                

                print("Available resolutions:")
                for stream in yt.streams:
                    if stream.resolution:
                        print(stream.resolution)

                    res = input("Enter the resolution you want to download (e.g. 720p): ")
                    stream = yt.streams.filter(res=res).first()

                    if stream is None:
                        print(f"Error: No stream found with resolution {res}")
                        continue
                    else:
                        breakpoint

                    print(f"Downloading {yt.title} ({stream.resolution})...\n")
                    stream.download(save_path)
                    print("\nDownload complete!\n")


                    choice = input("Enter 'c' to continue and download other videos or 'q' to quit: ")
                    if choice.lower() == 'q':
                        quit()

            except pytube.exceptions.RegexMatchError:
                print("Error: Invalid URL. Please enter a valid YouTube video URL.")

    else:
        print("You pressed a wrong button. please try again.")




'''choice = input("Enter 'c' to continue and download other videos or 'q' to quit: ")
if choice.lower() == 'q':
    quit()'''