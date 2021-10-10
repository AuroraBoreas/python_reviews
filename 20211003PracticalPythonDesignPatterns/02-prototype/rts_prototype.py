from concrete import Concrete, deepcopy

class Knight(Concrete):
    def __init__(self, level):
        self.unit_type = 'Knight'
        filename = './02-prototype/dat/{}_{}.dat'.format(self.unit_type, level)

        with open(filename, 'r') as f:
            lines = f.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return 'Type: {0}\n' \
               'Life: {1}\n' \
               'Speed: {2}\n' \
               'Attack Power: {3}\n' \
               'Attack Range: {4}\n' \
               'Weapon: {5}\n'.format(self.unit_type, self.life, self.speed, self.attack_power, self.attack_range, self.weapon)

    def clone(self):
        return deepcopy(self)

class Archer(Concrete):
    def __init__(self, level):
        self.unit_type = 'Archer'
        filename = f'./02-prototype/dat/{self.unit_type}_{level}.dat'
        with open(filename, 'r') as f:
            lines = f.read().split('\n')
            self.life = lines[0]
            self.speed = lines[1]
            self.attack_power = lines[2]
            self.attack_range = lines[3]
            self.weapon = lines[4]

    def __str__(self):
        return 'Type: {0}\n' \
               'Life : {1}\n' \
               'Speed : {2}\n' \
               'Attack power : {3}\n' \
               'Attack range : {4}\n' \
               'Weapon : {5}\n'.format(self.unit_type, self.life, self.speed, self.attack_power, self.attack_range, self.weapon)

    def clone(self):
        return deepcopy(self)

class Barracks:
    def __init__(self):
        self.units = {
            'knight' : {
                1: Knight(1),
                2: Knight(2),
            },
            'archer' : {
                1: Archer(1),
                2: Archer(2),
            }
        }

    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()

if __name__ == '__main__':
    barracks = Barracks()
    k1 = barracks.build_unit('knight', 1)
    a2 = barracks.build_unit('archer', 2)
    print("[knight1] {}".format(k1))
    print("[archer2] {}".format(a2))