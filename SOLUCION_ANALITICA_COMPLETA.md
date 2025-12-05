# Sistema de Dos Masas y Dos Resortes Colgantes
## Solución Analítica Completa

---

## 1. Descripción del Problema

### Configuración Física del Sistema

Consideramos un sistema mecánico compuesto por dos masas conectadas por resortes en una disposición vertical:

```
      [Techo fijo]
           |
       [Resorte 1, k₁]
           |
       [Masa 1, m₁]
           |
       [Resorte 2, k₂]
           |
       [Masa 2, m₂]
```

**Parámetros del sistema:**
- $m_1$: masa 1 (kg)
- $m_2$: masa 2 (kg)
- $k_1$: constante de elasticidad del resorte 1 (N/m)
- $k_2$: constante de elasticidad del resorte 2 (N/m)

### El Truco del Equilibrio Estático

La clave para simplificar este problema es reconocer que:

1. **Sistema en equilibrio:** Las masas están colgando en reposo, habiendo deformado los resortes por su propio peso
2. **Desviaciones desde equilibrio:** En lugar de medir posiciones absolutas desde el techo, medimos solo las desviaciones $y_1(t)$ y $y_2(t)$ respecto a la posición de equilibrio
3. **Cancelación de gravedad:** Al medir desde el equilibrio, la gravedad se cancela matemáticamente con la deformación inicial de los resortes

**Variables principales:**
- $y_1(t)$: desplazamiento de la masa 1 desde su posición de equilibrio (positivo hacia abajo)
- $y_2(t)$: desplazamiento de la masa 2 desde su posición de equilibrio (positivo hacia abajo)

---

## 2. Análisis de Fuerzas y Modelación Matemática

### Análisis de Fuerzas sobre Cada Masa

#### Fuerzas sobre la Masa 1

Cuando la masa 1 se desplaza una cantidad $y_1$ desde su posición de equilibrio:

**Fuerza del Resorte 1:**
- El resorte 1 conecta el techo con la masa 1
- Una desviación $y_1$ desde el equilibrio genera una fuerza restauradora
- Por la ley de Hooke: $F_{k_1} = -k_1 y_1$

**Fuerza del Resorte 2:**
- El resorte 2 conecta las dos masas
- Lo que importa es la separación relativa entre masas: $(y_2 - y_1)$
- Si $y_2 > y_1$, el resorte 2 se estira, jalando la masa 1 hacia abajo
- Fuerza sobre masa 1: $F_{k_2} = k_2(y_2 - y_1)$

**Gravedad:**
- ¡No aparece! Se cancela con la deformación inicial del equilibrio estático

**Fuerza neta sobre masa 1:**
$$\sum F_1 = -k_1 y_1 + k_2(y_2 - y_1)$$

#### Fuerzas sobre la Masa 2

Cuando la masa 2 se desplaza una cantidad $y_2$ desde su posición de equilibrio:

**Fuerza del Resorte 2:**
- Por acción y reacción, si el resorte 2 ejerce fuerza $k_2(y_2 - y_1)$ sobre masa 1, ejerce la opuesta sobre masa 2
- Fuerza sobre masa 2: $F_{k_2} = -k_2(y_2 - y_1)$

**Gravedad:**
- ¡No aparece! Se cancela con la deformación inicial del equilibrio estático

**Fuerza neta sobre masa 2:**
$$\sum F_2 = -k_2(y_2 - y_1)$$

### Ecuaciones de Movimiento (Segunda Ley de Newton)

Aplicando $\sum F = m \cdot a$:

$$m_1 \ddot{y}_1 = -k_1 y_1 + k_2(y_2 - y_1)$$

$$m_2 \ddot{y}_2 = -k_2(y_2 - y_1)$$

Reorganizando los términos:

$$m_1 \ddot{y}_1 + k_1 y_1 + k_2 y_1 - k_2 y_2 = 0$$

$$m_2 \ddot{y}_2 + k_2 y_2 - k_2 y_1 = 0$$

O en forma estándar (igualadas a cero):

$$m_1 \ddot{y}_1 + (k_1 + k_2) y_1 - k_2 y_2 = 0 \quad \text{...(1)}$$

$$m_2 \ddot{y}_2 - k_2 y_1 + k_2 y_2 = 0 \quad \text{...(2)}$$

---

## 3. Formulación Matricial del Sistema

### Forma Matricial Explícita

El sistema de ecuaciones diferenciales de segundo orden puede expresarse en forma matricial:

$$\begin{bmatrix} m_1 & 0 \\ 0 & m_2 \end{bmatrix} \begin{bmatrix} \ddot{y}_1 \\ \ddot{y}_2 \end{bmatrix} + \begin{bmatrix} k_1 + k_2 & -k_2 \\ -k_2 & k_2 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

### Notación Compacta

$$\mathbf{M} \ddot{\mathbf{y}} + \mathbf{K} \mathbf{y} = \mathbf{0}$$

Donde:

**Matriz de Masa:**
$$\mathbf{M} = \begin{pmatrix} m_1 & 0 \\ 0 & m_2 \end{pmatrix}$$

**Matriz de Rigidez:**
$$\mathbf{K} = \begin{pmatrix} k_1 + k_2 & -k_2 \\ -k_2 & k_2 \end{pmatrix}$$

**Vector de Desplazamientos:**
$$\mathbf{y}(t) = \begin{pmatrix} y_1(t) \\ y_2(t) \end{pmatrix}$$

### Interpretación Física de la Matriz de Rigidez

- **Diagonal principal $(k_1 + k_2)$ y $k_2$:** Resistencia de cada masa al desplazamiento
- **Términos fuera de diagonal $-k_2$:** Representan el **acoplamiento** entre masas
  - Lo que hace una masa afecta a la otra a través de los resortes de conexión

---

## 4. Solución Analítica mediante Valores y Vectores Propios

### Búsqueda de Soluciones de Forma Exponencial

Para resolver el sistema $\mathbf{M} \ddot{\mathbf{y}} + \mathbf{K} \mathbf{y} = \mathbf{0}$, buscamos soluciones de la forma:

$$\mathbf{y}(t) = \mathbf{A} e^{i\omega t}$$

donde $\mathbf{A} = \begin{pmatrix} A_1 \\ A_2 \end{pmatrix}$ es un vector de amplitudes constantes.

### Sustitución en la Ecuación Diferencial

Calculamos las derivadas de $\mathbf{y}(t) = \mathbf{A} e^{i\omega t}$:

$$\dot{\mathbf{y}}(t) = i\omega \mathbf{A} e^{i\omega t}$$

$$\ddot{\mathbf{y}}(t) = -\omega^2 \mathbf{A} e^{i\omega t}$$

Sustituyendo en la ecuación $\mathbf{M} \ddot{\mathbf{y}} + \mathbf{K} \mathbf{y} = \mathbf{0}$:

$$\mathbf{M} \left(-\omega^2 \mathbf{A} e^{i\omega t}\right) + \mathbf{K} \left(\mathbf{A} e^{i\omega t}\right) = \mathbf{0}$$

Factorizando $e^{i\omega t}$ (que nunca es cero):

$$-\omega^2 \mathbf{M} \mathbf{A} + \mathbf{K} \mathbf{A} = \mathbf{0}$$

Reorganizando:

$$(\mathbf{K} - \omega^2 \mathbf{M}) \mathbf{A} = \mathbf{0}$$

### Planteamiento del Problema de Valores Propios

Esta última ecuación es un sistema lineal homogéneo en $\mathbf{A}$. Para que exista una solución no trivial ($\mathbf{A} \neq \mathbf{0}$), el determinante de la matriz de coeficientes debe ser cero:

$$\det(\mathbf{K} - \omega^2 \mathbf{M}) = 0$$

Este es el **problema de valores propios generalizados** del sistema.

### Frecuencias Naturales y Modos Normales

Resolviendo la ecuación característica anterior, se obtienen:

**Dos frecuencias naturales:**

$$\omega_1 \quad \text{(frecuencia natural más baja)}$$
$$\omega_2 \quad \text{(frecuencia natural más alta)}$$

**Dos vectores propios (modos normales):**

$$\mathbf{v}_1 = \begin{pmatrix} v_{1,1} \\ v_{1,2} \end{pmatrix} \quad \text{asociado a } \omega_1$$

$$\mathbf{v}_2 = \begin{pmatrix} v_{2,1} \\ v_{2,2} \end{pmatrix} \quad \text{asociado a } \omega_2$$

**Interpretación física:**
- **Modo 1** ($\omega_1$, modo más lento): Las masas oscilan principalmente en la misma dirección (oscilación "en fase")
- **Modo 2** ($\omega_2$, modo más rápido): Las masas oscilan en direcciones opuestas (oscilación "en contrafase")

---

## 5. Solución General del Sistema

### Superposición de Modos

Como el sistema es lineal, la solución general es una combinación lineal de las soluciones individuales correspondientes a cada modo normal. Para el caso con velocidades iniciales cero (condiciones iniciales más simples), la solución toma la forma:

$$y_1(t) = A_1 v_{1,1} \cos(\omega_1 t) + A_2 v_{2,1} \cos(\omega_2 t)$$

$$y_2(t) = A_1 v_{1,2} \cos(\omega_1 t) + A_2 v_{2,2} \cos(\omega_2 t)$$

Donde:
- $A_1, A_2$ son las **amplitudes de cada modo**
- $v_{i,j}$ son las componentes del $i$-ésimo vector propio
- $\omega_1, \omega_2$ son las frecuencias naturales

### Forma Vectorial

En forma vectorial más compacta:

$$\mathbf{y}(t) = A_1 \mathbf{v}_1 \cos(\omega_1 t) + A_2 \mathbf{v}_2 \cos(\omega_2 t)$$

### Solución General Completa (con Fases)

Para el caso más general con velocidades iniciales arbitrarias:

$$\mathbf{y}(t) = A_1 \mathbf{v}_1 \cos(\omega_1 t + \phi_1) + A_2 \mathbf{v}_2 \cos(\omega_2 t + \phi_2)$$

Donde $\phi_1$ y $\phi_2$ son las fases iniciales de cada modo.

---

## 6. Determinación de las Constantes de Integración

### Aplicación de Condiciones Iniciales

Las constantes $A_1, A_2, \phi_1, \phi_2$ se determinan a partir de las condiciones iniciales en $t = 0$:

$$y_1(0) = y_{1,0}, \quad y_2(0) = y_{2,0}, \quad \dot{y}_1(0) = v_{1,0}, \quad \dot{y}_2(0) = v_{2,0}$$

### Caso Especial: Velocidades Iniciales Nulas

Si $v_{1,0} = v_{2,0} = 0$, la solución se simplifica a:

$$y_1(t) = A_1 v_{1,1} \cos(\omega_1 t) + A_2 v_{2,1} \cos(\omega_2 t)$$

$$y_2(t) = A_1 v_{1,2} \cos(\omega_1 t) + A_2 v_{2,2} \cos(\omega_2 t)$$

En este caso, las amplitudes se obtienen de las condiciones iniciales de posición:

$$y_{1,0} = A_1 v_{1,1} + A_2 v_{2,1} \quad \text{...(8)}$$

$$y_{2,0} = A_1 v_{1,2} + A_2 v_{2,2} \quad \text{...(9)}$$

En forma matricial:

$$\begin{pmatrix} v_{1,1} & v_{2,1} \\ v_{1,2} & v_{2,2} \end{pmatrix} \begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = \begin{pmatrix} y_{1,0} \\ y_{2,0} \end{pmatrix}$$

O:

$$\mathbf{V} \begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = \begin{pmatrix} y_{1,0} \\ y_{2,0} \end{pmatrix}$$

Resolviendo:

$$\begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = \mathbf{V}^{-1} \begin{pmatrix} y_{1,0} \\ y_{2,0} \end{pmatrix}$$

### Caso General: Velocidades Iniciales Arbitrarias

Para el caso con velocidades iniciales no nulas, tenemos un sistema de 4 ecuaciones con 4 incógnitas:

$$A_1 v_{1,1} \cos(\phi_1) + A_2 v_{2,1} \cos(\phi_2) = y_{1,0}$$

$$A_1 v_{1,2} \cos(\phi_1) + A_2 v_{2,2} \cos(\phi_2) = y_{2,0}$$

$$-A_1 \omega_1 v_{1,1} \sin(\phi_1) - A_2 \omega_2 v_{2,1} \sin(\phi_2) = v_{1,0}$$

$$-A_1 \omega_1 v_{1,2} \sin(\phi_1) - A_2 \omega_2 v_{2,2} \sin(\phi_2) = v_{2,0}$$

Este sistema se resuelve numéricamente para obtener $A_1, A_2, \phi_1, \phi_2$.

---

## 7. Ejemplo Numérico

### Parámetros del Sistema

Consideremos un caso concreto:
- $m_1 = 0.020$ kg
- $m_2 = 0.030$ kg
- $k_1 = 10.32$ N/m
- $k_2 = 10.32$ N/m

### Resultados Obtenidos

Resolviendo el problema de valores propios con los parámetros anteriores:

**Frecuencias naturales:**
$$\omega_1 \approx 12.0037 \text{ rad/s}$$
$$\omega_2 \approx 35.0986 \text{ rad/s}$$

**Vectores propios (modos normales):**
$$\mathbf{v}_1 = \begin{pmatrix} 1.0000 \\ 1.7208 \end{pmatrix} \quad \text{(modo en fase)}$$

$$\mathbf{v}_2 = \begin{pmatrix} 1.0000 \\ -0.3874 \end{pmatrix} \quad \text{(modo en contrafase)}$$

### Condiciones Iniciales Específicas

Supongamos:
- $y_{1,0} = 0$ m (masa 1 en equilibrio)
- $y_{2,0} = +0.055$ m (masa 2 jalada hacia abajo 5.5 cm)
- $v_{1,0} = 0$ m/s (velocidad inicial cero)
- $v_{2,0} = 0$ m/s (velocidad inicial cero)

**Nota:** Según nuestra convención, desplazamientos positivos corresponden a la dirección hacia abajo.

### Solución Particular

Determinando las amplitudes de cada modo con las condiciones iniciales dadas:

$$A_1 \approx 0.026089 \text{ m}$$
$$A_2 \approx -0.026089 \text{ m}$$

La solución particular para este caso es:

$$y_1(t) = 0.026089 \cos(12.0037t) - 0.026089 \cos(35.0986t)$$

$$y_2(t) = 0.044893 \cos(12.0037t) + 0.010107 \cos(35.0986t)$$

Esta solución describe la evolución temporal de las posiciones de ambas masas. Obsérvese que:
- La **amplitud positiva** $A_1 > 0$ en el modo 1 indica que la oscilación en fase domina inicialmente
- La masa 2 está dominada por el modo 1 (amplitud más grande: 0.044893 m), que representa ambas masas oscilando en fase
- El modo 2 (amplitud negativa $A_2 < 0$) contribuye con oscilaciones en contrafase para satisfacer la condición inicial
- Ambas masas oscilan periódicamente con la superposición de dos frecuencias naturales del sistema

---

## 8. Propiedades de la Solución

### Conservación de Energía

La solución satisface la conservación de energía mecánica. La energía total es:

$$E = \frac{1}{2}m_1\dot{y}_1^2 + \frac{1}{2}m_2\dot{y}_2^2 + \frac{1}{2}k_1 y_1^2 + \frac{1}{2}k_2(y_2-y_1)^2$$

Esta energía permanece constante durante todo el movimiento.

### Ortogonalidad de Modos

Los vectores propios correspondientes a diferentes frecuencias naturales satisfacen una relación de ortogonalidad con respecto a las matrices de masa y rigidez:

$$\mathbf{v}_i^T \mathbf{M} \mathbf{v}_j = 0 \quad \text{si } i \neq j$$

$$\mathbf{v}_i^T \mathbf{K} \mathbf{v}_j = 0 \quad \text{si } i \neq j$$

Esto justifica la descomposición en modos normales.

### Estabilidad

Como todas las frecuencias naturales son reales y positivas ($\omega_i > 0$), el sistema es estable. Las oscilaciones continúan indefinidamente sin crecer o amortiguarse (en la idealización sin fricción).

---

## Conclusión

La solución analítica del sistema de dos masas y dos resortes colgantes muestra cómo:

1. **La estructura matricial** del sistema dinámico revela el acoplamiento entre los grados de libertad
2. **Los valores propios** dan las frecuencias naturales del sistema
3. **Los vectores propios** describen los patrones de movimiento (modos)
4. **La superposición de modos** permite expresar cualquier movimiento como combinación de oscilaciones armónicas simples
5. **Las condiciones iniciales** determinan completamente la amplitud y fase de cada modo

Este enfoque es fundamental en ingeniería para el análisis de vibraciones, diseño de estructuras y control de sistemas dinámicos.
