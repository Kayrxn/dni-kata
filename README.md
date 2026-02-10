# Verificación de DNI ✅

**Resumen:**
El ejercicio valida un DNI español comprobando el formato (8 dígitos + letra) y calculando la letra correcta a partir del número.  
Si la letra calculada coincide con la letra dada, el DNI es válido.



## Cómo se resolvió 🔧
- Separamos responsabilidades: parseo, validación de formato, cálculo de letra y comparación. Cada parte está en su función para que sea fácil de probar.
- Para el formato usé una comprobación sencilla (regex o checks de longitud y dígitos).
- El cálculo de la letra se hace con `numero % 23` y se compara con la tabla de asignación en `src/tabla_asignacion.py`.
- Hay tests en `test/` que cubren DNIs correctos, incorrectos y con formato inválido.

## Términos ADD usados para las variables 🧭
- **Análisis:** nombres que vienen del input y ayudan a entender los datos crudos: `dni_str` (entrada cruda), `numero` (parte numérica como entero), `letra` (parte letra como carácter).
- **Diseño:** nombres que describen roles y comprobaciones: `es_formato_valido` (bool), `calcula_letra()` (función), `tabla_asignacion` (estructura de referencia).
- **Desarrollo:** nombres concretos usados en el código para implementar la lógica: `numero_dni`, `letra_esperada`, `indice` (resto de la división), `letra_calculada`.


