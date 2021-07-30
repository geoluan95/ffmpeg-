# ffmpeg-使用相关命令

1. 提取视频帧
ffmpeg -i  input.mp4  -ss 00:00:00 -frames:v 1  out.png
说明：-i input.mp4 截取的视频的名字
-ss 00:00:02 视频的时间戳
-frames:v 1 单独一帧
out.png 保存截取封面名字
2. 从视频文件中获取音频文件
ffmpeg -i input.mp4 -f wav -ar 16000 out.wav
说明：input.mp4：视频文件
-f wav wav编码
-ar 16000 音频采样率
out.wav 输出的音频文件
