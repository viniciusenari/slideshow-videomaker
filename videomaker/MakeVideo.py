import os
import moviepy.editor as mpy
from videomaker.ResizeImages import resize_all_images_in_folder, images_need_resizing
from videomaker.TitleText import create_title_text_clip


def resize_images(size):
    resize = images_need_resizing(size)
    if resize:
        print('Resizing images...')
        resize_all_images_in_folder(size, (255, 255, 255))
    directory = sorted(os.listdir('images/resized')) if resize else sorted(os.listdir('images/original'))
    return directory


def get_clip_duration(duration, directory):
    clip_duration = duration / (len(directory))
    return clip_duration


def create_title_card(title, clip_duration):
    title_clip = create_title_text_clip(title).set_duration(clip_duration)
    return title_clip


def create_image_clips(directory, clips, clip_duration):
    for image in directory:
        if image != '.gitkeep':
            clip = mpy.ImageClip(f'images/resized/{image}').set_duration(clip_duration)
            clips.append(clip)
    return clips


def concatenate_clips_and_add_audio(clips, duration):
    video = mpy.concatenate_videoclips(clips, method = "compose")
    audio_directory = os.listdir('song/')
    for filename in audio_directory:
        if filename != '.gitkeep':
            audio_file = filename
    audio_clip = mpy.AudioFileClip(f'song/{audio_file}').set_duration(duration)
    video = video.set_audio(audio_clip)
    return video


def create_video(title, size, duration = None):
    directory = resize_images(size)
    clip_duration = get_clip_duration(duration, directory)
    title_clip = create_title_card(title, clip_duration)
    clips = create_image_clips(directory, [title_clip], clip_duration)
    video = concatenate_clips_and_add_audio(clips, duration)
    return video


def write_video(video, bitrate = "16000k", threads = 1, filename = "video", preset = "ultrafast", fps = 24, codec = "mpeg4"):
    video.write_videofile(f'{filename}.mp4', fps = fps, codec = codec, threads = threads, preset = preset, bitrate = bitrate)