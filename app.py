from videomaker import create_video, write_video


if __name__ == "__main__":
    title = input('What title do you want to show on the beginning of your video? ')
    width, height = input('What is the resolution of your video? (Example: 1920x1080) ').split('x')
    duration = int(input('What is the duration of your audio track in seconds? '))
    video = create_video(title, [int(width), int(height)], duration)
    write_video(video)