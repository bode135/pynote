import os
os.chdir('my_ffmpeg')
# os.system('ls')

input_video = 'input.mkv'
output_video = 'ouput.mp4'
_ss, _t = 1, 3

cuda = 0

if(cuda):
    _cuda = '-vcodec h264_nvenc'
else:
    _cuda = ''

def get_file_format(file):
    return file.split('.')[-1]

if(get_file_format(input_video) != get_file_format(output_video)):
    _codec_copy = ''
else:
    _codec_copy = '-codec copy'


commands  = [
    'ffmpeg',
    '-ss', _ss,
    '-t', _t,
    '-accurate_seek',
    _codec_copy,
    '-avoid_negative_ts 1',

    '-i', input_video,
    _cuda,
    output_video
]
commands = [str(i) for i in commands]
cmd = ' '.join(commands)
cmd
# cmd_head = 'chcp 65001\necho y|'
cmd_head = 'echo y|'
cmd = cmd_head + cmd
print(cmd)
# import subprocess
# subprocess.Popen(cmd)
os.system(cmd)
# os.system('ls')

from moviepy.editor import *
# subclip = (3, 5)
# fps = 15
# clip_0 = VideoFileClip(input_video).subclip(subclip[0], subclip[1]).set_fps(fps)
# clip_0 = VideoFileClip(input_video)
# clip_0.duration
clip_0 = VideoFileClip(output_video)
print('output\'s duration: ', clip_0.duration)