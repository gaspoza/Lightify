class Group:
    """
        A group of Hue lights, tracked as a group on the bridge
    """

    def __init__(self, group_id, name, on, lights):
        self.id = group_id
        self.name = name
        self.on = on
        self.lights = lights

    def has_light_on(self):
        return any(light.on for light in self.lights)

    def __str__(self):
        return 'Group {id} : {name}'.format(id=self.id, name=self.name)
