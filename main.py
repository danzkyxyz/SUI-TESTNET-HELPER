import subprocess
import os
import time

def run_create_wallet():
    try:
        if not os.path.exists("createwallet.py"):
            print("❌ File createwallet.py tidak ditemukan!")
            return False
        
        print("🚀 Menjalankan createwallet.py...")
        result = subprocess.run(["python", "createwallet.py"], check=True)
        
        if os.path.exists("phrase.txt"):
            print("🔄 Mengubah nama phrase.txt menjadi data.txt...")
            os.rename("phrase.txt", "data.txt")
        else:
            print("❌ File phrase.txt tidak ditemukan, mungkin createwallet.py gagal.")
            return False
        
        if not os.path.exists("convert.js"):
            print("❌ File convert.js tidak ditemukan!")
            return False
            
        print("🚀 Menjalankan convert.js...")
        result = subprocess.run(["node", "convert.js"], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"❌ Error saat menjalankan convert.js: {result.stderr}")
        
        if os.path.exists("pvkey.txt"):
            print("🗑️ Menghapus pvkey.txt...")
            os.remove("pvkey.txt")
            
        if os.path.exists("data.txt"):
            print("🔄 Mengubah nama data.txt menjadi phrase.txt...")
            os.rename("data.txt", "phrase.txt")
            
        print("✅ Wallet creation and conversion completed!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error saat menjalankan create wallet: {e}")
        return False
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {str(e)}")
        return False

def run_claim_faucet():
    try:
        if not os.path.exists("faucet.py"):
            print("❌ File faucet.py tidak ditemukan!")
            return False
            
        print("🚀 Menjalankan faucet.py...")
        result = subprocess.run(["python", "faucet.py"], check=True)
        if result.returncode != 0:
            print(f"❌ Error saat menjalankan faucet.py: Return code {result.returncode}")
            return False
            
        print("✅ Faucet claim completed!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error saat menjalankan faucet claim: {e}")
        return False
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {str(e)}")
        return False

def run_transfer_faucet():
    try:
        if not os.path.exists("transfer.js"):
            print("❌ File transfer.js tidak ditemukan!")
            return False
            
        print("🚀 Menjalankan transfer.js...")
        result = subprocess.run(["node", "transfer.js"], check=True)
        if result.returncode != 0:
            print(f"❌ Error saat menjalankan transfer.js: Return code {result.returncode}")
            return False
            
        print("✅ Faucet transfer completed!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error saat menjalankan transfer: {e}")
        return False
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {str(e)}")
        return False

def main():
    try:
        # ASCII art dan author, dipusatkan
        ascii_art = """
  _____ _    _ _____   _______ ______  _____ _______ _   _ ______ _______
 / ____| |  | |_   _| |__   __|  ____|/ ____|__   __| \\ | |  ____|__   __|
| (___ | |  | | | |      | |  | |__  | (___    | |  |  \\| | |__     | |
 \\___ \\| |  | | | |      | |  |  __|  \\___ \\   | |  | . ` |  __|    | |
 ____) | |__| |_| |_     | |  | |____ ____) |  | |  | |\\  | |____   | |
|_____/ \\____/|_____|    |_|  |______|_____/   |_|  |_| \\_|______|  |_|


 _    _ ______ _      _____  ______ _____
| |  | |  ____| |    |  __ \\|  ____|  __ \\
| |__| | |__  | |    | |__) | |__  | |__) |
|  __  |  __| | |    |  ___/|  __| |  _  /
| |  | | |____| |____| |    | |____| | \\ \\
|_|  |_|______|______|_|    |______|_|  \\_\\

{:^78}
""".format("AUTHOR BY : AIRDROPDXNS")

        # Menampilkan ASCII art
        print(ascii_art)
        
        print("\n=== SUI Wallet Automation ===")
        print("1. Create SUI Wallet")
        print("2. Claim Faucet SUI")
        print("3. Send Faucet SUI")
        choice = input("Enter your choice (1, 2 or 3): ").strip()
        
        if choice == "1":
            success = run_create_wallet()
            if success:
                print("🎉 Wallet creation process completed successfully!")
            else:
                print("💥 Wallet creation process failed!")
                
        elif choice == "2":
            success = run_claim_faucet()
            if success:
                print("🎉 Faucet claim process completed successfully!")
            else:
                print("💥 Faucet claim process failed!")
                
        elif choice == "3":
            success = run_transfer_faucet()
            if success:
                print("🎉 Faucet transfer process completed successfully!")
            else:
                print("💥 Faucet transfer process failed!")
                
        else:
            print("❌ Invalid choice. Please select 1, 2 or 3.")
            
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan utama: {str(e)}")

if __name__ == "__main__":
    main()