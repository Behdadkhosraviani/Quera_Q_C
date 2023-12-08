# first step is to determine the guns and the bullets
Guns = {
    "name": ["Submachine Gun", "Assault Rifle", "Pistol", "Shotgun", "Sniper Rifle"],
    "range": [100, 200, 80, 50, 1000],
    "power": [10, 20, 8, 40, 30],
    "size": [0.5, 1, 0.5, 4, 3]
}

Bullets = {
    "name": ["A", "B", "C", "D"],
    "size": [0.5, 1, 3, 4],
    "damage": [1, 1.5, 3, 2]
}

# we make dictionaries out of this class scope so that we can access them easily


class Shooter:

    def set_gun_by_name(self, name: str):
        if name in Guns["name"]:  # check if name already exists
            self.name = name
            self.ind = Guns["name"].index(name)
        else:
            raise Exception("Name not found: %s" % name)

    def add_bullet_of_given_size_to_gun(self, size: float, count: int):
        # we write ifs here
        if self.name == None :  # check if we already have Gun
            raise Exception("your Gun is not selected")

        elif count < 0:  # check if count is positive
            raise Exception("count is out of range")

        elif size in Bullets["size"] and Guns["size"][self.ind] == size:
          self.bullet = Bullets["size"].index(size)
          self.count = count

        else:
            raise Exception("not matching size")

    def shoot_to_target(self, target_x: int,  target_y: int,  target_distance: int,  aim_x: int,  aim_y: int) -> float:
        if self.ind == None or self.bullet == None :  # check if bullets or gus are chosen
            raise Exception("you don't have a bullet or a Gun")

        elif target_distance > Guns["range"][self.ind]:
            return 0
        elif self.count == 0:
            print(0)
            return 0
        else:
            print(Guns["power"][self.ind] * Bullets["damage"][self.bullet])
            return Guns["power"][self.ind] * Bullets["damage"][self.bullet]

# now we test what we wrote  here


if __name__ == "__main__":
    shooter = Shooter()
    shooter.set_gun_by_name("Pistol")
    shooter.add_bullet_of_given_size_to_gun(0.5, 0)
    shooter.shoot_to_target(1, 1, 20, 5, 4)

