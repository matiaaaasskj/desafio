import temperatura
import masa
import tiempo


def convertir_temperatura(valor, unidad_origen, unidad_destino):
    if unidad_origen == "celsuis" and unidad_destino == "fahrenheir":
     return temperatura.celsius_a_fahrenheit(valor)

def convertir_masa(valor, unidad_origen, unidad_destino):
    if unidad_origen == "kilogramos" and unidad_destino == "gramos":
     return masa.kilogramos_a_gramos(valor)
  
def convertir_tiempo(valor, unidad_origen, unidad_destino):
    if unidad_origen == "segundos" and unidad_destino == "minutos":
      return tiempo.segundos_a_minutos(valor)

if __name__=="__main__":
    valor=20
    unidad_origen="celsius"
    unidad_destino="fahrenheir"
    resultado= convertir_temperatura(valor, unidad_origen, unidad_destino)
    print(f"{valor} grados {unidad_origen} equivale a {resultado} grados {unidad_destino}")