#!/bin/bash

# Ruta al entorno virtual
VIRTUAL_ENV="Automations/mientorno/bin/activate"

# Activa el entorno virtual
source $VIRTUAL_ENV

cd Automations/mientorno/test-pruebas-automatizadas/Project/tests/

behave --tags=Prueba1 -k -s
