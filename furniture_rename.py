import os

# huge bastardisation of reddu ylime and bluemorpho's codes into 1
# renames fresh furniture files "furniture_number_l" to
# wiki format "Furniture_Number"

# py furniture_rename.py

folder = r"C:\Program Files\Python 3.9\furniture"
# folder of your choice, must include r in front (at least for me :( )

# if mass renaming, for checking how many files were already named
count = 0

for file in os.listdir(folder):
        filename = os.path.splitext(file)[0]
# checks if each file is named according to the raw format + ends with .png
        if filename.startswith("furniture") == True and file.endswith(".png"):
                try:
                        old_name = os.path.join(folder, file)
# yeets the _l and makes it the correct format
                        filename = filename.replace("_l", "")
                        new_name = os.path.join(folder, filename.capitalize() + ".png")
                        os.rename(old_name, new_name)
                except IOError:
                        pass
# checks if file already renamed, length check (Furniture_1234567)
        elif len(file) == 21:
                count = count + 1
                print("Already renamed.")
        else:
                print("This ain't a raw furniture file.")

# Check
res = os.listdir(folder)
print(res)
print("Already named file count: " + str(count))
