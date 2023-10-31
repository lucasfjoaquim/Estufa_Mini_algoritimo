from dicionarios import dict_mestre


class ComparadorPlantas:

    def comparar_universal(self, planta_dict):

        temperatura, umidade = planta_dict.get("temperatura"), planta_dict.get("umidade")
        luz, ph = planta_dict.get("luz"), planta_dict.get("ph")
        warnings = 0
        status = ""
        tipo_planta = planta_dict.get("tipo_planta")
        comparacao_dict = dict_mestre[tipo_planta]
        # comparador status temperatura
        if comparacao_dict["temperatura"]["neutro"]["comp2"] is None:
            if comparacao_dict["temperatura"]["favoravel"][0] <= temperatura <= comparacao_dict["temperatura"]["favoravel"][1]:
                status += "temperature : favoravel / "
            elif comparacao_dict["temperatura"]["neutro"]["comp1"][0] <= temperatura <= comparacao_dict["temperatura"]["neutro"]["comp1"][1]:
                status += "temperatura : neutra / "
                warnings += 1
            else:
                status += "temperatura : desfavoravel / "
                warnings += 2
        else:
            if comparacao_dict["temperatura"]["favoravel"][0] <= temperatura <= comparacao_dict["temperatura"]["favoravel"][1]:
                status += "temperature : favoravel / "
            elif comparacao_dict["temperatura"]["neutro"]["comp1"][0] <= temperatura <= comparacao_dict["temperatura"]["neutro"]["comp1"][1] or comparacao_dict["temperatura"]["neutro"]["comp2"][0] <= temperatura <= comparacao_dict["temperatura"]["neutro"]["comp2"][1]:
                status += "temperatura : neutra / "
                warnings += 1
            else:
                status += "temperatura : desfavoravel / "
                warnings += 2

        # controlador status umidade
        if comparacao_dict["umidade"]["neutro"]["comp2"] is None:
            if comparacao_dict["umidade"]["favoravel"][0] <= umidade <= comparacao_dict["umidade"]["favoravel"][1]:
                status += "umidade : favoravel / "
            elif comparacao_dict["umidade"]["neutro"]["comp1"][0] <= umidade <= comparacao_dict["umidade"]["neutro"]["comp1"][1]:
                status += "umidade : neutra / "
                warnings += 1
            else:
                status += "umidade : desfavoravel / "
                warnings += 2
        else:
            if comparacao_dict["umidade"]["favoravel"][0] <= umidade <= comparacao_dict["umidade"]["favoravel"][1]:
                status += "umidade : favoravel / "
            elif comparacao_dict["umidade"]["neutro"]["comp1"][0] <= umidade <= comparacao_dict["umidade"]["neutro"]["comp1"][1] or comparacao_dict["umidade"]["neutro"]["comp2"][0] <= umidade <= comparacao_dict["umidade"]["neutro"]["comp2"][1]:
                status += "umidade : neutra / "
                warnings += 1
            else:
                status += "umidade : desfavoravel / "
                warnings += 2

        # controlador status horas de luz
        horas_de_luz = self.tranforma_porcentagem_de_luz_diaria_em_horas(luz)
        if comparacao_dict["luz"]["neutro"]["comp2"] is None:
            if comparacao_dict["luz"]["favoravel"][0] <= horas_de_luz <= comparacao_dict["luz"]["favoravel"][1]:
                status += "luminosidade : favoravel / "
            elif comparacao_dict["luz"]["neutro"]["comp1"][0] <= horas_de_luz <= comparacao_dict["luz"]["neutro"]["comp1"][1]:
                status += "luminosidade : neutra / "
                warnings += 1
            else:
                status += "luminosidade : desfavoravel / "
                warnings += 2
        else:
            if comparacao_dict["luz"]["favoravel"][0] <= horas_de_luz <= comparacao_dict["luz"]["favoravel"][1]:
                status += "luminosidade : favoravel / "
            elif comparacao_dict["luz"]["neutro"]["comp1"][0] <= horas_de_luz <= comparacao_dict["luz"]["neutro"]["comp1"][1] or comparacao_dict["luz"]["neutro"]["comp2"][0] <= horas_de_luz <= comparacao_dict["luz"]["neutro"]["comp2"][1]:
                status += "luminosidade : neutra / "
                warnings += 1
            else:
                status += "luminosidade : desfavoravel / "
                warnings += 2

        # controlador status ph
        if comparacao_dict["ph"]["neutro"]["comp2"] is None:
            if comparacao_dict["ph"]["favoravel"][0] <= ph <= comparacao_dict["ph"]["favoravel"][1]:
                status += "ph : favoravel "
            elif comparacao_dict["ph"]["neutro"]["comp1"][0] <= ph <= comparacao_dict["ph"]["neutro"]["comp1"][1]:
                status += "ph : neutro "
                warnings += 1
            else:
                status += "ph : desfavoravel "
                warnings += 2
        else:
            if comparacao_dict["ph"]["favoravel"][0] <= ph <= comparacao_dict["ph"]["favoravel"][1]:
                status += "ph : favoravel "
            elif comparacao_dict["ph"]["neutro"]["comp1"][0] <= ph <= comparacao_dict["ph"]["neutro"]["comp1"][1] or comparacao_dict["ph"]["neutro"]["comp2"][0] <= ph <= comparacao_dict["ph"]["neutro"]["comp2"][1]:
                status += "ph : neutro "
                warnings += 1
            else:
                status += "ph : desfavoravel "
                warnings += 2
        resposta = {"status" : status, "warnings" : warnings}
        return resposta

    @staticmethod
    def tranforma_porcentagem_de_luz_diaria_em_horas(porcentagem_de_luz):
        horas_de_luz = (porcentagem_de_luz / 10) * 2.4
        return horas_de_luz

