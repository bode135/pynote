echo y|ffmpeg -f concat -i mylist.txt    -vcodec h264_nvenc output.mp4
: echo y|ffmpeg -i "concat:1.mpg|2.mpg"   -vcodec h264_nvenc -strict -2 output.mp4
pause