import matplotlib.pyplot as plt
import os.path
import numpy as np

student_img = PIL.Image.open(student_file)
fig, ax = plt.subplots(1, 2)
ax[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
ax[1].imshow(student_img, interpolation='none')
ax[1].set_xticks(range(1050, 1410, 100))
ax[1].set_xlim(1050, 1400) # Measure in plt, experiment in iPython
ax[1].set_ylim(1100, 850)
fig.show()
