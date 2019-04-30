def phase0():


#------------------------------
#
#   JARLサマリーシート作成
#
#   仕様：記入フォームから、summaryフォーマットに変換


    import os

    fill_in_form = open( "form.txt" ,"r", encoding='utf-8')

    Callsign =""
#    GestOP_Callsign =""
#    GestOP_flag = "N"
#    Multi_OP_flag = "N"
#    FD_flag ="N"
#    yesno = "N"
#    okng = True
#    FD_coe = 1
    Ph0 = []


#----------------------------------------------------------------------
    print("\n")
    print("***　サマリーシート必要事項選択")
    print("\n")
    


#------------------------------------------------------------------------
#
#   コールサイン取得
#   サマリーシート作成
#
   

    fill_in = fill_in_form.readlines()

    for fill in fill_in :
        fill = fill.rstrip('\n')
        fill = fill.strip()
        fill = fill.split(":")
        if "コールサイン"==fill[0] :
            Callsign = fill[1]
            Callsign = Callsign.lstrip().rstrip()
            Ph0.append(Callsign)
            break

    fill_in_form.close()
    
    
    return Ph0
