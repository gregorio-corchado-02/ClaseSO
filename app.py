from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL



# inicializamos el servidor flask
app= Flask(__name__,static_folder='static',template_folder='templates')

#configuraciones para la conexion a la BD
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="dbcar"

app.secret_key='mysecretkey'

mysql=MySQL(app)



#declaramos una ruta

#ruta index o principal http://localhost:5000
#la ruta se compone de nombre y la funcion



#Creando mi primer Decorador o ruta para el Home
@app.route('/', methods=['GET','POST'])
def inicio():
    
    CS=mysql.connection.cursor()
    CS.execute ("SELECT * FROM autos ORDER BY id_auto")
    mysql.connection.commit()
    data = CS.fetchall() #fetchall () Obtener todos los registros

    total = CS.rowcount #total de registros

    print(total)
    return render_template('consultar.html', dataAutos = data, dataTotal = total)



#ejecucion 
if __name__== '__main__':
    app.run(port= 5000, debug=True)