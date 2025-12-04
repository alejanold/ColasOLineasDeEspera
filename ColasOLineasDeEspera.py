# ----------------------------------------------
# Programa para calcular modelos de colas:
# en este caso M/M/1, M/M/C y M/M/1/K
# Investigacion de Operaciones
# ----------------------------------------------
# Variables a usar:
# λ = tasa promedio de llegadas
# μ = tasa promedio de servicio
# C = numero de servidores
# a = que tan cargado esta el sistema
# ρ = utilizacion del sistema (que tanto se ocupa el servidor)
# ----------------------------------------------
import math

def factorial(n):
    return math.factorial(n)
# ----------------------------------------------
# MODELO M/M/1
# ----------------------------------------------
def modelo_mm1(lam, mu):
    print("\n--- MODELO M/M/1 ---")
    print(f"λ = {lam}, μ = {mu}")

    if lam >= mu:
        print("El sistema no es estable :( λ debe ser menor que μ.")
        return
        
    rho = lam / mu  # utilización
    L = rho / (1 - rho)  # número promedio en el sistema
    Lq = (rho**2) / (1 - rho)  # número promedio en cola
    W = L / lam  # tiempo en el sistema
    Wq = Lq / lam  # tiempo en cola

print("\n--- PROCEDIMIENTO ---")
    print(f"ρ = λ/μ = {lam}/{mu} = {round(rho, 4)}")
    print(f"L = ρ / (1 - ρ) = {round(L, 4)}")
    print(f"Lq = ρ^2 / (1 - ρ) = {round(Lq, 4)}")
    print(f"W = L / λ = {round(W, 4)}")
    print(f"Wq = Lq / λ = {round(Wq, 4)}")

# ----------------------------------------------
# MODELO M/M/C
# ----------------------------------------------
def modelo_mmc(lam, mu, c):
    print("\n--- MODELO M/M/C ---")
    print(f"λ = {lam}, μ = {mu}, C = {c}")

    a = lam / mu  # intensidad de tráfico
    rho = a / c   # utilización
    print(f"\na = λ/μ = {a}")
    print(f"ρ = a/C = {rho}")

    if rho >= 1:
        print("\n Sistema NO es estable porque ρ ≥ 1")
        return

    # Cálculo de P0 (para la probabilidad de 0 unidades en el sistema)
    suma = 0
    for n in range(c):
        suma += (a**n) / factorial(n)

    parte2 = (a**c) / (factorial(c) * (1 - rho))
    P0 = 1 / (suma + parte2)

    # Para la probabilidad de espera
    Pw = ( (a**c) / (factorial(c) * (1 - rho)) ) * P0

    # Para Lq
    Lq = Pw * (rho / (1 - rho))

    # L, W, Wq
    L = Lq + a
    W = L / lam
    Wq = Lq / lam

    print("\n--- PROCEDIMIENTO ---")
    print(f"P0 = {round(P0, 6)}")
    print(f"P(espera) = {round(Pw, 6)}")
    print(f"Lq = {round(Lq, 4)}")
    print(f"L = {round(L, 4)}")
    print(f"Wq = {round(Wq, 4)}")
    print(f"W = {round(W, 4)}")
