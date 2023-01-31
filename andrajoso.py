#El andrajoso
Vestido = float(input('Ingrese el valor del vestido:'))
if (Vestido>=2500):
    descuento = 0.15
else:
    descuento = 0.08
precio_final = Vestido - (Vestido * descuento)
print (f"El precio final es:{precio_final} con descuento:{descuento*100}%")
