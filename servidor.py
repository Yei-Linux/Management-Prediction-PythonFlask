from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy

from test import *

import  random

import os

#----------------------------#
#------SETTINGS OF FLASK-----#
#----------------------------#

__author__ = 'ibininja'
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/ia';
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False;
db=SQLAlchemy(app);

#----------------------------#
#------------MODELS----------#
#----------------------------#

#----------------------------#
#--------ENTITY RECTORS------#
#----------------------------#

class RECTORES(db.Model):

    ID= db.Column(db.Integer,primary_key=True)
    NOMBRE =db.Column(db.String(100));
    UNIVERSIDAD =db.Column(db.String(50));
    ANTECEDENTES_CORRUPCION=db.Column(db.String(30));
    ESTUDIOS_GESTION_PUBLICA = db.Column(db.String(10));
    PROFESION =db.Column(db.String(30));
    PRODUCCION_CIENTIFICA =db.Column(db.String(30));
    PROYECTOS_INVESTIGACION =db.Column(db.String(30));
    EXPERIENCIA =db.Column(db.String(30));
    ANOS_EXPERIENCIA = db.Column(db.String(30));
    GENERO =db.Column(db.String(30));
    EX_RECTOR =db.Column(db.String(30));
    TIPO_PERSONALIDAD=db.Column(db.String(30));
    GESTION =db.Column(db.String(30));
    TIPO_UNIV=db.Column(db.String(30));

#----------------------------#
#------ENTITY CANDIDATES-----#
#----------------------------#

class CANDIDATO(db.Model):

    ID= db.Column(db.Integer,primary_key=True)
    NOMBRE =db.Column(db.String(100));
    ID_UNIVERSIDAD =db.Column(db.Integer);
    EDAD =db.Column(db.String(30));
    ANTECEDENTES_CORRUPCION=db.Column(db.String(30));
    GRADO_ESTUDIO=db.Column(db.String(30));
    ESTUDIOS_GESTION_PUBLICA = db.Column(db.String(10));
    PROFESION =db.Column(db.String(30));
    PRODUCCION_CIENTIFICA =db.Column(db.String(30));
    PROYECTOS_INVESTIGACION =db.Column(db.String(30));
    EXPERIENCIA =db.Column(db.String(30));
    ANOS_EXPERIENCIA = db.Column(db.String(30));
    GENERO =db.Column(db.String(30));
    TIPO_PERSONALIDAD = db.Column(db.String(30));
    EX_RECTOR =db.Column(db.String(30));
    FILENAME = db.Column(db.String(30));

#----------------------------#
#--------ENTITY COLLEGE------#
#----------------------------#

class UNIVERSIDAD(db.Model):

    ID_UNIVERSIDAD = db.Column(db.Integer, primary_key=True)
    NOM_UNIVERSIDAD = db.Column(db.String(50));

#----------------------------#
#---------CONTROLLERS--------#
#----------------------------#

#----------------------------#
#------------HOME------------#
#----------------------------#

@app.route("/")
def main2():

        return render_template("inicio.html", title="data")


@app.route("/upload_0", methods=["GET","POST"])
def upload_0():

        return render_template("inicio.html", title="data")

#----------------------------#
#-----EMULATE MANAGEMENT-----#
#----------------------------#

@app.route("/upload0", methods=["GET","POST"])
def upload0():

        return render_template("index.html", title="data")

#----------------------------#
#-----------ACTIONS----------#
#----------------------------#

#----------------------------#
#-----EMULATE MANAGEMENT-----#
#----------------------------#

@app.route("/upload", methods=["GET","POST"])
def upload():

    # ----------------------------#
    # ---------UPLOAD DATA--------#
    # ----------------------------#

    global edad, expe2
    global ante
    global prod
    global proy
    global exre
    global tipo

    nombre = str(request.form["nombre"])
    universidad = str(request.form["universidad"])
    profesion = str(request.form["profesion"])

    edad = request.form['edad'];
    ante = request.form['antecedentes'];
    adm = request.form['administracion'];
    prod = request.form['produccion'];
    proy = request.form['proyectos'];
    anos_expe = request.form['experiencia'];
    exre = request.form['exrector'];
    tipo=  request.form['home'];

    if (ante=="si"):
        ante2=1;
    else:
        ante2=0;

    if (adm=="si"):
        adm2=1;
    else:
        adm2=0;

    if (prod=="si"):
        prod2=1;
    else:
        prod2=0;

    if (proy=="si"):
        proy2=1;
    else:
        proy2 = 0;

    if (anos_expe=="1"):

        expe="1-5"
        expe2=0
    else:
        if(anos_expe=="2"):
            expe = "6-10"
            expe2 = 3
        else:
            if (anos_expe == "3"):
                expe = "11-15"
                expe2 = 1
            else:
                if (anos_expe == "4"):
                    expe = "16 a mas"
                    expe2 = 2
                else:

                        expe = "No experiencia"
                        expe2 = 4


    if (exre == "si"):
        exre2 = 1;
    else:
        exre2 = 0;

    tipo2 = int(tipo);

    if (tipo2 == 3):
        tipo_personalidad = "ARQUITECTO";


    else:
        if (tipo2 == 11):
            tipo_personalidad = "LOGICO";


        else:
            if (tipo2 ==5):

                tipo_personalidad = "COMANDANTE"

            else:
                if (tipo2 == 10):
                    tipo_personalidad = "INNOVADOR"


                else:
                    if (tipo2 == 0):
                        tipo_personalidad = "ABOGADO"


                    else:
                        if (tipo2 == 13):
                            tipo_personalidad = "MEDIADOR"


                        else:
                            if (tipo2 == 14):
                                tipo_personalidad = "PROTAGONISTA"

                            else:
                                if (tipo2 == 1):
                                    tipo_personalidad = "ACTIVISTA"


                                else:
                                    if (tipo2 == 12):
                                        tipo_personalidad = "LOGISTA"


                                    else:
                                        if (tipo2 == 7):
                                            tipo_personalidad = "DEFENSOR"


                                        else:
                                            if (tipo2 == 8):
                                                tipo_personalidad = "EJECUTIVO"


                                            else:
                                                if (tipo2 == 6):
                                                    tipo_personalidad = "CONSUL"


                                                else:
                                                    if (tipo2 == 15):
                                                        tipo_personalidad = "VIRTUOSO"


                                                    else:
                                                        if (tipo2 == 4):
                                                            tipo_personalidad = "AVENTURERO"


                                                        else:
                                                            if (tipo2 == 9):
                                                                tipo_personalidad = "EMPRENDEDOR"


                                                            else:

                                                                tipo_personalidad = "ANIMADOR"

    # ----------------------------#
    # ----SET X AND Y(TEST.PY)----#
    # ----------TRAINNING---------#
    # ----------------------------#

    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(Get_X(),Get_Y());

    from sklearn.preprocessing import StandardScaler
    scaler=StandardScaler();
    scaler.fit(x_train);
    x_train=scaler.transform(x_train);
    x_test=scaler.transform(x_test);

    # ----------------------------#
    # NOW PREDICT WITH INPUT DATA #
    # ----------------------------#

    from sklearn.ensemble import RandomForestClassifier
    rfc = RandomForestClassifier();
    rfc.fit(x_train, y_train);
    print (rfc.score(x_test, y_test));

    pred2 = rfc.predict([[ante2,adm2, prod2, proy2, expe2, exre2,tipo2
                          ]]);
    print (pred2);

    #----------------------------------#
    #--SETTING PRED IN INTERVAL 1-100--#
    #----------------------------------#

    if (pred2 == [0]):
        pred2 = random.randrange(5, 15);

    if (pred2 == [2]):
        pred2 = random.randrange(15, 25);

    if (pred2 == [3]):
        pred2 = random.randrange(25, 35);

    if (pred2 == [4]):
        pred2 = random.randrange(35, 45);

    if (pred2 == [5]):
        pred2 = random.randrange(45, 55);

    if (pred2 == [6]):
        pred2 = random.randrange(55, 65);

    if (pred2 == [7]):
        pred2 = random.randrange(65, 75);

    if (pred2 == [8]):
        pred2 = random.randrange(75, 85);

    if (pred2 == [9]):
        pred2 = random.randrange(85, 95);

    if (pred2 == [1]):
        pred2 = random.randrange(90, 95);

    # ----------------------------#
    # -----SET LEVEL OF TRUST-----#
    # ----------------------------#

    conf=int(rfc.score(x_test, y_test)*100);

    type(pred2)

    print (tipo)

    print (pred2)

    return render_template("simular.html",nombre=nombre,universidad=universidad, edad=edad,ante=ante,prod=prod,proy=proy,
                           adm=adm, exre=exre,profesion=profesion, pred2=pred2,conf=conf,econ=tipo_personalidad,edu=expe);

#----------------------------#
#-----UPLOAD STATISTICS------#
#----------------------------#

@app.route("/upload2",methods=["GET","POST"])
def upload2(chartID = 'chart_ID', chart_type = 'pie', chart_height = 500,chart_width= 800, chart2ID = 'chart2_ID', chart2_type = 'line', chart2_height = 500,chart_width2= 800,chart3ID = 'chart3_ID', chart3_type = 'column', chart3_height = 500,chart_width3= 800):

    subtitleText='test';
    pageType = "graph";

    cant_rect = RECTORES.query.filter_by(ANTECEDENTES_CORRUPCION="Si").count();
    cant_rect2 = RECTORES.query.filter_by(ANTECEDENTES_CORRUPCION="No").count();

    cant_tip = RECTORES.query.filter_by(TIPO_UNIV="Publica").count();

    var1=(cant_rect2*100)/29
    var2=100-var1;

    var11 = (cant_tip * 100) / 29
    var22 = 100 - var11;

    #-------PRIMER GRAFICO------------------#
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, "width": chart_width,"plotBackgroundColor": "gray"};
    series=[{"name":'Porcentaje',"data": [{"name": 'SI TIENEN ANTECENDENTES: '+str(var1)+'%',"y":int(var1)}, {"name": 'NO TIENEN ANTECEDENTES '+str(var2)+'%',"y":int(var2)}]}];

    graphtitle = {"text": 'ANTECEDENTES DE CORRUPCION'}
    xAxis = {"categories": Get_Categories(), "title": {"text": 'Nombre'}}
    yAxis = {"categories": ['Buena', 'Mala', 'Promedio'], "title": {"text": 'Gestion'}}

    # -------SEGUNDO GRAFICO------------------#
    chart2 = {"renderTo": chart2ID, "type": chart2_type, "height": chart2_height,"width":chart_width2,"plotBackgroundColor": "gray","plotShadow": "false",};
    series2 = [{"name": 'Label1', "data":Get_Dataset()}];
    title2 = {"text": 'HISTORIA DE RECTORES'}
    xAxis2 = {"categories": Get_Categories(),"title": {"text": 'Nombre'}}
    yAxis2 = {"categories": ['1', '2', '3','4','5','6','7','8','9','10'],"title": {"text": 'Gestion'}}

    # -------TERCER GRAFICO------------------#
    chart3 = {"renderTo": chart3ID, "type": chart3_type, "height": chart3_height, "width": chart_width3,"plotBackgroundColor": "gray"};
    series3 = [{"name": 'Porcentaje', "data": [{"name": 'RECTORES EN UNIV. PUBLICAS: ' + str(var11) + '%', "y": int(var11)},
                                              {"name": 'RECTORES EN UNIV. PRIVADAS: ' + str(var22) + '%', "y": int(var22)}]}];

    graphtitle3 = {"text": 'CLASIFICACION DE UNIVERSIDADES'}
    xAxis3 = {"categories": ['Privadas','Publicas'], "title": {"text": 'Tipo de Universidad'}}
    yAxis3 = {"title": {"text": 'Porcentaje'}}

    return render_template('index2.html', chartID=chartID,pageType=pageType,subtitleText=subtitleText, chart=chart, series=series, graphtitle=graphtitle, xAxis=xAxis, yAxis=yAxis,chart2ID=chart2ID, chart2=chart2, series2=series2, title2=title2, xAxis2=xAxis2, yAxis2=yAxis2,chart3ID=chart3ID, chart3=chart3, series3=series3, graphtitle3=graphtitle3, xAxis3=xAxis3, yAxis3=yAxis3)


#----------------------------#
#------UPLOAD COLLEGES-------#
#----------------------------#

@app.route("/upload3", methods=["GET","POST"])
def upload3():

    myuniv = UNIVERSIDAD.query.all();

    return render_template('index3.html', myuniv=myuniv);

#----------------------------#
#-------UPLOAD RECTORS-------#
#----------------------------#

@app.route("/upload4", methods=["GET", "POST"])
def upload4():

    mycandidato = RECTORES.query.all();

    return render_template('index4.html', mycandidato=mycandidato);

#-------------------------------------------#
#------UPLOAD COLLEGES AND CANDIDATES-------#
#-------------------------------------------#

@app.route("/upload5", methods=["GET", "POST"])
def upload5():

    id_univ = str(request.form["homer"])

    mycandidat = CANDIDATO.query.filter_by(ID_UNIVERSIDAD=id_univ).all();
    myuniv = UNIVERSIDAD.query.all();

    return render_template('index5.html',mycandidat=mycandidat,myuniv=myuniv);

#------------------------------------------#
#-----EMULATE MANAGEMENT ON CANDIDATES-----#
#------------------------------------------#

@app.route("/upload6", methods=["GET","POST"])
def upload6():

    global tipo2, expe2
    id_candidat = (request.form["imageField"]);

    print (id_candidat);

    mycandidat = CANDIDATO.query.filter_by(ID=id_candidat).first();

    nombre = mycandidat.NOMBRE
    id_universidad = mycandidat.ID_UNIVERSIDAD
    profesion = mycandidat.PROFESION
    edad = mycandidat.EDAD
    ante = mycandidat.ANTECEDENTES_CORRUPCION
    adm = mycandidat.ESTUDIOS_GESTION_PUBLICA
    prod = mycandidat.PRODUCCION_CIENTIFICA
    proy = mycandidat.PROYECTOS_INVESTIGACION
    anos_expe = mycandidat.ANOS_EXPERIENCIA
    tipo_personalidad=mycandidat.TIPO_PERSONALIDAD
    exre = mycandidat.EX_RECTOR

    if (id_universidad==1):

        universidad="UNAC";

    else:

        universidad = "PUCP";

    if (ante=="Si"):
        ante2=1;
    else:
        ante2=0;

    if (adm=="Si"):
        adm2=1;
    else:
        adm2=0;

    if (prod=="Si"):
        prod2=1;
    else:
        prod2=0;

    if (proy=="Si"):
        proy2=1;
    else:
        proy2 = 0;

    if (anos_expe=="1-5"):
        expe2=0
    else:
        if(anos_expe=="6-10"):
            expe2 = 3
        else:
            if (anos_expe == "11-15"):
                expe2 = 1
            else:
                if (anos_expe == "16 a mas"):
                    expe2 = 2
                else:

                        expe2 = 4

    if (exre == "Si"):
        exre2 = 1;
    else:
        exre2 = 0;

    if(tipo_personalidad=="ARQUITECTO"):

        tipo2=3

    else:
        if (tipo_personalidad == "LOGICO"):

            tipo2 = 11

        else:
            if (tipo_personalidad == "COMANDANTE"):

                tipo2 = 5

            else:
                if (tipo_personalidad == "INNOVADOR"):

                    tipo2 = 10

                else:
                    if (tipo_personalidad == "ABOGADO"):

                        tipo2 = 0

                    else:
                        if (tipo_personalidad == "MEDIADOR"):

                            tipo2 = 13

                        else:
                            if (tipo_personalidad == "PROTAGONISTA"):

                                tipo2 = 14

                            else:
                                if (tipo_personalidad == "ACTIVISTA"):

                                    tipo2 = 1

                                else:
                                    if (tipo_personalidad == "LOGISTA"):

                                        tipo2 = 12

                                    else:
                                        if (tipo_personalidad == "DEFENSOR"):

                                            tipo2 = 7

                                        else:
                                            if (tipo_personalidad == "EJECUTIVO"):

                                                tipo2 = 8

                                            else:
                                                if (tipo_personalidad == "CONSUL"):

                                                    tipo2 = 6

                                                else:
                                                    if (tipo_personalidad == "VIRTUOSO"):

                                                        tipo2 = 15

                                                    else:
                                                        if (tipo_personalidad == "AVENTURERO"):

                                                            tipo2 = 4

                                                        else:
                                                            if (tipo_personalidad == "EMPRENDEDOR"):

                                                                tipo2 = 9

                                                            else:
                                                                if (tipo_personalidad == "ANIMADOR"):

                                                                    tipo2 = 2

    # ----------------------------#
    # ----SET X AND Y(TEST.PY)----#
    # ----------TRAINNING---------#
    # ----------------------------#

    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(Get_X(), Get_Y());

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler();
    scaler.fit(x_train);
    x_train = scaler.transform(x_train);
    x_test = scaler.transform(x_test);

    # ----------------------------#
    # NOW PREDICT WITH INPUT DATA #
    # ----------------------------#

    from sklearn.ensemble import RandomForestClassifier
    rfc = RandomForestClassifier();
    rfc.fit(x_train, y_train);
    print (rfc.score(x_test, y_test));

    pred2 = rfc.predict([[ante2,adm2,prod2, proy2,expe2, exre2,tipo2]]);
    print (pred2);

    # ----------------------------------#
    # --SETTING PRED IN INTERVAL 1-100--#
    # ----------------------------------#

    if (pred2 == [0]):
        pred2 = random.randrange(5, 15);

    if (pred2 == [2]):
        pred2 = random.randrange(15, 25);

    if (pred2 == [3]):
        pred2 = random.randrange(25, 35);

    if (pred2 == [4]):
        pred2 = random.randrange(35, 45);

    if (pred2 == [5]):
        pred2 = random.randrange(45, 55);

    if (pred2 == [6]):
        pred2 = random.randrange(55, 65);

    if (pred2 == [7]):
        pred2 = random.randrange(65, 75);

    if (pred2 == [8]):
        pred2 = random.randrange(75, 85);

    if (pred2 == [9]):
        pred2 = random.randrange(85, 95);

    if (pred2 == [1]):
        pred2 = random.randrange(90, 95);

    # ----------------------------#
    # -----SET LEVEL OF TRUST-----#
    # ----------------------------#

    conf = int(rfc.score(x_test, y_test) * 100);

    type(pred2)

    return render_template("simular.html", nombre=nombre, universidad=universidad, edad=edad, ante=ante, prod=prod,
                           proy=proy,
                           expe=anos_expe,adm=adm, exre=exre, profesion=profesion, pred2=pred2,
                           conf=conf,econ=tipo_personalidad,edu=anos_expe);

#--------------#
#-----MAIN-----#
#--------------#

if __name__ == "__main__":
    app.run(port=4555,debug=True)


