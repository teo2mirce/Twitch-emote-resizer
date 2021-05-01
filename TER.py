from pathlib import Path
import shutil
import os
import subprocess

in_dir="in"
out_dir="out"
dirpath = Path(out_dir)
if dirpath.exists() and dirpath.is_dir():
	shutil.rmtree(dirpath)
os.mkdir(dirpath)

# scaleFlags=["fast_bilinear","bilinear","bicubic","experimental","neighbor","area","bicublin","gauss","sinc","lanczos","spline","print_info","accurate_rnd","full_chroma_int","full_chroma_inp","bitexact"]
scaleFlags=["bicubic"]
for sf in scaleFlags:
	os.mkdir(out_dir+"/"+sf)

for filename in os.listdir(in_dir):
	temp_path=os.path.join(in_dir, filename)
	filename_no_ext=filename.split(".")[0]
	for sf in scaleFlags:
		subprocess.call(['ffmpeg', '-i', temp_path,'-vf','scale=112:112:flags='+sf, out_dir+"/"+sf+'/'+filename_no_ext+' 112'+'.png'])
		subprocess.call(['ffmpeg', '-i', temp_path,'-vf','scale=56:56:flags='+sf, out_dir+"/"+sf+'/'+filename_no_ext+' 56'+'.png'])
		subprocess.call(['ffmpeg', '-i', temp_path,'-vf','scale=28:28:flags='+sf, out_dir+"/"+sf+'/'+filename_no_ext+' 28'+'.png'])