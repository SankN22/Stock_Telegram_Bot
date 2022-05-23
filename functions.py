import yfinance as yf
import subprocess
import pandas as pd
from datetime import date, timedelta
from matplotlib import pyplot as plt
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

updater = Updater("BOT'S API ID",
				use_context=True)

def send_image(botToken, imageFile, chat_id):
        command = 'curl -s -X POST https://api.telegram.org/bot' + botToken + '/sendPhoto -F chat_id=' + chat_id + " -F photo=@" + imageFile
        subprocess.call(command.split(' '))
        return
        
Startyear = date.today() - timedelta(365)
Startyear.strftime('%Y-%m-%d')
Endyear = date.today() + timedelta(2)
Endyear.strftime('%Y-%m-%d')



Startmonth = date.today() - timedelta(30)
Startmonth.strftime('%Y-%m-%d')
Endmonth = date.today() + timedelta(2)
Endmonth.strftime('%Y-%m-%d')



Startday = date.today() - timedelta(1)
Startday.strftime('%Y-%m-%d')
Endday = date.today() + timedelta(2)
Endday.strftime('%Y-%m-%d')



def closing_priceyear(ticker):
    Assetyear = pd.DataFrame(yf.download(ticker, start=Startyear,
      end=Endyear)['Adj Close'])     
    return Assetyear
def closing_pricemonth(ticker):
    Assetmonth = pd.DataFrame(yf.download(ticker, start=Startmonth,
      end=Endmonth)['Adj Close'])     
    return Assetmonth
def closing_priceday(ticker):
    Assetday = pd.DataFrame(yf.download(ticker, start=Startday,
      end=Endday)['Adj Close'])     
    return Assetday

def shareyear(str1):
    GRAPH = closing_priceyear(str1)                  # CALL THE FUNCTION
    plt.plot(GRAPH, color='red', linewidth=2)
    plt.title(str1 +' Performance')
    plt.ylabel('Price (Rs)')
    plt.xlabel('Date')
    plt.savefig('image.png')
    send_image("BOT'S API ID", 'image.png', 'chat_id')
    plt.clf()
   
def sharemonth(str1):
    GRAPH = closing_pricemonth(str1)                  # CALL THE FUNCTION
    plt.plot(GRAPH, color='red', linewidth=2)
    plt.title(str1 +' Performance')
    plt.xlabel('Date')
    plt.ylabel('Price (Rs)')
    plt.savefig('image.png')
    send_image("BOT'S API ID", 'image.png', 'chat id')
    plt.clf()
    
def shareday(str1):
    GRAPH = closing_priceday(str1)                  # CALL THE FUNCTION
    plt.plot(GRAPH, color='red', linewidth=2)
    plt.title(str1 +' Performance')
    plt.ylabel('Price (Rs)')
    plt.xlabel('Date')
    plt.savefig('image.png')
    send_image("BOT'S API ID", 'image.png', 'chati id')
    plt.clf()
  
def nsetcs(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for TCS share\n"+
                              "/dailynsetcs\n"+ 
                              "/monthlynsetcs\n"+ 
                              "/yearlynsetcs\n")
def dailynsetcs(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TATASTEEL.NS')
def monthlynsetcs(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TCS.NS')
def yearlynsetcs(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TCS.NS')
#bse-tcs
def bsetcs(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for TCS share\n"+
                              "/dailybsetcs\n"+ 
                              "/monthlybsetcs\n"+ 
                              "/yearlybsetcs\n")
def dailybsetcs(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TCS.BO')
def monthlybsetcs(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TCS.BO')
def yearlybsetcs(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TCS.BO')
#***************AdaniPorts***********************
#nse-adaniports
def nseadaniports(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for adaniports share\n"+
                              "/dailynseadaniports\n"+ 
                              "/monthlynseadaniports\n"+ 
                              "/yearlynseadaniports\n")
def dailynseadaniports(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('ADANIPORTS.NS')
def monthlynseadaniports(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('ADANIPORTS.NS')
def yearlynseadaniports(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('ADANIPORTS.NS')
#bse-adaniports
def bseadaniports(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for adaniports share\n"+
                              "/dailybseadaniports\n"+ 
                              "/monthlybseadaniports\n"+ 
                              "/yearlybseadaniports\n")
def dailybseadaniports(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('ADANIPORTS.BO')
def monthlybseadaniports(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('ADANIPORTS.BO')
def yearlybseadaniports(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('ADANIPORTS.BO')
#*************************Asian Paints**************************
#nse-asianpaints
def nseasianpaints(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for asianpaints share\n"+
                              "/dailynseasianpaints\n"+ 
                              "/monthlynseasianpaints\n"+ 
                              "/yearlynseasianpaints\n")
def dailynseasianpaints(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('ASIANPAINT.BO')
def monthlynseasianpaints(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('ASIANPAINT.BO')
def yearlynseasianpaints(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('ASIANPAINT.BO')
#bse-asianpaints
def bseasianpaints(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for asianpaints share\n"+
                              "/dailybseasianpaints\n"+ 
                              "/monthlybseasianpaints\n"+ 
                              "/yearlybseasianpaints\n")
def dailybseasianpaints(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('ASIANPAINT.BO')
def monthlybseasianpaints(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('ASIANPAINT.BO')
def yearlybseasianpaints(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('ASIANPAINT.BO')
#********************AxisBank***********************************
#nse-axisbank
def nseaxisbank(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for axisbank share\n"+
                              "/dailynseaxisbank\n"+ 
                              "/monthlynseaxisbank\n"+ 
                              "/yearlynseaxisbank\n")
def dailynseaxisbank(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('AXISBANK.NS')
def monthlynseaxisbank(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('AXISBANK.NS')
def yearlynseaxisbank(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('AXISBANK.NS')
#bse-axisbank
def bseaxisbank(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for axisbank share\n"+
                              "/dailybseaxisbank\n"+ 
                              "/monthlybseaxisbank\n"+ 
                              "/yearlybseaxisbank\n")
def dailybseaxisbank(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('AXISBANK.BO')
def monthlybseaxisbank(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('AXISBANK.BO')
def yearlybseaxisbank(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('AXISBANK.BO')
#***************************BajajAuto*************************
#nse-bajajauto
def nsebajajauto(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for bajajauto share\n"+
                              "/dailynsebajajauto\n"+ 
                              "/monthlynsebajajauto\n"+ 
                              "/yearlynsebajajauto\n")
def dailynsebajajauto(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('BAJAJ-AUTO.NS')
def monthlynsebajajauto(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('BAJAJ-AUTO.NS')
def yearlynsebajajauto(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('BAJAJ-AUTO.NS')
#bse-bajajauto
def bsebajajauto(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for bajajauto share\n"+
                              "/dailybsebajajauto\n"+ 
                              "/monthlybsebajajauto\n"+ 
                              "/yearlybsebajajauto\n")
def dailybsebajajauto(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('BAJAJ-AUTO.BO')
def monthlybsebajajauto(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('BAJAJ-AUTO.BO')
def yearlybsebajajauto(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('BAJAJ-AUTO.BO')
#***************************BajajFinserv*****************
#nse-bajajfinserv
def nsebajajfinserv(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for bajajfinserv share\n"+
                              "/dailynsebajajfinserv\n"+ 
                              "/monthlynsebajajfinserv\n"+ 
                              "/yearlynsebajajfinserv\n")
def dailynsebajajfinserv(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('BAJAJFINSV.NS')
def monthlynsebajajfinserv(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('BAJAJFINSV.NS')
def yearlynsebajajfinserv(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('BAJAJFINSV.NS')
#bse-bajajfinserv
def bsebajajfinserv(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for bajajfinserv share\n"+
                              "/dailybsebajajfinserv\n"+ 
                              "/monthlybsebajajfinserv\n"+ 
                              "/yearlybsebajajfinserv\n")
def dailybsebajajfinserv(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('BAJAJFINSV.BO')
def monthlybsebajajfinserv(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('BAJAJFINSV.BO')
def yearlybsebajajfinserv(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('BAJAJFINSV.BO')
#*************************BajajFinance****************************
#nse-bajajfinance
def nsebajajfinance(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for bajajfinance share\n"+
                              "/dailynsebajajfinance\n"+ 
                              "/monthlynsebajajfinance\n"+ 
                              "/yearlynsebajajfinance\n")
def dailynsebajajfinance(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('BAJFINANCE.NS')
def monthlynsebajajfinance(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('BAJFINANCE.NS')
def yearlynsebajajfinance(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('BAJFINANCE.NS')
#bse-bajajfinance
def bsebajajfinance(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for bajajfinance share\n"+
                              "/dailybsebajajfinance\n"+ 
                              "/monthlybsebajajfinance\n"+ 
                              "/yearlybsebajajfinance\n")
def dailybsebajajfinance(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('BAJFINANCE.BO')
def monthlybsebajajfinance(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('BAJFINANCE.BO')
def yearlybsebajajfinance(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('BAJFINANCE.BO')
#***************************Britania****************************
#nse-britannia
def nsebritannia(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for britannia share\n"+
                              "/dailynsebritannia\n"+ 
                              "/monthlynsebritannia\n"+ 
                              "/yearlynsebritannia\n")
def dailynsebritannia(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('BRITANNIA.NS')
def monthlynsebritannia(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('BRITANNIA.NS')
def yearlynsebritannia(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('BRITANNIA.NS')
#bse-britannia
def bsebritannia(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for britannia share\n"+
                              "/dailybsebritannia\n"+ 
                              "/monthlybsebritannia\n"+ 
                              "/yearlybsebritannia\n")
def dailybsebritannia(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('BRITANNIA.BO')
def monthlybsebritannia(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('BRITANNIA.BO')
def yearlybsebritannia(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('BRITANNIA.BO')
#***********************Cipla*******************************
#nse-cipla
def nsecipla(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for cipla share\n"+
                              "/dailynsecipla\n"+ 
                              "/monthlynsecipla\n"+ 
                              "/yearlynsecipla\n")
def dailynsecipla(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('CIPLA.NS')
def monthlynsecipla(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('CIPLA.NS')
def yearlynsecipla(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('CIPLA.NS')
#bse-cipla
def bsecipla(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for cipla share\n"+
                              "/dailybsecipla\n"+ 
                              "/monthlybsecipla\n"+ 
                              "/yearlybsecipla\n")
def dailybsecipla(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('CIPLA.BO')
def monthlybsecipla(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('CIPLA.BO')
def yearlybsecipla(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('CIPLA.BO')
#*********************HCLtech**************************
#nse-hcltech
def nsehcltech(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for hcltech share\n"+
                              "/dailynsehcltech\n"+ 
                              "/monthlynsehcltech\n"+ 
                              "/yearlynsehcltech\n")
def dailynsehcltech(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HCLTECH.NS')
def monthlynsehcltech(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HCLTECH.NS')
def yearlynsehcltech(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HCLTECH.NS')
#bse-hcltech
def bsehcltech(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for hcltech share\n"+
                              "/dailybsehcltech\n"+ 
                              "/monthlybsehcltech\n"+ 
                              "/yearlybsehcltech\n")
def dailybsehcltech(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HCLTECH.BO')
def monthlybsehcltech(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HCLTECH.BO')
def yearlybsehcltech(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HCLTECH.BO')
#************************HDFC**************************
#nse-hdfc
def nsehdfc(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for hdfc share\n"+
                              "/dailynsehdfc\n"+ 
                              "/monthlynsehdfc\n"+ 
                              "/yearlynsehdfc\n")
def dailynsehdfc(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HDFC.NS')
def monthlynsehdfc(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HDFC.NS')
def yearlynsehdfc(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HDFC.NS')
#bse-hdfc
def bsehdfc(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for hdfc share\n"+
                              "/dailybsehdfc\n"+ 
                              "/monthlybsehdfc\n"+ 
                              "/yearlybsehdfc\n")
def dailybsehdfc(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HDFC.BO')
def monthlybsehdfc(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HDFC.BO')
def yearlybsehdfc(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HDFC.BO')
#*******************HeroMotoCo*******************
#nse-heromotoco
def nseheromotoco(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for heromotoco share\n"+
                              "/dailynseheromotoco\n"+ 
                              "/monthlynseheromotoco\n"+ 
                              "/yearlynseheromotoco\n")
def dailynseheromotoco(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HEROMOTOCO.NS')
def monthlynseheromotoco(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HEROMOTOCO.NS')
def yearlynseheromotoco(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HEROMOTOCO.NS')
#bse-heromotoco
def bseheromotoco(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for heromotoco share\n"+
                              "/dailybseheromotoco\n"+ 
                              "/monthlybseheromotoco\n"+ 
                              "/yearlybseheromotoco\n")
def dailybseheromotoco(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HEROMOTOCO.BO')
def monthlybseheromotoco(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HEROMOTOCO.BO')
def yearlybseheromotoco(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HEROMOTOCO.BO')
#*********************hindalco*****************************
#nse-hindalco
def nsehindalco(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for hindalco share\n"+
                              "/dailynsehindalco\n"+ 
                              "/monthlynsehindalco\n"+ 
                              "/yearlynsehindalco\n")
def dailynsehindalco(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HINDALCO.NS')
def monthlynsehindalco(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HINDALCO.NS')
def yearlynsehindalco(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HINDALCO.NS')
#bse-hindalco
def bsehindalco(update: Update, context: CallbackContext):
    update.message.reply_text("Choose the time span for hindalco share\n"+
                              "/dailybsehindalco\n"+ 
                              "/monthlybsehindalco\n"+ 
                              "/yearlybsehindalco\n")
def dailybsehindalco(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HINDALCO.BO')
def monthlybsehindalco(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HINDALCO.BO')
def yearlybsehindalco(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HINDALCO.BO')
#************************ZEEL*************************
#nse-ZEEL
def nsezeel(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for ZEEL share\n"+
                              "/dailynsezeel\n"+ 
                              "/monthlynsezeel\n"+ 
                              "/yearlynsezeel\n")
def dailynsezeel(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('ZEEL.NS')
def monthlynsezeel(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('ZEEL.NS')
def yearlynsezeel(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('ZEEL.NS')
#bse-ZEEL
def bsezeel(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for ZEEL share\n"+
                              "/dailybsezeel\n"+ 
                              "/monthlybsezeel\n"+ 
                              "/yearlybsezeel\n")
def dailybsezeel(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('ZEEL.BO')
def monthlybsezeel(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('ZEEL.BO')
def yearlybsezeel(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('ZEEL.BO')
#************************Wipro*************************
#nse-Wipro
def nsewipro(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for WIPRO share\n"+
                              "/dailynsewipro\n"+ 
                              "/monthlynsewipro\n"+ 
                              "/yearlynsewipro\n")
def dailynsewipro(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('WIPRO.NS')
def monthlynsewipro(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('WIPRO.NS')
def yearlynsewipro(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('WIPRO.NS')
#bse-Wipro
def bsewipro(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for WIPRO share\n"+
                              "/dailybsewipro\n"+ 
                              "/monthlybsewipro\n"+ 
                              "/yearlybsewipro\n")
def dailybsewipro(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('WIPRO.BO')
def monthlybsewipro(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('WIPRO.BO')
def yearlybsewipro(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('WIPRO.BO')
#************************Upl*************************
#nse-Upl
def nseupl(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for UPL share\n"+
                              "/dailynseupl\n"+ 
                              "/monthlynseupl\n"+ 
                              "/yearlynseupl\n")
def dailynseupl(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('UPL.NS')
def monthlynseupl(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('UPL.NS')
def yearlynseupl(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('UPL.NS')
#bse-Upl
def bseupl(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for UPL share\n"+
                              "/dailybseupl\n"+ 
                              "/monthlybseupl\n"+ 
                              "/yearlybseupl\n")
def dailybseupl(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('UPL.BO')
def monthlybseupl(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('UPL.BO')
def yearlybseupl(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('UPL.BO')
#************************Titan*************************
#nse-Titan
def nsetitan(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for TITAN share\n"+
                              "/dailynsetitan\n"+ 
                              "/monthlynsetitan\n"+ 
                              "/yearlynsetitan\n")
def dailynsetitan(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TITAN.NS')
def monthlynsetitan(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TITAN.NS')
def yearlynsetitan(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TITAN.NS')
#bse-Titan
def bsetitan(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for TITAN share\n"+
                              "/dailybsetitan\n"+ 
                              "/monthlybsetitan\n"+ 
                              "/yearlybsetitan\n")
def dailybsetitan(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TITAN.BO')
def monthlybsetitan(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TITAN.BO')
def yearlybsetitan(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TITAN.BO')
#************************Tatasteel*************************
#nse-Tatasteel
def nsetatasteel(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for TATA STEEL share\n"+
                              "/dailynsetatasteel\n"+ 
                              "/monthlynsetatasteel\n"+ 
                              "/yearlynsetatasteel\n")
def dailynsetatasteel(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TATASTEEL.NS')
def monthlynsetatasteel(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TATASTEEL.NS')
def yearlynsetatasteel(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TATASTEEL.NS')
#bse-Tatasteel
def bsetatasteel(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for TATA STEEL share\n"+
                              "/dailybsetatasteel\n"+ 
                              "/monthlybsetatasteel\n"+ 
                              "/yearlybsetatasteel\n")
def dailybsetatasteel(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TATASTEEL.BO')
def monthlybsetatasteel(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TATASTEEL.BO')
def yearlybsetatasteel(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TATASTEEL.BO')
#************************Tatachemical*************************
#nse-Tatachemical
def nsetatachemical(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for TATA CHEMICAL share\n"+
                              "/dailynsetatachemical\n"+ 
                              "/monthlynsetatachemical\n"+ 
                              "/yearlynsetatachemical\n")
def dailynsetatachemical(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TATACHEM.NS')
def monthlynsetatachemical(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TATACHEM.NS')
def yearlynsetatachemical(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TATACHEM.NS')
#bse-Tatachemical
def bsetatachemical(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for TATA CHEMICAL share\n"+
                              "/dailybsetatachemical\n"+ 
                              "/monthlybsetatachemical\n"+ 
                              "/yearlybsetatachemical\n")
def dailybsetatachemical(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TATACHEM.BO')
def monthlybsetatachemical(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TATACHEM.BO')
def yearlybsetatachemical(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TATACHEM.BO')
#************************Tatapower*************************
#nse-Tatapower
def nsetatapower(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for TATA POWER share\n"+
                              "/dailynsetatapower\n"+ 
                              "/monthlynsetatapower\n"+ 
                              "/yearlynsetatapower\n")
def dailynsetatapower(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TATAPOWER.NS')
def monthlynsetatapower(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TATAPOWER.NS')
def yearlynsetatapower(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TATAPOWER.NS')
#bse-Tatapower
def bsetatapower(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for TATA POWER share\n"+
                              "/dailybsetatapower\n"+ 
                              "/monthlybsetatapower\n"+ 
                              "/yearlybsetatapower\n")
def dailybsetatapower(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('TATAPOWER.BO')
def monthlybsetatapower(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('TATAPOWER.BO')
def yearlybsetatapower(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('TATAPOWER.BO')
#************************Sunpharma*************************
#nse-Sunpharma
def nsesunpharma(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for SUN PHARMA share\n"+
                              "/dailynsesunpharma\n"+ 
                              "/monthlynsesunpharma\n"+ 
                              "/yearlynsesunpharma\n")
def dailynsesunpharma(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('SUNPHARMA.NS')
def monthlynsesunpharma(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('SUNPHARMA.NS')
def yearlynsesunpharma(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('SUNPHARMA.NS')
#bse-Sunpharma
def bsesunpharma(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for SUN PHARMA share\n"+
                              "/dailybsesunpharma\n"+ 
                              "/monthlybsesunpharma\n"+ 
                              "/yearlybsesunpharma\n")
def dailybsesunpharma(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('SUNPHARMA.BO')
def monthlybsesunpharma(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('SUNPHARMA.BO')
def yearlybsesunpharma(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('SUNPHARMA.BO')
#************************Reliance*************************
#nse-Reliance
def nsereliance(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for RELIANCE share\n"+
                              "/dailynsereliance\n"+ 
                              "/monthlynsereliance\n"+ 
                              "/yearlynsereliance\n")
def dailynsereliance(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('RELIANCE.NS')
def monthlynsereliance(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('RELIANCE.NS')
def yearlynsereliance(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('RELIANCE.NS')
#bse-Reliance
def bsereliance(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for RELIANCE share\n"+
                              "/dailybsereliance\n"+ 
                              "/monthlybsereliance\n"+ 
                              "/yearlybsereliance\n")
def dailybsereliance(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('RELIANCE.BO')
def monthlybsereliance(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('RELIANCE.BO')
def yearlybsereliance(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('RELIANCE.BO')
#************************Maruti*************************
#nse-Maruti
def nsemaruti(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for MARUTI share\n"+
                              "/dailynsemaruti\n"+ 
                              "/monthlynsemaruti\n"+ 
                              "/yearlynsemaruti\n")
def dailynsemaruti(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('MARUTI.NS')
def monthlynsemaruti(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('MARUTI.NS')
def yearlynsemaruti(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('MARUTI.NS')
#bse-Maruti
def bsemaruti(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for MARUTI share\n"+
                              "/dailybsemaruti\n"+ 
                              "/monthlybsemaruti\n"+ 
                              "/yearlybsemaruti\n")
def dailybsemaruti(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('MARUTI.BO')
def monthlybsemaruti(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('MARUTI.BO')
def yearlybsemaruti(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('MARUTI.BO')
#************************IndusInd*************************
#nse-IndusInd
def nseindusind(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for INDUSIND BANK LIMITED share\n"+
                              "/dailynseindusind\n"+ 
                              "/monthlynseindusind\n"+ 
                              "/yearlynseindusind\n")
def dailynseindusind(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('INDUSINDBK.NS')
def monthlynseindusind(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('INDUSINDBK.NS')
def yearlynseindusind(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('INDUSINDBK.NS')
#bse-IndusInd
def bseindusind(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for INDUSIND BANK LIMITED share\n"+
                              "/dailybseindusind\n"+ 
                              "/monthlybseindusind\n"+ 
                              "/yearlybseindusind\n")
def dailybseindusind(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('INDUSINDBK.BO')
def monthlybseindusind(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('INDUSINDBK.BO')
def yearlybseindusind(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('INDUSINDBK.BO')
#************************Icici*************************
#nse-Icici
def nseicicibank(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for ICICI BANK LIMITED share\n"+
                              "/dailynseicicibank\n"+ 
                              "/monthlynseicicibank\n"+ 
                              "/yearlynseicicibank\n")
def dailynseicicibank(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('ICICIBANK.NS')
def monthlynseicicibank(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('ICICIBANK.NS')
def yearlynseicicibank(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('ICICIBANK.NS')
#bse-Icici
def bseicicibank(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for ICICI BANK LIMITED share\n"+
                              "/dailybseicicibank\n"+ 
                              "/monthlybseicicibank\n"+ 
                              "/yearlybseicicibank\n")
def dailybseicicibank(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('ICICIBANK.BO')
def monthlybseicicibank(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('ICICIBANK.BO')
def yearlybseicicibank(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('ICICIBANK.BO')
#************************HidustanUniliver*************************
#nse-HidustanUniliver
def nsehinduuniliver(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for HINDUSTAN UNILIVER LIMITED share\n"+
                              "/dailynsehinduuniliver\n"+ 
                              "/monthlynsehinduuniliver\n"+ 
                              "/yearlynsehinduuniliver\n")
def dailynsehinduuniliver(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HINDUNILVR.NS')
def monthlynsehinduuniliver(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HINDUNILVR.NS')
def yearlynsehinduuniliver(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HINDUNILVR.NS')
#bse-HidustanUniliver
def bsehinduuniliver(update: Update, context: CallbackContext):
    update.message.reply_text("Whose the time span for HINDUSTAN UNILIVER LIMITED share\n"+
                              "/dailybsehinduuniliver\n"+ 
                              "/monthlybsehinduuniliver\n"+ 
                              "/yearlybsehinduuniliver\n")
def dailybsehinduuniliver(update: Update, context: CallbackContext):
    update.message.reply_text("Todays Charts\n")
    shareday('HINDUNILVR.BO')
def monthlybsehinduuniliver(update: Update, context: CallbackContext):
    update.message.reply_text("Monthly Charts\n")
    sharemonth('HINDUNILVR.BO')
def yearlybsehinduuniliver(update: Update, context: CallbackContext):
    update.message.reply_text("Yearly Charts\n")
    shareyear('HINDUNILVR.BO')

