# import ffmpeg as fm
# inp = fm.input('inp.mp4')

# out = fm.output(inp, 'out.mp3')
# print(out)
# print(fm.run(out))
# if out:
#     print("Success")

from pytube import YouTube
def yt_download(link,res):
    #v_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    yt = YouTube(link)
    stream = yt.streams

    filtered_stream = stream.filter(resolution=res,file_extension='mp4',progressive=True)

    s = filtered_stream.first()
    #path = os.getcwd()
    #print("Downloading...")
    path = 'file:///sdcard/Download'
    s.download(path)
    # print("Complete")

# for stream in streams:
#     print(stream)

#filtered_streams = streams.filter(only_audio=True)
# for stream in filtered_streams:
#     print(filtered_streams[abr])

# highest_res_stream = streams.get_highest_resolution()
# print(highest_res_stream)

# audio_stream = streams.get_audio_only()
# print(audio_stream)

# stream = streams.get_highest_resolution()
# stream.download(output_path="/home/p/Documents")

# def on_complete():
#     print("Download completed successfully!")

# stream.register_on_complete_callback(on_complete)
# # stream.download()

# def on_progress(stream, chunk, file_handle, bytes_remaining):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     progress = (bytes_downloaded / total_size) * 100
#     print(f"Progress: {progress:.2f}%")
