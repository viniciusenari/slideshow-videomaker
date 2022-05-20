import moviepy.editor as mpy
import os


title = "Divisão dos Universitários, RM Pinda"
title_text = mpy.TextClip(txt = title,
                        fontsize = 40,
                        color = 'white',
                        bg_color = 'blue')

title_text.save_frame("test.png")