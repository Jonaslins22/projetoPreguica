from flask import Flask, render_template, request, redirect, url_for, flash, session



dados=[]
class Usuario:

    def __init__(self,usuario,senha):
        self.usuario=usuario
        self.senha=senha        


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SECRET_KEY']= 'XUXA'

@app.route('/')
def hello_world(): 
    return render_template('home.html',log = session)

@app.route('/login')
def teste2(): 
    return render_template('login.html')


@app.route('/registro')
def principal():
    return render_template('registro.html')

@app.route('/login',methods=['POST'])
def login():
    login = request.form['usuario']
    senha = request.form['senha']
    for dado in dados:
        if dado.usuario==login:
            if dado.senha==senha:
                session['logado']=dado.usuario
                return redirect('/')
    return redirect('/login')
    

@app.route('/registro',methods=['POST'])
def cadastro():
    usuario = request.form['usuario']
    senha = request.form['senha']
    confirmsenha=request.form['senha2']

    if senha==confirmsenha:
        dados.append(Usuario(usuario,senha))
        return redirect ('/login')
    return redirect ('/registro')

@app.route('/carro')
def auditt():
    return "carro"
    

@app.route('/sair')
def sair():
    del session['logado']
    return redirect ('/login')

if __name__ == '__main__':
    app.run(debug=True)

    
