# Python to unlock PDF which is protected editing with password
# pip install pikepdf is needed
# drop a .pdf to unlock.py, and then *_u.pdf is created

import sys, pikepdf
pdf = pikepdf.open(sys.argv[1], allow_overwriting_input=True)
pdf.save(sys.argv[1][:-4] + "_u.pdf")

# If D&D does not work on Win11, create a batch file and drop PDF to the .bat
# unlock_py.bat
#   python unlock.py %1
