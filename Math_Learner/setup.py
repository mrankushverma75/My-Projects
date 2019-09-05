import sys
from cx_Freeze import setup , Executable

main_file = "E:\Python\Math_Learner\Quiz_Game.py"
file_title = "Easy Math Learner"

base = None
if sys.platform == "win64":
    base = "Win64GUI"
includes = ["atexit","re"]

setup(
    name = file_title,
    version = "1.0",
    options = {"build_exe" : {"includes" : includes}},
    executables = [Executable(main_file,base = base)])
