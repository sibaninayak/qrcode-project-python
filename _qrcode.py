#import qrcode

#img = qrcode.make('lucky tu helu gate badmas pila rugia khali deha kharap hauchi tro')

#type(img)  # qrcode.image.pil.PilImage
#img.save("msg.png")

import io 
import qrcode
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size= 40,
    border=2,
)
qr.add_data("kitty is a good girl")
qr.make(fit=True)

img = qr.make_image(fill_color = "pink")