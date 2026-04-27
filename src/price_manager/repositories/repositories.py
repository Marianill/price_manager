
T = TypeVar('T', bound=EntidadBase)


class IRepositorio(abc.ABC, Generic[T]):
  """Interfaz para repositorios que manejan entidades con operaciones CRUD básicas."""

  @abc.abstractmethod
  def crear(self, entidad: T) -> T:
    """Crea una nueva entidad en el repositorio.

    Args:
        entidad (T): La entidad a crear.

    Returns:
        T: La entidad creada.

    Raises:
        ValueError: Si ya existe una entidad con el mismo ID.
    """
    pass

  @abc.abstractmethod
  def leer_por_id(self, id: int) -> Optional[T]:
    """Lee una entidad del repositorio por su ID.

    Args:
        id (int): El ID de la entidad a leer.

    Returns:
        Optional[T]: La entidad si se encuentra, None en caso contrario.
    """
    pass

  @abc.abstractmethod
  def leer_todos(self) -> List[T]:
    """Lee todas las entidades del repositorio.

    Returns:
        List[T]: Una lista de todas las entidades.
    """
    pass

  @abc.abstractmethod
  def actualizar(self, entidad: T) -> T:
    """Actualiza una entidad existente en el repositorio.

    Args:
        entidad (T): La entidad a actualizar (debe tener un ID existente).

    Returns:
        T: La entidad actualizada.

    Raises:
        ValueError: Si no se encuentra la entidad para actualizar.
    """
    pass

  @abc.abstractmethod
  def eliminar(self, id: int) -> bool:
    """Elimina una entidad del repositorio por su ID.

    Args:
        id (int): El ID de la entidad a eliminar.

    Returns:
        bool: True si la entidad fue eliminada, False si no se encontró.
    """
    pass


class CategoriaRepository(IRepositorio[Categoria]):
  """Implementación del repositorio de categorías."""

  def __init__(self):
      self.__categorias = {}

  def crear(self, categoria: Categoria) -> Categoria:
        if categoria.id in self.__categorias:
            raise ValueError("Ya existe una categoría con el mismo ID.")
        self.__categorias[categoria.id] = categoria
        return categoria

  def leer_por_id(self, id: int) -> Optional[Categoria]:
        return self.__categorias.get(id)

  def leer_todos(self) -> List[Categoria]:
        return self.__categorias.values()

  def actualizar(self, categoria: Categoria) -> Categoria:
        if categoria.id not in self.__categorias:
            raise ValueError("No se encontró la categoría para actualizar.")
        self.__categorias[categoria.id] = categoria
        return categoria

  def eliminar(self, id: int) -> bool:
        if id not in self.__categorias:
            return False
        del self.__categorias[id]
        return True

class ProveedorRepository(IRepositorio[Proveedor]):
  """Implementación del repositorio de proveedores."""

  def __init__(self):
      self.__proveedores = {}

  def crear(self, proveedor: Proveedor) -> Proveedor:
        if proveedor.id in self.__proveedores:
            raise ValueError("Ya existe un proveedor con el mismo ID.")
        self.__proveedores[proveedor.id] = proveedor
        return proveedor

  def leer_por_id(self, id: int) -> Optional[Proveedor]:
        return self.__proveedores.get(id)
  
  def leer_todos(self) -> List[Proveedor]:
        return self.__proveedores.values()

  def actualizar(self, proveedor: Proveedor) -> Proveedor:
        if proveedor.id not in self.__proveedores:
            raise ValueError("No se encontró el proveedor para actualizar.")
        self.__proveedores[proveedor.id] = proveedor
        return proveedor

  def eliminar(self, id: int) -> bool:
        if id not in self.__proveedores:
            return False
        del self.__proveedores[id]
        return True

class PrecioRepository(IRepositorio[Precio]):
  """Implementación del repositorio de precios."""

  def __init__(self):
      self.__precios = {}

  def crear(self, precio: Precio) -> Precio:
        if precio.id in self.__precios:
            raise ValueError("Ya existe un precio con el mismo ID.")
        self.__precios[precio.id] = precio
        return precio

  def leer_por_id(self, id: int) -> Optional[Precio]:
        return self.__precios.get(id)
        
  def leer_todos(self) -> List[Precio]:
        return self.__precios.values()

  def actualizar(self, precio: Precio) -> Precio:
        if precio.id not in self.__precios:
            raise ValueError("No se encontró el precio para actualizar.")
        self.__precios[precio.id] = precio
        return precio

  def eliminar(self, id: int) -> bool:
        if id not in self.__precios:
            return False
        del self.__precios[id]
        return True

class ProductoRepository(IRepositorio[Producto]):
  """Implementación del repositorio de productos."""

  def __init__(self):
      self.__productos = {}

  def crear(self, producto: Producto) -> Producto:
        if producto.id in self.__productos:
            raise ValueError("Ya existe un producto con el mismo ID.")
        self.__productos[producto.id] = producto
        return producto

  def leer_por_id(self, id: int) -> Optional[Producto]:
        return self.__productos.get(id)

  def leer_todos(self) -> List[Producto]:
        return self.__productos.values()

  def actualizar(self, producto: Producto) -> Producto:
        if producto.id not in self.__productos:
            raise ValueError("No se encontró el producto para actualizar.")
        self.__productos[producto.id] = producto
        return producto

  def eliminar(self, id: int) -> bool:
        if id not in self.__productos:
            return False
        del self.__productos[id]
        return True
  

class IRepositorioStock(abc.ABC):
  """Interfaz para repositorios del tipo Stock."""

  @abc.abstractmethod
  def crear(self, stock: Stock) -> Stock:
    """Crea un nuevo registro de stock.

    Args:
        stock (Stock): El objeto Stock a crear.

    Returns:
        Stock: El objeto Stock creado.

    Raises:
        ValueError: Si ya existe un registro de stock para el mismo producto.
    """
    pass

  @abc.abstractmethod
  def leer_por_producto(self, producto_id: int) -> Optional['Stock']:
    """Lee un registro de stock por ID de producto.

    Args:
        producto_id (int): El ID del producto asociado al stock.

    Returns:
        Optional[Stock]: El objeto Stock si se encuentra, None en caso contrario.
    """
    pass

  @abc.abstractmethod
  def actualizar(self, stock: 'Stock') -> 'Stock':
    """Actualiza un registro de stock existente.

    Args:
        stock (Stock): El objeto Stock a actualizar (debe tener un producto_id existente).

    Returns:
        Stock: El objeto Stock actualizado.

    Raises:
        ValueError: Si no se encuentra el stock para actualizar.
    """
    pass

  @abc.abstractmethod
  def eliminar(self, producto_id: int) -> bool:
    """Elimina un registro de stock por ID de producto.

    Args:
        producto_id (int): El ID del producto asociado al stock a eliminar.

    Returns:
        bool: True si el stock fue eliminado, False si no se encontró.
    """
    pass

class StockRepository(IRepositorioStock):
  """Implementación del repositorio de stock."""

  def __init__(self):
      self.__stock = {}

  def crear(self, stock: Stock) -> Stock:
        if stock.producto_id in self.__stock:
            raise ValueError("Ya existe un registro de stock para el mismo producto.")
        self.__stock[stock.producto_id] = stock
        return stock
  
  def leer_por_producto(self, producto_id: int) -> Optional[Stock]:
        return self.__stock.get(producto_id)

  def actualizar(self, stock: Stock) -> Stock:
        if stock.producto_id not in self.__stock:
            raise ValueError("No se encontró el stock para actualizar.")
        self.__stock[stock.producto_id] = stock
        return stock

  def eliminar(self, producto_id: int) -> bool:
        if producto_id not in self.__stock:
            return False
        del self.__stock[producto_id]
        return True

  

class IRepositorioCotizacionDolar(abc.ABC):
  """Interfaz para repositorios del tipo RepositorioCotizacionDolar."""

  @abc.abstractmethod
  def crear(self, cotizacion: 'CotizacionDolar') -> 'CotizacionDolar':
    """Crea una nueva cotización de dólar.

    Args:
        cotizacion (CotizacionDolar): El objeto CotizacionDolar a crear.

    Returns:
        CotizacionDolar: El objeto CotizacionDolar creado.

    Raises:
        ValueError: Si ya existe una cotización para el mismo tipo y fecha.
    """
    pass

  @abc.abstractmethod
  def leer_por_tipo_y_fecha(self, tipo_id: int, fecha: datetime.date) -> Optional['CotizacionDolar']:
    """Lee una cotización de dólar por tipo y fecha.

    Args:
        tipo_id (int): El ID del tipo de cotización (e.g., 'Oficial', 'Blue').
        fecha (datetime.date): La fecha de la cotización.

    Returns:
        Optional[CotizacionDolar]: La cotización si se encuentra, None en caso contrario.
    """
    pass

  @abc.abstractmethod
  def leer_historico_por_tipo(self, tipo_id: int) -> List['CotizacionDolar']:
    """Lee el histórico de cotizaciones para un tipo específico.

    Args:
        tipo_id (int): El ID del tipo de cotización.

    Returns:
        List[CotizacionDolar]: Una lista de cotizaciones históricas para el tipo dado.
    """
    pass

  @abc.abstractmethod
  def actualizar(self, cotizacion: 'CotizacionDolar') -> 'CotizacionDolar':
    """Actualiza una cotización de dólar existente.

    Args:
        cotizacion (CotizacionDolar): El objeto CotizacionDolar a actualizar.

    Returns:
        CotizacionDolar: El objeto CotizacionDolar actualizado.

    Raises:
        ValueError: Si no se encuentra la cotización para actualizar.
    """
    pass

  @abc.abstractmethod
  def eliminar(self, tipo_id: int, fecha: datetime.date) -> bool:
    """Elimina una cotización de dólar por tipo y fecha.

    Args:
        tipo_id (int): El ID del tipo de cotización.
        fecha (datetime.date): La fecha de la cotización a eliminar.

    Returns:
        bool: True si la cotización fue eliminada, False si no se encontró.
    """
    pass


class CotizacionDolarRepository(IRepositorioCotizacionDolar):
  """Implementación del repositorio de cotizaciones de dólar."""

  def __init__(self):
      self.__cotizaciones = {}

  def crear(self, cotizacion: CotizacionDolar) -> CotizacionDolar:
        if (cotizacion.tipo_id, cotizacion.fecha) in self.__cotizaciones:
            raise ValueError("Ya existe una cotización para el mismo tipo y fecha.")
        self.__cotizaciones[(cotizacion.tipo.id, cotizacion.fecha)] = cotizacion
        return cotizacion

  def leer_por_tipo_y_fecha(self, tipo_id: int, fecha: datetime.date) -> Optional[CotizacionDolar]:
        for cotizacion in self.__cotizaciones.values():
            if cotizacion.id == tipo_id and cotizacion.fecha == fecha:
                return cotizacion
        return None

  def leer_historico_por_tipo(self, tipo_id: int) -> List[CotizacionDolar]:
        return [cotizacion for cotizacion in self.__cotizaciones.values() if cotizacion.tipo_id == tipo_id]

  def actualizar(self, cotizacion: CotizacionDolar) -> CotizacionDolar:
        if (cotizacion.tipo_id, cotizacion.fecha) not in self.__cotizaciones:
            raise ValueError("No se encontró la cotización para actualizar.")
        self.__cotizaciones[(cotizacion.tipo_id, cotizacion.fecha)] = cotizacion
        return cotizacion
  
  def eliminar(self, tipo_id: int, fecha: datetime.date) -> bool:
        for cotizacion in self.__cotizaciones.values():
            if cotizacion.tipo_id == tipo_id and cotizacion.fecha == fecha:
                del self.__cotizaciones[(cotizacion.tipo_id, cotizacion.fecha)]
                return True
        return False
  

