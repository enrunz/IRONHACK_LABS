![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: API & Web Data Scraping and Web Data Pipeline

## Overview

Este proyecto utiliza una API llamada Teleport. Aquí se puede encontrar información a cerca de ciudades y zonas metropolitanas en el mundo. Algunos de los datos proporcionados son: población, ubicación, país, nombres alternos, etc. 

Nuestro proyecto utiliza específicamente un set de datos en forma de índices que califican diferentes cualidades de una ciudad. Por ejemplo, la seguridad, la vivienda, los impuestos, etc. 

El proyecto crea una función para extraer los índices de algunas ciudades y crear un Data Frame. 

En su primera estapa (la que se está presentando), este proyecto se concentra en la obtención de datos de las ciudades y la utilización de dichos datos para entender cuales son las carencias de cada ciudad. Estas estarían dictadas por los rubros con los índices más bajos. 

Con esta información en mano, se hace una búsqueda de las representaciones públicas de la ciudad en Wikipedia. ¿Cómo se describe la ciudad? ¿Se habla de los rubros carentes? 

Se realiza una comparación que nos indique si los rubros problematicos de la ciudad aparecen dentro de las descripciones en la página de wikipedia. 


FUTURO DEL PROYECTO:

En una segunda etapa de este proyecto, la documentación de la imagen pública de la ciudad podría obtenerse también de páginas propias del ayuntamiento o la administración pública. Para evitar sesgos, se podrían utilizar también páginas de diarios no afiliados al gobierno o twitter para que funcionen como la contraparte.

También se podrían crear bases de datos de conjuntos de ciudades con algún rasgo específico en común. Por ejemplo el idioma, la afición al fútbol, etc. A partir de estas bases de datos se pueden inferir valores globales de cada rubro. 

---

##Contenidos

-Este README.md
-Una carpeta con recursos sin fruto para consideración futura. (FAILS)
-Un Jupyter Notebook que contiene el trabajo con la API y el Web Scraping de Wikuipedia. 
-Un archivo cities.csv que contiene un prototipo de Data Frame compuesto. Se obtuvo la información de los índices de 10 ciudades en Norte América.  

----

## Links

API: https://developers.teleport.org/api/
API ENDPOINT CREATOR: https://developers.teleport.org/api/reference/
Embedded protocol: city:search-results/city:item/city:urban_area/ua:scores
