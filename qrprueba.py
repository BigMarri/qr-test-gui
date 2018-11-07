#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from PIL import Image
import qrcode

class Aplicacion():
	def __init__(self):
		self.raiz = Tk()
		self.raiz.geometry('800x700')
		self.raiz.configure(bg = 'beige')
		#self.Label.configure(bg = 'beige')
		self.raiz.title('Aplicación')
		self.nomb = StringVar()
		self.ape = StringVar()

		self.boton1 = ttk.Button(self.raiz, text='Ejecutar',
                   command=self.codigoQR).grid(row=3, columnspan=2, padx=5, pady=5) #pack(side=BOTTOM)
		self.etiq1 = ttk.Label(self.raiz, text="Nombre:").grid(row=0)
		#self.etiq1.pack(side=TOP, fill=BOTH, expand=True,
                        #padx=10, pady=5)
		self.nombre = ttk.Entry(self.raiz, textvariable=self.nomb,
                              width=10).grid(row=0, column=1)
		#self.nombre.pack(side=TOP, fill=X, expand=True,
                       #padx=20, pady=5)
		self.etiq2 = ttk.Label(self.raiz, text="Apellidos:").grid(row=1)
		#self.etiq2.pack(side=TOP, fill=BOTH, expand=True,
                        #padx=10, pady=5)
		self.apell = ttk.Entry(self.raiz, textvariable=self.ape,
                              width=10).place(relx=0.5, rely =0.5, relwidth = 0.3)
		#self.apell.pack(side=TOP, fill=X, expand=True,
                       #padx=20, pady=5)
		self.raiz.mainloop()


	def codigoQR(self, *args):
		qr = qrcode.QRCode(
    			version=1,
    			error_correction=qrcode.constants.ERROR_CORRECT_L,
   			 box_size=10,
   			 border=2,
			)
		nomb = self.nomb.get()
		ape = self.ape.get()
		qr_string = nomb + '\n' + ape
		qr.add_data(qr_string)

		qr.make(fit=True)
		img = qr.make_image(fill_color="black", back_color="white")
		img.save(ape + nomb + ".png")

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
