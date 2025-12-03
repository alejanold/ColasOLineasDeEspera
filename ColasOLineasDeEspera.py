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
