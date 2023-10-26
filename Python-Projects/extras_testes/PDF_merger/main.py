import os
import pathlib
from pypdf import PdfMerger

merger = PdfMerger()
PDF_PATH = []

# Specify the path to the folder you want to list the contents of
ROOT_PATH = pathlib.Path()
ASSETS_PATH = str(ROOT_PATH) + "/assets"

# Use the os.listdir() function to get a list of files and directories in the folder
folderContents = os.listdir(ASSETS_PATH)

PDF_PATH = sorted(folderContents, key=lambda x: int(x.split(".")[1].split(" ")[1]))

for pdf in folderContents:
    merger.append("assets/"+pdf)

merger.write("result.pdf")
merger.close()