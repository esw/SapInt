class ConversionNoExiste(Exception):
    """
    El factor de conversion entre las medidas no existe
    """
    pass

class UnidadMedidaNoExiste(Exception):
    """
    La Unidad de medida no existe
    """
    pass

class SistemaMedidaNoExiste(Exception):
    """
    El sistema de medida no existe
    """
    pass

class TipoUnidadNoExiste(Exception):
    """
    El tipo de unidad de medida no existe
    """
    pass

class TipoNoCompatible(Exception):
    """
    El tipo de unidad de medida no es compatible para hacer operaciones entre las medidas
    """
    pass