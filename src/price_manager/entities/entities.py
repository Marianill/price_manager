
class Categoria:
    def __init__(self, id: int, nombre: str):
        """ Constructor
        Args:
            id (int): El identificador único de la categoría.
            nombre (str): El nombre de la categoría.
        """
        self.__id:int = id
        self.__nombre:str = nombre

    @property
    def id(self):
        """ Getter para el atributo id.
        Returns:
            int: El identificador único de la categoría.
        """
        return self.__id

    @id.setter
    def id(self, id: int):
        """ Setter para el atributo id.
        Args:
            id (int): El nuevo identificador de la categoría.
        """
        self.__id = id

    @property
    def nombre(self):
        """ Getter para el atributo nombre.
        Returns:
            str: El nombre de la categoría.
        """
        return self.__nombre
  
    @nombre.setter
    def nombre(self, nombre: str):
        """ Setter para el atributo nombre.
        Args:
            nombre (str): El nuevo nombre de la categoría.
        """
        self.__nombre = nombre
        
        
class Proveedor:
    def __init__(self, id: int, nombre: str, contacto: str):
        """ Constructor
        Args:
            id (int): El identificador único del proveedor.
            nombre (str): El nombre legal del proveedor.
            contacto (str): La vía de contacto del proveedor.
        """
        self.__id:int = id
        self.__nombre:str = nombre
        self.__contacto:str = contacto

    @property
    def id(self):
        """ Getter para el atributo id.
        Returns:
            int: El identificador único del proveedor.
        """
        return self.__id

    @id.setter
    def id(self, id: int):
        """ Setter para el atributo id.
        Args:
            id (int): El nuevo identificador del proveedor.
        """
        self.__id = id

    @property
    def nombre(self):
        """ Getter para el atributo nombre.
        Returns:
            str: El nombre legal del proveedor.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """ Setter para el atributo nombre.
        Args:
            nombre (str): El nuevo nombre legal del proveedor.
        """
        self.__nombre = nombre
    
    @property
    def contacto(self):
        """ Getter para el atributo contacto.
        Returns:
            str: La vía de contacto del proveedor.
        """
        return self.__contacto

    @contacto.setter
    def contacto(self, contacto: str):
        """ Setter para el atributo contacto.
        Args:
            contacto (str): La nueva vía de contacto del proveedor.
        """
        self.__contacto = contacto


class Precio:
    def __init__(self, id: int, valor: float, moneda: str, fecha: datetime.date):
        """ Constructor
        Args:
            id (int): El identificador único del precio.
            valor (float): El valor del precio.
            moneda (str): La moneda del precio.
            fecha (datetime.date): La fecha del precio.
        """
        self.__id:int = id
        self.__valor:float = valor
        self.__moneda:str = moneda
        self.__fecha:datetime.date = fecha

    @property
    def id(self):
        """ Getter para el atributo id.
        Returns:
            int: El identificador único del precio.
        """
        return self.__id
    
    @id.setter
    def id(self, id: int):
        """ Setter para el atributo id.
        Args:
            id (int): El nuevo identificador del precio.
        """
        self.__id = id

    @property
    def valor(self):
        """ Getter para el atributo valor.
        Returns:
            float: El valor del precio.
        """
        return self.__valor

    @valor.setter
    def valor(self, nuevo_valor: float):
        """ Setter para el atributo valor.
        Args:
            valor (float): El nuevo valor del precio.
        """
        if self.validar_valorPrecio(nuevo_valor):
            self.__valor = nuevo_valor
        else:
            print("El valor del precio debe ser mayor a cero.")

    @property
    def moneda(self):
        """ Getter para el atributo moneda.
        Returns:
            str: La moneda del precio.
        """
        return self.__moneda

    @moneda.setter
    def moneda(self, nueva_moneda: str):
        """ Setter para el atributo moneda.
        Args:
            moneda (str): La nueva moneda del precio.
        """
        if self.validar_moneda(nueva_moneda):
            self.__moneda = nueva_moneda
        else:
            print("La moneda del precio debe tener 3 caracteres.")

    @property
    def fecha(self):
        """ Getter para el atributo fecha.
        Returns:
            datetime.date: La fecha del precio.
        """
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha: datetime.date):
        """ Setter para el atributo fecha.
        Args:
            fecha (datetime.date): La nueva fecha del precio.
        """
        self.__fecha = fecha
    
    def validar_valorPrecio(self, valor):
        """ Valida que el valor del precio sea mayor o igual a cero.
        """
        if valor <= 0:
            return False
        return True

    def validar_moneda(self, moneda):
        """ Valida que la moneda del precio sea una cadena de 3 caracteres.
        """
        if len(moneda) == 3:
            return True
        return False
  

class CotizacionDolar:
    def __init__(self, tipo: str, valor: float, fecha: datetime.date, tipo_id: int):
        """ Constructor
        Args:
            tipo (str): El tipo de cotización.
            valor (float): El valor de la cotización.
            fecha (datetime.date): La fecha de la cotización.
        """
        self.__tipo_id = tipo_id
        self.__tipo:str = tipo
        self.__valor:float = valor
        self.__fecha:datetime.date = fecha

    @property
    def tipo(self):
        """ Getter para el atributo tipo.
        Returns:
            str: El tipo de cotización.
        """
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        """ Setter para el atributo tipo.
        Args:
            tipo (str): El nuevo tipo de cotización.
        """
        self.__tipo = tipo

    @property
    def tipo_id(self):
        """ Getter para el atributo tipo_id.
        Returns:
            int: El identificador único del tipo de cotización.
        """
        return self.__tipo_id
    
    @tipo_id.setter
    def tipo_id(self, tipo_id: int):
        """ Setter para el atributo tipo_id.
        Args:
            tipo_id (int): El nuevo identificador del tipo de cotización.
        """
        self.__tipo_id = tipo_id

    @property
    def valor(self):
        """ Getter para el atributo valor.
        Returns:
            float: El valor de la cotización.
        """
        return self.__valor

    @valor.setter
    def valor(self, nuevo_valor: float):
        """ Setter para el atributo valor.
        Args:
            valor (float): El nuevo valor de la cotización.
        """
        if self.validar_valorCotizacion(nuevo_valor):
            self.__valor = nuevo_valor
        else:
            print("El valor de la cotización debe ser positivo.")

    @property
    def fecha(self):
        """ Getter para el atributo fecha.
        Returns:
            datetime.date: La fecha de la cotización.
        """
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha: datetime.date):
        """ Setter para el atributo fecha.
        Args:
            fecha (datetime.date): La nueva fecha de la cotización.
        """
        self.__fecha = fecha

    def validar_valorCotizacion(self, nuevo_valor):
        """ Valida que el valor de la cotización sea positivo.
        """
        if nuevo_valor < 0:
            return False
        return True

  
class Producto:
    def __init__(self, id: int, nombre: str, descripcion: str, precio: Precio, categoria: Categoria, proveedor: Proveedor):
        """ Constructor
        Args:
            id (int): El identificador único del producto.
            nombre (str): El nombre del producto.
            descripcion (str): La descripción del producto.
            precio (Precio): El precio del producto.
            categoria (Categoria): La categoría del producto.
            proveedor (Proveedor): El proveedor del producto.
        """
        self.__id:int = id
        self.__nombre:str = nombre
        self.__descripcion:str = descripcion
        self.__precio:Precio = precio
        self.__categoria:Categoria = categoria
        self.__proveedor:Proveedor = proveedor

    @property
    def id(self):
        """ Getter para el atributo id.
        Returns:
            int: El identificador único del producto.
        """
        return self.__id

    @id.setter
    def id(self, id: int):
        """ Setter para el atributo id.
        Args:
            id (int): El nuevo identificador del producto.
        """
        self.__id = id

    @property
    def nombre(self):
        """ Getter para el atributo nombre.
        Returns:
            str: El nombre del producto.
        """
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """ Setter para el atributo nombre.
        Args:
            nombre (str): El nuevo nombre del producto.
        """
        self.__nombre = nombre

    @property
    def descripcion(self):
        """ Getter para el atributo descripcion.
        Returns:
            str: La descripción del producto.
        """
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        """ Setter para el atributo descripcion.
        Args:
            descripcion (str): La nueva descripción del producto.
        """
        self.__descripcion = descripcion

    @property
    def precio(self):
        """ Getter para el atributo precio.
        Returns:
            Precio: El precio del producto.
        """
        return self.__precio

    @precio.setter
    def precio(self, precio: Precio):
        """ Setter para el atributo precio.
        Args:
            precio (Precio): El nuevo precio del producto.
        """
        self.__precio = precio

    @property
    def categoria(self):
        """ Getter para el atributo categoria.
        Returns:
            Categoria: La categoría del producto.
        """
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria: Categoria):
        """ Setter para el atributo categoria.
        Args:
            categoria (Categoria): La nueva categoría del producto.
        """
        self.__categoria = categoria

    @property
    def proveedor(self):
        """ Getter para el atributo proveedor.
        Returns:
            Proveedor: El proveedor del producto.
        """
        return self.__proveedor

    @proveedor.setter
    def proveedor(self, proveedor: Proveedor):
        """ Setter para el atributo proveedor.
        Args:
            proveedor (Proveedor): El nuevo proveedor del producto.
        """
        self.__proveedor = proveedor

    
class Stock:
    def __init__(self, producto_id: int, cantidad: int):
        """ Constructor
        Args:
            producto_id (int): El identificador único del producto.
            cantidad (int): La cantidad en stock del producto.
        """
        self.__producto_id:int = producto_id
        self.__cantidad:int = cantidad

    @property
    def producto_id(self):
        """ Getter para el atributo producto_id.
        Returns:
            int: El identificador único del producto.
        """
        return self.__producto_id

    @producto_id.setter
    def producto_id(self, producto_id: int):
        """ Setter para el atributo producto_id.
        Args:
            producto_id (int): El nuevo identificador del producto.
        """
        self.__producto_id = producto_id

    @property
    def cantidad(self):
        """ Getter para el atributo cantidad.
        Returns:
            int: La cantidad en stock del producto.
        """
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        """ Setter para el atributo cantidad.
        Args:
            cantidad (int): La nueva cantidad en stock del producto.
        """
        if self.validar_cantidad_producto(nueva_cantidad):
            self.__cantidad = nueva_cantidad
        else:
            print("La cantidad en stock debe ser mayor a cero.")

    def validar_cantidad_producto(self, cantidad):
        """ Valida que la cantidad en stock de un producto sea mayor o igual a cero.
        """
        if cantidad < 0:
            return False
        return True
  
