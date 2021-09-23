from models import Logins, Usuario

SQL_DELETA_LOGINS = 'delete from logins where id = %s'
SQL_LOGINS_POR_ID = 'SELECT id, nome, email, senha from emails where id = %s'
SQL_USUARIOS_POR_ID = 'SELECT id, nome, password from usuarios where id = %s'
SQL_ATUALIZA_LOGINS = 'UPDATE logins SET nome=%s, email=%s, senha=%s where id = %s'
SQL_BUSCA_LOGINS = 'SELECT id, nome, email, senha from logins'
SQL_CRIA_LOGINS = 'INSERT into logins (nome, email, senha) values (%s, %s, %s)'


class LoginsDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, logins):
        cursor = self.__db.connection.cursor()

        if (logins.id):
            cursor.execute(SQL_ATUALIZA_LOGINS, (logins.nome, logins.email, logins.senha, logins.id))
        else:
            cursor.execute(SQL_CRIA_LOGINS, (logins.nome, logins.email, logins.senha))
            logins.id = cursor.lastrowid
        self.__db.connection.commit()
        return logins

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LOGINS)
        logins = traduz_logins(cursor.fetchall())
        return logins

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LOGINS_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Logins(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_LOGINS, (id, ))
        self.__db.connection.commit()


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIOS_POR_ID, (id,))
        dados = cursor.fetchone()
        usuarios = traduz_usuarios(dados) if dados else None
        return usuarios


def traduz_logins(logins):
    def cria_logins_com_tupla(tupla):
        return Logins(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_logins_com_tupla, logins))


def traduz_usuarios(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])