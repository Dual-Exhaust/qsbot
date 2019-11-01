import glob
import os
import shutil

src_dir = os.path.dirname(__file__)
# print('src_dir: ' + src_dir)

dst_dir = os.path.join(os.getcwd(), "qsbot_examples")
# print('dst_dir: ' + dst_dir)

# print('cwd: ' + os.getcwd())


shutil.rmtree(dst_dir, ignore_errors=True)

os.makedirs(dst_dir)

pattern = '[0-9]*.py'

srcs = glob.glob(os.path.join(src_dir, pattern))
# print(srcs)

for src in srcs:
    # print('src: ' + src)
    relpath = os.path.relpath(src, src_dir)
    # print('relpath: ' + relpath)
    dst = os.path.join(dst_dir, relpath)
    # print('dst: ' + dst)
    shutil.copyfile(src, dst)
