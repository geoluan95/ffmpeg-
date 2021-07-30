# ffmpeg-使用相关命令

1. 提取视频帧
ffmpeg -i  + *.mp4 +  -ss 00:00:00 -frames:v 1 " + out.png
