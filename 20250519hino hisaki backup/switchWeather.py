def switchweather(weather,images):
    if weather.find("時々") >-1: #文字の検出
        split=weather.split('時々')#時々　で区切るようにする
        if split[0]=="晴れ":#区切ったときの0文字目
         return images[0]
        elif split[0]=="くもり":
            return images[1]      #＝＝（同じ）
        elif split[0]=="雨":
            return images[2]
        elif split[0]=="雪":
            return  images[3]
        elif split[0]=="雷雨":
            return images[4]
    if weather.find("後") >-1:
        split=weather.split('後')
        if "晴れ"in split[1]:
         return images[0]
        elif "くもり"in split[1]:
            return images[1]      #＝＝（同じ）
        elif "雨" in split[1]:
            return images[2]
        elif "雪"in split[1]:
            return  images[3]
        elif "雷雨"in split[1]:
            return images[4]
    if weather.find("から") >-1:
        split=weather.split('から')
        if split[1]=="晴れ":
         return images[0]
        elif split[1]=="くもり":
            return images[1]      #＝＝（同じ）
        elif split[1]=="雨":
            return images[2]
        elif split[1]=="雪":
            return  images[3]
        elif split[1]=="雷雨":
            return images[4]
    if weather.find("所により") >-1: #文字の検出
        split=weather.split('所により')
        if split[0]=="晴れ":#区切ったときの0文字目
         return images[0]
        elif split[0]=="くもり":
            return images[1]      #＝＝（同じ）
        elif split[0]=="雨":
            return images[2]
        elif split[0]=="雪":
            return  images[3]
        elif split[0]=="雷雨":
            return images[4]
    if weather.find("明け方まで") >-1:
        split=weather.split('明け方まで')
        if split[1]=="晴れ":
         return images[0]
        elif split[1]=="くもり":
            return images[1]      #＝＝（同じ）
        elif split[1]=="雨":
            return images[2]
        elif split[1]=="雪":
            return  images[3]
        elif split[1]=="雷雨":
            return images[4]
    #単体
    if weather=="晴れ":
        return images[0]
    elif weather=="くもり":
        return images[1]      #＝＝（同じ）
    elif weather=="雨":
        return images[2]
    elif weather=="雪":
        return  images[3]
    elif weather=="雷雨":
        return images[4]
    else:
        return images[2]