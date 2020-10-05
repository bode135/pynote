import os
os.chdir('my_ffmpeg')
# os.system('ls')

files = []
f1 = '1.mkv'
f2 = '2.mkv'
for i in range(3):
    fname = str(i) + '.mkv'
    files.append(fname)
# files = [f1, f2]
files
f_data = 'file \'' + '\'\nfile \''.join(files) +'\''
print(f_data)

f_list = 'list.txt'
with open(f_list, 'w', encoding='gbk') as f:
    f.write(f_data)
call = 'ffmpeg -f concat -i {} -c copy output.mkv'.format(f_list)
call
cmd_head = 'echo y|'


os.system(cmd_head + call)
# os.getcwd()