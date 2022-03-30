from pytube import YouTube

def on_complete(stream, file_path):
    print('Download complete')
    print(file_path)

def on_progress(stream, chunk, bytes_remaining):
    progress = f'{100 - round(bytes_remaining / stream.filesize * 100, 2)}%'
    print(progress)

link = input('Enter the link of the video: ')

video_object = YouTube(link, on_complete_callback=on_complete, on_progress_callback=on_progress)
print()

print(f"Title: {video_object.title}")
print(f"Length: {round(video_object.length / 60,2)} minutes")
print(f"Views: {video_object.views}")
print(f"Author: {video_object.author}")

#. Download
print('download: (b)est | (w)orst | (a)udio only | (e)xit')
choice = input('choice: ')

match choice:
    case 'b':
        video_object.streams.get_highest_resolution().download(r"C:\Users\utkar\Downloads")
    case 'w':
        video_object.streams.get_lowest_resolution().download(r"C:\Users\utkar\Downloads")
    case 'a':
        video_object.streams.get_audio_only().download(r"C:\Users\utkar\Downloads")
    case 'e':
        exit()