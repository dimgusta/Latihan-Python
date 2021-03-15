import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o') #ini merupakan tanda point perpotongan suatu nilai dengan lib numpy marker = garis o = titik
#plt.plot(ypoints, 'o:r') #ini merupakan tanda point perpotongan suatu nilai dengan lib numpy tanpa marker o = titik : jenis garis r=warna merah 


plt.show()


""" Tanda yang bisa digunakan https://www.w3schools.com/python/matplotlib_markers.asp
'o'	Circle	
'*'	Star	
'.'	Point	s
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
"""

""" Jenis garis
Line Syntax	Description
'-'	Solid line	
':'	Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
"""

""" Jenis Warna
'r'	Red	
'g'	Green	
'b'	Blue	
'c'	Cyan	
'm'	Magenta	
'y'	Yellow	
'k'	Black	
'w'	White
"""