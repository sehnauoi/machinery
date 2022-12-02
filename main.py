from discount import *
from admin import *
from os import system
import json

def clear():
    system('clear')

def inp():
    y = int(input("Input : "))
    return y
   
def back():
    x = input("Kembali ? [ y : n ]")
    if x == 'y':
        main()
    else:
        quit()

def get_weight():
    data = json.load(open('/workspaces/machinery/laundry/datas/settings.json'))
    for x in data['settings']:
        perkilo = x['perkilo']
    return perkilo

def menu1():
    os.system('clear')
    print("""
    Laundry Uhuy
    """)
    perkilo = get_weight()
    weight = float(input("Masukan berat laundry (kg) : "))
    prices = weight * perkilo
    method = int(input("""
Pilih Metode Pencucian
1. Kilat (1 hari)
2. Super Cepat (1-2 hari)
3. Cepat (2-3 hari)
4. Biasa (3-5 hari)
Input : """))
    name = input("\nAtas Nama : ").lower()

    # m_id, m_name, m_date = look_member(name)
    # print(m_id, m_name, m_date)

    # # convert membership year and month to month only so it can be subtracted to look membership type
    # membership_date = int(m_date[0:4]) * 12 + int(m_date[5:7])
    # converted_date = int(date[0:4]) * 12 + int(date[5:7])
    # membership_counter = converted_date - membership_date

    disc = generate_discount_price(prices, method, name )
    
    os.system('clear')
    print(f"""
    Total berat : {weight}
    Total biaya : Rp.{prices}
    """)
    if disc == 0:
        print("    Diskon sebesar Rp. 0")
    else:
        print(f"    Diskon sebesar Rp. {disc}")
        
    save_data(name, weight, prices)

def menu2():
    print("""

    Pilih Menu
    1. Tambah Member Baru
    2. Lihat List Member
    3. Cari Member
    4. Hapus Member

            """)
    
    x = inp()
    match x:
        case 0:
            quit()

        case 1:
            new_member()

        case 2:
            for x in read_member():
                print(x)
            
        case 3:
            x = input("masukan nama yang ingin dicari : ")
            m_name, m_date = look_member(str(x))
            print(f"""
==========================
{m_name} Data
Terdatar pada {m_date}
==========================
        """)

        case 4:
            delete_data()

def main():
    clear()
    print("""
==========================
    Wilujeng Sumping    
                        
    1. Laundry          
    2. Admin            
                        
    0. Exit             
==========================""")
    x = inp()
    match x:
        case 0:
            quit()
        case 1:
            menu1()
        case 2:
            menu2()

# while True:
#     main()
# main()
try:
    if __name__ == "__main__":
        main()

except ValueError:
    print('program crashed')
