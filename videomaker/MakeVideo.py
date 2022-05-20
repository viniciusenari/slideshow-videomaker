import os
import moviepy.editor as mpy
from ResizeImages import resize_all_images_in_folder
from TitleText import create_title_text_clip

def create_videofile(filename, audio_file, title, fps = 24, codec = 'mpeg4', threads = 4, preset = 'slow', bitrate = '8000k', dimensions = [1280, 720], resize = True, duration = None):
    if resize: resize_all_images_in_folder('images/original', 1280, 720, (255, 255, 255))
    directory = sorted(os.listdir('images/resized')) if resize else sorted(os.listdir('images/original'))

    clip_duration = duration / (len(directory))
    clips = []

    title_text = create_title_text_clip(title).set_duration(clip_duration)
    clips.append(title_text)

    for image in directory:
        print(image)
        if image != '.gitkeep':
            clip = mpy.ImageClip(f'images/resized/{image}').set_duration(clip_duration)
            clips.append(clip)

    video = mpy.concatenate_videoclips(clips, method = "compose")

    audio_clip = mpy.AudioFileClip(f'song/{audio_file}').set_duration(duration)

    video = video.set_audio(audio_clip)

    video.write_videofile(f'{filename}.mp4', fps = fps, codec = codec, threads = threads, preset = preset, bitrate = bitrate)


