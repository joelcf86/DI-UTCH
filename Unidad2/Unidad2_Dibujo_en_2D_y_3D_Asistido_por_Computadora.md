# DIBUJO PARA INGENIERÍA

## UNIDAD 2. Dibujo en 2D y 3D Asistido por Computadora

### Datos generales de la unidad

| Concepto | Valor |
|---|---|
| Horas del Saber | 6 |
| Horas del Saber Hacer | 12 |
| Horas Totales | 18 |

**Propósito esperado:** El estudiante desarrollará modelos geométricos en 2D y 3D a través del uso de software dedicado para el bocetado de piezas mecánicas.

## 1. Temario de la unidad (alineado al programa de la asignatura)

| # | Tema | Saber | Saber hacer | Ser y convivir |
|---|---|---|---|---|
| 1 | Elaboración de croquis 2D | Identificar el uso y aplicación de: entidades de croquis (líneas, rectángulos, círculos, arcos, elipses, líneas constructivas), herramientas de croquis (equidistancia, conversión de entidades, recorte y extensión de entidades) y relaciones de croquis (coincidente, paralelo, perpendicular, tangente, horizontal, vertical, concéntrico). | Realizar proyecciones ortogonales de piezas mecánicas utilizando entidades, herramientas y relaciones de croquis aplicando acotación necesaria para la correcta definición del croquis. Aplicar las técnicas de acotación utilizando los respectivos comandos del software dedicado. | Resolver problemas de complejidad básica a media en la realización de croquis 2D de piezas mecánicas aplicando los conceptos de dibujo en ingeniería. |
| 2 | Representación gráfica de piezas mecánicas en 3D | Identificar los conceptos de: operaciones croquizadas de salientes y cortes (extrusiones, revoluciones, barridos) y operaciones aplicadas (redondeos, chaflanes, vaciados, matrices). | Dibujar piezas mecánicas en 3D utilizando los principales comandos para detalle de piezas en el software dedicado de CAD. | Resolver problemas de complejidad básica a media en la elaboración de piezas mecánicas en 3D aplicando procesos constructivos de modelado. |
| 3 | Aplicación de acabados y materiales | Identificar los comandos básicos para definir acabados y materiales (propiedades físicas) de una pieza. | Aplicar a piezas mecánicas en 3D propiedades físicas de materiales y acabados, en el software dedicado de CAD. | Fortalecer la actitud proactiva a través de la asignación de piezas y asignación de acabados. |

## 2. Planeación sugerida del cuatrimestre (Unidad 2)

| Semana | Sesión Saber (6 h) | Sesión Saber Hacer (12 h) |
|---|---|---|
| 1-2 | Tema 1. Entidades y herramientas de croquis (1.1, 1.2) | Croquis 2D de piezas: línea, rectángulo, círculo; equidistancia y conversión |
| 3-4 | Tema 1. Relaciones de croquis y acotación (1.3) | Proyecciones ortogonales acotadas de piezas mecánicas |
| 5-6 | Tema 2. Salientes, cortes y operaciones (2.1, 2.2) | Modelado 3D: extruir, revolucionar, redondeo, chaflán, vaciado, matriz |
| 7-8 | Tema 3. Materiales y acabados (3.1, 3.2) | Propiedades físicas y acabados aplicados a piezas 3D |

---

# TEMA 1. Elaboración de croquis 2D

## 1.1 Entidades de croquis

Las **entidades de croquis** son los elementos geométricos 2D que se dibujan sobre un plano de trabajo. En SolidWorks se crean desde la pestaña **Sketch** y constituyen la base de todas las operaciones 3D.

### 1.1.1 Entidades básicas

| Entidad | Símbolo / comando | Descripción | Aplicación |
|---|---|---|---|
| Línea | Line (L) | Segmento recto entre dos puntos definido por inicio y fin | Aristas rectas, ejes, contornos |
| Rectángulo | Rectangle (R) | Polígono de 4 lados definido por 2 o 3 puntos | Placas, bases, perfiles |
| Círculo | Circle (C) | Perímetro definido por centro y radio | Taladros, ejes, bridas, rotores |
| Arco | Arc | Porción de circunferencia (centro o 3 puntos) | Transiciones y redondeos grandes |
| Elipse | Ellipse | Curva cerrada con dos ejes | Geometría elíptica (engranes-bases) |
| Línea constructiva | Centerline | Línea de referencia (no es arista) | Simetrías, ejes de revolución, ayudas |

### 1.1.2 Pasos para crear entidades en SolidWorks

1. Seleccionar un plano o cara donde iniciar el croquis (Face/Plane → Sketch).
2. Elegir la **entidad** en la barra **Sketch**.
3. Indicar los puntos: inicio y fin (línea), dos esquinas (rectángulo), centro y radio (círculo).
4. Definir la geometría con **cotas** y **relaciones** hasta que todo el croquis quede en negro (totalmente definido).
5. Salir del croquis y aplicarle una operación (Ej: **Extrude**) para convertirlo en 3D.

### 1.1.3 Consejos de diseño

- Emplear **líneas constructivas** para referencias que no deben figurar en la pieza.
- Alternar entre el estado de **definido** (negro) y **sobrescrito/indefinido** (azul): un croquis totalmente definido evita errores de reconstrucción.
- Usar relaciones geométricas (ver subtema 1.3) para capturar intención de diseño en lugar de dimensiones redundantes.

## 1.2 Herramientas de croquis

Las herramientas de croquis modifican o generan nueva geometría a partir de entidades existentes.

### 1.2.1 Herramientas principales

| Herramienta | Función | Uso típico |
|---|---|---|
| Entidades equidistantes (Offset Entities) | Copia entidades seleccionadas a una distancia dada hacia dentro/fuera | Paredes de tubos, espesores constantes de chapa |
| Convertir entidades (Convert Entities) | Proyecta aristas/caras existentes sobre el plano del croquis | Aprovechar geometría de la pieza para nuevo croquis |
| Recortar entidades (Trim) | Elimina porciones de líneas/arcos hasta intersecciones | Limpieza de sobrantes al dibujar perfiles |
| Extender entidades (Extend) | Alarga una entidad hasta la primera que corta | Cerrar contornos al lado de la siguiente arista |
| Simetría de entidades | Copia entidades respecto a una línea constructiva | Perfiles simétricos de piezas |

### 1.2.2 Secuencia de trabajo recomendada

1. Dibujar la forma aproximada con entidades sencillas.
2. Aplicar **relaciones de croquis** (paralelismo, tangencia, simetría).
3. **Recortar** los sobrantes y **extender** lo que falte para cerrar el contorno.
4. Aprovechar **Convert Entities** para elementos derivados de caras ya modeladas.
5. Usar **Offset** para perfiles con espesor constante (casquillos, nervios).
6. **Acotar** y definir el croquis completamente.

### 1.2.3 Errores frecuentes y solución

| Error | Causa | Solución |
|---|---|---|
| Perfil abierto al extruir | Entidades sin intersección real | Recortar/extender hasta cerrar |
| Croquis sobrescrito (rojo) | Cotas o relaciones contradictorias | Quitar relación/cota que sobra |
| Simetría que no funciona | Falta línea constructiva central | Agregar Centerline y relación "Symmetric" |
| Diagonal que aparece | Entidad no intencional sobrante | Trim de los segmentos |

## 1.3 Relaciones de croquis

Las **relaciones** definen la intención geométrica entre entidades del croquis (y contra ejes/origen). Hacen el croquis robusto: al mover una entidad, las relacionadas se adaptan.

### 1.3.1 Relaciones principales

| Relación | Efecto | Cuándo usarla |
|---|---|---|
| Coincidente (Coincident) | Fija un punto sobre otra entidad | Unir extremos, puntos en líneas/círculos |
| Paralela (Parallel) | Las líneas quedan a la misma dirección | Lados de rectángulos y perfiles |
| Perpendicular (Perpendicular) | Las líneas quedan a 90° entre sí | Esquinas, ejes perpendiculares |
| Tangente (Tangent) | Línea/arco tocan la curva sin cortarla | Transiciones línea-arco, ruedas |
| Horizontal | La línea o puntos quedan horizontales | Bases, cotas de ancho |
| Vertical | La línea o puntos quedan verticales | Lados, cotas de altura |
| Concéntrico (Concentric) | Dos círculos/arcos comparten centro | Taladros y redondeos concéntricos |

### 1.3.2 Cómo aplicar una relación

1. Mantener pulsada la tecla **Ctrl** y seleccionar dos o más entidades.
2. En el panel **Properties** (o la ventana contextual) aparecen **Add Relations**.
3. Elegir la relación: paralela, perpendicular, tangente, etc.
4. Verificar que el croquis conserve o gane el estado "totalmente definido".

### 1.3.3 Relación vs cota

| Herramienta | Qué fija | Ejemplo |
|---|---|---|
| Relación | La forma (dirección, contacto) | Lado vertical, tangente al arco |
| Cota | La magnitud (distancia, ángulo) | Largo 50 mm, radio 12 mm |

Una buena práctica: definir **forma con relaciones** y **tamaño con cotas**. El resultado es un croquis totalmente definido, listo para la operación 3D.

---

# TEMA 2. Representación gráfica de piezas mecánicas en 3D

## 2.1 Operaciones croquizadas de salientes y cortes

Las **operaciones de construcción (features)** convierten los croquis en modelos 3D. Se dividen en **salientes** (agregan material) y **cortes** (quitan material), y según su trayectoria se clasifican en **extrusión, revolución y barrido**.

### 2.1.1 Extrusión (Extrude)

Operación que desplaza un perfil cerrado en línea recta perpendicular al croquis.

| Elemento | Descripción |
|---|---|
| Saliente (Boss) | Agrega material desde el plano (ej. base de una pieza) |
| Corte (Cut) | Elimina material a través de la pieza (ej. agujero) |
| Dirección | Unidireccional, bidireccional o hasta superficie/cuerpo |
| Finalizar (End condition) | Ciego (Blind), hasta la siguiente, hasta superficie, a través de todo (Through All), a media distancia (Mid Plane) |
| Ángulo de salida (Draft) | Inclinación de las paredes para fundición/inyección |

**Pasos:** dibujar croquis cerrado → **Features > Extruded Boss/Cut-Base** → definir profundidad y condición de finalización → aceptar.

### 2.1.2 Revolución (Revolve)

Genera material al hacer girar un perfil cerrado alrededor de un **eje central** (línea constructiva).

- Indicada para cuerpos de revolución: ejes, poleas, copas, tornillos, ruedas.
- El perfil **no debe cruzar el eje** y debe quedar a un solo lado.
- Configuración: ángulo de revolución (360° típico) y eje de giro.

### 2.1.3 Barrido (Sweep)

Desplaza un perfil a lo largo de una **trayectoria** (curva de guía) para crear perfiles constantes o variables.

- Aplicaciones: ductos, cables, manijas, guías de riel, cuerpos de revolución complejos.
- Componentes: **profile** (perfil de sección, cerrado) y **path** (trayectoria; puede ser 3D en croquis 3D o aristas).
- Con **guías (guide curves)** se controla el cambio de sección a lo largo del camino.

### 2.1.4 Comparativa rápida

| Operación | Movimiento | Aplicación | Dónde se define el perfil |
|---|---|---|---|
| Extruir | Recto perpendicular | Bases, nervios, agujeros rectos | Croquis 2D (plano/cara) |
| Revolucionar | Rotación alrededor de eje | Cuerpos de revolución | Croquis 2D + eje |
| Barrir | Sigue una trayectoria | Ductos, guías, manijas | Perfil 2D + trayectoria |

## 2.2 Operaciones aplicadas

Las **operaciones aplicadas (placed features)** detallan la pieza sin necesidad de croquis adicionales: se aplican sobre aristas, caras o volúmenes ya modelados.

### 2.2.1 Redondeo (Fillet)

Suaviza aristas creando una superficie tangente a las caras adyacentes.

| Variante | Uso |
|---|---|
| Radio constante | Esquinas típicas, desgaste reducido |
| Radio variable | Transiciones deslizantes |
| Cara a cara | Superficies curvas continuas |

**Pasos:** **Features > Fillet** → seleccionar aristas o caras → radio → aplicar. Seleccionar primero el **edge/face** y luego editar el radio; los redondeos se hacen preferentemente al final del modelado.

### 2.2.2 Chaflán (Chamfer)

Bisela aristas con línea recta a 45° (o con dos distancias).

- Se usa en la entrada de agujeros, extremos de piezas, alojamientos de tornillos y para facilitar el ensamble.
- Tipos: ángulo-distancia, distancia-distancia y vértice.

### 2.2.3 Vaciado (Shell)

Elimina el interior de la pieza dejando una pared de espesor constante (casco).

- Aplicación: cajas, carcasas, contenedores, soportes aligerados.
- **Pasos:** seleccionar las caras a remover (facing, removidas) → espesor de pared → aceptar. Si se quitaron varias caras, el resultado es una caja abierta por esos lados.

### 2.2.4 Matrices (Pattern)

Repite una o varias operaciones/cuerpos de forma organizada.

| Matriz | Descripción | Ejemplo |
|---|---|---|
| **Lineal (Linear)** | Repite en direcciones 1 o 2 con espaciado definido | Agujeros en fila de una brida |
| **Circular (Circular)** | Repite alrededor de un eje con número y ángulo | Agujeros de rueda, taladros de sujeción |

**Pasos:** seleccionar la operación a repetir → definir dirección (o eje) → espaciado y número de instancias → **Skip instances** para omitir algunas → aceptar.

### 2.2.5 Buenas prácticas de modelado

1. Ordenar: **base → cortes → detalles (redondeos/chaflanes) → matrices**.
2. Los **redondeos ideales** se aplican al final para reducir reconstrucciones.
3. Usar **referencias en el FeatureManager** para documentar la intención.
4. Verificar con **Evaluate > Measure** las dimensiones resultantes.

---

# TEMA 3. Aplicación de acabados y materiales

## 3.1 Propiedades físicas de materiales

Definir correctamente el **material** de una pieza permite calcular masa, volumen, centro de gravedad y preparar el modelo para simulación y fabricación.

### 3.1.1 Asignación de material

**Pasos (SolidWorks):** botón derecho sobre Material en el FeatureManager (o pieza → **Edit Material**) → seleccionar material de la biblioteca (ej. AISI 1045, Aluminio 6061, Nylon) → **Apply** → cerar.

| Familia | Ejemplos | Uso típico |
|---|---|---|
| Aceros | AISI 1020, 1045, 4140 | Ejes, estructuras, elementos de precisión |
| Inoxidables | AISI 304, 316 | Alimentación, ambiente corrosivo |
| Aluminios | 6061-T6, 7075 | Soportes ligeros, carcasas |
| Cobre / latón | C26000, C28000 | Contactos, componentes eléctricos |
| Polímeros | Nylon, ABS, POM | Engranes, rodamientos de deslizamiento |

### 3.1.2 Propiedades físicas y cálculos

| Propiedad | Qué es | Comando |
|---|---|---|
| Densidad | Masa por volumen (kg/m³) | Material database |
| Masa | Cantidad de materia de la pieza | Evaluate > Mass Properties |
| Volumen | Espacio que ocupa | Mass Properties |
| Centro de masa | Punto de equilibrio | Mass Properties |
| Área superficial | Superficie expuesta | Mass Properties |

La densidad del material asignado es la base: al cambiar de material, la masa se recalcula automáticamente sin volver a modelar.

## 3.2 Acabados y materiales

El **acabado** define la apariencia y, en muchos casos, la condición funcional de las superficies (tacto, reflexión, rugosidad, resistencia a la corrosión).

### 3.2.1 Acabado superficial (aparición)

| Tipo de acabado | Ejemplo |
|---|---|
| Pulidos / brillo | Transmisiones visibles, espejos |
| Mate / satinado | Carcasas, superficies estándar |
| Granallado / arenado | Acabados textiles para piezas mecanizadas |
| Texturizados | Agarre, paneles decorativos |

### 3.2.2 Aplicación de apariencia (Appearance)

**Pasos (SolidWorks):** seleccionar la pieza o cara → **Edit Appearance** (o arrastrar desde Manage Appearances) → elegir librería (Plastic/Metal/…) → ajustar color, hilo, reflexión → aplicar.

- La apariencia **no altera** propiedades físicas (la masa depende del material, no del color).
- Se puede aplicar por **pieza, cara o característica** (el más selectivo es a cara).
- Se usan **decals / textos** para etiquetado, logotipos o seriales del producto.

### 3.2.3 Acabado en el plano (símbolo Ra)

Aunque la apariencia es visual, la especificación de fabricación del acabado se documenta en el **plano** con el símbolo de rugosidad (Ra):

- **Ra 0.8 / 1.6** — superficies pulidas para ajustes e interferencias.
- **Ra 3.2** — acabado fino de mecanizado general.
- **Ra 6.3 / 12.5** — superficies torneadas/fresadas convencionales.
- Sin símbolo — superficie en bruto (colada o forja).

### 3.2.4 Flujo completo de acabados y materiales

1. **Modelar** la pieza (subtema 2.1/2.2).
2. **Asignar material** para propiedades físicas (3.1).
3. **Aplicar apariencia/acabado** para presentación (3.2).
4. **Verificar** masa y centro de gravedad con Mass Properties.
5. **Documentar** material y acabado en el plano (U3).

---

**Fin de la Unidad 2**