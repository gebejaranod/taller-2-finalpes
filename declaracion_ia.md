# Declaración de uso de IA generativa

**Modelos:**

- Claude Opus 5.5 (`claude-opus-5-5`), en la aplicación Claude Code, entre el 7 y el 11 de noviembre de 2026. Con este modelo se hizo el trabajo que se describe abajo.
- Otros modelos, como Claude Sonnet, en chats aparte para consultar términos, conceptos y código.

**Porcentaje de ayuda:** *(completar)*

## Cómo se trabajó

El equipo guio el taller paso a paso en una sola conversación con Claude. En cada punto, el equipo decidía qué hacer y cómo tratar los datos. Claude escribía y ejecutaba el código y explicaba los resultados con las cifras obtenidas. Luego el equipo revisaba, pedía cambios y escribía las conclusiones. Claude no avanzaba al siguiente punto sin que el equipo lo pidiera.

En paralelo, el equipo usó chats aparte con otros modelos, como Claude Sonnet, para consultar términos, conceptos y código mientras avanzaba. Esos chats no hacen parte de la conversación principal, y sus prompts no se incluyen en esta declaración.

Hubo una primera versión del taller que Claude generó a partir de una instrucción general. Se descartó y el taller se rehízo desde cero con este método. De esa versión solo se reutilizó la estructura de costos del punto 5 (canal de contacto más oferta, y el presupuesto de la Práctica 4). Sus cifras y fuentes se actualizaron.

## Qué hizo cada uno

| Actividad | Equipo | Claude |
|---|---|---|
| 1. Datos | Exploró los datos en Metabase y decidió el tratamiento de las edades imposibles, los nulos, los salarios negativos y las categorías mal escritas | Desplegó Metabase en Docker, cargó los datos, escribió el código de limpieza y pasó a código los gráficos que el equipo hizo en Metabase |
| 2. Modelos | Eligió los modelos a partir de una tabla de opciones de las prácticas del curso. Exigió no tocar el conjunto de prueba hasta elegir el modelo. Escribió la conclusión sobre qué modelo conviene según el costo de la campaña | Escribió la división de los datos, los pipelines, la búsqueda de hiperparámetros, las matrices de confusión y la tabla comparativa |
| 3. Análisis cuantitativo | Eligió Random Forest con el criterio de campañas caras y pidió promediar validación y prueba para los límites de costo | Calculó los precios máximos y los costos de empate, e hizo las matrices de validación y prueba |
| 4. Análisis cualitativo | Eligió SHAP y escribió la interpretación de cómo funciona el modelo | Explicó el método sin términos estadísticos y escribió el código de SHAP, ICE y la elección de un cliente por cuadrante |
| 5. Generación de valor | Pidió fuentes de menos de tres años, redujo el equipo de implementación y definió las tablas de costos y de recuperación | Buscó y verificó las fuentes en la web y calculó los costos y el tiempo de recuperación |
| 6. Presentación | Definió las cuatro diapositivas y lo que muestra cada una | Construyó la presentación en HTML |
| 7. Esta declaración | Pidió una declaración corta, enfocada en el proceso, y la revisó | La redactó a partir de la conversación |
| Entrega | Pidió armar el repositorio y publicarlo | Armó la carpeta de entrega y el README, y publicó el repositorio en GitHub |

Claude también verificó con los datos las afirmaciones del equipo antes de dejarlas en el notebook. Todas las cifras del notebook salen del código ejecutado.

## Prompts principales

Estos son algunos prompts del equipo, copiados tal como se escribieron. El registro completo de la conversación está guardado.

1. *"Vamos a realizar este taller de ciencia aplicada de datos, asi que revisa primero esta documentacion y practicas de ML y tentlas muy presentes para ir desarrollando este taller"*, y luego *"Desde cero, paso a paso"*.
2. *"primero despliega un contenedor con metabase y mete los datos de churm para yo revisar y ahcer la exploracion"*
3. *"para las edades que son imposibles, que tratamiento recomiendoas, son pocos unos por encima de 100 y otros por debajo de 18 […] el salario tienen unos pocos con valores negativos, pero los salarios e ngeneral manteiene una tendencia plana y son muy similares […]"*
4. *"inportate, los datos de finales de test no se tocan hasta que el modelo no este afinado con los datos de prueba, asi esta actualmente?"*
5. *"si el precio de la campaña de retencion es poca o bara es mejor booting pero si es mas cara es major random forest […] logistica no cumple porque aunque atrama mas que se van, atrapa mucho mas de los que no se van y esto genera una campaña mucho mas cara […] esto que te acabo de decir es la conculison de los modelos"*
6. *"se basa e ngran medidoa en la edad y el numero de producotos, para los casos en donde se quivoco vemos que son datos que no indicaban abandono como los otros que vimos en la exploracion inicial […]"*
7. *"la idea es que sea corta no mas de 4 diapositivas la primera mostrando el dolor, la segunda un esquema o grafica endonde se pasan los datos por los dos modelos […]"*
8. *"dame una tabla con las estimaciones y las fuentes de donde las sacaste, haz que no seam mas viejas a 3 años ya que la infacion en colombia ha cambiado mucho eso"*, y luego *"la estimacion esta muy alta creo yo con un solo cientifico/ingeniero de datos, el lider de negocio, quita integracino crm y deja el resto"*
