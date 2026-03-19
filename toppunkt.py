# Importerer relevante biblioteker
import numpy as np
import matplotlib.pyplot as plt

# Definerer funksjonen fra oppgaven
def f(x):
    return np.exp(-x/4) * np.arctan(x)

# Definerer likningen som bestemmer toppunktet
def g(x):
    return np.arctan(x) - 4/(x**2 + 1)

# Startintervall for halveringsmetoden, fordi nullpunktet ligger mellom de
a = 1
b = 2

# Utfører halveringsmetoden 100 ganger
for i in range(100):
    m = (a + b) / 2     # midtpunktet i intervallet

    # Finner ut hvilken halvdel nullpunktet er i
    if g(a) * g(m) < 0:
        b = m
    else:
        a = m

# Midtpunktet i siste intervall er tilnærmet løsning

# Finner x- og y-koordinaten
x_topp = (a + b) / 2
y_topp = f(x_topp)

# Skriver ut punktet
print(f"x_topp = {x_topp:.4f}")
print(f"y_topp = {y_topp:.4f}")
print(f"Toppunkt = ({x_topp:.4f}, {y_topp:.4f})")

# Lager plott
x = np.linspace(-4, 8, 1000)
y = f(x)

plt.figure(figsize=(8,5))
plt.plot(x, y, label=r"$f(x)=e^{-x/4}\arctan(x)$")
plt.plot(x_topp, y_topp, 'ro', label=f"Toppunkt ({x_topp:.4f}, {y_topp:.4f})")
plt.axvline(x_topp, linestyle='--')
plt.axhline(y_topp, linestyle='--')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plott av funksjonen")
plt.grid(True)
plt.legend()
plt.show()