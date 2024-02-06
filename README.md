# twst-furniture-renamer
Renames furniture files from twst of the `furniture_1234567_l` name to `Furniture_1234567`.png
Decodes and renames files in .txt format
Displays count of files processed at the end of the run

## v1.15 exclusive
Also moves .txt files in source folder into another `furnituretxt` folder to keep the source folder contents clean.

# How to use
1. Run command line as administrator (v1.15 only)
2. Check and rename _folder_ source directory in the file to the directory of your choice (IMPORTANT)
3. Enter `py furniture_rename.py` into command line to use (Windows)

# Restrictions
- Ignores all files that do not follow the naming convention.
Do not rename target files prior to use.
- (v1.15) If the same .txt file exists in both the source and `furnituretxt` folder, the source folder copy will not be moved.
