class Automata:
    def __init__(self, estados=None, alfabeto=None, estado_inicial=None, estados_aceptacion=None, transiciones=None):
        """
        Representación de un Autómata Finito.
        - estados (Q): set de nombres de estados (ej. {'q0', 'q1'})
        - alfabeto (Sigma): set de símbolos (ej. {'0', '1'})
        - estado_inicial (q0): str (ej. 'q0')
        - estados_aceptacion (F): set de estados de aceptación (ej. {'q1'})
        - transiciones (delta): dict de la forma {(origen, simbolo): {destino1, destino2, ...}}
        """
        self.estados = set(estados) if estados else set()
        self.alfabeto = set(alfabeto) if alfabeto else set()
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = set(estados_aceptacion) if estados_aceptacion else set()
        self.transiciones = transiciones if transiciones is not None else {}

    def agregar_estado(self, estado, es_inicial=False, es_aceptacion=False):
        """Añade un estado al autómata."""
        self.estados.add(estado)
        if es_inicial:
            self.estado_inicial = estado
        if es_aceptacion:
            self.estados_aceptacion.add(estado)

    def agregar_transicion(self, origen, simbolo, destino):
        """
        Añade una transición delta(origen, simbolo) -> destino.
        Soporta AFN al guardar los destinos en un conjunto (set).
        """
        if origen not in self.estados or destino not in self.estados:
            raise ValueError("Los estados de origen y destino deben existir en el autómata.")
        if simbolo != 'λ' and simbolo != '' and simbolo not in self.alfabeto:
            raise ValueError(f"El símbolo '{simbolo}' no pertenece al alfabeto.")

        clave = (origen, simbolo)
        if clave not in self.transiciones:
            self.transiciones[clave] = set()
        self.transiciones[clave].add(destino)

    def obtener_transicion(self, origen, simbolo):
        """Retorna el conjunto de estados destino para un origen y símbolo dados."""
        return self.transiciones.get((origen, simbolo), set())

    def es_afn(self):
        """Determina si el autómata es no determinista (AFN o AFN-λ)."""
        for (origen, simbolo), destinos in self.transiciones.items():
            if simbolo in ('λ', '') or len(destinos) > 1:
                return True
        return False