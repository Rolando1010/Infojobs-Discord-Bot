<p align="center">
    <img src="./static/chatbot.png" width="100"/>
</p>

# Infojobs Discord Bot

### Este proyecto fue creada para participar en la hackaton organizada por [midudev](https://twitch.tv/midudev) junto a [Infojobs](https://infojobs.net/)

<br>

## De qué trata?
El proyecto consiste en un bot de discord al que puedes realizar consultas a través de comandos para obtener información rápidamente sobre ofertas de trabajo en infojobs.

<br>

### Con esta aplicación puedes acceder a funcionalidades como:
* Navegar entre todas las ofertas de trabajo ofrecidas.

* Consultar ofertas de trabajo por: categoria, habilidad, país y ID.

* Puedes buscar órdenes de trabajo que coincidan con lo que necesites.

* Obtén recomendaciones sobre ofertas de trabajo que se solicitan tus conocimientos a partir de tu perfil en github.

* Consultar categorías, habilidades y países.

* Puede obtener estadísticas sobre las ofertas de trabajo según lenguajes, tecnologías frontend y backend; así cómo por países y categorías

<br>

## Tecnologías
* Python
* Discord
* Redis
* Infojobs API
* Github API

<br>

# Ejecutándolo

### Es necesario tener una cuenta de Cloudinary e ingresar las siguientes variables en un archivo de variables de entorno:
```env
DISCORD_BOT_TOKEN
REDIS_HOST
REDIS_PORT
REDIS_PASSWORD
INFOJOBS_TOKEN
GITHUB_TOKEN
```

### Descargas el proyecto de github
```bash
git clone https://github.com/Rolando1010/Impage
```

### Desde una terminal ingresas a la raíz del proyecto, instalas las dependencias y ejecutas el proyecto
```bash
cd Infojobs-Discord-Bot
pip install -r requirements.txt
cd src
python run_discord_bot.py
```