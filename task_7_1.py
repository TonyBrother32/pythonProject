import os
root = "my_project"

for dir_in in ["settings", "mainapp", "adminapp", "authapp"]:
    dir_path = os.path.join(root, dir_in)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
