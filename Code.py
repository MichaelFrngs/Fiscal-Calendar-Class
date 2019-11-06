import datetime as dt
import time
import os
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta #Lets you use (years_ago = datetime.datetime.now() - relativedelta(years=5))

class Calendar(object):
    def __init__(self):
      self.CurrentDate = dt.datetime.now()
      self.OffsetNumOfDays = -4 #Feel free to change the report date you need. Live data is usually -1
      self.CurrentDate = self.CurrentDate + dt.timedelta(days=self.OffsetNumOfDays)
    
      #Reformatting to use .loc on fiscal calendar file
      if self.CurrentDate.day < 10:
        self.CurrentDateReformat_day = "0" + str(self.CurrentDate.day)
      else: 
        self.CurrentDateReformat_day = str(self.CurrentDate.day)
      
      if self.CurrentDate.month < 10:
        self.CurrentDateReformat_month = "0" + str(self.CurrentDate.month)
      else: 
        self.CurrentDateReformat_month = str(self.CurrentDate.month)
        
      self.CurrentDateReformat = str(self.CurrentDate.year) + "-" + str(self.CurrentDateReformat_month) + "-" + str(self.CurrentDateReformat_day)
  
      
      self.ReportDate = self.CurrentDate + dt.timedelta(days=-self.CurrentDate.weekday()-1, weeks=-1) #Selects last sunday
      print("Report Date: ", self.ReportDate,self.ReportDate + dt.timedelta(days=6))
       
      self.ReportMonth = self.ReportDate.month 
      self.ReportDay = self.ReportDate.day 
      self.ReportYear = self.ReportDate.year
      
      self.ReportMonth2 = (self.ReportDate + dt.timedelta(days=6)).month 
      self.ReportDay2 = (self.ReportDate + dt.timedelta(days=6)).day 
      self.ReportYear2 = (self.ReportDate + dt.timedelta(days=6)).year
  
      
      self.CurrentMonth = self.CurrentDate.month 
      self.CurrentDay = self.CurrentDate.day 
      self.CurrentYear = self.CurrentDate.year
      
      if self.ReportMonth == 1 or self.ReportMonth == 2 or self.ReportMonth == 3:
        self.ReportQuarter = 1
      elif self.ReportMonth == 4 or self.ReportMonth == 5 or self.ReportMonth == 6:
        self.ReportQuarter = 2
      elif self.ReportMonth == 7 or self.ReportMonth == 8 or self.ReportMonth == 9:
        self.ReportQuarter = 3
      else:
        self.ReportQuarter = 4
      print("Current Quarter: ",self.ReportQuarter)
    
      Quarter_months_list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
  
      os.chdir("C:/Users/mfrangos/Desktop/Fiscal Calendars")
      
      self.FiscalCalendar = pd.read_excel("GeneralLedger Calendar.xlsx")
      
      self.CurrentFiscalDay = self.FiscalCalendar.loc[self.FiscalCalendar["Date"] == self.CurrentDateReformat]["GL DAY"].iloc[0]
      self.CurrentFiscalWeek = self.FiscalCalendar.loc[self.FiscalCalendar["Date"] == self.CurrentDateReformat]["GL WK"].iloc[0]
      self.CurrentFiscalYear = self.FiscalCalendar.loc[self.FiscalCalendar["Date"] == self.CurrentDateReformat]["GL YR"].iloc[0]
      self.CurrentFiscalPeriod = self.FiscalCalendar.loc[self.FiscalCalendar["Date"] == self.CurrentDateReformat]["GL PD"].iloc[0]
      self.CurrentFiscalDate = str(self.CurrentFiscalYear) + "-" + str(self.CurrentFiscalPeriod) + "-" + str(self.CurrentFiscalDay)
      
      self.Short_CurrentFiscalDay = self.FiscalCalendar.loc[self.FiscalCalendar["Date"] == self.CurrentDateReformat]["SHORT GL DAY"].iloc[0]
      self.Short_CurrentFiscalWeek = self.FiscalCalendar.loc[self.FiscalCalendar["Date"] == self.CurrentDateReformat]["SHORT GL WK"].iloc[0]
      
      print("Report Fiscal Date: ", self.CurrentFiscalDay, f" ||| Offset by {self.OffsetNumOfDays} days from current fiscal day of {self.CurrentFiscalDay - self.OffsetNumOfDays}")
      
    #Calendar Dates
    def Calendar_Date_to_Calendar_words(self,day,month,year):
      output = date(day=day, month=month, year=year).strftime('%A %d %B %Y')
      return output
    def Calendar_Date_to_Calendar_month(self,day,month,year):
      output = date(day=day, month=month, year=year).strftime('%B')
      return output
    def Calendar_Date_to_Calendar_day(self,day,month,year):
      output = date(day=day, month=month, year=year).strftime('%d')
      return output
    def Calendar_Date_to_WeekDay(self,day,month,year):
      output = date(day=day, month=month, year=year).strftime('%A')
      return output
    def Calendar_Date_to_Calendar_year(self,day,month,year):
      output = date(day=day, month=month, year=year).strftime('%Y')
      return output
    
    
    
    def WK_Format(self,date):
      if self.date < 10:
        self.output = str("WK0") + str(date)
      else:
        self.output = str(date)
      return self.output
  
  ###For extracting datetime from Tableau business date
  #TY_date_time_list = []
  #from time import strptime
  #i=0
  #for year in TY_Daily_Margins.iloc[:, 5]:
  #  month = TY_Daily_Margins.iloc[i, 6]
  #  day = TY_Daily_Margins.iloc[i, 7]
  #  #print(month[:3])
  #  TY_date_time_list.append(date(day=day, year=year, month=strptime(f'{month[:3]}','%b').tm_mon))
  #  i=i+1
    
  
      #
    def Calendar_Date_to_FiscalDate(self,Calendar_Date):
      #DT_Fiscaldate = Fiscal_Date
      #assuming we're passing date_times
      #print(FiscalCalendar.loc[(FiscalCalendar["GL DAY"] == Calendar_Date.day)].head())
      #print(FiscalCalendar.loc[(FiscalCalendar["GL PD"] == Calendar_Date.month)].head())
      #print(FiscalCalendar.loc[(FiscalCalendar["GL YR"] == Calendar_Date.year)].head())
      
      self.Fiscal_Date = self.FiscalCalendar.loc[((self.FiscalCalendar["calendar day"] == Calendar_Date.day) & 
                                       (self.FiscalCalendar["calendar month"] == Calendar_Date.month) &
                                       (self.FiscalCalendar["calendar year"] == Calendar_Date.year))]
      
      return [self.Fiscal_Date["GL DAY"], self.Fiscal_Date["GL WK"], self.Fiscal_Date["GL PD"], self.Fiscal_Date["GL YR"]]
        
  #test = dt.date(year = 2018, month = 7, day = 12)
  #Output = Calendar_Date_to_FiscalDate(test)
      
    def date_time_to_fiscal_week(self,datetime_stamp,FiscalCalendar):
      self.fiscal_week = (self.FiscalCalendar.loc[self.FiscalCalendar["Date"] == datetime_stamp])["GL WK"]
      return self.fiscal_week
  
    def int_to_month_string(self,some_integer):
      if some_integer <= 0:
        Distance_from_zero = abs(some_integer)  
        #allows for negative numbers to loop around the number 12
        some_integer = 12 - Distance_from_zero%12
      else:
        pass
      if some_integer == 1:
        return  "Jan"
      elif some_integer == 2:
        return  "Feb"
      elif some_integer == 3:
        return  "Mar"      
      elif some_integer == 4:
        return  "Apr"        
      elif some_integer == 5:
        return  "May"
      elif some_integer == 6:
        return  "Jun"
      elif some_integer == 7:
        return  "Jul"
      elif some_integer == 8:
        return  "Aug"
      elif some_integer == 9:
        return  "Sep"
      elif some_integer == 10:
        return  "Oct"      
      elif some_integer == 11:
        return  "Nov"      
      elif some_integer == 12:       
        return  "Dec"

    def Fiscal_WK_to_Fiscal_Period(self,week_integer):
      #handles for numbers starting with 0
      if (len(str(week_integer)) > 1) and str(week_integer)[0] == "0":
        week_integer = int(str(week_integer)[1:])
      else:
        pass
      Fiscal_Period = self.FiscalCalendar.loc[self.FiscalCalendar["GL WK"] == week_integer]["GL PD"].iloc[1]
      return Fiscal_Period
    
    def Date_Code_to_Fiscal_Date(self,DCODE):
      Fiscal_Date = self.FiscalCalendar.loc[(self.FiscalCalendar["DCODE"] == int(DCODE))].reset_index(drop=True)
      Fiscal_Day =     Fiscal_Date["GL WK"]
      Fiscal_Year =    Fiscal_Date["GL YR"]
      Fiscal_Month =   Fiscal_Date["GL PD"]
      Fiscal_Quarter = Fiscal_Date["Quarter"]
      Week_Day =       Fiscal_Date["DAY2"]
      #print("Data return order: Fiscal_Year, Fiscal_Month, Fiscal_Day, Fiscal_Quarter, Week_Day")
      return Fiscal_Year, Fiscal_Month, Fiscal_Day, Fiscal_Quarter, Week_Day
    
    def GL_YR_and_GL_WK_to_GLPD(self,GL_YR,GL_WK):
      GL_PD = self.FiscalCalendar.loc[(self.FiscalCalendar["GL YR"] == GL_YR) & (self.FiscalCalendar["GL WK"] == GL_WK)]["GL PD"].iloc[1]
      return GL_PD

#Create Calendar Object
Current_Calendar = Calendar()
#############################################################################################################

#Example
Current_Calendar.CurrentDate
#Current_Calendar.Date_Code_to_Fiscal_Date(20190101)
