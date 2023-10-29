import qrcode

a = "Hola"

qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 2)

qr.add_data(a)
qr.make(fit=True)
imagen_qr = qr.make_image(fill_color = "black",
                        back_color="white")

imagen_qr.save = ("codigo_qr.png")