# Urban Routes Test Automation

Este proyecto contiene pruebas automatizadas para la aplicación **Urban Routes**.

## 📌 Descripción del Proyecto

El objetivo de este proyecto es validar de forma automática el flujo de pedido de un taxi en la plataforma Urban Routes, incluyendo:

- Selección de origen y destino.
- Elección de tarifa.
- Validación de número de teléfono mediante código SMS.
- Agregado de tarjeta de pago.
- Inclusión de comentarios para el conductor.
- Selección de requisitos adicionales como manta o helado.
- Confirmación final del pedido.

Las pruebas están diseñadas utilizando Selenium WebDriver para interactuar con la interfaz de usuario de la aplicación.

## ⚙️ Tecnologías Utilizadas

- **Python 3**
- **Selenium WebDriver**
- **pytest** (opcional, si se estructura como módulo de pruebas)
- **CDP Logs** para capturar el código de confirmación del SMS.
- **Page Object Model (POM)** para mantener el código organizado y reutilizable.
- **Esperas explícitas** mediante `WebDriverWait` para sincronizar los pasos del flujo.

## 🧪 Cómo Ejecutar las Pruebas

### Requisitos Previos

- Tener **Python 3.7+** instalado.
- Tener **Google Chrome** y el correspondiente **ChromeDriver** instalado y en el PATH.
- Instalar las dependencias del proyecto 


