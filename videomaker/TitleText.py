import moviepy.editor as mpy

def create_title_text_clip(text, frame_color = (16, 78, 139)):
    title_text = mpy.TextClip(txt = text,
                    font = "Candara-Bold",
                    size= (800, 0),
                    color = 'white')

    title_text = title_text.set_position("center")
    tt_width, tt_height = title_text.size

    background_frame = mpy.ColorClip(size=(tt_width + 100, tt_height + 50), color = frame_color)
    background_frame = background_frame.set_position("center")
    background_color = mpy.ColorClip(size=(1280, 720), color = (0, 0, 0))

    final_clip = mpy.CompositeVideoClip([background_color, background_frame, title_text])
    return final_clip