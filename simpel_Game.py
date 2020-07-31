input('Pikirkan sebuah angka dari 1 - 100 kemudian ketik dan tekan ENTER : ')
print('Komputer akan menebak angka yang anda ketikan tadi')

#Base data
batas_bawah = 1
batas_atas = 100
jumlah_tebakan = 0
sudah_ketebak = False

while not sudah_ketebak:
  #ambil nilai tengah antara batas atas dan batas bawah
  tebakan_sementara = batas_bawah + int((batas_atas - batas_bawah)/2)
  jumlah_tebakan = jumlah_tebakan + 1
  
  print('Angkanya {} bukan?'.format(tebakan_sementara))
  petunjuk = 'B. kalau kebesaran, K. kalau kekecilan, Y. kalau sudah ketebak. Jawab: '
  respon = ''

  # kalau user masukin input selain B,K,Y suruh ulang lagi
  while not (respon == 'B' or respon=='K' or respon =='Y'):
    respon = input(petunjuk)
    respon = respon.upper() # konversi masukan user ke dalam huruf besar (upper case)

  if respon == 'K':
    # tebakan kekecilan, maka geser batas bawah. tebakan sementara plus 1 menjadi batas bawah baru
    batas_bawah = tebakan_sementara + 1
  elif respon == 'B':
    # tebakan kegedean, maka geser batas atas. tebakan sementara minus 1 menjadi batas atas baru
    batas_atas = tebakan_sementara - 1
  else:
    # tebakan sudah benar
    sudah_ketebak = True

print('Angkanya berhasi ditebak komputer pada percobaan ke-{}'.format(jumlah_tebakan))