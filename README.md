# Introduccion

Requisito previo para poder ejecutar scripts sin restricciones 
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Crear entorno virtual
```
ptyhon3 -m venv venv
```


Habilitar entorno virtual
```
Windows
.\venv\Scripts\Activate.ps1

Linux
source venv/bin/activate
```

Ejecutar script
```
Windows
python .\hola_mundo.py

Linux
python hola_mundo.py
```