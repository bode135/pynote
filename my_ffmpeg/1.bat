ffmpeg -i 1.mkv -qscale 4 1.mpg
ffmpeg -i 2.mkv -qscale 4 2.mpg

: ffmpeg -i "concat:1.ts|2.ts" -acodec copy -vcodec copy -absf aac_adtstoasc output.mp4
pause