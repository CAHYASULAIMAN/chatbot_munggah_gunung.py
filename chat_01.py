import string

#data pribadi
tanggal_munggah = ("15",'16','20','24')

chatbot_name = 'fitri' + 'bot'

while (True):
  user_massage = input('you: ').lower().strip(string.punctuation+string.whitespace)
  print (chatbot_name + ":", end=' ')

  if user_massage == 'quit' or user_massage == 'selesai':
    print ("sampai ketemu lagi")
    break

# blok bagian awal sapaan
  if user_massage == 'hallo':
    print ('halo juga ', end='')
  elif  user_massage == 'p' :
    print ('cok malah p', end='')
  elif  user_massage == 'cak' :
    print ('pie pie', end='')
  elif user_massage == 'cok':
      print ('jeluk sek bener, asem i', end='')
  elif 'uy' in user_massage :
      print ('pie cah', end='')
  elif user_massage == 'cah':
    print ('bicara', end='')
     
# blok bagian informasi kabar      
  elif 'kabar' in user_massage :
    print ('baik nih , kamu gimana?', end='')
  elif 'cuaca cerah' in user_massage :
    print ('iyaa ,secerah hati ku', end='')
  elif 'mendung' in user_massage :
    print ('hati apa cuaca', end='')
  elif user_massage == 'hati':
    print ('hehe sabar ya', end='')
  elif user_massage == 'cuaca':
    print ('cuma cuaca kan hehe', end='')
  elif 'munggah' in user_massage :
      print ('ngendi arepan', end='')
  elif 'andong' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'sumbing' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'sindoro' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'merbabu' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'merapi' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'telomoyo' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'lawu' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'mongkrang' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'prau' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'bismo' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'kembang' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'sikunir' in user_massage :
       print ('tanggal kapan sek', end='')
  elif 'slamet' in user_massage :
       print ('tenan e', end='')
       print ('tanggal kapan', end='')
  elif tanggal_munggah in user_massage :
      print ('isoh kui', end='')
  elif user_massage != tanggal_munggah :
      print ('sek tak delok info prei sek yo', end='')
    
# blok akhir chat
  elif user_massage == 'makasih' or user_massage == 'thanks':
    print ('masama', end='')
  else:
    print ('ehh pie kui', end='')
  print()
