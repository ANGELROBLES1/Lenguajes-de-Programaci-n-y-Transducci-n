class RecomendacionesProductos:
    def __init__(self):
        # usuario -> conjunto de productos comprados
        self.user_products = {}

        # producto -> conjunto de usuarios que lo compraron
        self.product_users = {}

    def addPurchase(self, usuario, producto):
        # Registrar producto en usuario
        if usuario not in self.user_products:
            self.user_products[usuario] = set()
        self.user_products[usuario].add(producto) # Agregar producto al conjunto del usuario

        # Registrar usuario en producto
        if producto not in self.product_users:
            self.product_users[producto] = set()
        self.product_users[producto].add(usuario)

    def getRecommendations(self, usuario):
        if usuario not in self.user_products: # El usuario no existe
            return []

        recomendaciones = set()
        productos_usuario = self.user_products[usuario] # Productos que el usuario ya compro

        for producto in productos_usuario:
            usuarios_relacionados = self.product_users.get(producto, set())

            for otro_usuario in usuarios_relacionados:
                if otro_usuario != usuario: # Evitar recomendar productos del mismo usuario
                    recomendaciones.update(
                        self.user_products.get(otro_usuario, set())
                    )

        # Quitar productos que el usuario ya compro
        recomendaciones -= productos_usuario

        return list(recomendaciones)

rs = RecomendacionesProductos() # Crear instancia del sistema de recomendaciones

rs.addPurchase("Santiago", "Laptop")
rs.addPurchase("Santiago", "Mouse")

rs.addPurchase("Deivid", "Laptop")
rs.addPurchase("Deivid", "Teclado")

rs.addPurchase("Pedro", "Mouse")
rs.addPurchase("Pedro", "Monitor")

print(rs.getRecommendations("Santiago")) 
