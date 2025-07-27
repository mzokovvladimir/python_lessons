import re


def is_valid_ip(ip_address: str) -> bool:
    """
    Перевіряє, чи є заданий рядок IP-адресою.

    Args:
      ip_address: Рядок, який потрібно перевірити.

    Returns:
      True, якщо рядок є IP-адресою, False в іншому випадку.
    """

    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    if not re.match(pattern, ip_address):
        return False

    numbers = ip_address.split(".")
    for number in numbers:
        if not 0 <= int(number) <= 255:
            return False

    return True


print(is_valid_ip("1.2.3.4"))