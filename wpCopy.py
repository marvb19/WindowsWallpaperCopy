import os
import shutil

try:
    src = "C:/users/marvin/appdata/local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"
    dest = "C:/Users/marvin/Pictures/wallpaper/"
    src_files = os.listdir(src)

    if not os.path.exists("C:/Users/marvin/Pictures/wallpaper"):
        os.mkdir("C:/Users/marvin/Pictures/wallpaper")

    dest_files = os.listdir(dest)

    for file_name in dest_files:
        full_file_name = os.path.join(dest, file_name)
        os.remove(full_file_name)

    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)

    dest_files = os.listdir(dest)
    for file_name in dest_files:
        full_file_name = os.path.join(dest, file_name)
        os.rename(full_file_name, full_file_name + ".jpg")

    os.startfile(dest)

except Exception:
    print("Error")
