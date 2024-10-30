from solders.keypair import Keypair

def main():
    # Чтение закрытых ключей из файла
    with open("private_keys.txt", "r") as file:
        private_keys = file.readlines()

    # Обработка каждого закрытого ключа
    for private_key_str in private_keys:
        private_key_str = private_key_str.strip()  # Убираем пробельные символы
        if private_key_str:
            try:
                # Создаём Keypair из закрытого ключа
                keypair = Keypair.from_base58_string(private_key_str)

                # Получаем открытый ключ (адрес)
                public_key = keypair.pubkey()
                print(f"{public_key}")
            except Exception as e:
                print(f"Ошибка при обработке ключа: {private_key_str} - {e}")

if __name__ == "__main__":
    main()
