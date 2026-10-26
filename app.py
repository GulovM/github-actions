"""
Простой калькулятор с базовыми математическими операциями.
"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("2 + 2 =", add(2, 2))
    print("10 / 2 =", divide(10, 2))
    print("Is 17 prime?", is_prime(17))

