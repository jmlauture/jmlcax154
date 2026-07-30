from pathlib import Path

file_path = Path("C:/Users/pasto/my_github/jmlcax154/SBA_Python2/")
taskfile = file_path / "tasks.txt"

print("file_path =",file_path)

if file_path.exists():
   print("The path exists.")
else:
   print("There is no such path")

# This block code works
# if taskfile.is_file():
#   print(f"The file {taskfile} exists.")
# else:
#   print("There is no such file")

try:
    with open(taskfile, "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"The requested file {taskfile} could not be found. \nCreate the file and try again.")