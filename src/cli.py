# src/cli.py
class CLI:
    @classmethod
    def print_list(cls, lst: list):
        print("\n".join(lst))

    @staticmethod
    def print(text: str):
        print(text)
