option = input("Enter option(1-ENCRYPT/2-DECRYPT/3-CRYPTANALYSIS): ")
dchar = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*_-'
if option in ('1', '2', '3'):
    print('--PROCESSING--')
    if option == '1':
        t = input('ENTER THE TEXT')
        s = 5
        c = 0
        x = str()
        for i in range (len(t)):
            f = dchar.find(t[i])
            if (f != -1):
                c= (f+5)%62
                x+= dchar[c]
            else:
                print('INVALID CHARACTER IN STRING')
                break
        print('Actual Text:'+t)
        print('Cipher:'+x)
    elif option == '2':
        t = input('ENTER THE TEXT')
        s = 5
        c = 0
        x = str()
        for i in range (len(t)):
            f = dchar.find(t[i])
            if (f != -1):
                c= (f-5)%62
                x+= dchar[c]
            else:
                print('INVALID CHARACTER IN STRING')
                break
        print('CIPHER:'+t)
        print('PLAIN TEXT:'+x)
    elif option == '3':
        file = open('D:\python\quadgrams.txt','r')
        quad = {}
        for line in file:
            k,val = line.split()
            quad[k] = val
        deciph=[]
        final={}
        t = input('ENTER THE TEXT  //*NEEDS TO BE ATLEAST FOUR LETTERS*//  :')
        print('CIPHER:'+t)
        c = 0
        for s in range(62):
            x = str()
            for i in range (len(t)):
                f = dchar.find(t[i])
                if (f != -1):
                    c= (f-s)%62
                    x+= dchar[c]
                else:
                    print('INVALID CHARACTER IN STRING')
                    break
            deciph.append(x)
        for q in quad:
            for k in deciph:
                count,dx = 0,4
                for y in range(0, len(k)):
                    v = k[0 + y:dx + y]
                    if (v == q):
                        print('please wait')
                        count = count + 1
                    elif (len(k) < (dx + y)):
                        break
                if (count==1):
                    final[k]=quad[q]
        print(final)
    

        


