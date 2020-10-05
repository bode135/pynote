chcp 65001

rem ffmpeg -i input.mkv -ss 3 -t 5 -codec copy cut.mkv
rem echo y|ffmpeg -ss 3 -t 5 -accurate_seek -i input.mkv -codec copy -avoid_negative_ts 1 cut.mkv

echo y|ffmpeg -ss 3 -t 1 -accurate_seek -i input.mkv -codec copy  -avoid_negative_ts 1 cut.mkv

rem echo y|ffmpeg -ss 3 -t 5 -i input.mkv -c:v libx264 -c:a aac -strict experimental -b:a 98k cut.mp4 -y

#pause