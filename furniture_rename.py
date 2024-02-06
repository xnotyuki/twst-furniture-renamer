import os
import base64

# huge bastardisation of reddu ylime and bluemorpho's codes into 1
# renames fresh furniture files "furniture_number_l" to wiki format "Furniture_Number"

# py furniture_rename.py

folder = r"C:\Program Files\Python 3.9\furniture"
# folder of your choice, must include r in front (at least for me :( )

# if mass renaming, for checking types of files processed
alreadyexist = 0
pngtopnglist = []
invalidfile = []
decodedlist = []

for file in os.listdir(folder):
        filename = os.path.splitext(file)[0]
# case 1: file matches raw format (prefix, length, digitlength) + already decoded
        if filename.startswith("furniture_") and len(filename) > 16 and filename[10:16].isdigit() and file.endswith(".png"):
                try:
                        old_name = os.path.join(folder, file)
                        filename = filename.replace("_l", "")
                        new_name = os.path.join(folder, filename.capitalize() + ".png")
                        os.rename(old_name, new_name)
                        pngtopnglist.append(filename.capitalize() + ".png")
                except IOError:
                        pass
# case 2: file matches raw format (prefix, length, digitlength)  + not decoded
        elif filename.startswith("furniture_") and len(filename) > 16 and filename[10:16].isdigit() and file.endswith(".txt"):
                imageData = open(folder + "\\" + file, "r").read()
                decodedData = base64.b64decode(imageData)
                filename = filename.replace("_l", "")
                filename = filename.capitalize()
                if os.path.exists(os.path.join(folder, filename + ".png")):#deletes _parsed file if it already exists
                        pass
                else:
                        imgFile = open(folder + "\\" + filename.removesuffix(".txt") + ".png", "wb")
                        imgFile.write(decodedData)
                        imgFile.close()
                        decodedlist.append(filename)
# case 3: file already renamed (capitalised prefix, length, digitlength, path exist) and decoded
        elif filename.startswith("Furniture_") and len(filename) == 17 and filename[10:16].isdigit() and os.path.exists(os.path.join(folder, filename + ".png")):
                alreadyexist = alreadyexist + 1
                print("> ??? Already renamed.")
        else:
                invalidfile.append(filename)
                print("> !!! This ain't a raw furniture file.")
                
# Number of files: already named, .png renames, .txt renames, invalid files
res = os.listdir(folder)
print(res)
print(">>>>>>> Already named file count: " + str(alreadyexist))
print(">>>>>>> .png file rename count: " + str(len(pngtopnglist)))
print(">>>>>>> .png files renamed: " + str(pngtopnglist))
print(">>>>>>> Decoded file count: " + str(len(decodedlist)))
print(">>>>>>> Decoded files: " + str(decodedlist))
print(">>>>>>> Invalid file count: " + str(len(invalidfile)))
print(">>>>>>> Invalid files: " + str(invalidfile))
