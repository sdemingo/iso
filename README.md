
# Código para prácticas para ISO

En este directorio encontrarás código, scripts y programas que usaremos durante el módulo de Implantación de Sistemas Operativos del ciclo de Administración de Sistemas y Redes.


## ⏬ Como descargar el directorio

Primero necesitas instalar en tu máquina virtual de Debian el comando `git`. Este programa permite sincronizar directorios de tu disco duro con directorios alojados en Github. Para ello ejecuta:

```
$ sudo apt update
$ sudo apt install git
```

Ahora puedes descargar el directorio completo de `iso` en tu maquina virtual. A esta operación se le llama *clonar* un repositorio. Ubícate en el directorio donde quieras descargarte `iso` (por ejemplo en tu *home* personal) y ejecuta:

```
$ git clone http://github.com/sdemingo/iso.git
```

Todo esto solo debes realizarlo una sola vez. Tras terminar esta operaciones ya tendrás el directorio `iso` instalado en tu máquina y podrás acceder a el siempre que necesites. 


## 🔃 Como actualizar el directorio

Cada cierto tiempo, es posible que se publiquen cambios o nuevos contenidos en el directorio. Para descargar la última versión del directorio **no necesitas repetir todo lo anterior**. Únicamente basta con que de vez en cuando, entres el directorio `iso` (allí donde lo tengas guardado en tu máquina virtual) y ejecutes dentro de el:

``` 
$ git pull
```


