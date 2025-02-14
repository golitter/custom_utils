# python使用pdb进行调试，在终端显示的同时，将调试内容及调试所得信息保存到文件中

# Windows下的调试方法
python -m pdb lab.py 2>&1 | Tee-Object -FilePath pdbDebug.log

# Linux下的调试方法
script -q -c "python3 -m pdb test.py" pdbDebug.log