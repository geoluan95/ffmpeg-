# ------------获取pcm音频文件--------------
import os, re
import subprocess

filepath = "yu/"
filelist = os.listdir(filepath)

def clean_space(text):
  """"
  处理多余的空格
  """
  match_regex = re.compile(u'[\u4e00-\u9fa5。\.,，:：《》、\(\)（）]{1} +(?<![a-zA-Z])|\d+ +| +\d+|[a-z A-Z]+')
  should_replace_list = match_regex.findall(text)
  order_replace_list = sorted(should_replace_list,key=lambda i:len(i),reverse=True)
  for i in order_replace_list:
    if i == u' ':
      continue
    new_i = i.strip()
    text = text.replace(i,new_i)
  return text
for item in filelist:
    # 去除文件名中空格
    # print(item)
    if os.path.splitext(item)[1] == ".mp4":

        pattern = re.compile(r'[^\u4e00-\u9fa5]')
        new_title = re.sub(pattern, '', item)
        # new_title = clean_space(item)

        new_name = filepath + new_title + ".mp4"
        os.rename(filepath + item, new_name)

        cmd = "D:/ffmpeg/bin/ffmpeg -i " + new_name + " -vn -ar 16000 -ac 1 -f s16le " + filepath + "%s.pcm" % (
            new_title)
        print(cmd)
        subprocess.call(cmd, shell=True)

        os.rename(filepath + "%s.pcm" % (new_title), filepath + os.path.splitext(item)[0] + ".pcm")
        if os.path.exists(filepath + item):
            break
        else:
            os.rename(new_name, filepath + item)

print("Done")