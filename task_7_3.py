import shutil
import os

#shutil.copytree("my_project/authapp/templates", "my_project/templates", dirs_exist_ok=True)
#shutil.copytree("my_project/mainapp/templates", "my_project/templates", dirs_exist_ok=True)

for root, dirs, files in os.walk("my_project"):
    if root.find("templates") > 0 and len(files) == 0:
        shutil.copytree(root, "templates", dirs_exist_ok=True)
