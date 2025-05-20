import qrcode


url = input("URL: ").strip()
name = input("Name your file: ").strip()

img = qrcode.make(url)

img.save(name + ".png")
