class CoffeeMachine:
    def __init__(self):
        self.started = False

        # Yes it's a magic machine :)
        self.descale()
        self.fill_tank()
        self.fill_beans()
        self.empty_grounds()

        self._last_coffee_success = False
        self._display_settings = False

        self._water_hardness = 2
        self._grinder = 'medium'

    def start(self, lang = 'en'):
        self.started = True
        self.lang = lang

    def stop(self):
        self.started = False

    @property
    def messages(self):
        i18n = {
            'en': {
                'tank': 'Fill tank',
                'beans': 'Fill beans',
                'grounds': 'Empty grounds',
                'ready': 'Ready',
                'settings': 'Settings:\n - 1: water hardness\n - 2: grinder'
            },
            'fr': {
                'tank': 'Remplir reservoir',
                'beans': 'Ajouter grains',
                'grounds': 'Vider marc',
                'ready': 'Pret',
                'settings': 'Configurer:\n - 1: durete de l eau\n - 2: mouture'
            }
        }

        return i18n[self.lang]

    @property
    def message(self):
        if not self.started:
              return ""

        if self._display_settings:
            return self.messages['settings']

        if self.tank_content <= 10:
            return self.messages['tank']

        if self.beans_content < 3:
            return self.messages['beans']

        if self.grounds_content >= 30:
            return self.messages['grounds']

        if self.is_descaling_needed():
            return self.messages['descale']

        return self.messages['ready']

    @property
    def coffee_served(self):
      return self._last_coffee_success

    def take_coffee(self):
        if (self.tank_content == 0 or self.beans_content == 0):
            self._last_coffee_success = False
        else:
            self._last_coffee_success = True

            self.tank_content -= 1
            self.beans_content -= 1
            self.grounds_content += 1
            self.countdown_to_descale -= 1


    def fill_tank(self):
        self.tank_content = 60

    def fill_beans(self):
        self.beans_content = 40

    def empty_grounds(self):
        self.grounds_content = 0

    def show_settings(self):
        self._display_settings = True

    def hide_settings(self):
        self._display_settings = False

    def get_settings(self):
        return {
            'water hardness': self._water_hardness,
            'grinder': self._grinder
        }

    def descale(self):
        self.countdown_to_descale = 500

    def is_descaling_needed(self):
        return self.countdown_to_descale <= 0
