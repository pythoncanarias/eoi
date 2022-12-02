#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sqlite3



inicios = [
    "Estudiar sobre",
    "Leer un artículo sobre",
    "Leer un libro sobre",
    "Ver un vídeo acerca de",
    "Oir un podcast que hable de",
    "Entender el concepto de",
    "Escribir una nota sobre lo que sé de",
    "Preguntar a alguien que sepa de",
    "Dibujar un diagrama explicando",
]


finales = [
    "desarrollo web",
    "protocolo HTTP",
    "lenguaje HTML 5",
    "hojas de estilo en cacada CSS",
    "Django",
    "Flask",
    "Python",
    "SQL",
    "exportación e importación de datos",
    "procesadores",
    "sistemas en la nube",
    "programación asíncrona",
    "modelos Django",
    "microservicios",
    "Javascript",
    "bases de datos",
    "modelo vista/modelo/controlador",
    "modelos Entidad/Relación",
    "copias de seguridad",
    "el concepto de vista",
    "las vistas basadas en clases (CBV)",
    "el sistema de herencias de las plantillas",
]


def random_project():
    if random.random() >= 0.5:
        return None
    db = sqlite3.connect('db.sqlite3')
    cur = db.cursor()
    try:
        cur.execute('Select id from task_project')
        return random.choice([
            row[0] for row in cur.fetchall()
        ])
    finally:
        cur.close()


def random_priority():
    return random.choices(
        ['L', 'N', 'H'],
        weights=[1, 4, 2],
        )


def random_name():
    inicio = random.choice(inicios)
    final = random.choice(finales)
    return f"{inicio} {final}"


def nueva_tarea():
    name = random_name()
    priority = random_priority()
    orden = random.choice(range(100))
    id_project = random_project()
    print(
        f'Crear tarea "{name}"',
        f'prioridad {priority}',
        f'orden {orden}',
        f'proyecto {id_project}',
        sep=", "
    )


def main():
    for _ in range(20):
        print(nueva_tarea())


if __name__ == "__main__":
    main()
