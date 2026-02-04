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
        self.user_products[usuario].add(producto)

        # Registrar usuario en producto
        if producto not in self.product_users:
            self.product_users[producto] = set()
        self.product_users[producto].add(usuario)

    def getRecommendations(self, usuario):
        if usuario not in self.user_products:
            return []

        recomendaciones = set()
        productos_usuario = self.user_products[usuario]

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

rs = RecomendacionesProductos()

rs.addPurchase("Ana", "Laptop")
rs.addPurchase("Ana", "Mouse")

rs.addPurchase("Juan", "Laptop")
rs.addPurchase("Juan", "Teclado")

rs.addPurchase("Luis", "Mouse")
rs.addPurchase("Luis", "Monitor")

print(rs.getRecommendations("Ana"))

