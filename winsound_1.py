import winsound
def play_sound(weather):
       global play_sound
       if weather.find("時々") >-1: #文字の検出
              split=weather.split('時々')
              if split[0]=="晴れ":#区切ったときの0文字目
                     winsound.PlaySound(r"sounds\sunny.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
                     return
              elif split[0]=="くもり":
                     winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)  
                     return     #＝＝（同じ）
              elif split[0]=="雨":
                     winsound.PlaySound(r"sounds\rain.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return
              elif split[0]=="雪":
                     winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return
              elif split[0]=="雷雨":
                     winsound.PlaySound(r"sounds\thunder.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)             
                     return
       if weather.find("から") >-1: #文字の検出
              split=weather.split('から')
              if "晴れ" in split[1]:#区切ったときの0文字目
                     winsound.PlaySound(r"sounds\sunny.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)  
                     return 
              elif "くもり"in split[1]:
                     winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)  
                     return     #＝＝（同じ）
              elif "雨"in split[1]:
                     winsound.PlaySound(r"sounds\rain.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return
              elif "雪"in split[1]:
                     winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return
              elif "雷雨"in split[1]:
                     winsound.PlaySound(r"sounds\thunder.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return      
       if weather.find("後") >-1: #文字の検出
              split=weather.split('後')
              if "晴れ"in split[1] :#区切ったときの0文字目
                     winsound.PlaySound(r"sounds\sunny.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
                     return  
              elif  "くもり" in split[1] :
                     winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
                     return      #＝＝（同じ）
              elif  "雨" in split[1] :
                     winsound.PlaySound(r"sounds\rain.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return
              elif "雪"in split[1] :
                     winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return
              elif "雷雨"in split[1] :
                     winsound.PlaySound(r"sounds\thunder.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
                     return       
       if weather=="晴れ":
              winsound.PlaySound(r"sounds\sunny.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
              return  
       elif weather=="くもり":
              winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
              return         #＝＝（同じ）
       elif weather=="雨":
              winsound.PlaySound(r"sounds\rain.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
              return  
       elif weather=="雪":
              winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
              return  
       elif weather=="雷雨":
              winsound.PlaySound(r"sounds\thunder.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
              return        
       if weather.find("明け方まで") >-1: #文字の検出
              split=weather.split('明け方まで')
              if split[1]in"晴れ":#区切ったときの0文字目
                     winsound.PlaySound(r"sounds\sunny.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
                     return
              elif split[1]in"くもり":
                     winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)  
                     return     #＝＝（同じ）
              elif split[1]in"雨":
                     winsound.PlaySound(r"sounds\rain.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return
              elif split[1]in"雪":
                     winsound.PlaySound(r"sounds\cloudyorsnowy.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)
                     return
              elif split[1]in"雷雨":
                     winsound.PlaySound(r"sounds\thunder.wav", winsound.SND_FILENAME|winsound.SND_ASYNC)             
                     return
       winsound.PlaySound(r"sounds\rain.wav", winsound.SND_FILENAME|winsound.SND_ASYNC) 
def stop_sound():
       winsound.PlaySound(None, winsound.SND_PURGE)
