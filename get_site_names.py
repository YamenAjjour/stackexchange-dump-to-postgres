import os

dump_dir = "/media/webis20/corpora/corpora-thirdparty/corpora-stackexcahnge/http/"
for subdir, dirs, files in os.walk(dump_dir):
  print subdir.replace(dump_dir,"")
