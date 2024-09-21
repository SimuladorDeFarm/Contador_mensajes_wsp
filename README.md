# Herramienta en python para analisis de frecuencias en chats de Whatsapp

## Resumen
Herramienta escrita en python que genera estadisticas de mensajes de chats de 
whatapp 

genera:
- frecuencia de mensajes por dia de cada integrantes
- frecuencia total de mensajes

## Privacidad y Seguridad
Para el uso de este script es necesario que uses un chat exportado de whatsapp,
El programa no recoplina ningun tipo de informacion y solo se ejectua localmente.
Al exportar tu chat de whatsapp se precavido, no lo compartas con nadie y por el amor de 
dios o el dios en que creas no lo subas por error a github o a otra plataforma
al estar en archivo .txt es visible para cualquier persona

## Requistos:
- Poseer chat en formato .txt [como exportar chats de WhatsApp](https://faq.whatsapp.com/1180414079177245/?locale=ca_ES&cms_platform=android)
- Tener python instalado en la maquina
- Tener python-pandas python-openpyxl
- Editor de codigo a gusto

## Instalar

#### Linux
```bash
$ git clone https://github.com/SimuladorDeFarm/Contador_mensajes_wsp.git
$ cd Contador_mensajes_wsp
$ chmod +x contador_msj.py
```
Desconozco como ejecutar un archivo .py en otros sitemas operativos

## instrucciones

¡IMPORTANTE!:
  Evita tener emojis o caracteres especiales en los nombre de los contactos
  cambia el nombre de tu contacto y despues de eso exporta el chat de wsp.
  Tu nombre de ususario es el que tienes puesto en tu perfil de wsp.
  En el caso de no tener agregado un contacto desconozco si el nombre que 
  tendra en el archivo será su nombre de usuario o su numero telefonico 

- Guarda el chat de whatsapp en tu maquina local
- Mueve el archivo .txt a la carpeta `/contar_msj`
- Al inicio del archivo modifica la variable nombreArchivo para que calse
 con tu archivo, no coloques el formato
```bash
  nombreArchivo = "nombreDelArchivoSinformato"
```
- Modifica el vector personas y añade los integrantes del grupo o a otra
persona del chat
```bash
  personas = ["persona1","persona2", "persona3"... etc]

```
- Ejecuta el archivo con el siguiente comando
```bash
  $ python contar_msj.py
```
Al ejecutar el programa en la carpeta `/tablas` se crearan tres tantos
archivos .xlsx como personas ingresadas y tambien uno con frecuancia total,
los datos variarian dependiendo de la version.

## screenshots 

![imagen](https://github.com/user-attachments/assets/2d8103a7-f79c-4b1e-899f-795491f93856)

---------------------------------------------------------------------------------
Mi amigo se consiguio polola y dejo de pescar tanto el grupo asique esta herramienta
es para tener datos solidos de su dejadez y mostrarle un grafico en toda la cara que 
demuestra su gosting

quiero mucho a mi amigo
![imagen](https://github.com/user-attachments/assets/adccfb95-8087-4e36-a121-3ba983f1a749)


