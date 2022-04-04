import yfinance as yf
import subprocess
import pandas as pd
from datetime import date, timedelta
from matplotlib import pyplot as plt
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from functions import *
updater = Updater("5293034765:AAFOIJ0wRNEfe1fLRLP-XmpvUWGEZF8YvxE",
				use_context=True)
def start(update : Update, context : CallbackContext):
	update.message.reply_text("Welcome to Stocks bot,How may I help you. \n\nAvailable Commands\n/bse\n/nse\n")
# def Stocks( Update):
# 	update.message.reply_text("Available Commands\n"+
# 	 "/bse\n"+
# 	  "/nse\n")
def sensex(update : Update, context : CallbackContext):
	update.message.reply_text("Welcome to Bombay Stock Exchange\n"+
                                  "/bsestocks-View stocks in BSE\n"+
                                  "/bseindex-To view index of BSE\n")
def bsestocks(update : Update, context : CallbackContext):
	update.message.reply_text("List of Top Stocks in BSE\n"+
                                  "/bseadaniports\n"+
                                  "/bseasianpaint\n"+
                                  "/bseaxisbank\n"+
                                  "/bsebajajauto\n"+
                                  "/bsebajajfianance\n"+
                                  "/bsebajajfinserv\n"+
                                  "/bsebritania\n"+
                                  "/bsecipla\n"+
                                  "/bsehcltech\n"+
                                  "/bsehdfc\n"+
                                  "/bseheromotoco\n"+
                                  "/bsehidalco\n"+
                                  "/bsehinduuniliver\n"+
                                  "/bseicicibank\n"+
                                  "/bseindusind\n"+
                                  "/bsemaruti\n"+
                                  "/bsereliance\n"+
                                  "/bsesunpharma\n"+
                                  "/bsetcs\n"+
                                  "/bsetatapower\n"+
                                  "/bsetatachemical\n"+
                                  "/bsetatasteel\n"+
                                  "/bsetitan\n"+
                                  "/bseupl\n"+
                                  "/bsewipro\n"+
                                  "/bsezeel\n")
                                  
def bseindex(update : Update, context : CallbackContext):
	update.message.reply_text("Welcome to Bombay Stock Exchange\n"+
                                  "Todays index is 55423\n")
def nifty(update : Update, context : CallbackContext):
	update.message.reply_text("Welcome to National Stock Exchange\n"+
                                  "/nsestocks-View stocks in NSE\n"+
                                  "/nseindex-To view index of NSE\n")
def nsestocks(update : Update, context : CallbackContext):
	update.message.reply_text("List of Top Stocks in NSE\n"+
	                               "/nseadaniports\n"+
                                  "/nseasianpaint\n"+
                                  "/nseaxisbank\n"+
                                  "/nsebajajauto\n"+
                                  "/nsebajajfianance\n"+
                                  "/nsebajajfinserv\n"+
                                  "/nsebritania\n"+
                                  "/nsecipla\n"+
                                  "/nsehcltech\n"+
                                  "/nsehdfc\n"+
                                  "/nseheromotoco\n"+
                                  "/nsehidalco\n"+
                                  "/nsehinduuniliver\n"+
                                  "/nseicicibank\n"+
                                  "/nseindusind\n"+
                                  "/nsemaruti\n"+
                                  "/nsereliance\n"+
                                  "/nsesunpharma\n"+
                                  "/nsetcs\n"+
                                  "/nsetatapower\n"+
                                  "/nsetatachemical\n"+
                                  "/nsetatasteel\n"+
                                  "/nsetitan\n"+
                                  "/nseupl\n"+
                                  "/nsewipro\n"+
                                  "/nsezeel\n")

def nseindex(update : Update, context : CallbackContext):
	update.message.reply_text("Welcome to National Stock Exchange\n"+
                                  "Todays index is 19423\n")

def send_image(botToken, imageFile, chat_id):
        command = 'curl -s -X POST https://api.telegram.org/bot' + botToken + '/sendPhoto -F chat_id=' + chat_id + " -F photo=@" + imageFile
        subprocess.call(command.split(' '))
        return


# Startyear = date.today() - timedelta(365)
# Startyear.strftime('%Y-%m-%d')
# Endyear = date.today() + timedelta(2)
# Endyear.strftime('%Y-%m-%d')



# Startmonth = date.today() - timedelta(30)
# Startmonth.strftime('%Y-%m-%d')
# Endmonth = date.today() + timedelta(2)
# Endmonth.strftime('%Y-%m-%d')



# Startday = date.today() - timedelta(1)
# Startday.strftime('%Y-%m-%d')
# Endday = date.today() + timedelta(2)
# Endday.strftime('%Y-%m-%d')



# def closing_priceyear(ticker):
#     Assetyear = pd.DataFrame(yf.download(ticker, start=Startyear,
#       end=Endyear)['Adj Close'])     
#     return Assetyear
# def closing_pricemonth(ticker):
#     Assetmonth = pd.DataFrame(yf.download(ticker, start=Startmonth,
#       end=Endmonth)['Adj Close'])     
#     return Assetmonth
# def closing_priceday(ticker):
#     Assetday = pd.DataFrame(yf.download(ticker, start=Startday,
#       end=Endday)['Adj Close'])     
#     return Assetday

# def shareyear(str1):
#     GRAPH = closing_priceyear(str1)                  # CALL THE FUNCTION
#     plt.plot(GRAPH, color='red', linewidth=2)
#     plt.title(str1 +' Performance')
#     plt.ylabel('Price (Rs)')
#     plt.xlabel('Date')
#     plt.savefig('image.png')
#     send_image("5293034765:AAFOIJ0wRNEfe1fLRLP-XmpvUWGEZF8YvxE", 'image.png', '1099048606')
#     plt.clf()
   
# def sharemonth(str1):
#     GRAPH = closing_pricemonth(str1)                  # CALL THE FUNCTION
#     plt.plot(GRAPH, color='red', linewidth=2)
#     plt.title(str1 +' Performance')
#     plt.xlabel('Date')
#     plt.ylabel('Price (Rs)')
#     plt.savefig('image.png')
#     send_image("5293034765:AAFOIJ0wRNEfe1fLRLP-XmpvUWGEZF8YvxE", 'image.png', '1099048606')
#     plt.clf()
    
# def shareday(str1):
#     GRAPH = closing_priceday(str1)                  # CALL THE FUNCTION
#     plt.plot(GRAPH, color='red', linewidth=2)
#     plt.title(str1 +' Performance')
#     plt.ylabel('Price (Rs)')
#     plt.xlabel('Date')
#     plt.savefig('image.png')
#     send_image("5293034765:AAFOIJ0wRNEfe1fLRLP-XmpvUWGEZF8YvxE", 'image.png', '1099048606')
#     plt.clf()
  

# #*****************TCS***************************************
# #nse-tcs
# nsetcs( Update)
#     # update.message.reply_text("Choose the time span for TCS share\n"+
#     #                           "/dailynsetcs\n"+ 
#     #                           "/monthlynsetcs\n"+ 
#     #                           "/yearlynsetcs\n")
# dailynsetcs( Update)
# #     
# #     shareday('TATASTEEL.NS')
# monthlynsetcs( Update)
# #     
# #     sharemonth('TCS.NS')
# yearlynsetcs( Update)
# #     
# #     shareyear('TCS.NS')
# # #bse-tcs
# bsetcs( Update)
# #     update.message.reply_text("Choose the time span for TCS share\n"+
# #                               "/dailybsetcs\n"+ 
# #                               "/monthlybsetcs\n"+ 
# #                               "/yearlybsetcs\n")
# dailybsetcs( Update)
# #     
# #     shareday('TCS.BO')
# monthlybsetcs( Update)
# #     
# #     sharemonth('TCS.BO')
# yearlybsetcs( Update)
# #     
# #     shareyear('TCS.BO')
# # #***************AdaniPorts***********************
# # #nse-adaniports
# nseadaniports( Update)
# #     update.message.reply_text("Choose the time span for adaniports share\n"+
# #                               "/dailynseadaniports\n"+ 
# #                               "/monthlynseadaniports\n"+ 
# #                               "/yearlynseadaniports\n")
# dailynseadaniports( Update)
# #     
# #     shareday('ADANIPORTS.NS')
# monthlynseadaniports( Update)
# #     
# #     sharemonth('ADANIPORTS.NS')
# yearlynseadaniports( Update)
# #     
# #     shareyear('ADANIPORTS.NS')
# # #bse-adaniports
# bseadaniports( Update)
# #     update.message.reply_text("Choose the time span for adaniports share\n"+
# #                               "/dailybseadaniports\n"+ 
# #                               "/monthlybseadaniports\n"+ 
# #                               "/yearlybseadaniports\n")
# dailybseadaniports( Update)
# #     
# #     shareday('ADANIPORTS.BO')
# monthlybseadaniports( Update)
# #     
# #     sharemonth('ADANIPORTS.BO')
# yearlybseadaniports( Update)
# #     
# #     shareyear('ADANIPORTS.BO')
# # #*************************Asian Paints**************************
# # #nse-asianpaints
# nseasianpaints( Update)
# #     update.message.reply_text("Choose the time span for asianpaints share\n"+
# #                               "/dailynseasianpaints\n"+ 
# #                               "/monthlynseasianpaints\n"+ 
# #                               "/yearlynseasianpaints\n")
# dailynseasianpaints( Update)
# #     
# #     shareday('ASIANPAINT.BO')
# monthlynseasianpaints( Update)
# #     
# #     sharemonth('ASIANPAINT.BO')
# yearlynseasianpaints( Update)
# #     
# #     shareyear('ASIANPAINT.BO')
# # #bse-asianpaints
# # bseasianpaints( Update):
# #     update.message.reply_text("Choose the time span for asianpaints share\n"+
# #                               "/dailybseasianpaints\n"+ 
# #                               "/monthlybseasianpaints\n"+ 
# #                               "/yearlybseasianpaints\n")
# dailybseasianpaints( Update)
# #     
# #     shareday('ASIANPAINT.BO')
# monthlybseasianpaints( Update)
# #     
# #     sharemonth('ASIANPAINT.BO')
# yearlybseasianpaints( Update)
# #     
# #     shareyear('ASIANPAINT.BO')
# # #********************AxisBank***********************************
# # #nse-axisbank
# nseaxisbank( Update)
# #     update.message.reply_text("Choose the time span for axisbank share\n"+
# #                               "/dailynseaxisbank\n"+ 
# #                               "/monthlynseaxisbank\n"+ 
# #                               "/yearlynseaxisbank\n")
# dailynseaxisbank( Update)
# #     
# #     shareday('AXISBANK.NS')
# monthlynseaxisbank( Update)
# #     
# #     sharemonth('AXISBANK.NS')
# yearlynseaxisbank( Update)
# #     
# #     shareyear('AXISBANK.NS')
# # #bse-axisbank
# bseaxisbank( Update)
# #     update.message.reply_text("Choose the time span for axisbank share\n"+
# #                               "/dailybseaxisbank\n"+ 
# #                               "/monthlybseaxisbank\n"+ 
# #                               "/yearlybseaxisbank\n")
# dailybseaxisbank( Update)
# #     
# #     shareday('AXISBANK.BO')
# monthlybseaxisbank( Update)
# #     
# #     sharemonth('AXISBANK.BO')
# yearlybseaxisbank( Update)
# #     
# #     shareyear('AXISBANK.BO')
# # #***************************BajajAuto*************************
# # #nse-bajajauto
# nsebajajauto( Update)
# #     update.message.reply_text("Choose the time span for bajajauto share\n"+
# #                               "/dailynsebajajauto\n"+ 
# #                               "/monthlynsebajajauto\n"+ 
# #                               "/yearlynsebajajauto\n")
# dailynsebajajauto( Update)
# #     
# #     shareday('BAJAJ-AUTO.NS')
# monthlynsebajajauto( Update)
# #     
# #     sharemonth('BAJAJ-AUTO.NS')
# yearlynsebajajauto( Update)
# #     
# #     shareyear('BAJAJ-AUTO.NS')
# # #bse-bajajauto
# bsebajajauto( Update)
# #     update.message.reply_text("Choose the time span for bajajauto share\n"+
# #                               "/dailybsebajajauto\n"+ 
# #                               "/monthlybsebajajauto\n"+ 
# #                               "/yearlybsebajajauto\n")
# dailybsebajajauto( Update)
# #     
# #     shareday('BAJAJ-AUTO.BO')
# monthlybsebajajauto( Update)
# #     
# #     sharemonth('BAJAJ-AUTO.BO')
# yearlybsebajajauto( Update)
# #     
# #     shareyear('BAJAJ-AUTO.BO')
# # #***************************BajajFinserv*****************
# # #nse-bajajfinserv
# nsebajajfinserv( Update)
# #     update.message.reply_text("Choose the time span for bajajfinserv share\n"+
# #                               "/dailynsebajajfinserv\n"+ 
# #                               "/monthlynsebajajfinserv\n"+ 
# #                               "/yearlynsebajajfinserv\n")
# dailynsebajajfinserv( Update)
# #     
# #     shareday('BAJAJFINSV.NS')
# monthlynsebajajfinserv( Update)
# #     
# #     sharemonth('BAJAJFINSV.NS')
# yearlynsebajajfinserv( Update)
# #     
# #     shareyear('BAJAJFINSV.NS')
# # #bse-bajajfinserv
# bsebajajfinserv( Update)
# #     update.message.reply_text("Choose the time span for bajajfinserv share\n"+
# #                               "/dailybsebajajfinserv\n"+ 
# #                               "/monthlybsebajajfinserv\n"+ 
# #                               "/yearlybsebajajfinserv\n")
# dailybsebajajfinserv( Update)
# #     
# #     shareday('BAJAJFINSV.BO')
# monthlybsebajajfinserv( Update)
# #     
# #     sharemonth('BAJAJFINSV.BO')
# yearlybsebajajfinserv( Update)
# #     
# #     shareyear('BAJAJFINSV.BO')
# # #*************************BajajFinance****************************
# # #nse-bajajfinance
# nsebajajfinance( Update)
# #     update.message.reply_text("Choose the time span for bajajfinance share\n"+
# #                               "/dailynsebajajfinance\n"+ 
# #                               "/monthlynsebajajfinance\n"+ 
# #                               "/yearlynsebajajfinance\n")
# dailynsebajajfinance( Update)
# #     
# #     shareday('BAJFINANCE.NS')
# monthlynsebajajfinance( Update)
# #     
# #     sharemonth('BAJFINANCE.NS')
# yearlynsebajajfinance( Update)
# #     
# #     shareyear('BAJFINANCE.NS')
# # #bse-bajajfinance
# bsebajajfinance( Update)
# #     update.message.reply_text("Choose the time span for bajajfinance share\n"+
# #                               "/dailybsebajajfinance\n"+ 
# #                               "/monthlybsebajajfinance\n"+ 
# #                               "/yearlybsebajajfinance\n")
# dailybsebajajfinance( Update)
# #     
# #     shareday('BAJFINANCE.BO')
# monthlybsebajajfinance( Update)
# #     
# #     sharemonth('BAJFINANCE.BO')
# # yearlybsebajajfinance( Update
# #     
# #     shareyear('BAJFINANCE.BO')
# # #***************************Britania****************************
# # #nse-britannia
# nsebritannia( Update)
# #     update.message.reply_text("Choose the time span for britannia share\n"+
# #                               "/dailynsebritannia\n"+ 
# #                               "/monthlynsebritannia\n"+ 
# #                               "/yearlynsebritannia\n")
# dailynsebritannia( Update)
# #     
# #     shareday('BRITANNIA.NS')
# monthlynsebritannia( Update)
# #     
# #     sharemonth('BRITANNIA.NS')
# yearlynsebritannia( Update)
# #     
# #     shareyear('BRITANNIA.NS')
# # #bse-britannia
# bsebritannia( Update)
# #     update.message.reply_text("Choose the time span for britannia share\n"+
# #                               "/dailybsebritannia\n"+ 
# #                               "/monthlybsebritannia\n"+ 
# #                               "/yearlybsebritannia\n")
# dailybsebritannia( Update)
# #     
# #     shareday('BRITANNIA.BO')
# monthlybsebritannia( Update)
# #     
# #     sharemonth('BRITANNIA.BO')
# yearlybsebritannia( Update)
# #     
# #     shareyear('BRITANNIA.BO')
# # #***********************Cipla*******************************
# # #nse-cipla
# nsecipla( Update)
# #     update.message.reply_text("Choose the time span for cipla share\n"+
# #                               "/dailynsecipla\n"+ 
# #                               "/monthlynsecipla\n"+ 
# #                               "/yearlynsecipla\n")
# dailynsecipla( Update)
# #     
# #     shareday('CIPLA.NS')
# monthlynsecipla( Update)
# #     
# #     sharemonth('CIPLA.NS')
# yearlynsecipla( Update)
# #     
# #     shareyear('CIPLA.NS')
# # #bse-cipla
# bsecipla( Update)
# #     update.message.reply_text("Choose the time span for cipla share\n"+
# #                               "/dailybsecipla\n"+ 
# #                               "/monthlybsecipla\n"+ 
# #                               "/yearlybsecipla\n")
# dailybsecipla( Update)
# #     
# #     shareday('CIPLA.BO')
# monthlybsecipla( Update)
# #     
# #     sharemonth('CIPLA.BO')
# yearlybsecipla( Update)
# #     
# #     shareyear('CIPLA.BO')
# # #*********************HCLtech**************************
# # #nse-hcltech
# nsehcltech( Update)
# #     update.message.reply_text("Choose the time span for hcltech share\n"+
# #                               "/dailynsehcltech\n"+ 
# #                               "/monthlynsehcltech\n"+ 
# #                               "/yearlynsehcltech\n")
# dailynsehcltech( Update)
# #     
# #     shareday('HCLTECH.NS')
# monthlynsehcltech( Update)
# #     
# #     sharemonth('HCLTECH.NS')
# yearlynsehcltech( Update)
# #     
# #     shareyear('HCLTECH.NS')
# # #bse-hcltech
# bsehcltech( Update)
# #     update.message.reply_text("Choose the time span for hcltech share\n"+
# #                               "/dailybsehcltech\n"+ 
# #                               "/monthlybsehcltech\n"+ 
# #                               "/yearlybsehcltech\n")
# dailybsehcltech( Update)
# #     
# #     shareday('HCLTECH.BO')
# monthlybsehcltech( Update)
# #     
# #     sharemonth('HCLTECH.BO')
# yearlybsehcltech( Update)
# #     
# #     shareyear('HCLTECH.BO')
# # #************************HDFC**************************
# # #nse-hdfc
# nsehdfc( Update)
# #     update.message.reply_text("Choose the time span for hdfc share\n"+
# #                               "/dailynsehdfc\n"+ 
# #                               "/monthlynsehdfc\n"+ 
# #                               "/yearlynsehdfc\n")
# dailynsehdfc( Update)
# #     
# #     shareday('HDFC.NS')
# monthlynsehdfc( Update)
# #     
# #     sharemonth('HDFC.NS')
# yearlynsehdfc( Update)
# #     
# #     shareyear('HDFC.NS')
# # #bse-hdfc
# bsehdfc( Update)
# #     update.message.reply_text("Choose the time span for hdfc share\n"+
# #                               "/dailybsehdfc\n"+ 
# #                               "/monthlybsehdfc\n"+ 
# #                               "/yearlybsehdfc\n")
# dailybsehdfc( Update)
# #     
# #     shareday('HDFC.BO')
# monthlybsehdfc( Update)
# #     
# #     sharemonth('HDFC.BO')
# yearlybsehdfc( Update)
# #     
# #     shareyear('HDFC.BO')
# # #*******************HeroMotoCo*******************
# # #nse-heromotoco
# nseheromotoco( Update)
# #     update.message.reply_text("Choose the time span for heromotoco share\n"+
# #                               "/dailynseheromotoco\n"+ 
# #                               "/monthlynseheromotoco\n"+ 
# #                               "/yearlynseheromotoco\n")
# dailynseheromotoco( Update)
# #     
# #     shareday('HEROMOTOCO.NS')
# monthlynseheromotoco( Update)
# #     
# #     sharemonth('HEROMOTOCO.NS')
# yearlynseheromotoco( Update)
# #     
# #     shareyear('HEROMOTOCO.NS')
# # #bse-heromotoco
# bseheromotoco( Update)
# #     update.message.reply_text("Choose the time span for heromotoco share\n"+
# #                               "/dailybseheromotoco\n"+ 
# #                               "/monthlybseheromotoco\n"+ 
# #                               "/yearlybseheromotoco\n")
# dailybseheromotoco( Update)
# #     
# #     shareday('HEROMOTOCO.BO')
# monthlybseheromotoco( Update)
# #     
# #     sharemonth('HEROMOTOCO.BO')
# yearlybseheromotoco( Update)
# #     
# #     shareyear('HEROMOTOCO.BO')
# # #*********************hindalco*****************************
# # #nse-hindalco
# nsehindalco( Update)
# #     update.message.reply_text("Choose the time span for hindalco share\n"+
# #                               "/dailynsehindalco\n"+ 
# #                               "/monthlynsehindalco\n"+ 
# #                               "/yearlynsehindalco\n")
# dailynsehindalco( Update)
# #     
# #     shareday('HINDALCO.NS')
# monthlynsehindalco( Update)
# #     
# #     sharemonth('HINDALCO.NS')
# yearlynsehindalco( Update)
# #     
# #     shareyear('HINDALCO.NS')
# # #bse-hindalco
# bsehindalco( Update)
# #     update.message.reply_text("Choose the time span for hindalco share\n"+
# #                               "/dailybsehindalco\n"+ 
# #                               "/monthlybsehindalco\n"+ 
# #                               "/yearlybsehindalco\n")
# dailybsehindalco( Update)
# #     
# #     shareday('HINDALCO.BO')
# monthlybsehindalco( Update)
# #     
# #     sharemonth('HINDALCO.BO')
# yearlybsehindalco( Update)
# #     
# #     shareyear('HINDALCO.BO')
# # #************************ZEEL*************************
# # #nse-ZEEL
# nsezeel( Update)
# #     update.message.reply_text("Whose the time span for ZEEL share\n"+
# #                               "/dailynsezeel\n"+ 
# #                               "/monthlynsezeel\n"+ 
# #                               "/yearlynsezeel\n")
# dailynsezeel( Update)
# #     
# #     shareday('ZEEL.NS')
# monthlynsezeel( Update)
# #     
# #     sharemonth('ZEEL.NS')
# yearlynsezeel( Update)
# #     
# #     shareyear('ZEEL.NS')
# # #bse-ZEEL
# bsezeel( Update)
# #     update.message.reply_text("Whose the time span for ZEEL share\n"+
# #                               "/dailybsezeel\n"+ 
# #                               "/monthlybsezeel\n"+ 
# #                               "/yearlybsezeel\n")
# dailybsezeel( Update)
# #     
# #     shareday('ZEEL.BO')
# monthlybsezeel( Update)
# #     
# #     sharemonth('ZEEL.BO')
# yearlybsezeel( Update)
# #     
# #     shareyear('ZEEL.BO')
# # #************************Wipro*************************
# # #nse-Wipro
# nsewipro( Update)
# #     update.message.reply_text("Whose the time span for WIPRO share\n"+
# #                               "/dailynsewipro\n"+ 
# #                               "/monthlynsewipro\n"+ 
# #                               "/yearlynsewipro\n")
# dailynsewipro( Update)
# #     
# #     shareday('WIPRO.NS')
# monthlynsewipro( Update)
# #     
# #     sharemonth('WIPRO.NS')
# yearlynsewipro( Update)
# #     
# #     shareyear('WIPRO.NS')
# # #bse-Wipro
# bsewipro( Update)
# #     update.message.reply_text("Whose the time span for WIPRO share\n"+
# #                               "/dailybsewipro\n"+ 
# #                               "/monthlybsewipro\n"+ 
# #                               "/yearlybsewipro\n")
# dailybsewipro( Update)
# #     
# #     shareday('WIPRO.BO')
# monthlybsewipro( Update)
# #     
# #     sharemonth('WIPRO.BO')
# yearlybsewipro( Update)
# #     
# #     shareyear('WIPRO.BO')
# # #************************Upl*************************
# # #nse-Upl
# nseupl( Update)
# #     update.message.reply_text("Whose the time span for UPL share\n"+
# #                               "/dailynseupl\n"+ 
# #                               "/monthlynseupl\n"+ 
# #                               "/yearlynseupl\n")
# dailynseupl( Update)
# #     
# #     shareday('UPL.NS')
# monthlynseupl( Update)
# #     
# #     sharemonth('UPL.NS')
# yearlynseupl( Update)
# #     
# #     shareyear('UPL.NS')
# # #bse-Upl
# bseupl( Update)
# #     update.message.reply_text("Whose the time span for UPL share\n"+
# #                               "/dailybseupl\n"+ 
# #                               "/monthlybseupl\n"+ 
# #                               "/yearlybseupl\n")
# dailybseupl( Update)
# #     
# #     shareday('UPL.BO')
# monthlybseupl( Update)
# #     
# #     sharemonth('UPL.BO')
# yearlybseupl( Update)
# #     
# #     shareyear('UPL.BO')
# # #************************Titan*************************
# # #nse-Titan
# nsetitan( Update)
# #     update.message.reply_text("Whose the time span for TITAN share\n"+
# #                               "/dailynsetitan\n"+ 
# #                               "/monthlynsetitan\n"+ 
# #                               "/yearlynsetitan\n")
# dailynsetitan( Update)
# #     
# #     shareday('TITAN.NS')
# monthlynsetitan( Update)
# #     
# #     sharemonth('TITAN.NS')
# yearlynsetitan( Update)
# #     
# #     shareyear('TITAN.NS')
# # #bse-Titan
# bsetitan( Update)
# #     update.message.reply_text("Whose the time span for TITAN share\n"+
# #                               "/dailybsetitan\n"+ 
# #                               "/monthlybsetitan\n"+ 
# #                               "/yearlybsetitan\n")
# dailybsetitan( Update)
# #     
# #     shareday('TITAN.BO')
# monthlybsetitan( Update)
# #     
# #     sharemonth('TITAN.BO')
# yearlybsetitan( Update)
# #     
# #     shareyear('TITAN.BO')
# # #************************Tatasteel*************************
# # #nse-Tatasteel
# nsetatasteel( Update)
# #     update.message.reply_text("Whose the time span for TATA STEEL share\n"+
# #                               "/dailynsetatasteel\n"+ 
# #                               "/monthlynsetatasteel\n"+ 
# #                               "/yearlynsetatasteel\n")
# dailynsetatasteel( Update)
# #     
# #     shareday('TATASTEEL.NS')
# monthlynsetatasteel( Update)
# #     
# #     sharemonth('TATASTEEL.NS')
# yearlynsetatasteel( Update)
# #     
# #     shareyear('TATASTEEL.NS')
# # #bse-Tatasteel
# bsetatasteel( Update)
# #     update.message.reply_text("Whose the time span for TATA STEEL share\n"+
# #                               "/dailybsetatasteel\n"+ 
# #                               "/monthlybsetatasteel\n"+ 
# #                               "/yearlybsetatasteel\n")
# dailybsetatasteel( Update)
# #     
# #     shareday('TATASTEEL.BO')
# monthlybsetatasteel( Update)
# #     
# #     sharemonth('TATASTEEL.BO')
# yearlybsetatasteel( Update)
# #     
# #     shareyear('TATASTEEL.BO')
# # #************************Tatachemical*************************
# # #nse-Tatachemical
# nsetatachemical( Update)
# #     update.message.reply_text("Whose the time span for TATA CHEMICAL share\n"+
# #                               "/dailynsetatachemical\n"+ 
# #                               "/monthlynsetatachemical\n"+ 
# #                               "/yearlynsetatachemical\n")
# dailynsetatachemical( Update)
# #     
# #     shareday('TATACHEM.NS')
# monthlynsetatachemical( Update)
# #     
# #     sharemonth('TATACHEM.NS')
# yearlynsetatachemical( Update)
# #     
# #     shareyear('TATACHEM.NS')
# # #bse-Tatachemical
# bsetatachemical( Update)
# #     update.message.reply_text("Whose the time span for TATA CHEMICAL share\n"+
# #                               "/dailybsetatachemical\n"+ 
# #                               "/monthlybsetatachemical\n"+ 
# #                               "/yearlybsetatachemical\n")
# dailybsetatachemical( Update)
# #     
# #     shareday('TATACHEM.BO')
# monthlybsetatachemical( Update)
# #     
# #     sharemonth('TATACHEM.BO')
# yearlybsetatachemical( Update)
# #     
# #     shareyear('TATACHEM.BO')
# # #************************Tatapower*************************
# # #nse-Tatapower
# nsetatapower( Update)
# #     update.message.reply_text("Whose the time span for TATA POWER share\n"+
# #                               "/dailynsetatapower\n"+ 
# #                               "/monthlynsetatapower\n"+ 
# #                               "/yearlynsetatapower\n")
# dailynsetatapower( Update)
# #     
# #     shareday('TATAPOWER.NS')
# monthlynsetatapower( Update)
# #     
# #     sharemonth('TATAPOWER.NS')
# yearlynsetatapower( Update)
# #     
# #     shareyear('TATAPOWER.NS')
# # #bse-Tatapower
# bsetatapower( Update)
# #     update.message.reply_text("Whose the time span for TATA POWER share\n"+
# #                               "/dailybsetatapower\n"+ 
# #                               "/monthlybsetatapower\n"+ 
# #                               "/yearlybsetatapower\n")
# dailybsetatapower( Update)
# #     
# #     shareday('TATAPOWER.BO')
# monthlybsetatapower( Update)
# #     
# #     sharemonth('TATAPOWER.BO')
# yearlybsetatapower( Update)
# #     
# #     shareyear('TATAPOWER.BO')
# # #************************Sunpharma*************************
# # #nse-Sunpharma
# nsesunpharma( Update)
# #     update.message.reply_text("Whose the time span for SUN PHARMA share\n"+
# #                               "/dailynsesunpharma\n"+ 
# #                               "/monthlynsesunpharma\n"+ 
# #                               "/yearlynsesunpharma\n")
# dailynsesunpharma( Update)
# #     
# #     shareday('SUNPHARMA.NS')
# monthlynsesunpharma( Update)
# #     
# #     sharemonth('SUNPHARMA.NS')
# yearlynsesunpharma( Update)
# #     
# #     shareyear('SUNPHARMA.NS')
# # #bse-Sunpharma
# bsesunpharma( Update)
# #     update.message.reply_text("Whose the time span for SUN PHARMA share\n"+
# #                               "/dailybsesunpharma\n"+ 
# #                               "/monthlybsesunpharma\n"+ 
# #                               "/yearlybsesunpharma\n")
# dailybsesunpharma( Update)
# #     
# #     shareday('SUNPHARMA.BO')
# monthlybsesunpharma( Update)
# #     
# #     sharemonth('SUNPHARMA.BO')
# yearlybsesunpharma( Update)
# #     
# #     shareyear('SUNPHARMA.BO')
# # #************************Reliance*************************
# # #nse-Reliance
# nsereliance( Update)
# #     update.message.reply_text("Whose the time span for RELIANCE share\n"+
# #                               "/dailynsereliance\n"+ 
# #                               "/monthlynsereliance\n"+ 
# #                               "/yearlynsereliance\n")
# dailynsereliance( Update)
# #     
# #     shareday('RELIANCE.NS')
# monthlynsereliance( Update)
# #     
# #     sharemonth('RELIANCE.NS')
# yearlynsereliance( Update)
# #     
# #     shareyear('RELIANCE.NS')
# #bse-Relianc
# bsereliance( Update)
# #     update.message.reply_text("Whose the time span for RELIANCE share\n"+
# #                               "/dailybsereliance\n"+ 
# #                               "/monthlybsereliance\n"+ 
# #                               "/yearlybsereliance\n")
# dailybsereliance( Update)
# #     
# #     shareday('RELIANCE.BO')
# monthlybsereliance( Update)
# #     
# #     sharemonth('RELIANCE.BO')
# yearlybsereliance( Update)
# #     
# #     shareyear('RELIANCE.BO')
# # #************************Maruti*************************
# # #nse-Maruti
# nsemaruti( Update)
# #     update.message.reply_text("Whose the time span for MARUTI share\n"+
# #                               "/dailynsemaruti\n"+ 
# #                               "/monthlynsemaruti\n"+ 
# #                               "/yearlynsemaruti\n")ailynsemaruti( Update):
# #     
# #     shareday('MARUTI.NS')
# monthlynsemaruti( Update)
# #     
# #     sharemonth('MARUTI.NS')
# yearlynsemaruti( Update)
# #     
# #     shareyear('MARUTI.NS')
# # #bse-Maruti
# bsemaruti( Update)
# #     update.message.reply_text("Whose the time span for MARUTI share\n"+
# #                               "/dailybsemaruti\n"+ 
# #                               "/monthlybsemaruti\n"+ 
# #                               "/yearlybsemaruti\n")
# dailybsemaruti( Update)
# #     
# #     shareday('MARUTI.BO')
# monthlybsemaruti( Update)
# #     
# #     sharemonth('MARUTI.BO')
# yearlybsemaruti( Update)
# #     
# #     shareyear('MARUTI.BO')
# # #************************IndusInd*************************
# # #nse-IndusInd
# nseindusind( Update)
# #     update.message.reply_text("Whose the time span for INDUSIND BANK LIMITED share\n"+
# #                               "/dailynseindusind\n"+ 
# #                               "/monthlynseindusind\n"+ 
# #                               "/yearlynseindusind\n")
# dailynseindusind( Update)
# #     
# #     shareday('INDUSINDBK.NS')
# monthlynseindusind( Update)
# #     
# #     sharemonth('INDUSINDBK.NS')
# yearlynseindusind( Update)
# #     
# #     shareyear('INDUSINDBK.NS')
# # #bse-IndusInd
# bseindusind( Update)
# #     update.message.reply_text("Whose the time span for INDUSIND BANK LIMITED share\n"+
# #                               "/dailybseindusind\n"+ 
# #                               "/monthlybseindusind\n"+ 
# #                               "/yearlybseindusind\n")
# dailybseindusind( Update)
# #     
# #     shareday('INDUSINDBK.BO')
# monthlybseindusind( Update)
# #     
# #     sharemonth('INDUSINDBK.BO')
# yearlybseindusind( Update)
# #     
# #     shareyear('INDUSINDBK.BO')
# # #************************Icici*************************
# # #nse-Icici
# nseicicibank( Update)
# #     update.message.reply_text("Whose the time span for ICICI BANK LIMITED share\n"+
# #                               "/dailynseicicibank\n"+ 
# #                               "/monthlynseicicibank\n"+ 
# #                               "/yearlynseicicibank\n"
# dailynseicicibank( Update)
# #     
# #     shareday('ICICIBANK.NS')
# monthlynseicicibank( Update)
# #     
# #     sharemonth('ICICIBANK.NS')
# yearlynseicicibank( Update)
# #     
# #     shareyear('ICICIBANK.NS')
# # #bse-Icici
# bseicicibank( Update)
# #     update.message.reply_text("Whose the time span for ICICI BANK LIMITED share\n"+
# #                               "/dailybseicicibank\n"+ 
# #                               "/monthlybseicicibank\n"+ 
# #                               "/yearlybseicicibank\n")
# dailybseicicibank( Update)
# #     
# #     shareday('ICICIBANK.BO')
# monthlybseicicibank( Update)
# #     
# #     sharemonth('ICICIBANK.BO')
# yearlybseicicibank( Update)
# #     
# #     shareyear('ICICIBANK.BO')
# # #************************HidustanUniliver*************************
# # #nse-HidustanUniliver
# nsehinduuniliver( Update)
# #     update.message.reply_text("Whose the time span for HINDUSTAN UNILIVER LIMITED share\n"+
# #                               "/dailynsehinduuniliver\n"+ 
# #                               "/monthlynsehinduuniliver\n"+ 
# #                               "/yearlynsehinduuniliver\n")
# dailynsehinduuniliver( Update)
# #     
# #     shareday('HINDUNILVR.NS')
# monthlynsehinduuniliver( Update)
# #     
# #     sharemonth('HINDUNILVR.NS')
# yearlynsehinduuniliver( Update)
# #     
# #     shareyear('HINDUNILVR.NS')
# # #bse-HidustanUniliver
# bsehinduuniliver( Update)
# dailybsehinduuniliver( Update)#     
# #     shareday('HINDUNILVR.BO')
# monthlybsehinduuniliver( Update)#     
# #     sharemonth('HINDUNILVR.BO')
# yearlybsehinduuniliver( Update)#     
# #     shareyear('HINDUNILVR.BO')



#Start
updater.dispatcher.add_handler(CommandHandler('start', start))
#Available options
updater.dispatcher.add_handler(CommandHandler('bse', sensex))
updater.dispatcher.add_handler(CommandHandler('nse', nifty))
#bse
updater.dispatcher.add_handler(CommandHandler('bsestocks', bsestocks))
updater.dispatcher.add_handler(CommandHandler('bseindex', bseindex))
#nse
updater.dispatcher.add_handler(CommandHandler('nsestocks', nsestocks))
updater.dispatcher.add_handler(CommandHandler('nseindex', nseindex))
#shares
updater.dispatcher.add_handler(CommandHandler('nseadaniports', nseadaniports))
updater.dispatcher.add_handler(CommandHandler('dailynseadaniports', dailynseadaniports))
updater.dispatcher.add_handler(CommandHandler('monthlynseadaniports', monthlynseadaniports))
updater.dispatcher.add_handler(CommandHandler('yearlynseadaniports', yearlynseadaniports))
updater.dispatcher.add_handler(CommandHandler('bseadaniports', bseadaniports))
updater.dispatcher.add_handler(CommandHandler('dailybseadaniports', dailybseadaniports))
updater.dispatcher.add_handler(CommandHandler('monthlybseadaniports', monthlybseadaniports))
updater.dispatcher.add_handler(CommandHandler('yearlybseadaniports', yearlybseadaniports))
updater.dispatcher.add_handler(CommandHandler('nseasianpaints', nseasianpaints))
updater.dispatcher.add_handler(CommandHandler('dailynseasianpaints', dailynseasianpaints))
updater.dispatcher.add_handler(CommandHandler('monthlynseasianpaints', monthlynseasianpaints))
updater.dispatcher.add_handler(CommandHandler('yearlynseasianpaints', yearlynseasianpaints))
updater.dispatcher.add_handler(CommandHandler('bseasianpaints', bseasianpaints))
updater.dispatcher.add_handler(CommandHandler('dailybseasianpaints', dailybseasianpaints))
updater.dispatcher.add_handler(CommandHandler('monthlybseasianpaints', monthlybseasianpaints))
updater.dispatcher.add_handler(CommandHandler('yearlybseasianpaints', yearlybseasianpaints))
updater.dispatcher.add_handler(CommandHandler('nseaxisbank', nseaxisbank))
updater.dispatcher.add_handler(CommandHandler('dailynseaxisbank', dailynseaxisbank))
updater.dispatcher.add_handler(CommandHandler('monthlynseaxisbank', monthlynseaxisbank))
updater.dispatcher.add_handler(CommandHandler('yearlynseaxisbank', yearlynseaxisbank))
updater.dispatcher.add_handler(CommandHandler('bseaxisbank', bseaxisbank))
updater.dispatcher.add_handler(CommandHandler('dailybseaxisbank', dailybseaxisbank))
updater.dispatcher.add_handler(CommandHandler('monthlybseaxisbank', monthlybseaxisbank))
updater.dispatcher.add_handler(CommandHandler('yearlybseaxisbank', yearlybseaxisbank))
updater.dispatcher.add_handler(CommandHandler('nsebajajauto', nsebajajauto))
updater.dispatcher.add_handler(CommandHandler('dailynsebajajauto', dailynsebajajauto))
updater.dispatcher.add_handler(CommandHandler('monthlynsebajajauto', monthlynsebajajauto))
updater.dispatcher.add_handler(CommandHandler('yearlynsebajajauto', yearlynsebajajauto))
updater.dispatcher.add_handler(CommandHandler('bsebajajauto', bsebajajauto))
updater.dispatcher.add_handler(CommandHandler('dailybsebajajauto', dailybsebajajauto))
updater.dispatcher.add_handler(CommandHandler('monthlybsebajajauto', monthlybsebajajauto))
updater.dispatcher.add_handler(CommandHandler('yearlybsebajajauto', yearlybsebajajauto))
updater.dispatcher.add_handler(CommandHandler('nsebajajfinance', nsebajajfinance))
updater.dispatcher.add_handler(CommandHandler('dailynsebajajfinance', dailynsebajajfinance))
updater.dispatcher.add_handler(CommandHandler('monthlynsebajajfinance', monthlynsebajajfinance))
updater.dispatcher.add_handler(CommandHandler('yearlynsebajajfinance', yearlynsebajajfinance))
updater.dispatcher.add_handler(CommandHandler('bsebajajfinance', bsebajajfinance))
updater.dispatcher.add_handler(CommandHandler('dailybsebajajfinance', dailybsebajajfinance))
updater.dispatcher.add_handler(CommandHandler('monthlybsebajajfinance', monthlybsebajajfinance))
updater.dispatcher.add_handler(CommandHandler('yearlybsebajajfinance', yearlybsebajajfinance))
updater.dispatcher.add_handler(CommandHandler('nsebajajfinserv', nsebajajfinserv))
updater.dispatcher.add_handler(CommandHandler('dailynsebajajfinserv', dailynsebajajfinserv))
updater.dispatcher.add_handler(CommandHandler('monthlynsebajajfinserv', monthlynsebajajfinserv))
updater.dispatcher.add_handler(CommandHandler('yearlynsebajajfinserv', yearlynsebajajfinserv))
updater.dispatcher.add_handler(CommandHandler('bsebajajfinserv', bsebajajfinserv))
updater.dispatcher.add_handler(CommandHandler('dailybsebajajfinserv', dailybsebajajfinserv))
updater.dispatcher.add_handler(CommandHandler('monthlybsebajajfinserv', monthlybsebajajfinserv))
updater.dispatcher.add_handler(CommandHandler('yearlybsebajajfinserv', yearlybsebajajfinserv))
updater.dispatcher.add_handler(CommandHandler('nsebritannia', nsebritannia))
updater.dispatcher.add_handler(CommandHandler('dailynsebritannia', dailynsebritannia))
updater.dispatcher.add_handler(CommandHandler('monthlynsebritannia', monthlynsebritannia))
updater.dispatcher.add_handler(CommandHandler('yearlynsebritannia', yearlynsebritannia))
updater.dispatcher.add_handler(CommandHandler('bsebritannia', bsebritannia))
updater.dispatcher.add_handler(CommandHandler('dailybsebritannia', dailybsebritannia))
updater.dispatcher.add_handler(CommandHandler('monthlybsebritannia', monthlybsebritannia))
updater.dispatcher.add_handler(CommandHandler('yearlybsebritannia', yearlybsebritannia))
updater.dispatcher.add_handler(CommandHandler('nsecipla', nsecipla))
updater.dispatcher.add_handler(CommandHandler('dailynsecipla', dailynsecipla))
updater.dispatcher.add_handler(CommandHandler('monthlynsecipla', monthlynsecipla))
updater.dispatcher.add_handler(CommandHandler('yearlynsecipla', yearlynsecipla))
updater.dispatcher.add_handler(CommandHandler('bsecipla', bsecipla))
updater.dispatcher.add_handler(CommandHandler('dailybsecipla', dailybsecipla))
updater.dispatcher.add_handler(CommandHandler('monthlybsecipla', monthlybsecipla))
updater.dispatcher.add_handler(CommandHandler('yearlybsecipla', yearlybsecipla))
updater.dispatcher.add_handler(CommandHandler('nsehcltech', nsehcltech))
updater.dispatcher.add_handler(CommandHandler('dailynsehcltech', dailynsehcltech))
updater.dispatcher.add_handler(CommandHandler('monthlynsehcltech', monthlynsehcltech))
updater.dispatcher.add_handler(CommandHandler('yearlynsehcltech', yearlynsehcltech))
updater.dispatcher.add_handler(CommandHandler('bsehcltech', bsehcltech))
updater.dispatcher.add_handler(CommandHandler('dailybsehcltech', dailybsehcltech))
updater.dispatcher.add_handler(CommandHandler('monthlybsehcltech', monthlybsehcltech))
updater.dispatcher.add_handler(CommandHandler('yearlybsehcltech', yearlybsehcltech))
updater.dispatcher.add_handler(CommandHandler('nsehdfc', nsehdfc))
updater.dispatcher.add_handler(CommandHandler('dailynsehdfc', dailynsehdfc))
updater.dispatcher.add_handler(CommandHandler('monthlynsehdfc', monthlynsehdfc))
updater.dispatcher.add_handler(CommandHandler('yearlynsehdfc', yearlynsehdfc))
updater.dispatcher.add_handler(CommandHandler('bsehdfc', bsehdfc))
updater.dispatcher.add_handler(CommandHandler('dailybsehdfc', dailybsehdfc))
updater.dispatcher.add_handler(CommandHandler('monthlybsehdfc', monthlybsehdfc))
updater.dispatcher.add_handler(CommandHandler('yearlybsehdfc', yearlybsehdfc))
updater.dispatcher.add_handler(CommandHandler('nseheromotoco', nseheromotoco))
updater.dispatcher.add_handler(CommandHandler('dailynseheromotoco', dailynseheromotoco))
updater.dispatcher.add_handler(CommandHandler('monthlynseheromotoco', monthlynseheromotoco))
updater.dispatcher.add_handler(CommandHandler('yearlynseheromotoco', yearlynseheromotoco))
updater.dispatcher.add_handler(CommandHandler('bseheromotoco', bseheromotoco))
updater.dispatcher.add_handler(CommandHandler('dailybseheromotoco', dailybseheromotoco))
updater.dispatcher.add_handler(CommandHandler('monthlybseheromotoco', monthlybseheromotoco))
updater.dispatcher.add_handler(CommandHandler('yearlybseheromotoco', yearlybseheromotoco))
updater.dispatcher.add_handler(CommandHandler('nsehindalco', nsehindalco))
updater.dispatcher.add_handler(CommandHandler('dailynsehindalco', dailynsehindalco))
updater.dispatcher.add_handler(CommandHandler('monthlynsehindalco', monthlynsehindalco))
updater.dispatcher.add_handler(CommandHandler('yearlynsehindalco', yearlynsehindalco))
updater.dispatcher.add_handler(CommandHandler('bsehindalco', bsehindalco))
updater.dispatcher.add_handler(CommandHandler('dailybsehindalco', dailybsehindalco))
updater.dispatcher.add_handler(CommandHandler('monthlybsehindalco', monthlybsehindalco))
updater.dispatcher.add_handler(CommandHandler('yearlybsehindalco', yearlybsehindalco))
updater.dispatcher.add_handler(CommandHandler('nsehinduuniliver', nsehinduuniliver))
updater.dispatcher.add_handler(CommandHandler('dailynsehinduuniliver', dailynsehinduuniliver))
updater.dispatcher.add_handler(CommandHandler('monthlynsehinduuniliver', monthlynsehinduuniliver))
updater.dispatcher.add_handler(CommandHandler('yearlynsehinduuniliver', yearlynsehinduuniliver))
updater.dispatcher.add_handler(CommandHandler('bsehinduuniliver', bsehinduuniliver))
updater.dispatcher.add_handler(CommandHandler('dailybsehinduuniliver', dailybsehinduuniliver))
updater.dispatcher.add_handler(CommandHandler('monthlybsehinduuniliver', monthlybsehinduuniliver))
updater.dispatcher.add_handler(CommandHandler('yearlybsehinduuniliver', yearlybsehinduuniliver))
updater.dispatcher.add_handler(CommandHandler('nseicicibank', nseicicibank))
updater.dispatcher.add_handler(CommandHandler('dailynseicicibank', dailynseicicibank))
updater.dispatcher.add_handler(CommandHandler('monthlynseicicibank', monthlynseicicibank))
updater.dispatcher.add_handler(CommandHandler('yearlynseicicibank', yearlynseicicibank))
updater.dispatcher.add_handler(CommandHandler('bseicicibank', bseicicibank))
updater.dispatcher.add_handler(CommandHandler('dailybseicicibank', dailybseicicibank))
updater.dispatcher.add_handler(CommandHandler('monthlybseicicibank', monthlybseicicibank))
updater.dispatcher.add_handler(CommandHandler('yearlybseicicibank', yearlybseicicibank))
updater.dispatcher.add_handler(CommandHandler('nseindusind', nseindusind))
updater.dispatcher.add_handler(CommandHandler('dailynseindusind', dailynseindusind))
updater.dispatcher.add_handler(CommandHandler('monthlynseindusind', monthlynseindusind))
updater.dispatcher.add_handler(CommandHandler('yearlynseindusind', yearlynseindusind))
updater.dispatcher.add_handler(CommandHandler('bseindusind', bseindusind))
updater.dispatcher.add_handler(CommandHandler('dailybseindusind', dailybseindusind))
updater.dispatcher.add_handler(CommandHandler('monthlybseindusind', monthlybseindusind))
updater.dispatcher.add_handler(CommandHandler('yearlybseindusind', yearlybseindusind))
updater.dispatcher.add_handler(CommandHandler('nsemaruti', nsemaruti))
updater.dispatcher.add_handler(CommandHandler('dailynsemaruti', dailynsemaruti))
updater.dispatcher.add_handler(CommandHandler('monthlynsemaruti', monthlynsemaruti))
updater.dispatcher.add_handler(CommandHandler('yearlynsemaruti', yearlynsemaruti))
updater.dispatcher.add_handler(CommandHandler('bsemaruti', bsemaruti))
updater.dispatcher.add_handler(CommandHandler('dailybsemaruti', dailybsemaruti))
updater.dispatcher.add_handler(CommandHandler('monthlybsemaruti', monthlybsemaruti))
updater.dispatcher.add_handler(CommandHandler('yearlybsemaruti', yearlybsemaruti))
updater.dispatcher.add_handler(CommandHandler('nsereliance', nsereliance))
updater.dispatcher.add_handler(CommandHandler('dailynsereliance', dailynsereliance))
updater.dispatcher.add_handler(CommandHandler('monthlynsereliance', monthlynsereliance))
updater.dispatcher.add_handler(CommandHandler('yearlynsereliance', yearlynsereliance))
updater.dispatcher.add_handler(CommandHandler('bsereliance', bsereliance))
updater.dispatcher.add_handler(CommandHandler('dailybsereliance', dailybsereliance))
updater.dispatcher.add_handler(CommandHandler('monthlybsereliance', monthlybsereliance))
updater.dispatcher.add_handler(CommandHandler('yearlybsereliance', yearlybsereliance))
updater.dispatcher.add_handler(CommandHandler('nsesunpharma', nsesunpharma))
updater.dispatcher.add_handler(CommandHandler('dailynsesunpharma', dailynsesunpharma))
updater.dispatcher.add_handler(CommandHandler('monthlynsesunpharma', monthlynsesunpharma))
updater.dispatcher.add_handler(CommandHandler('yearlynsesunpharma', yearlynsesunpharma))
updater.dispatcher.add_handler(CommandHandler('bsesunpharma', bsesunpharma))
updater.dispatcher.add_handler(CommandHandler('dailybsesunpharma', dailybsesunpharma))
updater.dispatcher.add_handler(CommandHandler('monthlybsesunpharma', monthlybsesunpharma))
updater.dispatcher.add_handler(CommandHandler('yearlybsesunpharma', yearlybsesunpharma))
updater.dispatcher.add_handler(CommandHandler('nsetatapower', nsetatapower))
updater.dispatcher.add_handler(CommandHandler('dailynsetatapower', dailynsetatapower))
updater.dispatcher.add_handler(CommandHandler('monthlynsetatapower', monthlynsetatapower))
updater.dispatcher.add_handler(CommandHandler('yearlynsetatapower', yearlynsetatapower))
updater.dispatcher.add_handler(CommandHandler('bsetatapower', bsetatapower))
updater.dispatcher.add_handler(CommandHandler('dailybsetatapower', dailybsetatapower))
updater.dispatcher.add_handler(CommandHandler('monthlybsetatapower', monthlybsetatapower))
updater.dispatcher.add_handler(CommandHandler('yearlybsetatapower', yearlybsetatapower))
updater.dispatcher.add_handler(CommandHandler('nsetatachemical', nsetatachemical))
updater.dispatcher.add_handler(CommandHandler('dailynsetatachemical', dailynsetatachemical))
updater.dispatcher.add_handler(CommandHandler('monthlynsetatachemical', monthlynsetatachemical))
updater.dispatcher.add_handler(CommandHandler('yearlynsetatachemical', yearlynsetatachemical))
updater.dispatcher.add_handler(CommandHandler('bsetatachemical', bsetatachemical))
updater.dispatcher.add_handler(CommandHandler('dailybsetatachemical', dailybsetatachemical))
updater.dispatcher.add_handler(CommandHandler('monthlybsetatachemical', monthlybsetatachemical))
updater.dispatcher.add_handler(CommandHandler('yearlybsetatachemical', yearlybsetatachemical))
updater.dispatcher.add_handler(CommandHandler('nsetatasteel', nsetatasteel))
updater.dispatcher.add_handler(CommandHandler('dailynsetatasteel', dailynsetatasteel))
updater.dispatcher.add_handler(CommandHandler('monthlynsetatasteel', monthlynsetatasteel))
updater.dispatcher.add_handler(CommandHandler('yearlynsetatasteel', yearlynsetatasteel))
updater.dispatcher.add_handler(CommandHandler('bsetatasteel', bsetatasteel))
updater.dispatcher.add_handler(CommandHandler('dailybsetatasteel', dailybsetatasteel))
updater.dispatcher.add_handler(CommandHandler('monthlybsetatasteel', monthlybsetatasteel))
updater.dispatcher.add_handler(CommandHandler('yearlybsetatasteel', yearlybsetatasteel))
updater.dispatcher.add_handler(CommandHandler('nsetitan', nsetitan))
updater.dispatcher.add_handler(CommandHandler('dailynsetitan', dailynsetitan))
updater.dispatcher.add_handler(CommandHandler('monthlynsetitan', monthlynsetitan))
updater.dispatcher.add_handler(CommandHandler('yearlynsetitan', yearlynsetitan))
updater.dispatcher.add_handler(CommandHandler('bsetitan', bsetitan))
updater.dispatcher.add_handler(CommandHandler('dailybsetitan', dailybsetitan))
updater.dispatcher.add_handler(CommandHandler('monthlybsetitan', monthlybsetitan))
updater.dispatcher.add_handler(CommandHandler('yearlybsetitan', yearlybsetitan))
updater.dispatcher.add_handler(CommandHandler('nseupl', nseupl))
updater.dispatcher.add_handler(CommandHandler('dailynseupl', dailynseupl))
updater.dispatcher.add_handler(CommandHandler('monthlynseupl', monthlynseupl))
updater.dispatcher.add_handler(CommandHandler('yearlynseupl', yearlynseupl))
updater.dispatcher.add_handler(CommandHandler('bseupl', bseupl))
updater.dispatcher.add_handler(CommandHandler('dailybseupl', dailybseupl))
updater.dispatcher.add_handler(CommandHandler('monthlybseupl', monthlybseupl))
updater.dispatcher.add_handler(CommandHandler('yearlybseupl', yearlybseupl))
updater.dispatcher.add_handler(CommandHandler('nsewipro', nsewipro))
updater.dispatcher.add_handler(CommandHandler('dailynsewipro', dailynsewipro))
updater.dispatcher.add_handler(CommandHandler('monthlynsewipro', monthlynsewipro))
updater.dispatcher.add_handler(CommandHandler('yearlynsewipro', yearlynsewipro))
updater.dispatcher.add_handler(CommandHandler('bsewipro', bsewipro))
updater.dispatcher.add_handler(CommandHandler('dailybsewipro', dailybsewipro))
updater.dispatcher.add_handler(CommandHandler('monthlybsewipro', monthlybsewipro))
updater.dispatcher.add_handler(CommandHandler('yearlybsewipro', yearlybsewipro))
updater.dispatcher.add_handler(CommandHandler('nsezeel', nsezeel))
updater.dispatcher.add_handler(CommandHandler('dailynsezeel', dailynsezeel))
updater.dispatcher.add_handler(CommandHandler('monthlynsezeel', monthlynsezeel))
updater.dispatcher.add_handler(CommandHandler('yearlynsezeel', yearlynsezeel))
updater.dispatcher.add_handler(CommandHandler('bsezeel', bsezeel))
updater.dispatcher.add_handler(CommandHandler('dailybsezeel', dailybsezeel))
updater.dispatcher.add_handler(CommandHandler('monthlybsezeel', monthlybsezeel))
updater.dispatcher.add_handler(CommandHandler('yearlybsezeel', yearlybsezeel))
updater.dispatcher.add_handler(CommandHandler('nsetcs', nsetcs))
updater.dispatcher.add_handler(CommandHandler('dailynsetcs', dailynsetcs))
updater.dispatcher.add_handler(CommandHandler('monthlynsetcs', monthlynsetcs))
updater.dispatcher.add_handler(CommandHandler('yearlynsetcs', yearlynsetcs))
updater.dispatcher.add_handler(CommandHandler('bsetcs', bsetcs))
updater.dispatcher.add_handler(CommandHandler('dailybsetcs', dailybsetcs))
updater.dispatcher.add_handler(CommandHandler('monthlybsetcs', monthlybsetcs))
updater.dispatcher.add_handler(CommandHandler('yearlybsetcs', yearlybsetcs))

updater.start_polling()