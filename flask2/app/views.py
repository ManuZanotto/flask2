from flask import render_template, request
from app import app
from app.controllers import alunos, professores

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/alunos')
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

@app.route('/professores')
def listar_professores():
    return render_template('professores.html', professores=professores)

@app.route('/alunos/<int:aluno_id>')
def detalhes_aluno(aluno_id):
    aluno = alunos[aluno_id]
    return render_template('detalhes_aluno.html', aluno=aluno)

@app.route('/professor/<int:professor_id>')
def detalhes_professor(professor_id):
    professor = professores[professor_id]
    return render_template('detalhes_professor.html', professor=professor)
