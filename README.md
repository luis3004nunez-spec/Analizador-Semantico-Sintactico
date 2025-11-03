# Analizador Sintáctico y Semántico con Verificación de Tipos  
### Lenguaje MiniLang – Proyecto de Compiladores

---

## Descripción

Este proyecto implementa un **Analizador Sintáctico y Semántico** utilizando **Python** y la librería **PLY (Python Lex-Yacc)**.  
El lenguaje diseñado, denominado **MiniLang**, permite realizar operaciones aritméticas, asignaciones y concatenaciones de cadenas con **verificación de tipos**, controlando errores semánticos como:

- Uso de variables no definidas  
- Operaciones inválidas entre tipos  
- División por cero  
- Conversión implícita entre tipos numéricos  

El analizador muestra mensajes claros y educativos, pensados para comprender mejor las etapas del proceso de compilación.

---

## Autor

**Nombre:** Luis E. Nuñez  
**Matrícula:** 1-08-1958  
**Materia:** Compiladores  
**Universidad:** Universidad Tecnológica de Santiago (UTESA)

---

## Objetivos del Proyecto

- Aplicar los conceptos del **Capítulo 5: Análisis Sintáctico** del libro *Compiladores: Principios, Técnicas y Herramientas*.  
- Desarrollar un **analizador sintáctico** que detecte errores estructurales del lenguaje.  
- Implementar un **analizador semántico** que valide tipos y expresiones.  
- Simular el comportamiento de un compilador básico para propósitos académicos.

---
## === Luis E Nunez--1081958 - Analizador Sintáctico y Semántico ===
## Escribe una sentencia o presiona Ctrl+Z (Windows) o Ctrl+D (Linux) para salir.

MiniLang > a = 10;
Asignado: a = 10 (int)

MiniLang > b = 5.5;
Asignado: b = 5.5 (float)

MiniLang > c = a + b;
Advertencia: conversión implícita entre int y float
Asignado: c = 15.5 (float)

MiniLang > mensaje = "Resultado:";
Asignado: mensaje = Resultado: (string)

MiniLang > resultado = mensaje + " Exitoso!";
Asignado: resultado = Resultado: Exitoso! (string)


---
## Requisitos

- **Python 3.8 o superior**  
- Librería **PLY** (Python Lex-Yacc)

Instalación de PLY:
```bash
pip install ply


