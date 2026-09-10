# DIBUJO PARA INGENIERÍA

## UNIDAD 3. Ensambles 3D y elaboración de planos

### Datos generales de la unidad

| Concepto | Valor |
|---|---|
| Horas del Saber | 7 |
| Horas del Saber Hacer | 16 |
| Horas Totales | 23 |

**Propósito esperado:** El estudiante desarrollará modelos 3D complejos mediante el ensamble de piezas y elaborará planos de taller normalizados a partir del modelo, que describan las características de sistemas mecatrónicos y robóticos.

## 1. Temario de la unidad (alineado al programa de la asignatura)

| # | Tema | Saber | Saber hacer | Ser y convivir |
|---|---|---|---|---|
| 1 | Construcción de Ensambles | Identificar los conceptos y técnicas relacionados con la construcción de ensambles: añadir piezas a un ensamble, relaciones de posición básicas, inserción de sub-ensambles, creación de un sistema de coordenadas para realizar un análisis de propiedades físicas, comandos respectivos del software dedicado. | Realizar ensambles de piezas considerando los diversos tipos de relaciones de posición básicas: coincidentes, paralelo, perpendicular, tangente, concéntrico, distancia y de ángulo, en el software dedicado de CAD. | Fortalecer la actitud crítica a través de la integración de piezas y mecanismos desarrollados individualmente. |
| 2 | Manipulación de Ensambles | Identificar los conceptos y técnicas relacionados con la manipulación de ensambles: relaciones de posición avanzada y mecánicas, reemplazo de una pieza por otra en un ensamble, realización de la detección de colisión cuando se mueva una pieza, detección de interferencias, vista explosionada de un ensamble, comandos respectivos del software dedicado. | Realizar ensambles de piezas considerando los diversos tipos de relaciones de posición avanzada y mecánicas: simétrica, posición de trayecto, distancia y ángulo límite, leva, ranura, bisagra y engranaje, que incluya detección de colisión, volumen de interferencias y vista explosionada de un ensamble. | Fortalecer el diálogo y la colaboración a través del trabajo en equipo para el desarrollo de proyectos de integración. |
| 3 | Creación de planos, vistas, dimensiones y anotaciones | Describir las características de una pieza o ensamble en 3D mediante la creación de planos en 2D: plantillas de planos, vistas de dibujo (principales, proyectadas, de sección, de detalle, rotura, posición alternativa, corte, isométricos y explosionada), acotación asociada, anotaciones para especificar información de fabricación, ensamble, listado de piezas y materiales (tablas y globos indicativos), control de versiones. | Elaborar planos usando las herramientas del software de CAD que incluya la descripción de las características de una pieza o ensamble contemplando: estándar de dibujo, unidades de acotación, nombre y logotipo de la empresa, nombre del autor, símbolo del sistema de proyección, escalas, número de hoja, vistas, acotación, anotaciones y control de versiones. | Fortalecer la actitud crítica y responsabilidad técnica en la elaboración de planos que permitan la fabricación de sistemas mecatrónicos y robóticos. |

## 2. Planeación sugerida del cuatrimestre (Unidad 3)

| Semana | Sesión Saber (7 h) | Sesión Saber Hacer (16 h) |
|---|---|---|
| 1-2 | Tema 1. Construcción de ensambles (1.1, 1.2, 1.3) | Ensambles con mates básicos: coincidente, paralelo, perpendicular, tangente, concéntrico, distancia, ángulo |
| 3-5 | Tema 2. Manipulación de ensambles (2.1-2.4) | Mates avanzados/mecánicos, reemplazo, colisión e interferencias, vista explosionada |
| 6-8 | Tema 3. Planos, vistas y acotación (3.1-3.4) | Plano de pieza/ensamble: plantilla, vistas, acotación, lista de materiales, anotaciones y control de versiones |

---

# TEMA 1. Construcción de Ensambles

## 1.1 Añadir piezas a un ensamble y relaciones de posición básicas

Un **ensamble** es un documento que integra varias piezas (y sub-ensambles) con **relaciones de posición (mates)** que definen cómo interactúan para formar el mecanismo. En SolidWorks el archivo de ensamble tiene extensión `.sldasm`.

### 1.1.1 Añadir piezas

| Método | Cómo |
|---|---|
| Insertar pieza existente | pestaña **Assembly > Insert Components** → se seleccionan piezas ya guardadas |
| Pieza en contexto | Insertar nueva pieza referenciando el ensamble (diseño top-down) |
| Biblioteca | Arrastrar piezas estándar (tornillos, rodamientos) desde la Toolbox |
| Sub-ensamble | Insertar archivos `.sldasm` ya creados (ver 1.2) |

**Reglas básicas:** la primera pieza que se inserta suele **fijarse** (F) para servir de base; las demás se colocan con mates (relaciones de posición).

### 1.1.2 Relaciones de posición básicas (predefinidas)

| Mate | Efecto | Ejemplo |
|---|---|---|
| Coincidente (Coincident) | Dos caras/planos/ejes quedan en el mismo plano o punto | Cara del eje contra cara del cojinete |
| Paralelo (Parallel) | Dos caras/ejes quedan paralelos | Guías paralelas |
| Perpendicular (Perpendicular) | Caras/ejes a 90° | Base del soporte horizontal |
| Tangente (Tangent) | Superficies se tocan sin penetrar | Rueda contra la superficie de apoyo |
| Concéntrico (Concentric) | Dos ejes/cilindros comparten el centro | Eje dentro del orificio |
| Distancia (Distance) | Separación fija entre caras/ejes | Separación entre dos placas |
| Ángulo (Angle) | Ángulo fijo entre caras/ejes | Posición angular de una manivela |

### 1.1.3 Procedimiento de ensamble con mates básicos

1. **Insertar** la pieza base y **fijarla** (contexto → Fix).
2. Insertar la siguiente pieza; elegir **Mate** (o Smart Mates al arrastrar planos).
3. Seleccionar las **caras/ejes** que se acoplan (por ejemplo, eje del perno y orificio).
4. Elegir el tipo de mate (**Coincident** para contacto, **Concentric** para centrar).
5. Definir los parámetros (distancia/ángulo si aplica) y **aceptar**.
6. Repetir hasta dejar el mecanismo con los **grados de libertad** intencionados (ej. una articulación giratoria: concéntrico + coincidente).

### 1.1.4 Grados de libertad

Cada mate **restringe movimientos** de la pieza. Un árbol bien hecho deja solo los grados de libertad que el mecanismo necesita:

| Mecanismo | Se permite | Mates resultantes |
|---|---|---|
| Articulación giratoria | Rotación en el eje | Concentric + Coincident |
| Corredera | Traslación en una dirección | Parallel + Coincident (dos caras) |
| Ensamble rígido | Ninguno | 6 grados restringidos (2 coincidentes + concentric) |

## 1.2 Inserción de sub-ensambles

Un **sub-ensamble** es un ensamble contenido dentro de otro; estructura al proyecto en conjuntos de nivel (tópico del producto).

### 1.2.1 Concepto y ventajas

| Ventaja | Descripción |
|---|---|
| Estructura | Organiza el árbol del producto por módulos |
| Eficiencia | Menos mates por nivel; el sub-ensamble se maneja como una pieza |
| Colaboración | Se monta por subconjuntos en equipos distintos |
| Sustitución | Permite planos de sustitución según la lógica del nivel |

### 1.2.2 Cómo insertar un sub-ensamble

1. Crear primero el sub-ensamble `.sldasm` con sus propios mates (ej. "mordaza_ensamblada").
2. En el ensamble superior: **Insert Components** → seleccionar el `.sldasm`.
3. Aplicar mates del ensamble superior contra el sub-ensamble como si fuera una pieza.
4. Definir si el sub-ensamble entra **rígido** o **flexible** (Flexible permite que sus mates internos se muevan).

### 1.2.3 Momento de uso

- Cuando la pieza es un **módulo repetible** (mordaza, pinza, eje-motor).
- Cuando el conjunto **supera 20-30 componentes**, por orden.
- Cuando se requiere **sustituir** una versión del módulo sin tocar el resto.

## 1.3 Sistema de coordenadas y análisis de propiedades físicas

### 1.3.1 Sistemas de coordenadas en el ensamble

| Referencia | Uso |
|---|---|
| Origen del ensamble | Referencia global del producto |
| Sistemas de coordenadas de piezas | Participan en mates y análisis (mecanismo de robots: local) |
| Ejes/planos de referencia | Guías para mates, operaciones y vistas |

### 1.3.2 Creación de un sistema de coordenadas

1. Insertar planos/ejes de referencia o usar el origen del ensamble.
2. Crear **coordinate system** (Reference Geometry > Coordinate System) clara del conjunto: origen, eje X/Y/Z.
3. Nombrarlo de forma significativa (ej. "CSYS_MontajeNivel0").

### 1.3.3 Análisis de propiedades físicas del ensamble

Con **Evaluate > Mass Properties** sobre el ensamble se obtiene:

| Propiedad | Qué reporta |
|---|---|
| Total volume | Volumen combinado de todos los cuerpos |
| Total mass | Masa combinada (considerando cada material) |
| Center of mass | Ubicación del centro de gravedad del conjunto |
| Moments / products of inertia | Inercia para mover el mecanismo |

**Aplicaciones:** balanceo de robótica (CG dentro de la base), selección de actuadores (peso total), peso para transporte y para estructuras de soporte.

---

# TEMA 2. Manipulación de Ensambles

## 2.1 Relaciones de posición avanzadas y mecánicas

Los **mates mecánicos y avanzados** conectan el movimiento entre piezas, típico de mecanismos.

### 2.1.1 Mates avanzados

| Mate | Efecto | Ejemplo |
|---|---|---|
| Simétrica (Symmetry) | Dos piezas quedan simétricas respecto a un plano del ensamble | Mitades de una carcasa, espejos de soporte |
| Posición de trayecto (Path) | Un punto de la pieza sigue una trayectoria (camino) | Seguidor sobre leva, corredera de riel |
| Distancia límite (LimitDistance) | La separación se mueve dentro de un rango | Recorrido de un pistón con tope |
| Ángulo límite (LimitAngle) | El ángulo oscila entre dos límites | Giro de brazo entre 0° y 90° |
| Amplio rango (Width) | Centra a una pieza dentro de dos caras | Rueda centrada entre dos paredes |

### 2.1.2 Mates mecánicos

| Mate | Conecta | Aplicación |
|---|---|---|
| Leva (Cam) | Cara de leva + cara del seguidor | Excéntricas y seguimiento de levas |
| Ranura (Slot) | Eje cilíndrico deslizando en una ranura | Guías ranuradas, acoplamientos |
| Bisagra (Hinge) | Dos cilindros concéntricos con traslación limitada | Puertas, trampillas |
| Engranaje (Gear) | Dos ejes/cilindros con relación de velocidad | Transmisiones, reductores |
| Huella (Screw) | Avance según rotación | Tornillos sin fin, acoplamientos roscados |
| Universal | Dos ejes (cardan) | Transmisión cardánica |

### 2.1.3 Aplicación práctica

1. **Leva + seguidor:** crear mate **Path/Limit** para el seguidor y **Cam** entre la guía y la leva; se obtiene movimiento periódico.
2. **Piñón-corona:** mate **Gear** seleccionando los dos cilindros y escribiendo la **relación** de dientes; al girar uno, el otro rota proporcional.
3. **Puerta:** mate **Bisagra** (dos cilindros concéntricos) + superficie de tope para limitar el giro.

## 2.2 Reemplazo de una pieza por otra

### 2.2.1 Para qué sirve

- Probar **variantes** de diseño (material, espesor de pared) sin reconstruir el ensamble.
- Actualizar la pieza **revisada** (nueva versión) manteniendo los mates.
- Sustituir entre piezas de la misma familia (pernos de distinta longitud).

### 2.2.2 Procedimiento

| Método | Pasos |
|---|---|
| Replace (recomendado) | Seleccionar la pieza en el árbol → botón derecho **Replace Components** → elegir la nueva pieza (o la misma con otra configuración) |
| Manual | Quitar la pieza, insertar la nueva y reaplicar mates |

Con **Replace** los mates se remapean automáticamente si las caras/ejes coinciden; conviene revisar qué mates se perdieron.

### 2.2.3 Comprobaciones tras el reemplazo

- Reconstruir el ensamble (**Ctrl+B**) y buscar errores de mates.
- Revisar **interferencias** (2.3) con la nueva geometría.
- Recargar las **propiedades de masa** si cambió el material.

## 2.3 Detección de colisión e interferencias

### 2.3.1 Movimiento con detección de colisión

Al mover una pieza (arrastrar), **Move Component > Collision Detection** cancela el movimiento cuando dos piezas **tocarían**:

- Impide que **penetren** durante el arrastre (true without penetrating).
- Resalta en verde los **contactos**.
- Se usa para validar la cinemática del mecanismo mientras se mueve.

### 2.3.2 Análisis de interferencias

**Evaluate > Interference Detection** analiza todo el ensamble:

| Resultado | Significado |
|---|---|
| Volumen de interferencia | Región donde dos cuerpos se solapan (m³ o mm³) |
| Interferencias reportadas | Listas de pares de piezas que chocan |
| No se reporta | Geometría válida sin solapamiento |

**Pasos:** seleccionar el ensamble (o lista de piezas) → **Calculate** → revisar los pares en conflicto → editar la pieza o el mate para eliminarla → recalcular.

### 2.3.3 Dónde se aplica

- Antes de fabricar: garantizar que **ningún componente** penetra en otro.
- En robótica: descartar colisiones entre el brazo y el entorno previo a la programación.
- En ensambles móviles: asegurar el **recorrido libre** del mecanismo (colisión detection + límites de mates).

## 2.4 Vista explosionada de un ensamble

La **vista explosionada** separa visualmente las piezas, respetando las direcciones de extracción (ej: eje Z), manteniendo la posición original en las opciones de ensamble.

### 2.4.1 Concepto y utilidad

- Muestra el **orden y dirección de montaje** de cada componente.
- Estándar en **plano de conjunto** y en **manuales/instrucciones de armado**.
- Permite producir **animaciones de ensamble** (interpolando entre explodido y montado).

### 2.4.2 Comandos

| Comando | Función |
|---|---|
| Exploded View | Genera pasos de explosión (escoge piezas y dirección de desplazamiento) |
| Reorder steps | Ajusta el orden de la explosión |
| Animate collapse/explode | Reproduce el movimiento de ida y vuelta |
| Insert exploded view in drawing | Coloca una vista explosionada en el plano (U3, vista de dibujo) |

### 2.4.3 Procedimiento

1. **Assembly > Exploded View**.
2. Seleccionar las **piezas** y la **dirección** (una arista/eje del ensamble).
3. Ajustar **distancia** de separación por paso (o arrastrar con doble flecha).
4. Añadir más pasos para el siguiente grupo; **reordenar** para reflejar la secuencia real de montaje.
5. Guardar la vista (aparece en el FeatureManager como *Exploded View*); al terminar, usarla en animación o plano.

---

# TEMA 3. Creación de planos, vistas, dimensiones y anotaciones

## 3.1 Plantillas de planos

La **plantilla de plano** define el formato de la hoja y el punto de partida de todo dibujo de taller.

### 3.1.1 Elementos que define la plantilla

| Elemento | Qué se configura |
|---|---|
| Tamaño de hoja | Formato ISO (A0-A4) o ANSI (A-E); orientación horizontal/vertical |
| Estándar de dibujo | ISO o ASME (influye en líneas, acotación, símbolos) |
| Unidades | milímetros o pulgadas; precisión (2 decimales típico) |
| Cajetín / rotulado | Nombre de la empresa, logotipo, nombre y número del plano, autor, fecha, material |
| Símbolo de proyección | Primer ángulo (ISO) o tercer ángulo (ASME) |
| Escala | Escala base de las vistas (1:1, 1:2...) |
| Número de hoja | Índice de página (Hoja 1 de N) |
| Notas estándar | Tolerancias generales, texto de fabricación |

### 3.1.2 Procedimiento en SolidWorks

1. **File > New > Drawing** (o desde el modelo: **New Drawing From View**).
2. **Sheet Format** — elegir plantilla (.drwdot) o configurar formato propio con **Edit Sheet Format**.
3. Editar el **cajetín**: texto de empresa, logotipo (imagen), campos anotados (autor, fecha).
4. Configurar **Options > Document Properties**: norma (ISO/ASME), unidades, grosores de línea, estilo de acotación.
5. Guardar como plantilla reutilizable (**Save Sheet Format**) en el directorio de plantillas.

## 3.2 Vistas de dibujo

A partir del modelo 3D, el software genera las **vistas 2D** automáticamente y asociadas a él.

### 3.2.1 Tipos de vista

| Vista | Uso |
|---|---|
| Principal (Standard) | Vista base del dibujo (frontal, superior, lateral) |
| Proyectada (Projected) | Vistas siguientes derivadas de la principal (90° o vista auxiliar) |
| De sección (Section) | Corte recto en un plano, muestra detalles internos |
| De detalle (Detail) | Ampliación de una zona específica a mayor escala |
| De rotura (Break) | Acorta piezas largas omitiendo el tramo central |
| Posición alternativa (Alternate Position) | Sobre la misma pieza muestra dos posiciones (ej. abierto/cerrado) |
| Corte como sección anidada (Crop) | Recorta una vista a un contorno cerrado |
| Isométrica (Isometric) | Vista 3D para la comprensión del conjunto |
| Explosionada (Exploded) | Vista del ensamble separado (desde Exploded View de la U3) |

### 3.2.2 Procedimiento general

1. Desde la pieza o ensamble: **File > New > Drawing From View**.
2. Elegir el **modelo** y **dibujar la vista principal** (orientación estándar: Isométrico/iso o frontal).
3. **Projected View** para añadir las demás vistas derivadas (superior, lateral...).
4. Según necesidad: **Section View** (seleccionando un plano de corte), **Detail View** (círculo sobre la zona), **Break View** (borde de rotura en extremos), **Cropped View**.
5. En ensambles: insertar la **Exploded View** guardada (3.4 de U3).
6. Regla: cada elemento de la pieza se repite **mínimamente**; las aristas ocultas solo si aportan.

### 3.2.3 Normas de colocación

- La vista principal (frontal) es la de mayor información.
- Las **vistas proyectadas** respetan el **sistema de proyección** declarado en el cajetín (1er/3er ángulo).
- Escalas por vista: la vista principal define la hoja; los detalles pueden usar escala 2:1, 5:1.

## 3.3 Acotación de piezas y ensambles

La **acotación** del plano convierte el modelo 3D en instrucciones de fabricación.

### 3.3.1 Acotación asociada

- En CAD las cotas **se asocian al modelo**: al reconstruir la pieza, el plano se actualiza automáticamente.
- Se insertan con **Smart Dimension** (Model Items para traer automáticamente las cotas del croquis/operación).

### 3.3.2 Acotación de elementos típicos

| Elemento | Acotación esperada |
|---|---|
| Taladros | Diámetro Ø y ubicación del centro (2 cotas de posición) |
| Redondeos | Radio R (en vistas donde se vea el arco) |
| Chaflanes | 45° o dos distancias (asociado a la arista) |
| Piezas de ensamble / posiciones | Cota de material de posición entre piezas (ej. posición del centro o del montaje) |
| Tolerancias | Añadir desviaciones o ajustes (H7/g6) según subtema 1.3 (U1) |

### 3.3.3 Procedimiento y reglas

1. **Model Items** para heredar cotas; revisar y completar con **Smart Dimension**.
2. Evitar **duplicidad**: cada dimensión una sola vez.
3. Colocar cotas **fuera del contorno** cuando la vista esté limpia.
4. Acotar las zonas repetidas una sola vez (matrices lineales/circulares se indican con número de instancias).
5. En ensambles, acotar **posiciones relativas** (coincidencias de centros, ángulos) y cotas generales del conjunto (largo, ancho, alto y diámetros exteriores).

## 3.4 Anotaciones, listado de piezas y control de versiones

### 3.4.1 Anotaciones (notas de fabricación y ensamble)

| Tipo de nota | Ejemplo de contenido |
|---|---|
| Notas de fabricación | "Cotas en mm. Tolerancia general ±0.2 mm. Rebabas removidas" |
| Notas de ensamble | "Apretar los tornillos con 12 N·m. Aplicar fijador de rosca" |
| Notas de material | "Material: Acero AISI 1045. Acabado: granallado" |
| Marca de superficie | Símbolo Ra sobre superficies funcionales |
| Símbolos de tolerancia geométrica | Cuadro de posición/flatness con referencias |

Se insertan con **Annotation > Note**, **Surface Finish**, **Geometric Tolerance** y se sitúan en la hoja fuera del área de vista.

### 3.4.2 Lista de piezas (tabla de materiales BOM) y globos

| Elemento | Contenido |
|---|---|
| Tabla de materiales (BOM) | N° de globo, número de pieza, descripción, cantidad, material |
| Globo (Balloon) | Círculo con el número enlazado a cada componente de la vista |
| Columnas típicas | Item No., Part No., Descripción, Qty, Material, Mass |

**Procedimiento:** en el plano de ensamble **Insert > Tables > Bill of Materials** → seleccionar el ensamble → configuración de columnas; luego **Auto Balloon** para numerar los globos en la vista. La tabla se **actualiza sola** si cambia el ensamble.

### 3.4.3 Control de versiones

Cada hoja debe identificar su **revisión** para trazabilidad:

| Campo | Función |
|---|---|
| Número de plano | Identifica el documento (ej: DI-2024-014) |
| Revisión (A, B, C...) | Nivel de cambio de la hoja |
| Fecha y autor | Quién y cuándo se generó/liberó |
| Estado (Release) | "Liberado publicación" / "Pendiente revisión" |

**Reglas prácticas:**

- Al modificar un modelo definitivo, crear **nueva revisión**, no sobrescribir la liberada.
- Registrar en la **carpeta de sistema** (PTC/PLM o simplemente carpeta versionada) la pieza revisada y su plano.
- La tabla de materiales del ensamble lista las versiones de cada componente (configuraciones/material).
- Verificar la coherencia **modelo ↔ plano ↔ lista de materiales** antes de cada liberación.

### 3.4.4 Flujo completo de elaboración del plano

1. **Modelar** piezas/ensamble (U2, U3) con mates y propiedades de masa.
2. **Plantilla** de plano con estándar, unidades, cajetín y símbolo de proyección (3.1).
3. Insertar **vistas** (principal, proyectadas, sección/detalle, isométrica y explosionada) (3.2).
4. **Acotar** de forma asociada y completa (3.3).
5. Añadir **notas, marcas de superficie y tolerancias** (3.4).
6. Insertar **BOM + globos** en planos de ensamble.
7. Completar **cajetín** (revisión, fecha, autor) y **liberar**.

---

**Fin de la Unidad 3**