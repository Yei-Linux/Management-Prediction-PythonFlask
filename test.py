import pandas as pd
import numpy as np
import sqlalchemy
from matplotlib import pyplot as plt

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost:3306/ia')

elecciones = pd.read_sql_table("rectores", engine,
                               columns=['ID','NOMBRE', 'UNIVERSIDAD', 'ANTECEDENTES_CORRUPCION',
                                        'ESTUDIOS_GESTION_PUBLICA', 'PROFESION', 'PRODUCCION_CIENTIFICA',
                                        'PROYECTOS_INVESTIGACION', 'EXPERIENCIA','ANOS_EXPERIENCIA',
                                        'GENERO', 'EX_RECTOR','TIPO_PERSONALIDAD' ,'GESTION','TIPO_UNIV'])

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

elecciones['nombre']=encoder.fit_transform(elecciones.NOMBRE.values)
elecciones['antecedentes'] = encoder.fit_transform(elecciones.ANTECEDENTES_CORRUPCION.values)
elecciones['gestion_publica'] = encoder.fit_transform(elecciones.ESTUDIOS_GESTION_PUBLICA.values)
elecciones['produccion'] = encoder.fit_transform(elecciones.PRODUCCION_CIENTIFICA.values)
elecciones['proyecto'] = encoder.fit_transform(elecciones.PROYECTOS_INVESTIGACION.values)
elecciones['anos_experiencia'] = encoder.fit_transform(elecciones.ANOS_EXPERIENCIA.values)
elecciones['exrector'] = encoder.fit_transform(elecciones.EX_RECTOR.values)
elecciones['tipo_personalidad'] = encoder.fit_transform(elecciones.TIPO_PERSONALIDAD.values)
elecciones['gestion'] = encoder.fit_transform(elecciones.GESTION.values)

x = elecciones[
        ['antecedentes', 'gestion_publica', 'produccion', 'proyecto',
         'anos_experiencia', 'exrector','tipo_personalidad']];

y = elecciones[['gestion']];

def Get_X():

    return x;

def Get_Y():

    return y;

def Get_Dataset():

    dataSet = [];
    i = 0;

    while i < 29:

        dataSet.append([i, elecciones['gestion'][i]]);

        i = i + 1;

    return  dataSet;

def Get_Categories():

    categorias = [];
    i = 0;

    while i < 29:

        categorias.append(elecciones.NOMBRE.values[i]);

        i = i + 1;

    return categorias;


