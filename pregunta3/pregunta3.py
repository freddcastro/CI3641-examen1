class Programa:
    """
    Clase que representa un programa con un nombre y un lenguaje de programación.

    Atributos:
    ----------
    nombre : str
        El nombre del programa.
    lenguaje : str
        El lenguaje de programación utilizado en el programa. Debe ser alfanumérico.
    """

    def __init__(self, nombre, lenguaje):
        if not lenguaje.isalnum():
            raise ValueError("el lenguaje debe ser alfanumérico")
        self.nombre = nombre
        self.lenguaje = lenguaje


class Interprete:
    """
    Clase que representa a un intérprete para <lenguaje> escrito en <lenguaje_base>.

    Atributos:
    ----------
    lenguaje_base : str
       El lenguaje en el cual está escrito el traductor.
    lenguaje : str
        El lenguaje objetivo.

    """

    def __init__(self, lenguaje_base, lenguaje):
        if not lenguaje_base.isalnum() or not lenguaje.isalnum():
            raise ValueError(
                "los lenguajes ingresados deben ser alfanuméricos")
        self.lenguaje_base = lenguaje_base
        self.lenguaje = lenguaje


class Traductor:
    """
    Clase Traductor que representa a un traductor, desde <lenguaje_origen> hacia <lenguaje_destino>,
    escrito en <lenguaje_base>.

    Atributos:
    ----------
    lenguaje_base : str
        El lenguaje en el cual está escrito el traductor.
    lenguaje_origen : str
        El lenguaje de origen desde el cual se traducirá.
    lenguaje_destino : str
        El lenguaje de destino al cual se traducirá.

    """

    def __init__(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
        if not lenguaje_base.isalnum() or not lenguaje_origen.isalnum() or not lenguaje_destino.isalnum():
            raise ValueError(
                "los lenguajes ingresados deben ser alfanuméricos")
        self.lenguaje_base = lenguaje_base
        self.lenguaje_origen = lenguaje_origen
        self.lenguaje_destino = lenguaje_destino


class Simulador:
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase.

        Atributos:
            programas (dict): Un diccionario para almacenar programas.
            interpretadores (dict): Un diccionario para almacenar interpretadores.
            traductores (dict): Un diccionario para almacenar traductores.
            lenguaje_local (str): Una cadena que representa el lenguaje local, por defecto "LOCAL".
        """
        self.programas = {}
        self.interpretadores = {}
        self.traductores = {}
        self.lenguaje_local = "LOCAL"

    def define(self, tipo, argumentos):
        """
        Define un nuevo programa, intérprete o traductor basado en el tipo especificado.

        Parámetros:
        tipo (str): El tipo de entidad a definir. Puede ser "PROGRAMA", "INTERPRETE" o "TRADUCTOR".
        argumentos (list): Lista de argumentos necesarios para definir la entidad.
            - Para "PROGRAMA": [nombre_programa, ruta_ejecutable]
            - Para "INTERPRETE": [nombre_interprete, lenguaje]
            - Para "TRADUCTOR": [nombre_traductor, lenguaje_origen, lenguaje_destino]

        Comportamiento:
        - Si el tipo es "PROGRAMA", se define un nuevo programa con el nombre y la ruta del ejecutable especificados.
        - Si el tipo es "INTERPRETE", se define un nuevo intérprete para el lenguaje especificado.
        - Si el tipo es "TRADUCTOR", se define un nuevo traductor del lenguaje de origen al lenguaje de destino especificados.
        - Si el tipo no es válido, se imprime un mensaje de error.

        Retorna:
        None
        """
        if argumentos[0] in self.programas:
            print(f"Error: El programa de nombre '{argumentos[0]}' ya existe.")
            return
        if tipo.upper() == "PROGRAMA":
            self.programas[argumentos[0]] = Programa(
                argumentos[0], argumentos[1])
            print(
                f"Se definió el programa '{argumentos[0]}', ejecutable en '{argumentos[1]}'.")
        elif tipo.upper() == "INTERPRETE":
            self.interpretadores[argumentos[1]] = Interprete(
                argumentos[0], argumentos[1])
            print(
                f"Se definió un intérprete para '{argumentos[1]}' escrito en '{argumentos[0]}'.")
        elif tipo.upper() == "TRADUCTOR":
            self.traductores[argumentos[1]] = Traductor(
                argumentos[0], argumentos[1], argumentos[2])
            print(
                f"Se definió un traductor de '{argumentos[1]}' a '{argumentos[2]}', escrito en '{argumentos[0]}'.")
        else:
            print(f"Error: Tipo inválido '{tipo}'.")

    def interpretador_es_ejecutable(self, lenguaje):
        """
        Verifica si un intérprete para un lenguaje dado es ejecutable en el lenguaje local.

        Args:
            lenguaje (str): El lenguaje para el cual se desea verificar si el intérprete es ejecutable.

        Returns:
            bool: True si el intérprete es ejecutable en el lenguaje local, False en caso contrario.

        El método realiza una búsqueda recursiva en la estructura de intérpretes para determinar si el 
        lenguaje base del intérprete coincide con el lenguaje local.
        """
        if lenguaje in self.interpretadores:
            if self.interpretadores[lenguaje].lenguaje_base.strip() == self.lenguaje_local:
                return True
            else:
                return self.interpretador_es_ejecutable(
                    self.interpretadores[lenguaje].lenguaje_base)
        else:
            if lenguaje.strip() == self.lenguaje_local:
                return True
            else:
                return False

    def traductor_es_ejecutable(self, lenguaje):
        """
        Verifica si un traductor para un lenguaje dado es ejecutable.

        Este método comprueba si el lenguaje especificado tiene un traductor
        registrado y si tanto el lenguaje base como el lenguaje destino del
        traductor son ejecutables. Si no es directamente ejecutable, busca
        recursivamente un traductor que sea ejecutable.

        Args:
            lenguaje (str): El lenguaje para el cual se desea verificar si 
                    el traductor es ejecutable.

        Returns:
            bool: True si el traductor es ejecutable, False en caso contrario.
        """
        if lenguaje in self.traductores:
            print("aca")
            print(self.interpretador_es_ejecutable(
                self.traductores[lenguaje].lenguaje_base))
            if self.interpretador_es_ejecutable(self.traductores[lenguaje].lenguaje_base) and self.interpretador_es_ejecutable(self.traductores[lenguaje].lenguaje_destino):
                return True
            else:
                # Si no existe, debemos buscar de forma recursiva un traductor que sea ejecutable.
                return self.traductor_es_ejecutable(self.traductores[lenguaje].lenguaje_base)
        else:
            return False

    def executable(self, nombre):
        """
        Determina si un programa puede ser ejecutado, basandose en su lenguaje y los interpretadores o traductores disponibles.

        Args:
            nombre (str): El nombre del programa a determinar su ejecutabilidad.

        Returns:
            None: Este método sólo imprime si el método es ejecutable o no.

        Prints:
            - "Si, es posible ejecutar el programa '{nombre}'." Si el programa puede ser ejecutado.
            - "No es posible ejecutar el programa '{nombre}'." Si el programa no puede ser ejecutado.
            - "Error: El programa de nombre '{nombre}' no existe." Si el programa no existe en la lista de programas.

        The method follows these steps:
            1. Verifica si el programa existe en la lista de programas.
            2. Si el programa existe, verifica si su lenguaje es el lenguaje local.
            3. Si el lenguaje no es el local, verifica si hay un interprete (o un conjunto de interpretes) disponible.
            4. Si no hay interpretador(es) disponibles, verifica si hay un traductor que cumple los siguientes puntos:
            - El traductor debe estar escrito en un lenguaje ejecutable.
            - El traductor debe llevar (o traducir) a un lenguaje ejecutable.
        """

        if nombre in self.programas:
            lenguaje = self.programas[nombre].lenguaje
            # Acá, debemos comprobar si el lenguaje es ejecutable.
            if lenguaje == self.lenguaje_local:
                print(
                    f"Si, es posible ejecutar el programa '{nombre}'.")
            else:
                # Si no está escrito en local, comprobamos si existe un intérprete (o un conjunto de intérpretes)
                # hacia ese lenguaje, desde local.
                if lenguaje in self.interpretadores:
                    if self.interpretador_es_ejecutable(lenguaje) is True:
                        print(
                            f"Si, es posible ejecutar el programa '{nombre}'.")
                    else:
                        print(
                            f"No es posible ejecutar el programa '{nombre}'.")
                else:
                    # """
                    # Ahora, si no existe un interpretador directo, o una cadena de interpretadores, debemos verificar que exista un
                    # traductor tal que:
                    # - El traductor debe estar escrito en un lenguaje ejecutable (osea, su lenguaje base debe ser ejecutable en local)
                    # - El traductor debe llevar a un lenguaje ejecutable (es decir, su lenguaje destino debe ser ejecutable en local)
                    # """

                    if lenguaje in self.traductores:
                        if self.traductor_es_ejecutable(lenguaje) is True:
                            print(
                                f"Si, es posible ejecutar el programa '{nombre}'.")
                        else:
                            print(
                                f"No es posible ejecutar el programa '{nombre}'.")

                    else:
                        print(
                            f"No es posible ejecutar el programa '{nombre}'.")
        else:
            print(f"Error: El programa de nombre '{nombre}' no existe.")

    def run(self):
        while True:
            data = input().split()
            if data[0].upper() == "DEFINIR":
                tipo, *argumentos = data[1:]
                self.define(tipo, argumentos)
            elif data[0].upper() == "EJECUTABLE":
                nombre = data[1]
                self.executable(nombre.strip())
            elif data[0] == "SALIR":
                break
            else:
                print("Accion inválida.")


if __name__ == "__main__":
    simulator = Simulador()
    simulator.run()
