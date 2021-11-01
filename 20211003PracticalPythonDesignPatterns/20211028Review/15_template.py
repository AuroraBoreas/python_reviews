# template method 

class Context:
    def template_method(self):
        self.do_this()
        self.do_that()
        self.hook1()
        self.analyze()
        self.hook2()
        
    def do_this(self):
        pass

    def do_that(self):
        pass

    def hook1(self):
        pass

    def analyze(self):
        pass

    def hook2(self):
        pass
