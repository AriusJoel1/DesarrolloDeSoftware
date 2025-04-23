# src/belly.py

class Belly:
    def __init__(self, clock_service=None):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.clock_service = clock_service or self.get_current_time  # Usamos el reloj del sistema si no pasamos uno

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        print(f"He comido {pepinos} pepinos.")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        # Verificar que ambas condiciones se cumplan correctamente:
        # Se han esperado al menos 1.5 horas Y se han comido más de 10 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False

    # Simulación del tiempo actual (si no hay un servicio de reloj)
    def get_current_time(self):
        import time
        return time.time()
