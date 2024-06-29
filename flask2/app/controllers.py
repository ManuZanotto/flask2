from app.models import Aluno, Professor

alunos = [
    Aluno("Ana Carolina Nunes", 20, "https://github.com/anacarolina", "https://linkedin.com/in/anacarolina", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Arthur Cantele Palmira", 21, "https://github.com/arthurcantele", "https://linkedin.com/in/arthurcantele", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Arthur Fogaça", 22, "https://github.com/arthurfogaca", "https://linkedin.com/in/arthurfogaca", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Arthur Zinani Pedroni", 23, "https://github.com/arthurzinani", "https://linkedin.com/in/arthurzinani", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Bernardo Mossi", 20, "https://github.com/bernardomossi", "https://linkedin.com/in/bernardomossi", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Carolina Sachet", 21, "https://github.com/carolinasachet", "https://linkedin.com/in/carolinasachet", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Caroline Orlandí Bigolin", 22, "https://github.com/carolinebigolin", "https://linkedin.com/in/carolinebigolin", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Eduarda Salvador Terhorst", 23, "https://github.com/eduardaterhorst", "https://linkedin.com/in/eduardaterhorst", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Eduardo Augusto Picinin", 20, "https://github.com/eduardopicinin", "https://linkedin.com/in/eduardopicinin", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Eduardo Hainzenreder Pedroso", 21, "https://github.com/eduardopedroso", "https://linkedin.com/in/eduardopedroso", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Estevan de Paula", 22, "https://github.com/estevande", "https://linkedin.com/in/estevande", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Gabriel Carvalho Susin", 23, "https://github.com/gabrielsusin", "https://linkedin.com/in/gabrielsusin", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Gabriel Guerra", 20, "https://github.com/gabrielguerra", "https://linkedin.com/in/gabrielguerra", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Gabriel Zorzi Pezzi", 21, "https://github.com/gabrielpezzi", "https://linkedin.com/in/gabrielpezzi", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Giancarlo Zanetti Malgarizi", 22, "https://github.com/giancarlomalgarizi", "https://linkedin.com/in/giancarlomalgarizi", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Giovanni Camargo Gardenal Morandi", 23, "https://github.com/giovannimorandi", "https://linkedin.com/in/giovannimorandi", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Guilherme Resemini Zanol", 20, "https://github.com/guilhermezanol", "https://linkedin.com/in/guilhermezanol", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Heitor Trotto Mesquita", 21, "https://github.com/heitormesquita", "https://linkedin.com/in/heitormesquita", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Igor Rodrigues Ribeiro", 22, "https://github.com/igorribeiro", "https://linkedin.com/in/igorribeiro", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Ivo Viesser Neto", 23, "https://github.com/ivoneto", "https://linkedin.com/in/ivoneto", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("João Vítor Brombatti Feiten", 20, "https://github.com/joaovitorfeiten", "https://linkedin.com/in/joaovitorfeiten", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("João Vítor Mendes", 21, "https://github.com/joaovitormendes", "https://linkedin.com/in/joaovitormendes", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("João Vítor Michelon", 22, "https://github.com/joaovitormichelon", "https://linkedin.com/in/joaovitormichelon", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Kauã Drum Fortuna", 23, "https://github.com/kauafortuna", "https://linkedin.com/in/kauafortuna", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Manoela Gomes Zanotto", 17, "https://github.com/ManuZanotto", "https://linkedin.com/in/manoelazanotto", "Estudante EM e técnico de Informática.", "https://www.petz.com.br/blog//wp-content/uploads/2019/06/cachorro-filhote.jpg"),
    Aluno("Maria Thereza Adamatti Rizzotto", 21, "https://github.com/mariarizzotto", "https://linkedin.com/in/mariarizzotto", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Otávio Griebeler Turra", 22, "https://github.com/otavioturra", "https://linkedin.com/in/otavioturra", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Pedro David Brum", 23, "https://github.com/pedrobrum", "https://linkedin.com/in/pedrobrum", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Pedro do Nascimento", 20, "https://github.com/pedronascimento", "https://linkedin.com/in/pedronascimento", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Pedro Henrique Gasparin Machado", 21, "https://github.com/pedrogasparin", "https://linkedin.com/in/pedrogasparin", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Rafael Armando Zanella", 22, "https://github.com/rafaelzanella", "https://linkedin.com/in/rafaelzanella", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Vítor Augusto Rumke", 23, "https://github.com/vitorrumke", "https://linkedin.com/in/vitorrumke", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("Vitória Tumelero dos Santos", 20, "https://github.com/vitoriatumelero", "https://linkedin.com/in/vitoriatumelero", "Estudante de Engenharia.", "path/to/photo.jpg"),
    Aluno("William dos Santos da Silva", 21, "https://github.com/williamsilva", "https://linkedin.com/in/williamsilva", "Estudante de Engenharia.", "path/to/photo.jpg"),
]

professores = [
    Professor("Edertec", "https://github.com/edertec", "https://www.instagram.com/edertec", "Professor de Programação e dono da Gautica.", "https://pbs.twimg.com/profile_images/1793819396126679041/ug_z6zHm_400x400.jpg"),
    Professor("Marcelo Fardo", "https://github.com/marcelofardo", "https://linkedin.com/in/arthurcantele", "Professor de Games e coordenador de criação digital na UCS.", "https://0.academia-photos.com/2276301/723973/24484114/s200_marcelo.fardo.jpg"),
    Professor("Cris", "https://github.com/cristinacemin", "https://linkedin.com/in/criscemin", "Professora de Banco de Dados e cordenadora do técnico de Informática do Cetec.", "https://static.vecteezy.com/ti/vetor-gratis/t2/550980-de-icone-de-usuario-gratis-vetor.jpg"),
    Professor("Diego Flores", "https://github.com/didi", "https://linkedin.com/in/diegoflores", "Professor de suportes e redes e mandante do bloco 71.", "https://i1.rgstatic.net/ii/profile.image/908696896929793-1593661631544_Q512/Diego-Flores-11.jpg"),
    Professor("Rafael Perini", "https://github.com/fofis", "https://linkedin.com/in/perini", "Professor de gerenciamento de projetos.", "https://www.conferencebr.com/socioperfil/foto/capa300/1222254.jpg")
]
 