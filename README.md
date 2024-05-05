<header>
<h1>Proyecto Pruebas de Automatización en Urban Routes</h1>
</header>
<main>
<h2>Descripción del proyecto</h2>
<h4>El objetivo principal de este proyecto es garantizar el correcto funcionamiento de las funcionalidades clave de la aplicación. El proceso que se llevó a cabo fue el siguiente:</h4>
<ul>
<h4 style="margin-bottom: 0;">1. Configuración de la ruta:</h4>
<li style="margin-bottom: 0;">Verificar que el usuario pueda ingresar la dirección de origen y destino correctamente.</li>
<li style="margin-bottom: 0;">Confirmar que el sistema calcule la ruta correctamente y muestre la información de la ruta al usuario.</li>
<h4 style="margin-bottom: 0;">2. Selección de tarifa Comfort:</h4>
<li style="margin-bottom: 0;">Comprobar que el usuario pueda seleccionar la opción de tarifa "Comfort" correctamente.</li>
<li style="margin-bottom: 0;">Validar que la tarifa seleccionada se refleje correctamente en la interfaz de usuario.</li>
<h4 style="margin-bottom: 0;">3. Rellenar número de teléfono:</h4>
<li style="margin-bottom: 0;">Verificar que el usuario pueda ingresar su número de teléfono en el campo correspondiente.</li>
<li style="margin-bottom: 0;">Confirmar que el número de teléfono se valide correctamente y se acepte en el sistema.</li>
<h4 style="margin-bottom: 0;">4. Agregar una tarjeta de crédito:</h4>
<li style="margin-bottom: 0;">Comprobar que el usuario pueda agregar una tarjeta de crédito para el pago.</li>
<li style="margin-bottom: 0;">Validar que los datos de la tarjeta se ingresen correctamente y se almacenen en el sistema.</li>
<h4 style="margin-bottom: 0;">5. Escribir un mensaje para el conductor:</h4>
<li style="margin-bottom: 0;">Verificar que el usuario pueda escribir un mensaje opcional para el conductor.</li>
<h4 style="margin-bottom: 0;">6. Solicitar una manta y pañuelos:</h4>
<li style="margin-bottom: 0;">Comprobar que el usuario pueda solicitar una manta y pañuelos para el viaje.</li>
<h4 style="margin-bottom: 0;">7. Pedir helados:</h4>
<li style="margin-bottom: 0;">Verificar que el usuario pueda agregar helados a su pedido antes del viaje.</li>
<h4 style="margin-bottom: 0;">8. Hacer pedido de taxi y esperar la validación e información del conductor:</h4>
<li style="margin-bottom: 0;">Comprobar que los modales de confirmación y detalles del pedido aparezcan correctamente después de realizar las acciones correspondientes.
</li>
</ul>
<h2>Tecnologías y Técnicas Utilizadas</h2>
<ul>
<li>Python</li>
<li>Pytest</li>
<li>Selenium</li>
<li>Page Object Model(POM)</li>
</ul>

<h2>Estructura del Proyecto</h2>
<h4>El proyecto incluye los siguientes archivos:</h4>
<ul>
<li>main.py: Contiene las pruebas de clase y funcionalidad.</li>
<li>data.py: Almacena los datos para las pruebas. </li>
<li>utility.py: Contiene una función que devuelve un codigo de un número de confirmación de teléfono </li>
<li>Urban_Routes_Page: Contiene los localizadores y métodos necesarios en la clase </li>
</ul>

<h2>Lista de comprobación</h2>
<table>
<tr>
<th>Caso de Prueba</th>
<th>Estado</th>
</tr>

<tr>
<td>1. Configurar la dirección </td>
<td>✔</td>
</tr>
<tr>
<td>2. Seleccionar la tarifa Comfort</td>
<td>✔</td>
</tr>
<tr>
<td>3. Rellenar y verificar el número de teléfono</td>
<td>✔</td>
</tr>
<tr>
<td>4. Agregar una tarjeta de credito</td>
<td>✔</td>
</tr>
<tr>
<td>5. Escribir un mensaje para el controlador </td>
<td>✔</td>
</tr>
<tr>
<td>6. Pedir una manta y pañuelos </td>
<td>✔</td>
</tr>
<tr>
<td>7. Pedir 2 helados </td>
<td>✔</td>
</tr>
<tr>
<td>8. Hacer pedido de taxi</td>
<td>✔</td>
</tr>
<tr>
<td>9. Esperar la validación e información del conductor</td>
<td>✔</td>
</tr>
</table>

<h2>Instrucciones de Ejecución</h2>
<ul>
<li>1. Tener instalados Python 3 y pip en su sistema</li>
<li>2. Crea un entorno virtual y actívalo</li>
<li>3. Instalar Pytest en la terminal con el comando: pip install pytest</li>
<li>4 Instalar Selenium en la terminal con el comando: pip install selenium</li>
<li>5. Ejecuta las pruebas en la terminal con el comando: pytest</li>
</ul>
</main>

