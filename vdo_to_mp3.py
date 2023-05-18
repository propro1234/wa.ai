# import ffmpeg as fm
# inp = fm.input('inp.mp4')

# out = fm.output(inp, 'out.mp3')
# print(out)
# print(fm.run(out))
# if out:
#     print("Success")

from pytube import YouTube
def yt_download(v,res):
    #v_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    yt = YouTube(v)

    streams = yt.streams

    filtered_streams = streams.filter(resolution=res)
    stream = filtered_streams.first()
    #print("Stream of desired stream: ",stream)
    stream.download(output_path="file:///sdcard/Download/")

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
