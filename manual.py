import requests
import time

# Endpoint untuk klaim gas faucet Sui testnet
FAUCET_URL = "https://faucet.testnet.sui.io/gas"

# Headers
headers = {
    "Content-Type": "application/json",
}

def claim_sui_gas(wallet_address):
    """Fungsi untuk klaim SUI gas tokens."""
    data = {
        "FixedAmountRequest": {
            "recipient": wallet_address
        }
    }

    retry_attempts = 3  # Jumlah maksimal percobaan ulang
    wait_time = 50  # Waktu tunggu (dalam detik) sebelum mencoba ulang

    for attempt in range(retry_attempts):
        try:
            # Mengirim permintaan POST untuk klaim token
            response = requests.post(FAUCET_URL, json=data, headers=headers)

            # Cek apakah permintaan berhasil
            if response.status_code == 200:
                result = response.json()
                # Ambil detail dari hasil klaim
                transferred_gas = result.get("transferredGasObjects", [])
                if transferred_gas:
                    amount = transferred_gas[0]["amount"]
                    tx_digest = transferred_gas[0]["transferTxDigest"]
                    print("Sedang klaim faucet...")
                    print("Klaim sukses!")
                    print(f"Jumlah gas yang ditransfer: {amount}")
                    print(f"Transfer Tx Digest: {tx_digest}")
                else:
                    print("Klaim faucet berhasil, tetapi tidak ada objek gas yang ditransfer.")
                break  # Keluar dari loop jika berhasil
            elif response.status_code == 429:
                print(f"Error 429: Too Many Requests. Menunggu {wait_time} detik sebelum mencoba lagi...")
                time.sleep(wait_time)  # Tunggu 50 detik sebelum mencoba ulang
            else:
                print("Klaim sukses!")  # Hanya mencetak pesan sukses tanpa detail respons lainnya
                break  # Jika bukan error 429, keluar dari loop
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")
            break

def main():
    print("=======================================")
    print("=     Klaim Faucet SUI Testnet        =")
    print("=        Created By:r0otz             =")
    print("=        How to find me?              =")
    print("=  https://t.me/sahabatrhyeofficial   =")      
    print("=======================================")

    while True:
        print("\nMenu:")
        print("1. Klaim faucet")
        print("2. Keluar")

        pilihan = input("Masukkan pilihan:? ")

        if pilihan == "1":
            wallet_address = input("Masukkan alamat wallet yang ingin digunakan: ")
            if wallet_address:
                print(f"Melakukan klaim untuk alamat: {wallet_address}")
                claim_sui_gas(wallet_address)
            else:
                print("Alamat wallet tidak valid.")

        elif pilihan == "2":
            print("Terima kasih telah menggunakan skrip ini")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()