

## Autor
**Angel de Jesus Robles Araque**

## Asignatura
**Lenguajes de Programacion y Transduccion**

## Profesor
**Joaquín Sánchez**

## Universidad
**Universidad Sergio Arboleda**

---

## Descripción general

Contiene la solucion a varios problemas relacionados con el diseño e implementación de estructuras de datos en Python, aplicadas a:

1. Un sistema de navegación tipo historial (goBack / goForward).
2. Una funcion de autocompletado eficiente.
3. Un sistema de recomendación de productos basado en relaciones usuario-producto.

Cada problema incluye:
- Diseño conceptual
- Diagramas explicativos
- Implementacion en Python
- Explicacion del funcionamiento de los metodos

## Problema 1: Sistema de navegacion Web (Historial)

### Descripcion
Se implementa un sistema similar al historial de un navegador web, permitiendo:
- Visitar nuevas páginas
- Retroceder (`goBack`)
- Avanzar (`goForward`)

### Estructura utilizada
- Dos pilas (stacks):
  - Una para el historial anterior
  - Otra para el historial siguiente

### Conceptos aplicados
- Pilas
- Manejo de estados

## Problema 2: Funcion de Autocompletar

### Descripcion
Se desarrollo una función de autocompletar que, dado un prefijo, devuelve todas las palabras que comienzan con dicho prefijo, similar a los motores de busqueda.

### Estructura utilizada
- **(Arbol de prefijos)**

### Clases principales

#### Clase `TrieNode`
Representa un nodo del Trie.
- Contiene:
  - Un diccionario de hijos
  - Un indicador de fin de palabra

#### Clase `Trie`
Encapsula toda la logica del autocompletado.

### Métodos principales

- `insert(word)`  
  Inserta una palabra en el Trie caracter por caracter.

- `autocomplete(prefix)`  
  Devuelve todas las palabras almacenadas que comienzan con el prefijo dado.

## Problema 3: Sistema de Recomendación de Productos

### Descripcion
Se implemento un sistema de recomendacion basado en el principio:
> "Los usuarios que compraron X también compraron Y"

El sistema analiza las compras realizadas por los usuarios y recomienda productos adquiridos por otros usuarios con intereses similares.

### Estructuras utilizadas
- Diccionarios
- Conjuntos (sets)

### Estructura interna

- `user_products`:  
  Relacion usuario → productos comprados

- `product_users`:  
  Relacion producto → usuarios que lo compraron

---

### Metodos principales

#### `addPurchase(usuario, producto)`
Registra una compra:
- Agrega el producto al conjunto del usuario
- Agrega el usuario al conjunto del producto

#### `getRecommendations(usuario)`
- Busca productos comprados por otros usuarios relacionados
- Excluye los productos que el usuario ya compro
- Devuelve una lista de recomendaciones unicas


print(rs.getRecommendations("Santiago"))

