from coffee_machine import CoffeeMachine

class CoffeeMachineLibrary(object):
    def __init__(self):
        self.sut = CoffeeMachine()
        self.handled = []

    def i_start_the_coffee_machine_using_language_lang(self, lang = 'en'):
        self.sut.start(lang)

    def i_shutdown_the_coffee_machine(self):
        self.sut.stop()

    def message_message_should_be_displayed(self, message = ''):
        if self.sut.message != message:
            raise AssertionError('%s != %s' % (self.sut.message, message))

    def coffee_should_be_served(self):
        if not self.sut.coffee_served:
            raise AssertionError('No coffee served')

    def coffee_should_not_be_served(self):
        if self.sut.coffee_served:
            raise AssertionError('A coffee is served')

    def i_take_a_coffee(self):
        self.sut.take_coffee()

    def i_empty_the_coffee_grounds(self):
        self.sut.empty_grounds()

    def i_fill_the_beans_tank(self):
        self.sut.fill_beans()

    def i_fill_the_water_tank(self):
        self.sut.fill_tank()

    def i_take_coffee_number_coffees(self, coffee_number = 10):
        coffee_number = int(coffee_number)
        while (coffee_number > 0):
            self.i_take_a_coffee()
            coffee_number = coffee_number - 1

            if 'water' in self.handled:
                self.i_fill_the_water_tank()

            if 'beans' in self.handled:
                self.i_fill_the_beans_tank()

            if 'grounds' in self.handled:
                self.i_empty_the_coffee_grounds()

    def i_handle_water_tank(self):
        self.handled.append('water')

    def i_handle_beans(self):
        self.handled.append('beans')

    def i_handle_coffee_grounds(self):
        self.handled.append('grounds')

    def displayed_message_is(self, free_text = ""):
        displayed = [line.strip() for line in self.sut.message.split("\n")]
        expected = [line.strip() for line in free_text.split("\n")]

        if displayed != expected:
            raise AssertionError('%s != %s' % (expected, displayed))

    def i_switch_to_settings_mode(self):
        self.sut.show_settings()

    def settings_should_be(self, *args, **kwargs):
        datatable = ''.join(args)

        expected_settings = [[cell.strip() for cell in line.split('|')] for line in datatable.split("\n")]
        settings = [['', k, str(self.sut.get_settings()[k]), ''] for k in self.sut.get_settings().keys()]

        if expected_settings != settings:
            raise AssertionError('%s != %s' % (expected_settings, settings))
