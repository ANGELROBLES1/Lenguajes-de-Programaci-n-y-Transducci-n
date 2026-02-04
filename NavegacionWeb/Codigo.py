class NavegadorWeb:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = None

    def loadPage(self, url):
        if self.current_page is not None: # Si hay una pagina actual se guarda en el back_stack
            self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()
        print(f"Cargando pagina: {url}")

    def goBack(self):
        if not self.back_stack:
            print("No existen paginas anteriores")
            return

        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop() # Se obtiene la ultima pagina del back_stack y se asigna como pagina actual
        print(f"Volviendo a: {self.current_page}")

    def goForward(self):
        if not self.forward_stack: 
            print("No existen paginas siguientes")
            return

        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(f"Avanzando a: {self.current_page}")

    def getCurrentPage(self):
        return self.current_page


#Usos
browser = NavegadorWeb()
browser.loadPage("usergioarboleda.com")
browser.loadPage("x.com")
browser.loadPage("github.com")

browser.goBack()      # x.com
browser.goBack()      # usergioarboleda.com
browser.goForward()   # x.com
browser.goForward()   # github.com
browser.goForward()   # No existen paginas siguientes
