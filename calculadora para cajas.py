Numero1 = float(
    input("Primer paso ingrese la tasa de conversion del Euro (€) del dia: "))
Numero2 = float(
    input("Primer paso ingrese la tasa de conversion del Dolar ($) del dia: "))

Tasadeconversion = Numero1 / Numero2

primeros_tres_digitos = str(round(Tasadeconversion, 5))[:5]

Billeto1 = float(
    input("De que nominacion es el billete de Euro (€) entregado : "))
Valorventa = float(
    input("Cual es el valor de la venta actual  en Euro (€) : "))

vueltoEuro = Billeto1 - Valorventa

Primeraconversion = vueltoEuro * Tasadeconversion
vueltoendolar = str(round(Primeraconversion, 5))[:5]

print(("Vuelto a dar al cliente en dolares"), vueltoendolar, ("$"))

vuelto1 = float(
    input("Cual es la cantidad en efectivo que le entregaras al cliente ($): "))

vuelto2 = vuelto1 - float(vueltoendolar)

vueltototal1 = str(round(vuelto2, 5))[:5]
vueltototal2 = str(round(vuelto2/Tasadeconversion, 5))[:5]

print("La tasa de conversion de Euro/Dolar es : ", primeros_tres_digitos)
print("Vuelto en Euros :", vueltoEuro,  "€")
print("vuelto en dolar :", vueltoendolar, ("$"))

print(vueltototal1, ("$ VUELTO EN DOLAR EN PAGO MOVIL "))
print(vueltototal2, ("€ VUELTO EN EURO EN PAGO MOVIL"))
