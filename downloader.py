from pytube import YouTube
import os

again = "y"

while again.lower() == "y":
    # ask for the link from the user
    link = input("Enter the link of YouTube video you want to download: ")
    yt = YouTube(link)

    # Showing details
    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length)
    print("Rating of video: ", yt.rating)
    print("Thumbnail", yt.thumbnail_url)

    # Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()

    # Asking for the location of the video
    location = input("Location of Video: ")
    if location == "":
        user = os.getlogin()
        # Use os.path.join to create a platform-independent path
        location = os.path.join('C:\\Users', user, 'Downloads') if os.name == 'nt' else os.path.join('/Users', user, 'Downloads')

    # Starting download
    print("Downloading...")
    ys.download(location)
    print("Download completed!!")
    again = input("Download again? [y/n] ")
