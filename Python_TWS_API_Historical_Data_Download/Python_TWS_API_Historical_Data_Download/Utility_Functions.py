import os
import gzip
import Drive_to_Save_Files_to
import sys

Drive_to_Save_Files_to.Drive_Function_Class.Drive_Function(sys.argv[1])

class Instrument_Type_Class:
    Inst_Type = ""
    @classmethod
    def Inst_Type_Function(cls, T):
        cls.Inst_Type = T

Instrument_Type_Class.Inst_Type_Function(sys.argv[2])



class Write_to_File:
    #def __init__(self):
       #Raw_File = open("C:\Python TWS API\Python_TWS_API_Historical_Data_Download\Python_TWS_API_Historical_Data_Download\TestFile.txt","w")

    #def open_File_to_Save_Ticks_to(self, PathFileName:str):
    #    self.Raw_File = open(PathFileName,"a")

    #def saving_Bars_to_File(self, bar):
    #    self.Raw_File.write(bar.date + "|" + str(bar.open) + "|" + str(bar.high) + "|" + str(bar.low) + "|" + str(bar.close) + "|" + str(bar.volume) + "|" + str(bar.barCount) + "\n")
    #    #self.Raw_File.write(bar.date + "|" + str(bar.open) + "|" + str(bar.high) + "|" + str(bar.low) + "|" + str(bar.close) + "|" + str(bar.volume) + "|" + str(bar.barCount) + "\n")
    #    print(bar.date + "|" + str(bar.open) + "|" + str(bar.high) + "|" + str(bar.low) + "|" + str(bar.close) + "|" + str(bar.volume) + "|" + str(bar.barCount) + "\n")

    ### For Bars
    @staticmethod
    def saving_Bars_to_File(Ticks_List, trading_date_item, Ticker_Symbol, Sec_Type_and_Currency):
        # For Stocks:
        if Sec_Type_and_Currency == "STK|USD":
            Folder = r"{}:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\\".format(Drive_to_Save_Files_to.Drive_Function_Class.Dr) + Ticker_Symbol
            if os.path.exists(Folder):
                pass
            else:
                os.makedirs(r"{}:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\\".format(Drive_to_Save_Files_to.Drive_Function_Class.Dr) + Ticker_Symbol)
            Raw_File = gzip.open(r"{}:\Raw_Data\Raw_1_sec_Bar_Data\US_Stocks\\".format(Drive_to_Save_Files_to.Drive_Function_Class.Dr) + 
                                 Ticker_Symbol + "\\" + Ticker_Symbol + "_Bars_" + trading_date_item + ".txt.gz","wb")
            Raw_File.write(b"DateTime_UTC|Open|High|Low|Close|Volume|Count|\r\n")
            for l in Ticks_List:
                Raw_File.write(l.encode())
            Raw_File.close
        else:
        # For FX:
            Folder = r"{}:\Raw_Data\Raw_1_sec_Bar_Data\FX\\".format(Drive_to_Save_Files_to.Drive_Function_Class.Dr) + Ticker_Symbol
            if os.path.exists(Folder):
                pass
            else:
                os.makedirs(r"{}:\Raw_Data\Raw_1_sec_Bar_Data\FX\\".format(Drive_to_Save_Files_to.Drive_Function_Class.Dr) + Ticker_Symbol)
            Raw_File = gzip.open(r"{}:\Raw_Data\Raw_1_sec_Bar_Data\FX\\".format(Drive_to_Save_Files_to.Drive_Function_Class.Dr) + 
                                 Ticker_Symbol + "\\" + Ticker_Symbol + "_Bars_" + trading_date_item + ".txt.gz","wb")
            Raw_File.write(b"DateTime_UTC|Open|High|Low|Close|Volume|Count|\r\n")
            for l in Ticks_List:
                Raw_File.write(l.encode())
            Raw_File.close    
        #self.Raw_File.write(bar.date + "|" + str(bar.open) + "|" + str(bar.high) + "|" + str(bar.low) + "|" + str(bar.close) + "|" + str(bar.volume) + "|" + str(bar.barCount) + "\n")
        #print(bar.date + "|" + str(bar.open) + "|" + str(bar.high) + "|" + str(bar.low) + "|" + str(bar.close) + "|" + str(bar.volume) + "|" + str(bar.barCount) + "\n")
    
    #@staticmethod
    #def close_File_to_Save_Bars_to():
    #    self.Raw_File.close
    
    ### For Ticks
    @staticmethod
    def saving_Ticks_to_File(Ticks_List):
        Raw_File = open("{}:\Python TWS API\Python_TWS_API_Historical_Data_Download\Python_TWS_API_Historical_Data_Download\TestTicksFile.txt".format(Drive_to_Save_Files_to.Drive_Function_Class.Dr),"w")
        Raw_File.write("DateTime_UTC|Price|Size|Exchange|Condition_Code\n")
        for l in Ticks_List:
            Raw_File.write(l)
        Raw_File.close
        #self.Raw_File.write(bar.date + "|" + str(bar.open) + "|" + str(bar.high) + "|" + str(bar.low) + "|" + str(bar.close) + "|" + str(bar.volume) + "|" + str(bar.barCount) + "\n")
        #print(bar.date + "|" + str(bar.open) + "|" + str(bar.high) + "|" + str(bar.low) + "|" + str(bar.close) + "|" + str(bar.volume) + "|" + str(bar.barCount) + "\n")
    
    #@staticmethod
    #def close_File_to_Save_Ticks_to():
    #    self.Raw_File.close