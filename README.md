# Sistema Masa-Resorte (2 Masas, 2 Resortes)

Simulación de un sistema de dos masas conectadas por dos resortes en posición vertical, resuelto mediante ecuaciones diferenciales ordinarias.

## 📋 Descripción del Sistema

El sistema está configurado de la siguiente manera:

```
    ════════════════  (Punto fijo - Techo)
          │
         ╱╲
        ╱  ╲
       ╱    ╲   Resorte 1 (k₁, L₁)
        ╲  ╱
         ╲╱
          │
       ┌──────┐
       │  m₁  │   Masa 1
       └──────┘
          │
         ╱╲
        ╱  ╲
       ╱    ╲   Resorte 2 (k₂, L₂)
        ╲  ╱
         ╲╱
          │
       ┌──────┐
       │  m₂  │   Masa 2
       └──────┘
          │
          ↓ g (gravedad)
```

## 🔬 Modelo Matemático

### Ecuaciones de Movimiento

El sistema se modela mediante las siguientes ecuaciones diferenciales de segundo orden:

**Para la masa 1:**
$$m_1 \ddot{x}_1 = -k_1(x_1 - L_1) + k_2(x_2 - x_1 - L_2) + m_1 g$$

**Para la masa 2:**
$$m_2 \ddot{x}_2 = -k_2(x_2 - x_1 - L_2) + m_2 g$$

### Variables del Sistema

| Variable | Descripción | Unidades |
|----------|-------------|----------|
| $x_1, x_2$ | Posiciones de las masas (positivo hacia abajo) | m |
| $\dot{x}_1, \dot{x}_2$ | Velocidades de las masas | m/s |
| $m_1, m_2$ | Masas | kg |
| $k_1, k_2$ | Constantes de elasticidad de los resortes | N/m |
| $L_1, L_2$ | Longitudes naturales de los resortes | m |
| $g$ | Aceleración gravitacional | m/s² |

### Posiciones de Equilibrio

Las posiciones de equilibrio estático se calculan como:

$$x_{1,eq} = L_1 + \frac{(m_1 + m_2)g}{k_1}$$

$$x_{2,eq} = x_{1,eq} + L_2 + \frac{m_2 g}{k_2}$$

## 🚀 Instalación

### Requisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Dependencias

```bash
pip install numpy scipy matplotlib
```

## 💻 Uso

### Ejecución Básica

```bash
python sistema_masa_resorte.py
```

### Uso como Módulo

```python
from sistema_masa_resorte import SistemaMasaResorte

# Definir parámetros del sistema
m1 = 1.0      # kg
m2 = 2.0      # kg
k1 = 100.0    # N/m
k2 = 50.0     # N/m
L1 = 0.1      # m
L2 = 0.15     # m

# Crear el sistema
sistema = SistemaMasaResorte(m1, m2, k1, k2, L1, L2)

# Obtener posiciones de equilibrio
x1_eq, x2_eq = sistema.encontrar_equilibrio()

# Definir condiciones iniciales (x1, v1, x2, v2)
condiciones_iniciales = (x1_eq + 0.05, 0, x2_eq + 0.03, 0)

# Simular el sistema
t, x1, v1, x2, v2 = sistema.simular(
    condiciones_iniciales,
    t_final=10,
    num_puntos=1000
)

# Visualizar resultados
sistema.graficar_resultado(t, x1, v1, x2, v2, x1_eq, x2_eq)
```

### Parámetros de Simulación

| Parámetro | Descripción | Valor por defecto |
|-----------|-------------|-------------------|
| `t_inicial` | Tiempo inicial de simulación | 0 s |
| `t_final` | Tiempo final de simulación | 10 s |
| `num_puntos` | Número de puntos de evaluación | 1000 |

## 📊 Salida

El script genera:

1. **Consola**: Información detallada del sistema, posiciones de equilibrio y condiciones iniciales.

2. **Gráficos**: Cuatro subgráficas mostrando:
   - Posición de masa 1 vs tiempo
   - Velocidad de masa 1 vs tiempo
   - Posición de masa 2 vs tiempo
   - Velocidad de masa 2 vs tiempo

3. **Archivo de imagen**: `simulacion_masa_resorte.png`

## 🔧 Estructura del Código

```
sistema_masa_resorte.py
│
├── SistemaMasaResorte (Clase principal)
│   ├── __init__()           # Inicialización con parámetros
│   ├── ecuaciones()         # Sistema de EDOs
│   ├── encontrar_equilibrio() # Cálculo analítico del equilibrio
│   ├── simular()            # Integración numérica con odeint
│   └── graficar_resultado() # Visualización de resultados
│
└── main                     # Ejemplo de uso con parámetros predefinidos
```

## 📈 Ejemplo de Resultados

Con los parámetros por defecto:
- **m₁ = 1.0 kg**, **m₂ = 2.0 kg**
- **k₁ = 100 N/m**, **k₂ = 50 N/m**
- **L₁ = 0.1 m**, **L₂ = 0.15 m**

Se obtienen oscilaciones acopladas donde ambas masas oscilan con diferentes amplitudes y fases debido a la naturaleza acoplada del sistema.

## 🧮 Método Numérico

La integración se realiza usando `scipy.integrate.odeint`, que implementa el método LSODA (Livermore Solver for Ordinary Differential Equations with Automatic method switching). Este método:

- Cambia automáticamente entre métodos stiff y non-stiff
- Proporciona alta precisión
- Es eficiente para sistemas de ecuaciones diferenciales

## 📚 Referencias

- Thornton, S. T., & Marion, J. B. (2004). *Classical Dynamics of Particles and Systems*. Brooks/Cole.
- Edwards, C. H., & Penney, D. E. (2008). *Elementary Differential Equations with Boundary Value Problems*. Pearson.

## 📄 Licencia

Este proyecto es de uso académico para el curso de Modelación con Ecuaciones Diferenciales.

---
*Desarrollado para el Tecnológico de Monterrey - Ciencia de Datos*
