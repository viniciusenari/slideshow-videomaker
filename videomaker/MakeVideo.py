import os
import moviepy.editor as mpy
from videomaker.ResizeImages import resize_all_images_in_folder

def create_videofile(filename, audio_file, title, fps = 24, codec = 'mpeg4', threads = 4, preset = 'slow', bitrate = '8000k', dimensions = [1280, 720], resize = True, duration = None):
    if resize: resize_all_images_in_folder('images/original', 1280, 720, (255, 255, 255))
    directory = sorted(os.listdir('images/resized')) if resize else sorted(os.listdir('images/original'))

    clip_duration = duration / (len(directory) - 1)
    clips = []
    for image in directory:
        if image != '.gitkeep':
            clip = mpy.ImageClip(f'images/resized/{image}').set_duration(clip_duration)
            clips.append(clip)

    video = mpy.concatenate_videoclips(clips, method = "compose")

    video.write_videofile(f'{filename}.mp4', fps = fps, codec = codec, threads = threads, preset = preset, bitrate = bitrate, audio = f'song/{audio_file}')


title = "Asa"
create_videofile('test_video', 'WhatsApp Audio 2022-05-11 at 6.29.19 PM.mpeg', title,  24, 'mpeg4', 4, 'ultrafast', "32000k", [1280, 720], True, 118)