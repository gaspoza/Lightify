class Light:
    """
        Hue Light object
    """

    def __init__(self, light_id, name, light_type, brightness, hue, saturation, on, reachable):
        self.id = light_id
        self.name = name
        self.type = light_type
        self.brightness = brightness
        self.hue = hue
        self.saturation = saturation
        self.on = on
        self.reachable = reachable

    def __str__(self):
        return 'Light {id} : {name}'.format(id=self.id, name=self.name)
