
VERSION="1.0.1"
MODEL="GALLOOP"

class SDK:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.model=f"{MODEL}:{VERSION}"

    def info(self):
        return f"{self.name} version {self.version}"
    
    def get_information(self):
        return f"SDK Information: {self.model}"
    