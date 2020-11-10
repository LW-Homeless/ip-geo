# IP-GEO
Sencilla herramienta para Geoposicionar una direccion IP. La herramienta puede obterner las coordenadas y dirección de una dirección IP. entre los registro que se pueden optener son los siguientes:

- Ubicacion a nivel Continental.
- Ubicacion a nivel País.
- Ubicacion a nivel Ciudad.
- Direccion, coordenadas y zonas horaria.
- Código Postal.
- Otra Información.

# Requerimientos
- Para utilizar IP-GEO debe contar con una API-KEY de Maxmind, este último es requerido para la actualizacion automatica de las bases de datos que utiliza IP-GEO. Para obtener una API-KEY de Maxmind debe registrarse en Maxmind en el siguiente enlace https://www.maxmind.com/en/geolite2/signup

- Python 3.7.8.x o superior
- setuptools.

# Instruciones de uso
- Descarga o clona el repositorio.
- Instala las dependencia con el siguiente comando.

```
pip install -r requirements.txt
```
- Luego, ejecute el archivo Main.py con el siguiente comando.

```
python Main.py
```

------------
Se mostrará la siguiente pantalla.
Foto1

------------
Digitamos 1 "Ingresar API-KEY Maxmind", se le pedira ingresar la API-KEY Maxmind asignada (ver sección requerimientos). una vez digitada presionamos "Enter" y se mostrará nuevamente el menu de la aplicación.
Foto2

------------
Una vez digitada presionamos "Enter" y se mostrará nuevamente el menu de la aplicación.
Foto3

------------
Por último, digitamos 2 "Consultar IP" ingresamos la direccion IP a consultar.
Foto3
foto4

------------
Finamente, obternemos los resultados.
foto5
