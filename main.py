import img2pdf
import os

path = 'input'
outPath = 'output'

if not os.path.exists(path):
    os.mkdir(path)
if not os.path.exists(outPath):
    os.mkdir(outPath)

# # Clears output directory
# for d in os.listdir(outPath):
#     dir = os.path.join(outPath, d).replace('\\','/')
#     if os.path.isdir(d):
#         shutil.rmtree(dir)
#     else:
#         os.remove(dir)

# Filters through data
for subdir, dirs, files in os.walk(path):
    for file in files:
        f = open(os.path.join(outPath, file).replace('\\', '/').replace('.png', '.pdf'), "wb")
        f.write(img2pdf.convert(os.path.join(path, file).replace('\\', '/')))
        f.close()
