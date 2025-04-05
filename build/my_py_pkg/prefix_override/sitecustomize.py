import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bakelbakel/Documents/ros2_ex/install/my_py_pkg'
