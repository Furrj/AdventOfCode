from translate import find_valid, increment
import validation as v

input: str = "hepxcrrq"
alphabet: list[str] = [chr(ord("a") + i) for i in range(26)]


if __name__ == "__main__":
    print(increment("hepxxyaz"))
