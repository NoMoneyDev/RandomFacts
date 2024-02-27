import randfacts


class Fact_giver:

    def fact(self):
        factstr = '\n\n'.join([randfacts.get_fact() for _ in range(5)])
        return factstr