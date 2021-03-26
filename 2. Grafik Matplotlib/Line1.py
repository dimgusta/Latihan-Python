import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') #'ro' untuk membuat grafik point saja yg terlihat 
plt.axis([0, 6, 0, 20])        #nilai koordinat x = 0-6     koordinat y = 0-20
plt.ylabel('Nilai')            #label sumbu y
plt.xlabel('Waktu')            #label sumbu x

plt.show()

#https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py