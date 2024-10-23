import numpy as np

class Model:
    """Stores vertex information for a 3D Model"""
    def __init__(self, fileName: str, objectNames: list[str] = []) -> None:
        self.vertices = []
        self.edges = []
        self.objects = []

        if len(objectNames) > 0:
            self.load_model(fileName, objectNames)
        else:
            self.load_model(fileName)


    def load_model(self, fileName: str, objectNames: list[str] = []) -> None:
        """Loads vertices from a .obj file with file name 'fileName'

        :param fileName: The filename of the .obj file to load
        :param objectName: The name of a specific object to load from the specified .obj file"""
        
        self.vertices = []
        self.edges = []

        try:
            with open(f'Models/{fileName}', 'r') as file:
                for line in file:
                    if len(objectNames) > 0:
                        if line.startswith('o ') and (line.split()[1] not in objectNames):
                            break

                    if line.startswith('v '):
                        parts = line.strip().split()
                        x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                        self.vertices.append(np.matrix([x, y, z]))

                    if line.startswith('o '):
                        self.objects.append(line.split()[1])

        except FileNotFoundError:
            print(f"File not found: {fileName}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    model = Model('Donut.obj', 'Doughnut_Torus.003')
    print(len(model.vertices))