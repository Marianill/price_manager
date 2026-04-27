
class CategoriaService:
  """Servicio para operaciones relacionadas con categorías."""

  def __init__(self, categoria_repository: CategoriaRepository):
      self.__categoria_repository = categoria_repository

  def crear(self, categoria: Categoria) -> Categoria:
      if categoria.id in self.__categoria_repository:
            raise ValueError("Ya existe una categoría con el mismo ID.")
      if not categoria.nombre:
            raise ValueError("El nombre de la categoría es obligatorio.")
      return self.__categoria_repository.crear(categoria)

  def lista_categorias(self) -> List[Categoria]:
      return self.__categoria_repository.leer_todos()

  def obtener_categoria(self, id: int) -> Categoria:
      categoria = self.__categoria_repository.leer_por_id(id)
      if not categoria:
            raise ValueError(f"No se encontró la categoría con ID {id}.")
      return categoria

  def actualizar(self, categoria: Categoria) -> Categoria:
      if not categoria.nombre:
            raise ValueError("El nombre de la categoría es obligatorio.")
      if not self.__categoria_repository.leer_por_id(categoria.id):
            raise ValueError(f"No se encontró la categoría con ID {categoria.id}.")
      return self.__categoria_repository.actualizar(categoria)

  def eliminar(self, id: int) -> bool:
      return self.__categoria_repository.eliminar(id)

  
class ProveedorService:
  """Servicio para operaciones relacionadas con proveedores."""
  def __init__(self, proveedor_repository: ProveedorRepository):
      self.__proveedor_repository = proveedor_repository
  
  def crear(self, proveedor: Proveedor) -> Proveedor:
      if proveedor.id in self.__proveedor_repository:
            raise ValueError("Ya existe un proveedor con el mismo ID.")
      if not proveedor.nombre:
            raise ValueError("El nombre del proveedor es obligatorio.")
      if not proveedor.contacto:
            raise ValueError("El contacto del proveedor es obligatorio.")
      return self.__proveedor_repository.crear(proveedor)

  def lista_proveedores(self) -> List[Proveedor]:
      return self.__proveedor_repository.leer_todos()

  def obtener_proveedor(self, id: int) -> Proveedor:
      proveedor = self.__proveedor_repository.leer_por_id(id)
      if not proveedor:
            raise ValueError(f"No se encontró el proveedor con ID {id}.")
      return proveedor

  def actualizar(self, proveedor: Proveedor) -> Proveedor:
      if not proveedor.nombre:
            raise ValueError("El nombre del proveedor es obligatorio.")
      if not proveedor.contacto:
            raise ValueError("El contacto del proveedor es obligatorio.")
      if not self.__proveedor_repository.leer_por_id(proveedor.id):
            raise ValueError(f"No se encontró el proveedor con ID {proveedor.id}.")
      return self.__proveedor_repository.actualizar(proveedor)

  def eliminar(self, id: int) -> bool:
      return self.__proveedor_repository.eliminar(id)

  
class ProductoService:
  """Servicio para operaciones relacionadas con productos."""

  def __init__(self, producto_repository: ProductoRepository):
      self.__producto_repository = producto_repository

  def crear(self, producto: Producto) -> Producto:
      if producto.id in self.__producto_repository:
            raise ValueError("Ya existe un producto con el mismo ID.")
      if not producto.nombre:
            raise ValueError("El nombre del producto es obligatorio.")

      if not producto.descripcion:
            raise ValueError("La descripción del producto es obligatoria.")

      if not producto.precio:
            raise ValueError("El precio del producto es obligatorio.")

      if not producto.categoria:
            raise ValueError("La categoría del producto es obligatoria.")

      if not producto.proveedor:
            raise ValueError("El proveedor del producto es obligatorio.")

  
  def lista_productos(self) -> List[Producto]:
      return self.__producto_repository.leer_todos()

  def obtener_producto(self, id: int) -> Producto:
      producto = self.__producto_repository.leer_por_id(id)
      if not producto:
            raise ValueError(f"No se encontró el producto con ID {id}.")
      return producto

  def actualizar(self, producto: Producto) -> Producto:
      if not producto.nombre:
            raise ValueError("El nombre del producto es obligatorio.")
      if not producto.descripcion:
            raise ValueError("La descripción del producto es obligatoria.")
      if not producto.precio:
            raise ValueError("El precio del producto es obligatorio.")
      if not self.__producto_repository.leer_por_id(producto.id):
            raise ValueError(f"No se encontró el producto con ID {producto.id}.")
      return self.__producto_repository.actualizar(producto)

  def eliminar(self, id: int) -> bool:
      return self.__producto_repository.eliminar(id)


class StockService:
  """Servicio para operaciones relacionadas con stock."""

  def __init__(self, stock_repository: StockRepository):
      self.__stock_repository = stock_repository

  def registrar(self, producto_id: int, cantidad: int) -> Stock:
      stock = self.__stock_repository.leer_por_producto(producto_id)
      if not stock:
            stock = Stock(producto_id=producto_id, cantidad=cantidad)
      else:
            stock.cantidad += cantidad
      return self.__stock_repository.crear(stock)

  def buscar_stock(self, producto_id: int) -> int:
      stock = self.__stock_repository.leer_por_producto(producto_id)
      if not stock:
            raise ValueError(f"No se encontró el stock para el producto con ID {producto_id}.")
      return stock.cantidad

  def actualizar_stock(self, producto_id: int, cantidad: int) -> Stock:
      stock = self.__stock_repository.leer_por_producto(producto_id)
      if not stock:
            raise ValueError(f"No se encontró el stock para el producto con ID {producto_id}.")
      stock.cantidad = cantidad
      return self.__stock_repository.actualizar(stock)
  
  def eliminar_stock(self, producto_id: int) -> bool:
      return self.__stock_repository.eliminar(producto_id)
  
class CotizacionDolarService:
  """Servicio para operaciones relacionadas con cotizaciones de dólar."""
  def __init__(self, cotizacion_dolar_repository: CotizacionDolarRepository):
      self.__cotizacion_dolar_repository = cotizacion_dolar_repository
  
  def registrar_cotizacion(self, cotizacion: CotizacionDolar) -> CotizacionDolar:
      if not cotizacion.valor:
            raise ValueError("El valor de la cotización es obligatorio.")
      if not cotizacion.fecha:
            raise ValueError("La fecha de la cotización es obligatoria.")
      if not cotizacion.tipo:
            raise ValueError("El tipo de cotización es obligatorio.")
      return self.__cotizacion_dolar_repository.crear(cotizacion)

  def obtener_historico(self, tipo_id: int) -> List[CotizacionDolar]:
      return self.__cotizacion_dolar_repository.leer_historico_por_tipo(tipo_id)

  def actualizar_cotizacion(self, cotizacion: CotizacionDolar) -> CotizacionDolar:
      if not cotizacion.valor:
            raise ValueError("El valor de la cotización es obligatorio.")
      if not cotizacion.fecha:
            raise ValueError("La fecha de la cotización es obligatoria.")
      if not cotizacion.tipo:
            raise ValueError("El tipo de cotización es obligatorio.")
      self.__cotizacion_dolar_repository.leer_por_tipo_y_fecha(cotizacion.tipo_id, cotizacion.fecha)
      return self.__cotizacion_dolar_repository.actualizar(cotizacion)
  
  def eliminar_cotizacion(self, tipo_id: int, fecha: datetime.date) -> bool:
      return self.__cotizacion_dolar_repository.eliminar(tipo_id, fecha)
  

