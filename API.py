from flask import Flask,request,Response,jsonify
from flask_cors import CORS

app=Flask(__name__)

#Cualquier IP
cors = CORS(app, resources={r"/*": {"origin": "*"}})
#-------ESTUDIANTES YA REGISTRADOS
Estudiantes=[
    {"nombre":"Isai Figueroa","carnet":201904013},
    {"nombre":"Jonathan Farfán","carnet":201603213},
]

@app.route("/")
def inicio():
    return(jsonify({"ms":'CONSUMIENDO API'}))


@app.route('/peticiones/', methods=['GET'])
def GET():
    print("acabo de realizar un >>> GET")

    return (jsonify(Estudiantes))


@app.route('/peticiones/', methods=['POST'])
def POST():
    n_estudiante={
        "nombre":request.json['nombre'],
        "carnet":request.json['carnet']
    }
    Estudiantes.append(n_estudiante)
    print("--------acabo de realizar un >>> POST--------")


    return (jsonify({"respuesta":"Estudiantes agregado correctamente","Estudiantes":Estudiantes}))

@app.route('/peticiones/<int:carnet>', methods=['PUT'])
def PUT(carnet):
    print("--------acabo de realizar un >>> PUT--------")
    carnetFound = [estudiante for estudiante in Estudiantes if estudiante['carnet'] == carnet]
    if (len(carnetFound) > 0):
        carnetFound[0]['carnet'] = request.json['carnet']
        carnetFound[0]['nombre'] = request.json['nombre']
        return jsonify({
            'message': 'Se modificó correctamente',
            'Estudiantes': Estudiantes
        })
    return jsonify({'message': 'No se encontró el carnet'})
    



@app.route('/peticiones/<int:carnet>', methods=['DELETE'])
def DELETE(carnet):
    print("--------acabo de realizar un >>> DELETE--------")
    carnetFound = [estudiante for estudiante in Estudiantes if estudiante['carnet'] == carnet]
    if (len(carnetFound) > 0):
        Estudiantes.remove(carnetFound[0])
    return jsonify({
        'message': 'Estudiante Eliminado',
        'estudiantes': Estudiantes
    })

if __name__ =='__main__':
    app.run(debug=True,port=5000) 