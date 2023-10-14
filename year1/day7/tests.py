import unittest
import parsing as p


class Test(unittest.TestCase):
    def test_get_instruction_type(self):
        print(p.get_instruction_type("123"))
        print(p.get_instruction_type("lx"))
        print(p.get_instruction_type("NOT ax"))
        print(p.get_instruction_type("c LSHIFT 1"))
        print(p.get_instruction_type("1 AND cx"))
        print(p.get_instruction_type("dy OR ej"))


if __name__ == "__main__":
    unittest.main()
