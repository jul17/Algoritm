class Counter:

    number_of_comparison = 0
    number_of_exchange = 0

    @staticmethod
    def compare_count():
        Counter.number_of_comparison += 1
        pass

    @staticmethod
    def exchange_count():
        Counter.number_of_exchange += 1
        pass

    @staticmethod
    def counter_reset():
        Counter.number_of_exchange = 0
        Counter.number_of_comparison = 0