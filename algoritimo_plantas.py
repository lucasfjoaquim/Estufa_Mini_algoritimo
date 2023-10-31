from banco_de_dados import Banco
from comparador_plantas import ComparadorPlantas
import time
banco = Banco()
comp = ComparadorPlantas()

# escaneia uma planta individual
def verificar_status_planta(planta_dict):
    id_planta = planta_dict.get("id_planta")
    status = comp.comparar_universal(planta_dict)
    print(f"Status da planta {id_planta} sendo atualizados")
    banco.update_plant_status(id_planta, status["status"])
    banco.update_plant_warnings(id_planta, status["warnings"])

# pega a lista de todas as plantas
def escanear_banco():
    plantas_dict = banco.get_lista_de_plantas()
    for i in range(len(plantas_dict)):
        planta_dict = plantas_dict.get(i)
        verificar_status_planta(planta_dict)



