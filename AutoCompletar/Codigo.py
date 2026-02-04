class Prefijos:
    def __init__(self):
        self.children = {}
        self.is_end = False # indica si es el final de una palabra


class AutoCompletar:
    def __init__(self):
        self.root = Prefijos()

    def insert(self, word):
        node = self.root
        for char in word: # recorrer cada caracter en la palabra
            if char not in node.children:
                node.children[char] = Prefijos()
            node = node.children[char]
        node.is_end = True

    def _dfs(self, node, prefix, results):
        if node.is_end:
            results.append(prefix) # si es el final de una palabra, agregar al resultado

        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

    def autocomplete(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []  # prefijo no existe
            node = node.children[char]

        results = []
        self._dfs(node, prefix, results) # buscar todas las palabras que comienzan con el prefijo
        return results


# Uso
autocomplete_system = AutoCompletar()

words = ["casa", "carro", "camino", "perro", "persona", "programar"]
for word in words:
    autocomplete_system.insert(word)

print(autocomplete_system.autocomplete("ca"))
print(autocomplete_system.autocomplete("per"))
print(autocomplete_system.autocomplete("pro"))
print(autocomplete_system.autocomplete("z"))

