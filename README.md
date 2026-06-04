  # Análisis de Ventas - Trabajo Práctico
  
  ## Integrantes
  - P1 (Hugo): [Kenneth] - Líder y Organizador
  - P2 (Paco): [Kenneth] - Desarrollador Técnico
  - P3 (Luis): [Kenneth] - Revisor y QA
  
  ## Escenario
  Escenario B – Análisis de Ventas de una Pequeña Empresa
  
  ## Dataset
  Dataset de ventas simuladas diarias del año 2024.
  - Fuente: https://gist.github.com/khanusama20/ee33c2869dd5cf3cebdf020be1ca43f6
  - Formato: CSV (id, sales_date, sales_amount)
  
  ## Indicadores generados
  - Ventas totales del período
  - Promedio diario de ventas
  - Día con mayor venta
  - Ventas agrupadas por mes
  
  ## Ejecución
  ```bash
  python scripts/analisis_ventas.py
  
  Estructura
  
  ├── datos/          → Dataset CSV de ventas
  ├── scripts/        → Script de análisis en Python
  ├── resultados/     → Gráfico de evolución de ventas
  ├── README.md
  └── .gitignore
