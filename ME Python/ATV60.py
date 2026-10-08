def fahrenheit_para_celsius(f):
    return (5 / 9) * (f - 32)


fahrenheit = float(input("Digite a temperatura em ºF: "))
celsius = fahrenheit_para_celsius(fahrenheit)

print(f"{fahrenheit:.1f}ºF equivalem a {celsius:.2f}ºC")
