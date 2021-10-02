from cx_Freeze import setup, Executable

setup(name='tetris',
      version='0.1',
      description='tetris',
      executables = [Executable("tetris.py")])
