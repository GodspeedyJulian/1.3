def Lighten():
    BurnFlag=False
    for i in range (1,8):
        for n in range (1,8):
            Oldpixelvalue=Picture[i,j]
            PixelTemp=Oldpixelvalue *1.1
            NewPixelVale=int(PixelTemp)
            if NewPixelValue >225:
                NewPixelValue = 225
                BurnFlag = True
            Picture [i,j]=NewPixelValue
return BurnFlag
