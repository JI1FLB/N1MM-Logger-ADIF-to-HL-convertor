from Phase0 import phase0
#from Phase0_1 import phase0_1
from Phase1 import phase1
from Phase3 import phase3


#--------------------

Callsign = ""
Contest_name = ""
#FD_coe = 1
okng = True
Ph0_data = []


#----------------------------------------------------------------------------------
print("+-------------------------------------------------------------------------+")
print("|                                                                         |")
print("|                                                                         |")
print("|  N1MM logger+ ADIFファイルからTurboHAMログ変換ツールver1.0    　　　　　|")
print("|                                                                         |")
print("|                                                                         |")
print("|            2019/04/22 Copyright JI1FLB Seiichi Tanaka                   |")
print("|                                                                         |")
print("|   仕様                                                                  |")
print("|    1.入力条件                                                           |")
print("|       NtMM Logger+ でADIFファイルをExport　                             |")
print("|          ※ ファイル名は自分のコールサイン.adi                          |")
print("|       ソフトウェアの入力ガイダンスに合わせて、必要情報を入力            |")
print("|                                                                         |")
print("|                                                                         |")
print("|    2.出力ファイル 　                                                    |")
print("|       2.1　ハムログ用のＣＳＶファイル　                   　　　　　　　|")
print("|                                                                         |")
print("+-------------------------------------------------------------------------+")
print("+-------------------------------------------------------------------------+")
#------------------------------------------

#     Phase0を起動
#           コールサイン取得

Ph0_data = phase0()

Callsign = Ph0_data[0]

#FD_coe = int(Ph0_data[1])

#Contest_name = phase0_1( Callsign )

#print( 'Contest name ->'  + Contest_name )
#print("*** Completed the phase0 process"+"\n")

#  Phase1を起動
#       ADIFファイルのログライン分割を1ラインに修正

phase1( Callsign )

print("*** Completed the phase1 process"+"\n")


#Phase3を起動
#       ADIFファイルからTuboHAMログファイルに変換


phase3( Callsign , Contest_name )

print("*** Completed the phase3 process"+"\n")


