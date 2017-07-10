import json

file_directory = 'pokemon.json'
json_data = open(file_directory).read()

data = json.loads(json_data)


class Pokemon:
    def __init__(self, ident):
        self.id = ident - 1
        self.name = data[self.id]['identifier']
        self.height = data[self.id]['height']
        self.weight = data[self.id]['weight']
        self.base_experience = data[self.id]['base_experience']

    def get_name(self):
        return self.name

    def get_height(self):
        return str(self.height)

    def get_weight(self):
        return str(self.weight)

    def get_base_experience(self):
        return str(self.base_experience)


if __name__ == '__main__':
    pass

