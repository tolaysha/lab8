def main():
    input_code = '000000000000000'
    Cn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Ck = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    Nk = 0
    Mist_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(1, 32768):
        b = bin(i)                                      # b - РѕС€РёР±РєР° РІ РґРІРѕРёС‡РЅРѕР№ СЃРёСЃС‚РµРјРµ
        b = b[2:]                                       # i - РџРµСЂРІР°СЏ РѕС€РёР±РєР°
        b = '0'*(15-len(b)) + b                          #b - РІРµРєС‚РѕСЂ РѕС€РёР±РєРё



        mistakes_count = 0
        list_with_mistakes = input_code + ''
        mistake_sindrom = ''

        for bit in range(15):                                                    #СЃС‡РёС‚Р°РµРј РєРѕР»-РІРѕ РµРґРёРЅРёС†(СЂР°Р·СЂСЏРґРЅРѕСЃС‚СЊ РѕС€РёР±РєРё)
            if b[bit] == '1':
                list_with_mistakes = list_with_mistakes[0:bit] + str((int(
                    list_with_mistakes[bit]) + 1) % 2) + list_with_mistakes[bit+1:]     # Р”РµР»Р°РµРј РѕС€РёР±РєРё РІ РёСЃС…РѕРґРЅРѕРј
                mistakes_count += 1                                             # СЂРђР—Р РЇР”РќРћРЎРўР¬ РћРЁРР‘РљР

        # print(list_with_mistakes)
        Mist_count[mistakes_count] += 1
        # print(mistakes_count)
        if ((int(list_with_mistakes[0]) + int(list_with_mistakes[1]) + int(list_with_mistakes[2]) + int(
                list_with_mistakes[3]) + int(list_with_mistakes[4]) + int(list_with_mistakes[5]) + int(
                list_with_mistakes[6])) % 2 == int(list_with_mistakes[7])):
            mistake_sindrom = '0'
        else:
            mistake_sindrom = '1'

        if ((int(list_with_mistakes[0]) + int(list_with_mistakes[1]) + int(list_with_mistakes[2]) + int(
                list_with_mistakes[3]) + int(list_with_mistakes[8]) + int(list_with_mistakes[9]) + int(
            list_with_mistakes[10]))% 2==int(list_with_mistakes[11])):
            mistake_sindrom += '0'
        else:
            mistake_sindrom += '1'


        if ((int(list_with_mistakes[0]) + int(list_with_mistakes[1]) + int(list_with_mistakes[4]) + int(
                list_with_mistakes[5]) + int(list_with_mistakes[8]) + int(list_with_mistakes[9]) + int(
            list_with_mistakes[12])) % 2 == int(list_with_mistakes[13])):
            mistake_sindrom += '0'
        else:
            mistake_sindrom += '1'



        if ((int(list_with_mistakes[2]) + int(list_with_mistakes[4]) + int(list_with_mistakes[6]) + int(
                list_with_mistakes[8])+ int(list_with_mistakes[10])+ int(list_with_mistakes[12])+ int(
                list_with_mistakes[0] ))% 2==int(list_with_mistakes[14])):
            mistake_sindrom += '0'
        else:
            mistake_sindrom += '1'








        mistakes_bit =15- int(mistake_sindrom, 2)                                                                                         # РџРѕ РІРµРєС‚РѕСЂСѓ РѕС€РёР±РєРё РЅР°С…РѕРґРёРј РІ РєР°РєРѕРј Р±РёС‚Рµ РѕС€РёР±РєР°



        if mistakes_bit == 15:
            list_without_mistakes = list_with_mistakes
            Cn[mistakes_count] -= 1

        else:
            list_without_mistakes = list_with_mistakes[0:mistakes_bit] + str((int(
                list_with_mistakes[mistakes_bit]) + 1) % 2) + list_with_mistakes[mistakes_bit+1:]
                                                                                                        # РСЃРїСЂР°РІР»СЏРµРј СЌС‚Сѓ РѕС€РёР±РєСѓ
        if list_without_mistakes == input_code:
            # print('РћС€РёР±РєР° РёСЃРїСЂР°РІР»РµРЅР°!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            Ck[mistakes_count] += 1
            Cn[mistakes_count] += 1
        else:

            if ((int(list_without_mistakes[0]) + int(list_without_mistakes[1]) + int(list_without_mistakes[2]) == int(
                    list_without_mistakes[3])) and int(list_without_mistakes[0]) + int(list_without_mistakes[1]) + int(
                    list_without_mistakes[4]) == int(list_without_mistakes[5])) and (int(list_without_mistakes[0]) + int(
                    list_without_mistakes[2]) + int(list_without_mistakes[4]) == int(list_without_mistakes[6])):

                # print('РСЃРїСЂР°РІР»РµРЅa РЅРµРІРµСЂРЅРѕ  --------')
                Cn[mistakes_count] += 1
            else:
                # print('РќРµ РёСЃРїСЂР°РІР»РµРЅР°')
                Cn[mistakes_count] += 1

        # print(mistakes_bit)

    # print("VOT OTVEt " +  str(Ck[1]))

    print("_________________________________________")
    print('i  |РљРѕР»-РІРѕ   | РСЃРїСЂ. |  РСЃРїСЂ.%')
    print("_________________________________________")

    for n in range(1, 15):
        print('{0:1d}   {1:4d}       {2:4d}    {3:4d}   %'.format(n, Mist_count[n], Ck[n], int((Ck[n])/Mist_count[n])*100))


    print("__________________________________________")


main()