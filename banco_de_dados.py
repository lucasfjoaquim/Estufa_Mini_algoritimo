import os
from datetime import datetime
import time
import psycopg2
from dotenv import load_dotenv
load_dotenv()


class Banco:
    try:
        url = os.getenv("DATABASE_URL")
        connection = psycopg2.connect(url)
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")

    def execute(self, sql):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
            return
        except Exception as e:
            print(f"Erro com o execute : {e}")
            return "Erro no execute"

    def fetch(self, sql):
        try:
            with self.connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    dados = cursor.fetchall()
            return dados
        except Exception as e:
            print(f"Erro com o fetch : {e}")
            return "Erro no fetch"

    def get_lista_de_plantas(self):
        dados = []
        dados2 = self.fetch("SELECT id,plant_type FROM plant ORDER BY id ")
        ids_com_tipos = {}
        for dado in dados2:
            item = {dado[0]: dado[1]}
            ids_com_tipos.update(item)
            try:
                response = self.fetch("SELECT DISTINCT "
                                        "id,"
                                        "plant_id,"
                                        "temperature,"
                                        "humidity,"
                                        "light,"
                                        "ph,"
                                        "last_time_watered,"
                                        "created_at "
                                        f"FROM plant_info WHERE plant_id = {dado[0]} ORDER BY created_at DESC LIMIT 1")[0]
                dados.append(response)
            except Exception as e:
                print(f"planta {dado[0]} sem dados de status")
        lista_processada = {}
        index = 0
        for dado in dados:
            item = {"id": dado[0],
                    "id_planta": int(dado[1]),
                    "tipo_planta": ids_com_tipos.get(dado[1]),
                    "temperatura": float(dado[2]),
                    "umidade": float(dado[3]),
                    "luz": float(dado[4]),
                    "ph": float(dado[5]),
                    "ultima_vez_regada": self.converter_datetime(dado[6]),
                    "Data_do_registro": self.converter_datetime(dado[7])}

            lista_processada.update({index: item})
            index += 1
        return lista_processada

    def update_plant_status(self, plant_id, status):
        self.execute(f"UPDATE plant SET plant_status = '{status}' WHERE id = {plant_id}")

    def update_plant_warnings(self, plant_id, warnings):
        self.execute(f"UPDATE plant SET warning_level = {warnings} WHERE id = {plant_id}")


    @staticmethod
    def converter_datetime(dt):
        timestamp = dt.timestamp()
        tempo_legivel = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        return tempo_legivel

