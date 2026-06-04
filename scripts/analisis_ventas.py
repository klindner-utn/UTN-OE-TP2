import pandas as pd
import matplotlib.pyplot as plt

# Leer datos
df = pd.read_csv("datos/dataset.csv")
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Indicador 1: Ventas totales
ventas_totales = df["sales_amount"].sum()
print(f"Ventas totales: ${ventas_totales:,.2f}")

# Indicador 2: Promedio diario de ventas
promedio = df["sales_amount"].mean()
print(f"Promedio diario: ${promedio:,.2f}")

# Indicador 3: Dia con mayor venta
dia_max = df.loc[df["sales_amount"].idxmax()]
print(f"Día con mayor venta: {dia_max['sales_date'].date()} (${dia_max['sales_amount']:,.2f})")

# Indicador 4: Ventas por mes
df["mes"] = df["sales_date"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["sales_amount"].sum()
print("\nVentas por mes:")
print(ventas_por_mes)

# Gráfico: Evolucion de ventas por mes
plt.figure(figsize=(10, 5))
ventas_por_mes.plot(kind="bar")
plt.title("Evolución de Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Monto ($)")
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
print("\nGráfico guardado en resultados/grafico_ventas.png")
