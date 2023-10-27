# Tubes-Pengkom
  def microwave:
    def temperature:
      a = int(input("a: "))
      b = int(input("b: "))
      c = int(input("c: "))
      
      # Microwave Hanya bisa berada dalam satuan (0-9)
      if a > 9 or a < 0 or b < 0 or b > 9 or c < 0 or c > 9:
          print("Error! Silakan diulang kembali!")
      
      # Microwave hanye bisa berada pada suhu 50 - 300 derajat celcius
      else:
          if a == 0 and b >= 5:
              A = int(str(b) + str(c))
              print(f"{A} derajat Celcius")
          elif a == 0 and b < 5: 
              print("Error! Silakan diulang kembali!")
          elif a > 3:
              print("Error! Silakan diulang kembali!")
          elif a == 3:
              B = int(str(a) + str(b) + str(c))
              if B > 300:
                  print("Error! Silakan diulang kembali!")
              else:
                  print(f"{B} derajat celcius.")
          else:
              C = int(str(a) + str(b) + str(c))
              print(f"{C} derajat Celcius")
  
      
