"""
Simulación de un sistema de 2 masas y 2 resortes posicionados verticalmente.

El sistema está configurado como:
- Resorte 1 → Masa 1 → Resorte 2 → Masa 2
- El resorte 1 está fijo en la parte superior
- Las masas se mueven verticalmente bajo la influencia de la gravedad y los resortes

Ecuaciones de movimiento:
m1 * x1'' = -k1 * (x1 - L1) + k2 * (x2 - x1 - L2) + m1 * g
m2 * x2'' = -k2 * (x2 - x1 - L2) + m2 * g

donde:
- x1, x2: posiciones de las masas (positivo hacia abajo)
- L1, L2: longitudes naturales de los resortes
- k1, k2: constantes de elasticidad
- m1, m2: masas
- g: aceleración gravitacional
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class SistemaMasaResorte:
    """Clase para simular un sistema de 2 masas y 2 resortes vertical."""
    
    def __init__(self, m1, m2, k1, k2, L1, L2, g=9.8):
        """
        Inicializa el sistema.
        
        Parameters
        ----------
        m1 : float
            Masa 1 (kg)
        m2 : float
            Masa 2 (kg)
        k1 : float
            Constante de elasticidad resorte 1 (N/m)
        k2 : float
            Constante de elasticidad resorte 2 (N/m)
        L1 : float
            Longitud natural resorte 1 (m)
        L2 : float
            Longitud natural resorte 2 (m)
        g : float, optional
            Aceleración gravitacional (m/s²), default es 9.8
        """
        self.m1 = m1
        self.m2 = m2
        self.k1 = k1
        self.k2 = k2
        self.L1 = L1
        self.L2 = L2
        self.g = g
        
    def ecuaciones(self, y, t):
        """
        Define el sistema de ecuaciones diferenciales de primer orden.
        
        Parameters
        ----------
        y : array
            Vector de estado [x1, v1, x2, v2]
            x1, x2: posiciones
            v1, v2: velocidades
        t : float
            Tiempo
            
        Returns
        -------
        dydt : array
            Derivadas [dx1/dt, dv1/dt, dx2/dt, dv2/dt]
        """
        x1, v1, x2, v2 = y
        
        # Fuerzas en masa 1
        # Fuerza del resorte 1 (hacia arriba si estirado)
        F_resorte1 = -self.k1 * (x1 - self.L1)
        # Fuerza del resorte 2 (hacia abajo si x2 > x1 + L2)
        F_resorte2 = self.k2 * (x2 - x1 - self.L2)
        # Fuerza gravitacional (hacia abajo)
        F_gravedad1 = self.m1 * self.g
        
        # Aceleración masa 1
        a1 = (F_resorte1 + F_resorte2 + F_gravedad1) / self.m1
        
        # Fuerzas en masa 2
        # Fuerza del resorte 2 (hacia arriba si se comprime)
        F_resorte2_m2 = -self.k2 * (x2 - x1 - self.L2)
        # Fuerza gravitacional (hacia abajo)
        F_gravedad2 = self.m2 * self.g
        
        # Aceleración masa 2
        a2 = (F_resorte2_m2 + F_gravedad2) / self.m2
        
        return [v1, a1, v2, a2]
    
    def encontrar_equilibrio(self):
        """
        Calcula las posiciones de equilibrio del sistema.
        
        Returns
        -------
        tuple
            (x1_eq, x2_eq): posiciones de equilibrio
        """
        # Equilibrio estático: 0 = -k1*(x1 - L1) + k2*(x2 - x1 - L2) + m1*g
        #                      0 = -k2*(x2 - x1 - L2) + m2*g
        
        # De la segunda ecuación: x2 - x1 - L2 = m2*g/k2
        # Entonces: x2 = x1 + L2 + m2*g/k2
        
        # Sustituyendo en la primera:
        # -k1*(x1 - L1) + m2*g + m1*g = 0
        # x1 = L1 + (m1 + m2)*g/k1
        
        x1_eq = self.L1 + (self.m1 + self.m2) * self.g / self.k1
        x2_eq = x1_eq + self.L2 + self.m2 * self.g / self.k2
        
        return x1_eq, x2_eq
    
    def simular(self, condiciones_iniciales, t_inicial=0, t_final=10, num_puntos=1000):
        """
        Simula el sistema usando condiciones iniciales.
        
        Parameters
        ----------
        condiciones_iniciales : tuple
            (x1_0, v1_0, x2_0, v2_0) - posiciones y velocidades iniciales
        t_inicial : float, optional
            Tiempo inicial (default: 0)
        t_final : float, optional
            Tiempo final (default: 10 segundos)
        num_puntos : int, optional
            Número de puntos de evaluación (default: 1000)
            
        Returns
        -------
        tuple
            (t, x1, v1, x2, v2) - arrays de tiempo y soluciones
        """
        t = np.linspace(t_inicial, t_final, num_puntos)
        solucion = odeint(self.ecuaciones, condiciones_iniciales, t)
        
        x1 = solucion[:, 0]
        v1 = solucion[:, 1]
        x2 = solucion[:, 2]
        v2 = solucion[:, 3]
        
        return t, x1, v1, x2, v2
    
    def graficar_resultado(self, t, x1, v1, x2, v2, x1_eq=None, x2_eq=None):
        """
        Grafica los resultados de la simulación.
        
        Parameters
        ----------
        t : array
            Array de tiempos
        x1, v1, x2, v2 : array
            Posiciones y velocidades
        x1_eq, x2_eq : float, optional
            Posiciones de equilibrio para referencia
        """
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))
        
        # Posición masa 1
        axes[0, 0].plot(t, x1, 'b-', linewidth=2, label='Masa 1')
        if x1_eq is not None:
            axes[0, 0].axhline(y=x1_eq, color='r', linestyle='--', 
                              label=f'Equilibrio ({x1_eq:.3f} m)')
        axes[0, 0].set_xlabel('Tiempo (s)')
        axes[0, 0].set_ylabel('Posición (m)')
        axes[0, 0].set_title('Posición de Masa 1')
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].legend()
        
        # Velocidad masa 1
        axes[0, 1].plot(t, v1, 'g-', linewidth=2)
        axes[0, 1].axhline(y=0, color='k', linestyle='-', alpha=0.3)
        axes[0, 1].set_xlabel('Tiempo (s)')
        axes[0, 1].set_ylabel('Velocidad (m/s)')
        axes[0, 1].set_title('Velocidad de Masa 1')
        axes[0, 1].grid(True, alpha=0.3)
        
        # Posición masa 2
        axes[1, 0].plot(t, x2, 'b-', linewidth=2, label='Masa 2')
        if x2_eq is not None:
            axes[1, 0].axhline(y=x2_eq, color='r', linestyle='--',
                              label=f'Equilibrio ({x2_eq:.3f} m)')
        axes[1, 0].set_xlabel('Tiempo (s)')
        axes[1, 0].set_ylabel('Posición (m)')
        axes[1, 0].set_title('Posición de Masa 2')
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].legend()
        
        # Velocidad masa 2
        axes[1, 1].plot(t, v2, 'g-', linewidth=2)
        axes[1, 1].axhline(y=0, color='k', linestyle='-', alpha=0.3)
        axes[1, 1].set_xlabel('Tiempo (s)')
        axes[1, 1].set_ylabel('Velocidad (m/s)')
        axes[1, 1].set_title('Velocidad de Masa 2')
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig


# Ejemplo de uso
if __name__ == "__main__":
    print("=" * 60)
    print("SIMULACIÓN DE SISTEMA MASA-RESORTE (2 MASAS, 2 RESORTES)")
    print("=" * 60)
    
    # Parámetros del sistema
    m1 = 1.0      # kg
    m2 = 2.0      # kg
    k1 = 100.0    # N/m
    k2 = 50.0     # N/m
    L1 = 0.1      # m (longitud natural resorte 1)
    L2 = 0.15     # m (longitud natural resorte 2)
    g = 9.8       # m/s²
    
    print(f"\nParámetros del sistema:")
    print(f"  Masa 1 (m1): {m1} kg")
    print(f"  Masa 2 (m2): {m2} kg")
    print(f"  Constante resorte 1 (k1): {k1} N/m")
    print(f"  Constante resorte 2 (k2): {k2} N/m")
    print(f"  Longitud natural resorte 1 (L1): {L1} m")
    print(f"  Longitud natural resorte 2 (L2): {L2} m")
    print(f"  Gravedad (g): {g} m/s²")
    
    # Crear sistema
    sistema = SistemaMasaResorte(m1, m2, k1, k2, L1, L2, g)
    
    # Calcular equilibrio
    x1_eq, x2_eq = sistema.encontrar_equilibrio()
    print(f"\nPosiciones de equilibrio:")
    print(f"  Masa 1 en equilibrio: {x1_eq:.4f} m")
    print(f"  Masa 2 en equilibrio: {x2_eq:.4f} m")
    
    # Condiciones iniciales: pequeña perturbación desde el equilibrio
    x1_0 = x1_eq + 0.05      # Desplazamiento inicial +5 cm en masa 1
    v1_0 = 0.0               # Velocidad inicial nula
    x2_0 = x2_eq + 0.03      # Desplazamiento inicial +3 cm en masa 2
    v2_0 = 0.0               # Velocidad inicial nula
    
    print(f"\nCondiciones iniciales:")
    print(f"  Posición inicial masa 1: {x1_0:.4f} m")
    print(f"  Posición inicial masa 2: {x2_0:.4f} m")
    print(f"  Velocidades iniciales: 0 m/s")
    
    # Simular
    print(f"\nSimulando durante 10 segundos...")
    t, x1, v1, x2, v2 = sistema.simular(
        (x1_0, v1_0, x2_0, v2_0),
        t_inicial=0,
        t_final=10,
        num_puntos=1000
    )
    print("✓ Simulación completada")
    
    # Graficar
    print("\nGenerando gráficos...")
    fig = sistema.graficar_resultado(t, x1, v1, x2, v2, x1_eq, x2_eq)
    plt.savefig('simulacion_masa_resorte.png', dpi=150, bbox_inches='tight')
    print("✓ Gráficos guardados en 'simulacion_masa_resorte.png'")
    
    plt.show()
