class CambioBase():
  def __init__(self, baseO, numero, baseC):

    # Ahora en cambio de recibir parametros por inputs
    # los recibe desde la instanciación a la clase

    self.baseO = baseO
    self.numero = 0
    self.convertir = numero
    self.k = len(self.convertir) - 1
    self.baseC = baseC

    self.letras = {}
    self.j = 65
    '''
    Agrega las letras al diccionario
    '''
    for i in range(10, 36):
      self.letras[i] = chr(self.j)
      self.j += 1

  def base_n_10(self):
    '''
    Base n a base 10
    '''
    for i in self.convertir:
      num = 0
      try:
        num = int(i)
      except ValueError:
        for key, value in self.letras.items():
          if value == i:
            num = key
            return ['Error', False]
      finally:
        if num >= self.baseO:
          return ["El número no corresponde a la base dada", False]
        self.numero += num*(self.baseO**self.k)
        self.k -= 1
  
  def base_10_m(self):
    '''
    Base 10 a base m
    '''
    convertido = ""
    while( self.numero != 0 ):
      residuo = int(self.numero % self.baseC)
      self.numero = int(self.numero / self.baseC)

      if(residuo in self.letras):
        convertido += self.letras.get(residuo)
      else:
        convertido += str(residuo)

    #texto = f"El numero { self.convertir } de base { self.baseO } a base { self.baseC } es: "
    return ["".join(reversed(convertido)),True]
