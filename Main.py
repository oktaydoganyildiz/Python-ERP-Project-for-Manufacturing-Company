from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
from PIL import Image, ImageTk
import tkinter as tk
import pandas as pd
from tkinter import ttk
import time
import os
from pandastable import Table, TableModel
import seaborn as sns
import inventorize3 as inv
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import altair as alt
from fbprophet import Prophet
import math
from matplotlib import pyplot
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


root = Tk()
root.title("Çelik Metal San.Paz. ve Dış Tic.Ltd.Şti ERP Programı")

width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="gray25")
img = tk.PhotoImage(file='gif1.gif')
root.tk.call('wm', 'iconphoto', root._w, img)




# ========================================VARIABLES========================================
USERNAME = StringVar()
PASSWORD = StringVar()

PRODUCT_NAME = StringVar()
PRODUCT_PRICE = StringVar()
PRODUCT_CAP = StringVar()
PRODUCT_BOY = IntVar()
Tarih = StringVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()
giris_tarihi = StringVar()

#####SALES###
Stok_Kodu = StringVar()
Satis_Miktari = IntVar()
Deger = IntVar()
Satis_Tarihi = StringVar()


# ========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT,Tarih TEXT)")
    cursor.execute("SELECT * FROM `admin`")
    # cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    cursor.execute("SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()


def Exit():
    result = tkMessageBox.askquestion('Çelik Metal San.Paz. ve Dış Tic.Ltd.Şti', 'Emin misiniz ?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion('Çelik Metal San.Paz. ve Dış Tic.Ltd.Şti', 'Emin misiniz ?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Program Girişi")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    img = tk.PhotoImage(file='gif1.gif')
    loginform.tk.call('wm', 'iconphoto', loginform._w, img)
    LoginForm()


def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Kullanıcı Girişi", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Kullanıcı Adı:", font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Şifre :", font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Giriş Yap !", font=('arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)


def Home():
    global Home
    global photo2
    Home = Toplevel()
    Home.title("Çelik Metal San.Paz. ve Dış Tic.Ltd.Şti ERP Programı")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    img = tk.PhotoImage(file='gif1.gif')
    Home.tk.call('wm', 'iconphoto', Home._w, img)


    frame3 = Frame(Home, width=600, height=100,bg="black", bd=1, relief=SOLID)
    frame3.pack(side=TOP, pady=20)

    lbl_text3 = Label(frame3, text="Yönetim Paneli", font=('arial', 30),fg="white",bg="black", width=600)
    lbl_text3.pack(fill=X)


    canvas2 = tk.Canvas(Home,bg="gray25", width=700, height=600, highlightthickness=0)
    canvas2.pack(pady=20)
    photo2 = tk.PhotoImage(file ='celik7.png')
    canvas2.create_image(350, 200, image=photo2)


    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu5 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Çıkış Yap", command=Logout)
    filemenu.add_command(label="Programı Kapat", command=Exit2)

    menubar.add_cascade(label="Hesap", menu=filemenu)
    menubar.add_cascade(label="Envanter", menu=filemenu2)
    menubar.add_cascade(label="Üretim", menu=filemenu3)
    menubar.add_cascade(label="Satış ", menu=filemenu4)
    menubar.add_cascade(label="Talep Tahmin", menu=filemenu5)

    #filemenu2.add_command(label="Somun", command=ShowViewSomun)
    #filemenu2.add_command(label="Civata", command=ShowViewCivata)
    #filemenu2.add_command(label="Saplama", command=ShowViewSaplama)
    filemenu2.add_command(label="Envanter Bilgileri", command=openexcel)
    filemenu2.add_command(label="ABC Analizi", command=abc_analizi)


    filemenu3.add_command(label="Üretim Emri Gir", command=ShowAddNew)
    filemenu3.add_command(label="Üretim Emirlerini Gör", command=ShowView)
    filemenu3.add_command(label="Üretim Planı", command=uretim_plani)

    filemenu4.add_command(label="Satış Verileri Gir", command=Sales)
    filemenu4.add_command(label="Satış Tablosu", command=ShowSales)

    filemenu5.add_command(label="Yıllık Tahmin Somun", command=forecast_somun)
    filemenu5.add_command(label="Yıllık Tahmin Civata", command=forecast_civata)
    filemenu5.add_command(label="Yıllık Tahmin Saplama", command=forecast_saplama)


    Home.config(menu=menubar)
    Home.config(bg="gray25")
def safety_stok():


    require_cols = [0, 4, 6]
    require_cols_1 = [0, 1]

    somun = pd.read_excel('Sureler.xlsx', usecols=require_cols_1)
    civata = pd.read_excel('Sureler.xlsx', sheet_name=1, usecols=[0, 1, 2, 3, 4])
    saplama = pd.read_excel('Sureler.xlsx', sheet_name=2, usecols=[0, 1, 2, 3, 4])
    cnx = sqlite3.connect('pythontut.db')

    df_satis = pd.read_sql_query(
        "SELECT  Satis_Tarihi,Stok_Kodu,Satis_miktari FROM sales",
        cnx)
    #print (df_satis)
    # df_satis = pd.read_excel('satis_listesi.xlsx', usecols=require_cols)
    select = PRODUCT_NAME.get()
    urun_cesit = combobox2.get()



    if urun_cesit == 'SOMUN':

        urun_kodu = (PRODUCT_NAME.get())
        siparis_miktarı = PRODUCT_QTY.get()
        fp = pd.read_excel("envanter.xlsm", "somun", index_col=False)
        pd.set_option('display.max_rows', fp.shape[0] + 1)
        result = fp.head(1000)
        B = result.loc[result['Unnamed: 1'] == urun_kodu]
        stok_sayisi = (B['Unnamed: 7'].iloc[0])
        #########################################################
        cap = PRODUCT_CAP.get()
        #print(cap)
        B = somun.loc[somun[
                          'Cap'] == cap]  # Burada inputtaki çap değerini, dataframedeki çap başlıklı sütundaki indexle eşitliyor ve B değişkeni o indexi tutuyor.
        sure = (B['Sure'].iloc[
            0])  # Ardından "sure" değişkeni "B" değişkeninin tuttuğu indexte "Sure" Başlıklı sütunda o değeri alıyor.
        df_product = df_satis.loc[df_satis.Stok_Kodu == select]
        Average_daily_sales = df_product['Satis_miktari'].sum() / len(df_product.index)
        Average_daily_sales2= Average_daily_sales / len(df_product.index)
        maxleadtime = int(sure) / 86400 * (df_product['Satis_miktari'].max())
        averageleadtime = int(sure) / 86400 * Average_daily_sales2

        safety_stock_somun = (df_product['Satis_miktari'].max() * maxleadtime) - (Average_daily_sales2 * averageleadtime)
        #print("Güvenli Stok Miktarı :", round(safety_stock_somun))

        if ((siparis_miktarı)-(stok_sayisi))+(safety_stock_somun) > 0 :
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var.Safety stock miktarı: " +  str(round(safety_stock_somun))) + " Üretilmesi gereken miktar: " +str(int(((siparis_miktarı)-(stok_sayisi))+(safety_stock_somun)))
            btn_kont5 = Label(lowestframe, text=label, font=('arial', 15), fg="white", width=100, bg="gray25")
            btn_kont5.grid(row=0, column=0)

        elif ((siparis_miktarı)-(stok_sayisi))+(safety_stock_somun) < 0 :
            label = ("Stokta " + str(int(stok_sayisi))) + "adet var.Daha fazla üretilmesine gerek yok."
            btn_kont5 = Label(lowestframe, text=label, font=('arial', 15), fg="white", width=100, bg="gray25")
            btn_kont5.grid(row=0, column=0)



    elif urun_cesit == 'CİVATA':
        urun_kodu = PRODUCT_NAME.get()
        siparis_miktarı = PRODUCT_QTY.get()

        fp = pd.read_excel("envanter.xlsm", "civata", index_col=False)
        pd.set_option('display.max_rows', fp.shape[0] + 1)
        result = fp.head(1000)
        B = result.loc[result['Unnamed: 1'] == urun_kodu]
        stok_sayisi = (B['Unnamed: 7'].iloc[0])

        cap = PRODUCT_CAP.get()
        B = civata.loc[civata['Cap'] == cap]
        islemsuresimin = (B['islem suresimin'].iloc[0])
        boymin = (B['boymin'].iloc[0])
        islemsuresimax = (B['islem suresimax'].iloc[0])
        boymax = (B['boymax'].iloc[0])

        islemsuresifark = islemsuresimax - islemsuresimin
        boyfark = boymax - boymin
        boy1 = PRODUCT_BOY.get()
        df_product = df_satis.loc[df_satis.Stok_Kodu == select]  ##############
        Average_daily_sales = df_product['Satis_miktari'].sum() / len(df_product.index)

        sonsure1 = ((boy1 * islemsuresifark) - (islemsuresifark - boymin) + (
                            boyfark * islemsuresimin)) / boyfark

        maxleadtime_civata = int(sonsure1) / 86400 * df_product['Satis_miktari'].max()
        averageleadtime_civata = int(sonsure1) / 86400 * Average_daily_sales

        safety_stock_civata = (df_product['Satis_miktari'].max() * maxleadtime_civata) - (
                            Average_daily_sales * averageleadtime_civata)
        #print("Güvenli Stok Miktarı :", round(safety_stock_civata))

        if ((siparis_miktarı)-(stok_sayisi))+(safety_stock_civata) > 0 :
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var.Safety stock miktarı: " +  str(round(safety_stock_civata))) + " Üretilmesi gereken miktar: " +str(int(((siparis_miktarı)-(stok_sayisi))+(safety_stock_civata)))
            btn_kont5 = Label(lowestframe, text=label, font=('arial', 15), fg="white", width=100, bg="gray25")
            btn_kont5.grid(row=0, column=0)

        elif ((siparis_miktarı)-(stok_sayisi))+(safety_stock_civata) < 0 :
            label = ("Stokta " + str(int(stok_sayisi))) + "adet var.Daha fazla üretilmesine gerek yok."
            btn_kont5 = Label(lowestframe, text=label, font=('arial', 15), fg="white", width=100, bg="gray25")
            btn_kont5.grid(row=0, column=0)

    elif urun_cesit == 'SAPLAMA':
        urun_kodu = (PRODUCT_NAME.get())
        siparis_miktarı = PRODUCT_QTY.get()
        fp = pd.read_excel("envanter.xlsm", "saplama", index_col=False)
        pd.set_option('display.max_rows', fp.shape[0] + 1)
        result = fp.head(1000)
        B = result.loc[result['Unnamed: 1'] == urun_kodu]
        stok_sayisi = (B['Unnamed: 7'].iloc[0])

        cap = PRODUCT_CAP.get()
        B = saplama.loc[saplama['Cap'] == cap]
        islemsuresimin = (B['islem suresimin'].iloc[0])
        boymin = (B['boymin'].iloc[0])
        islemsuresimax = (B['islem suresimax'].iloc[0])
        boymax = (B['boymax'].iloc[0])

        islemsuresifark = islemsuresimax - islemsuresimin
        boyfark = boymax - boymin

        boy2 = PRODUCT_BOY.get()
        df_product = df_satis.loc[df_satis.Stok_Kodu == select]
        Average_daily_sales = df_product['Satis_miktari'].sum() / len(df_product.index)

        df_product = df_satis.loc[df_satis.Stok_Kodu == select]
        Average_daily_sales = df_product['Satis_miktari'].sum() / len(df_product.index)
        sonsure2 = ((boy2 * islemsuresifark) - (islemsuresifark - boymin) + (
                            boyfark * islemsuresimin)) / boyfark

        maxleadtime_saplama = int(sonsure2) / 86400 * df_product['Satis_miktari'].max()
        averageleadtime_saplama = int(sonsure2) / 86400 * Average_daily_sales

        safety_stock_saplama = (df_product['Satis_miktari'].max() * maxleadtime_saplama) - (
                            Average_daily_sales * averageleadtime_saplama)
        #print("Güvenli Stok Miktarı :", round(safety_stock_saplama))

        if ((siparis_miktarı)-(stok_sayisi))+(safety_stock_saplama) > 0 :
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var.Safety stock miktarı: " +  str(round(safety_stock_saplama))) + " Üretilmesi gereken miktar: " +str(int(((siparis_miktarı)-(stok_sayisi))+(safety_stock_saplama)))
            btn_kont5 = Label(lowestframe, text=label, font=('arial', 15), fg="white", width=100, bg="gray25")
            btn_kont5.grid(row=0, column=0)

        elif ((siparis_miktarı)-(stok_sayisi))+(safety_stock_saplama) < 0 :
            label = ("Stokta " + str(int(stok_sayisi))) + "adet var.Daha fazla üretilmesine gerek yok."
            btn_kont5 = Label(lowestframe, text=label, font=('arial', 15), fg="white", width=100, bg="gray25")
            btn_kont5.grid(row=0, column=0)




def abc_analizi():
    global f
    window2 = tk.Toplevel()

    cnx = sqlite3.connect('pythontut.db')

    raw_data = pd.read_sql_query(
        "SELECT  Stok_Kodu,Satis_miktari,Deger FROM sales",
        cnx)

    # raw_data = pd.read_excel('abc-data.xls')
    raw_data.head(5)
    raw_data.shape

    data = raw_data.drop_duplicates()
    data = data.dropna()
    data = data[data['Satis_miktari'] > 0]
    data.shape

    data1 = data[['Stok_Kodu', 'Satis_miktari', 'Deger']]
    data1.head()

    data_abc = inv.ABC(data1[['Stok_Kodu', 'Deger']])
    data_abc

    data_abc.Category.value_counts()

    data_summary = data_abc.groupby('Category').agg(Count=('Category', np.count_nonzero),
                                                    Percentage=('Percentage', np.sum)).reset_index()
    data_summary['Percentage'] = data_summary['Percentage'] * 100
    data_summary

    sns.countplot(x='Category', data=data_abc, label=True)

    data_abc1 = inv.ABC(data_abc[['Stok_Kodu', 'Deger']])
    (data_abc1.Category.value_counts())
    (data_abc1)


    window2.geometry('1024x520+200+100')
    window2.title('ABC Analizi')
    f = Frame(window2)
    f.pack(fill=BOTH, expand=1)
    df = data_abc1
    table = pt = Table(f, dataframe=df,
                                    showtoolbar=True, showstatusbar=True)
    pt.show()


    #app = TestApp()
    # launch the app
    #app.mainloop()





def forecast_somun():
    root = tk.Tk()
    root.title('Somun Yıllık Satış Tahmini')
    root.resizable(False, False)
    root.geometry('1024x520')
    LARGE_FONT = ("Verdana", 12)
    lbl_text = tk.Label(root, text="Somun Yıllık Satış Tahmini", font=('arial', 18), width=100)
    lbl_text.pack(side=TOP,pady=20)
    cnx = sqlite3.connect('pythontut.db')

    df = pd.read_sql_query(
        "SELECT strftime('%Y %m', Satis_Tarihi) as AYLAR,SUM(Satis_miktari) AS SATIS FROM sales WHERE Urun_cesit='SOMUN' GROUP BY strftime('%Y %m', Satis_Tarihi)",
        cnx)

    df['y'] = df['SATIS']
    df['ds'] = df['AYLAR']

    df = df.drop("AYLAR", axis=1)
    df = df.drop('SATIS', axis=1)

    m = Prophet(interval_width=0.95, daily_seasonality=True, yearly_seasonality=True)
    model = m.fit(df)

    future = m.make_future_dataframe(periods=12, freq='M')
    forecast = m.predict(future)
    forecast.head()

    tahmin = []
    for i in forecast['yhat'][-12:]:
        tahmin.insert(0, int(i))
        tahmin.reverse()
    analizler = {'Tahmini Satış Miktarı': tahmin}



    df2 = pd.DataFrame(tahmin, columns=['Tahmini Satış Miktarı'], index=['Ocak', 'Subat', 'Mart', 'Nisan', 'Mayis', 'Haziran',
                                                                 'Temmuz', 'Agustos', 'Eylul', 'Ekim', 'Kasim',
                                                                 'Aralik'])

    label = tk.Label(root, text=df2, font=LARGE_FONT)
    label.pack(side=tk.LEFT)
    plot1 = m.plot(forecast)
    canvas = FigureCanvasTkAgg(plot1, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT)

def forecast_civata():
    root = tk.Tk()
    root.title('Yillik Tahmin')
    root.resizable(False, False)
    root.geometry('1024x520')
    LARGE_FONT = ("Verdana", 12)
    lbl_text = tk.Label(root, text="Civata Yıllık Satış Tahmini", font=('arial', 18), width=100)
    lbl_text.pack(side=TOP, pady=20)
    cnx = sqlite3.connect('pythontut.db')

    df = pd.read_sql_query(
        "SELECT strftime('%Y %m', Satis_Tarihi) as AYLAR,SUM(Satis_miktari) AS SATIS FROM sales WHERE Urun_cesit='CİVATA' GROUP BY strftime('%Y %m', Satis_Tarihi)",
        cnx)

    df['y'] = df['SATIS']
    df['ds'] = df['AYLAR']

    df = df.drop("AYLAR", axis=1)
    df = df.drop('SATIS', axis=1)

    m = Prophet(interval_width=0.95, daily_seasonality=True, yearly_seasonality=True)
    model = m.fit(df)

    future = m.make_future_dataframe(periods=12, freq='M')
    forecast = m.predict(future)
    forecast.head()

    tahmin = []
    for i in forecast['yhat'][-12:]:
        tahmin.insert(0, int(i))
        tahmin.reverse()
    analizler = {'Tahmini Talep': tahmin}

    df2 = pd.DataFrame(tahmin, columns=['Tahmini Talep'], index=['Ocak', 'Subat', 'Mart', 'Nisan', 'Mayis', 'Haziran',
                                                                 'Temmuz', 'Agustos', 'Eylul', 'Ekim', 'Kasim',
                                                                 'Aralik'])

    label = tk.Label(root, text=df2, font=LARGE_FONT)
    label.pack(side=tk.LEFT)
    plot1 = m.plot(forecast)
    canvas = FigureCanvasTkAgg(plot1, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT)


def forecast_saplama():
    root = tk.Tk()
    root.title('Yillik Tahmin')
    root.resizable(False, False)
    root.geometry('1024x520')
    LARGE_FONT = ("Verdana", 12)
    lbl_text = tk.Label(root, text="Saplama Yıllık Satış Tahmini", font=('arial', 18), width=100)
    lbl_text.pack(side=TOP, pady=20)
    cnx = sqlite3.connect('pythontut.db')

    df = pd.read_sql_query(
        "SELECT strftime('%Y %m', Satis_Tarihi) as AYLAR,SUM(Satis_miktari) AS SATIS FROM sales WHERE Urun_cesit='SAPLAMA' GROUP BY strftime('%Y %m', Satis_Tarihi)",
        cnx)

    df['y'] = df['SATIS']
    df['ds'] = df['AYLAR']

    df = df.drop("AYLAR", axis=1)
    df = df.drop('SATIS', axis=1)

    m = Prophet(interval_width=0.95, daily_seasonality=True, yearly_seasonality=True)
    model = m.fit(df)

    future = m.make_future_dataframe(periods=12, freq='M')
    forecast = m.predict(future)
    forecast.head()

    tahmin = []
    for i in forecast['yhat'][-12:]:
        tahmin.insert(0, int(i))
        tahmin.reverse()
    analizler = {'Tahmini Talep': tahmin}

    df2 = pd.DataFrame(tahmin, columns=['Tahmini Talep'], index=['Ocak', 'Subat', 'Mart', 'Nisan', 'Mayis', 'Haziran',
                                                                 'Temmuz', 'Agustos', 'Eylul', 'Ekim', 'Kasim',
                                                                 'Aralik'])

    label = tk.Label(root, text=df2, font=LARGE_FONT)
    label.pack(side=tk.LEFT)
    plot1 = m.plot(forecast)
    canvas = FigureCanvasTkAgg(plot1, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT)


def Sales():
    global sales

    sales = Toplevel()
    sales.title("Yeni Satış Bilgisi Girişi")
    width = 800
    height = 600
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    sales.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # sales.resizable(0, 0)
    Sales_menu()



def Sales_menu():
    global MidAddNew2
    global combobox
    global cesit

    TopAddNew2 = Frame(sales, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew2.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew2, text="Yeni Satış Bilgisi Girişi", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew2 = Frame(sales, width=600)
    MidAddNew2.pack(side=TOP, pady=50)
    lbl_cesit = Label(MidAddNew2, text="Ürün Çeşidi:", font=('arial', 25), bd=10)
    lbl_cesit.grid(row=0, sticky=W)
    lbl_productname = Label(MidAddNew2, text="Ürün Kodu:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=1, sticky=W)
    lbl_qty = Label(MidAddNew2, text="Satış Miktarı:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=2, sticky=W)
    lbl_price = Label(MidAddNew2, text="Toplam Satış Fiyatı:", font=('arial', 25), bd=10)
    lbl_price.grid(row=3, sticky=W)
    lbl_tarih = Label(MidAddNew2, text="Satış Tarihi:", font=('arial', 25), bd=10)
    lbl_tarih.grid(row=4, sticky=W)
    lbl_uyarı = Label(MidAddNew2, text="Tarih bilgilerini YYYY-AA-GG Şeklinde Giriniz !", font=('arial', 10), bd=10,fg='red')
    lbl_uyarı.grid(row=5, sticky=W)

    combobox = ttk.Combobox(MidAddNew2, width="30", values=("SOMUN", "CİVATA", "SAPLAMA"))
    combobox.grid(row=0, column=1)

    productname = Entry(MidAddNew2, textvariable=Stok_Kodu, font=('arial', 25), width=15)
    productname.grid(row=1, column=1)
    productqty2 = Entry(MidAddNew2, textvariable=Satis_Miktari, font=('arial', 25), width=15)
    productqty2.grid(row=2, column=1)
    productprice = Entry(MidAddNew2, textvariable=Deger, font=('arial', 25), width=15)
    productprice.grid(row=3, column=1)
    Tarih = Entry(MidAddNew2, textvariable=Satis_Tarihi, font=('arial', 25), width=15)
    Tarih.grid(row=4, column=1)

    btn_add = Button(MidAddNew2, text="KAYDET", font=('arial', 18), width=30, bg="#009ACD",
                     command=lambda: [sales_ekle(), kayit_label()])
    btn_add.grid(row=5, column=1, pady=20)


def kayit_label():
    lbl_kayit = Label(MidAddNew2, text="Kayıt Başarılı !", font=('arial', 25), bd=10, fg="red")
    lbl_kayit.grid(row=6, column=1, sticky=W)



def sales_ekle():
    Database()
    cursor.execute("INSERT INTO `sales` (Stok_kodu,Satis_miktari,Deger,Satis_Tarihi,Urun_cesit) VALUES(?, ?, ?, ?, ?)",
                   (Stok_Kodu.get(), (Satis_Miktari.get()), (Deger.get()), (Satis_Tarihi.get()), (combobox.get())))
    conn.commit()
    Stok_Kodu.set("")
    Satis_Miktari.set("")
    Deger.set("")
    Satis_Tarihi.set("")

    cursor.close()
    conn.close()


def SalesForm():
    global tree2
    TopViewForm = Frame(salesform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(salesform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(salesform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Satış Bilgileri", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Ara", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Ara", command=Search2)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Filtre Kaldır", command=Reset2)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Sil", command=Delete2)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree2 = ttk.Treeview(MidViewForm,
                         columns=("Satis_sayisi", "Product Name", "Satis_Miktari", "Deger", "Tarih", "Urun_Cesidi"),
                         selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                         xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree2.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree2.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree2.heading('Satis_sayisi', text="Satis_sayisi", anchor=W)
    tree2.heading('Product Name', text="Ürün Kodu", anchor=W)

    tree2.heading('Satis_Miktari', text="Satis_Miktari", anchor=W)
    tree2.heading('Deger', text="Deger", anchor=W)
    tree2.heading('Tarih', text="Tarih", anchor=W)
    tree2.heading('Urun_Cesidi', text="Urun_Cesidi", anchor=W)

    tree2.column('#0', stretch=NO, minwidth=0, width=0)
    tree2.column('#1', stretch=NO, minwidth=0, width=0)
    tree2.column('#2', stretch=NO, minwidth=0)
    tree2.column('#3', stretch=NO, minwidth=0)
    tree2.column('#4', stretch=NO, minwidth=0)
    tree2.column('#5', stretch=NO, minwidth=0)
    tree2.column('#6', stretch=NO, minwidth=0)

    tree2.pack()
    DisplayData2()


def DisplayData2():
    Database()
    cursor.execute("SELECT * FROM `sales`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree2.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search2():
    if SEARCH.get() != "":
        tree2.delete(*tree2.get_children())
        Database()
        cursor.execute("SELECT * FROM `sales` WHERE `Stok_Kodu` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree2.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def Reset2():
    tree2.delete(*tree2.get_children())
    DisplayData2()
    SEARCH.set("")


def Delete2():
    if not tree2.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('Uyarı', 'Silmek İstediğinizden Emin misiniz ?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree2.focus()
            contents = (tree2.item(curItem))
            selecteditem2 = contents['values']
            tree2.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `sales` WHERE `Satis_Sayisi` = %d" % selecteditem2[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowSales():
    global salesform
    salesform = Toplevel()
    salesform.title("Satış Bilgileri")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    salesform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    salesform.resizable(0, 0)
    img = tk.PhotoImage(file='gif1.gif')
    salesform.tk.call('wm', 'iconphoto', salesform._w, img)
    SalesForm()


######################
def uretim_plani():
    cnx = sqlite3.connect('pythontut.db')

    df = pd.read_sql_query("SELECT product_name,Tarih,product_price,product_id FROM product", cnx)

    df["Başlangıç Tarihi"] = df["Tarih"]
    df["Bitiş Tarihi"] = df["product_price"]
    df["Üretimdeki Ürün"] = df["product_name"]
    df = df.drop("Tarih", axis=1)
    df = df.drop("product_price", axis=1)
    df = df.drop("product_name", axis=1)

    df["Başlangıç Tarihi"] = pd.to_datetime(df["Başlangıç Tarihi"])
    df["Bitiş Tarihi"] = pd.to_datetime(df["Bitiş Tarihi"])

    chart = alt.Chart(df.drop("product_id", 1)).mark_bar().encode(
        x='Başlangıç Tarihi',
        x2='Bitiş Tarihi',
        y=alt.Y('Üretimdeki Ürün',
                sort=list(df.sort_values(["Bitiş Tarihi", "Başlangıç Tarihi"])
                          ["Üretimdeki Ürün"])),
    )
    chart.show()


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Üretim Emri Girişi")
    width = 900
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable()
    img = tk.PhotoImage(file='gif1.gif')
    addnewform.tk.call('wm', 'iconphoto', addnewform._w, img)
    AddNewForm()


def kontrol_somun():
    global addnewform
    global MidAddNew
    global lowestframe
    global stok_sayisi
    global üretim_miktarı
    # urun_kodu=(PRODUCT_NAME.get())
    # siparis_miktarı= PRODUCT_QTY.get()
    try:
        urun_kodu = (PRODUCT_NAME.get())
        siparis_miktarı = PRODUCT_QTY.get()
        fp = pd.read_excel("envanter.xlsm", "somun", index_col=False)
        pd.set_option('display.max_rows', fp.shape[0] + 1)
        result = fp.head(1000)
        B = result.loc[result['Unnamed: 1'] == urun_kodu]
        stok_sayisi = (B['Unnamed: 7'].iloc[0])
        if siparis_miktarı < stok_sayisi:
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var")
        elif siparis_miktarı > stok_sayisi:
            üretim_miktarı = siparis_miktarı - stok_sayisi
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var " + str(int(üretim_miktarı)) + " adet daha üretilmesi gerekiyor")
        btn_kont5 = Label(lowestframe, text=label, font=('arial', 15),fg="white", width=50, bg="gray25")
        btn_kont5.grid(row=0, column=0, pady=20)
    except IndexError:
        label = "Stokta ürün mevcut değil yada eksik giriş yaptınız !"
        btn_kont5 = Label(lowestframe, text=label,fg="white", font=('arial', 15), width=50, bg="gray25")
        btn_kont5.grid(row=0, column=0, pady=20)


def kontrol_saplama():
    global addnewform
    global MidAddNew
    global lowestframe
    urun_kodu = (PRODUCT_NAME.get())
    siparis_miktarı = PRODUCT_QTY.get()
    try:
        fp = pd.read_excel("envanter.xlsm", "saplama", index_col=False)
        pd.set_option('display.max_rows', fp.shape[0] + 1)
        result = fp.head(1000)
        B = result.loc[result['Unnamed: 1'] == urun_kodu]
        stok_sayisi = (B['Unnamed: 7'].iloc[0])
        if siparis_miktarı < stok_sayisi:
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var")
        elif siparis_miktarı > stok_sayisi:
            üretim_miktarı = siparis_miktarı - stok_sayisi
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var " + str(int(üretim_miktarı)) + " adet daha üretilmesi gerekiyor")

        btn_kont5 = Label(lowestframe, text=label,fg="white", font=('arial', 18), width=30, bg="gray25")
        btn_kont5.grid(row=2, pady=20)
    except IndexError:
        label = "Stokta ürün mevcut değil yada eksik giriş yaptınız !"
        btn_kont5 = Label(lowestframe, text=label,fg="white", font=('arial', 15), width=50, bg="gray25")
        btn_kont5.grid(row=0, column=0, pady=20)


def kontrol_civata():
    global addnewform
    global MidAddNew
    global lowframe
    global lowestframe
    urun_kodu = (PRODUCT_NAME.get())
    siparis_miktarı = PRODUCT_QTY.get()

    try:
        fp = pd.read_excel("envanter.xlsm", "civata", index_col=False)
        pd.set_option('display.max_rows', fp.shape[0] + 1)
        result = fp.head(1000)
        B = result.loc[result['Unnamed: 1'] == urun_kodu]
        stok_sayisi = (B['Unnamed: 7'].iloc[0])
        if siparis_miktarı < stok_sayisi:
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var")
        elif siparis_miktarı > stok_sayisi:
            üretim_miktarı = siparis_miktarı - stok_sayisi
            label = ("Stokta " + str(int(stok_sayisi)) + " adet var " + str(int(üretim_miktarı)) + " adet daha üretilmesi gerekiyor")

        btn_kont5 = Label(lowestframe, text=label,fg="white", font=('arial', 18), width=30, bg="gray25")
        btn_kont5.grid(row=2, pady=20)

    except IndexError:
        label = "Stokta ürün mevcut değil yada eksik giriş yaptınız !"
        btn_kont5 = Label(lowestframe, text=label,fg="white", font=('arial', 15), width=50, bg="gray25")
        btn_kont5.grid(row=0, column=0, pady=20)


def AddNewForm():
    global MidAddNew
    global lowframe
    global lowestframe
    global combobox2
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)

    lbl_text = Label(TopAddNew, text="Üretim Emri Girişi", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lowframe = Frame(addnewform, width=300)
    lowframe.pack(side=TOP, pady=16)
    lowestframe = Frame(addnewform, width=300)
    lowestframe.pack(side=TOP, pady=16)

    lbl_cesit = Label(MidAddNew, text="Ürün Çeşidi:", font=('arial', 15), bd=10)
    lbl_cesit.grid(row=0, sticky=W)
    combobox2 = ttk.Combobox(MidAddNew, width="15", values=("SOMUN", "CİVATA", "SAPLAMA"))
    combobox2.grid(row=0, column=1)
    lbl_productname = Label(MidAddNew, text="Ürün Kodu:", font=('arial', 15), bd=10)
    lbl_productname.grid(row=1, sticky=W)
    lbl_productcap = Label(MidAddNew, text="Çap:", font=('arial', 15), bd=10)
    lbl_productcap.grid(row=2, sticky=W)
    lbl_productboy = Label(MidAddNew, text="Boy:", font=('arial', 15), bd=10)
    lbl_productboy.grid(row=3, sticky=W)
    lbl_qty = Label(MidAddNew, text="Sipariş Sayısı:", font=('arial', 15), bd=10)
    lbl_qty.grid(row=4, sticky=W)
    lbl_price = Label(MidAddNew, text="Son Teslim Tarihi:", font=('arial', 15), bd=10)
    lbl_price.grid(row=5, sticky=W)
    lbl_price2 = Label(MidAddNew, text="İşlem Başlangıç Tarihi:", font=('arial', 15), bd=10)
    lbl_price2.grid(row=6, sticky=W)

    # lbl_tarih = Label(MidAddNew, text="Tarih:", font=('arial', 25), bd=10)
    # lbl_tarih.grid(row=3, sticky=W)

    productname2 = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('arial', 15), width=10)
    productname2.grid(row=1, column=1)
    productcap2 = Entry(MidAddNew, textvariable=PRODUCT_CAP, font=('arial', 15), width=10)
    productcap2.grid(row=2, column=1)
    productboy2 = Entry(MidAddNew, textvariable=PRODUCT_BOY, font=('arial', 15), width=10)
    productboy2.grid(row=3, column=1)


    productqty2 = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('arial', 15), width=10)
    productqty2.grid(row=4, column=1)
    productprice2 = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('arial', 15), width=10)
    productprice2.grid(row=5, column=1)
    productprice3 = Entry(MidAddNew, textvariable=giris_tarihi, font=('arial', 15), width=10) #tarih
    productprice3.grid(row=6, column=1)
    # Tarih2 = Entry(MidAddNew, textvariable=Tarih, font=('arial', 25), width=15)
    # Tarih2.grid(row=3, column=1)

    btn_add = Button(lowframe, text="Ekle", font=('arial', 10), width=10, bg="#009ACD",
                     command=lambda: [AddNew(), siparis_lbl()])
    btn_add.grid(row=1, column=2, pady=20)

    btn_kont = Button(lowframe, text="Ürünü Kontrol Et ", font=('arial', 14), width=20, bg="#009ACD",
                      command=safety_stok)
    btn_kont.grid(row=0, column=2, padx=10)

    #btn_kont2 = Button(lowframe, text="Kontrol Saplama ", font=('arial', 10), width=12, bg="#009ACD",
     #                  command=kontrol_saplama)
    #btn_kont2.grid(row=0, column=2, padx=10)

    #btn_kont3 = Button(lowframe, text="Kontrol Civata ", font=('arial', 10), width=12, bg="#009ACD",
     #                  command=kontrol_civata)
    #btn_kont3.grid(row=0, column=3, padx=10, )


def siparis_lbl():
    lbl_price = Label(lowframe, text="Başarı ile eklendi !", font=('arial', 10), bd=10, fg="red")
    lbl_price.grid(row=2, column=2, sticky=W)


def openexcel():
    os.chdir('C:\\Users\\oktay\\Desktop\\celik\\v1.2')

    os.system('start excel.exe envanter.xlsm')


def AddNew():
    Database()

    cursor.execute("INSERT INTO `product` (product_name, product_qty, product_price,Tarih) VALUES(?, ?, ?, ?)",
                   (str(PRODUCT_NAME.get()), int(PRODUCT_QTY.get()), str(PRODUCT_PRICE.get()), (giris_tarihi.get())))
    conn.commit()
    PRODUCT_NAME.set("")
    PRODUCT_PRICE.set("")
    PRODUCT_QTY.set("")
    Tarih.set("")
    giris_tarihi.set("")
    cursor.close()
    conn.close()


##SİPARİS#
def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="Üretim Emirleri", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Ara", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Ara", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Filtre Kaldır", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Sil", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Product Name", "Product Qty", "Product Price", "Tarih"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ProductID', text="Sipariş NO", anchor=W)
    tree.heading('Product Name', text="Ürün Kodu", anchor=W)
    tree.heading('Product Qty', text="Sipariş Miktarı", anchor=W)
    tree.heading('Product Price', text="Son Teslim Tarihi", anchor=W)
    tree.heading('Tarih', text="İşlem Başlangıç Tarihi", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0)
    tree.column('#2', stretch=NO, minwidth=0)
    tree.column('#3', stretch=NO, minwidth=0)
    tree.column('#4', stretch=NO, minwidth=0)
    tree.column('#5', stretch=NO, minwidth=0)
    tree.pack()
    DisplayData()


def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `product` WHERE `product_name` LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")


def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('delete',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def ShowView():
    global viewform

    viewform = Toplevel()
    viewform.title("Üretim Emirleri")
    width = 1024
    height = 520
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    img = tk.PhotoImage(file='gif1.gif')
    viewform.tk.call('wm', 'iconphoto', viewform._w, img)
    ViewForm()


def ViewFormSomun():
    global treesomun
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=1000)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)

    lbl_text = Label(LeftViewForm, text="View Products", font=('arial', 18), width=30)
    lbl_text.pack(fill=X)

    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", )
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)

    fp = pd.read_excel("tes2.xlsm", "somuna", index_col=False)
    pd.set_option('display.max_rows', fp.shape[0] + 1)
    # df1 = pd.read_excel(fp, 'Sheet1')
    # fp.style.hide_index()
    # pd.options.display.float_format = "{:,.2f}".format
    # fp.style.format('{:,}')
    result = fp.head(10)
    """
    ###### SCATTER GRAPH #######

    #df = pd.DataFrame(data, columns=['Unemployment_Rate', 'Stock_Index_Price'])
    #fp.plot(x='Ürün Kodları', y='Toplam Adet', kind='scatter')
    #plt.show()

    ##### PİE CHART ######
    a=fp.drop(fp.index[len(fp) - 1])
    a.groupby(['Ürün Kodları']).sum().plot(kind='pie', y='Toplam Adet',labels=None)
    plt.show()
    """

    statistic_somun = Label(LeftViewForm, text=result, width=40, height=200, font=('arial', 15), )
    statistic_somun.pack(side=BOTTOM, padx=10, pady=100, fill=Y)

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    treesomun = ttk.Treeview(MidViewForm, columns=(
        "Stok Kodu", "Kalite", "DIN Formu", "Kaplama", "Cap", "Boy", "Adet", 'Raf', "Dokum NO", "Iz NO", "NOT"),
                             selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=treesomun.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=treesomun.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    treesomun.heading("Stok Kodu", text="Stok Kodu", anchor=W)
    treesomun.heading('Kalite', text="Kalite", anchor=W)
    treesomun.heading('DIN Formu', text="DIN Formu", anchor=W)
    treesomun.heading('Kaplama', text="Kaplama", anchor=W)
    treesomun.heading('Cap', text="Cap", anchor=W)
    treesomun.heading('Boy', text="Boy", anchor=W)
    treesomun.heading('Adet', text="Adet", anchor=W)
    treesomun.heading('Raf', text="Raf", anchor=W)
    treesomun.heading('Dokum NO', text="Dokum NO", anchor=W)
    treesomun.heading('Iz NO', text="Iz NO", anchor=W)
    treesomun.heading('NOT', text="NOT", anchor=W)

    treesomun.column('#0', stretch=NO, minwidth=0, width=0)
    treesomun.column('#1', stretch=NO, minwidth=0, width=200)
    treesomun.column('#2', stretch=NO, minwidth=0, width=200)
    treesomun.column('#3', stretch=NO, minwidth=0, width=120)
    treesomun.column('#4', stretch=NO, minwidth=0, width=120)
    treesomun.column('#5', stretch=NO, minwidth=0, width=120)
    treesomun.column('#6', stretch=NO, minwidth=0, width=120)
    treesomun.column('#7', stretch=NO, minwidth=0, width=120)
    treesomun.column('#8', stretch=NO, minwidth=0, width=120)
    treesomun.column('#9', stretch=NO, minwidth=0, width=120)
    treesomun.column('#10', stretch=NO, minwidth=0, width=120)

    treesomun.pack()
    DisplayDataSomun()


def ViewFormCivata():
    global treecivata
    TopViewForm = Frame(viewform2, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform2, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform2, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Searchhhhhhhhhh", )
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", )
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", )
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    treecivata = ttk.Treeview(MidViewForm, columns=(
    "Stok", "Kalite", "DIN Formu", "Kaplama", "Cap", "Boy", "Adet", "Raf", "Dokum NO", "Iz NO", "NOT")
                              , selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                              xscrollcommand=scrollbarx.set)
    scrollbary.config(command=treecivata.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=treecivata.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    treecivata.heading("Stok", text="Stok", anchor=W)
    treecivata.heading('Kalite', text="Kalite", anchor=W)
    treecivata.heading('DIN Formu', text="DIN Formu", anchor=W)
    treecivata.heading('Kaplama', text="Kaplama", anchor=W)
    treecivata.heading('Cap', text="Cap", anchor=W)
    treecivata.heading('Boy', text="Boy", anchor=W)
    treecivata.heading('Adet', text="Adet", anchor=W)
    treecivata.heading('Raf', text="Raf", anchor=W)
    treecivata.heading('Dokum NO', text="Dokum NO", anchor=W)
    treecivata.heading('Iz NO', text="Iz NO", anchor=W)
    treecivata.heading('NOT', text="NOT", anchor=W)

    treecivata.column('#0', stretch=NO, minwidth=0, width=0)
    treecivata.column('#1', stretch=NO, minwidth=0)
    treecivata.column('#2', stretch=NO, minwidth=0)
    treecivata.column('#3', stretch=NO, minwidth=0)
    treecivata.column('#4', stretch=NO, minwidth=0)
    treecivata.column('#5', stretch=NO, minwidth=0)
    treecivata.column('#6', stretch=NO, minwidth=0)
    treecivata.column('#7', stretch=NO, minwidth=0)
    treecivata.column('#8', stretch=NO, minwidth=0)
    treecivata.column('#9', stretch=NO, minwidth=0)
    treecivata.column('#10', stretch=NO, minwidth=0)

    treecivata.pack()
    DisplayDataCivata()


def DisplayDataSaplama():
    fp1 = pd.read_excel("envanter.xlsm", "saplama", na_filter=False)
    fp = fp1[1:]
    # df1 = pd.read_excel(fp, 'Sheet1')
    for _ in range(len(fp.index.values)):
        treesaplama.insert('', 'end', value=tuple(fp.iloc[_, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]].values))


def DisplayDataSomun():
    fp1 = pd.read_excel("envanter.xlsm", "somun", na_filter=False)
    fp = fp1[1:]
    for _ in range(len(fp.index.values)):
        treesomun.insert('', 'end', value=tuple(fp.iloc[_, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]].values))


def DisplayDataCivata():
    fp1 = pd.read_excel("envanter.xlsm", "civata", na_filter=False)
    fp = fp1[1:]
    # df1 = pd.read_excel(fp, 'Sheet1')
    for _ in range(len(fp.index.values)):
        treecivata.insert('', 'end', value=tuple(fp.iloc[_, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]].values))


# def Search():


# def Reset():

def ShowViewSaplama():
    global viewform3
    viewform3 = Toplevel()
    viewform3.title("Yeni Satış Bilgisi Girişi")
    width = 900
    height = 600
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform3.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform3.resizable(0, 0)
    img = tk.PhotoImage(file='gif1.gif')
    viewform3.tk.call('wm', 'iconphoto', viewform3._w, img)
    ViewFormSaplama()


def ShowViewCivata():
    global viewform2
    viewform2 = Toplevel()
    viewform2.title("Simple Inventory System/View Productasdsadsa")
    width = 900
    height = 600
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform2.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform2.resizable(0, 0)
    img = tk.PhotoImage(file='gif1.gif')
    viewform2.tk.call('wm', 'iconphoto', viewform2._w, img)

    ViewFormCivata()


def ShowViewSomun():
    global viewform
    viewform = Toplevel()
    viewform.title("Somun Bilgileri")
    width = 1000
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    img = tk.PhotoImage(file='gif1.gif')
    viewform.tk.call('wm', 'iconphoto', viewform._w, img)
    ViewFormSomun()


def showing():
    lb = Button(Home, text="SOMUN", font=('arial', 25), bd=10, command=ShowViewSomun, activebackground="green",
                relief="ridge")
    lb.place(x=100, y=250)

    lb = Button(Home, text="CIVATA", font=('arial', 25), bd=10, command=ShowViewCivata, activebackground="green",
                relief="ridge")
    lb.place(x=100, y=350)

    lb = Button(Home, text="SAPLAMA", font=('arial', 25), bd=10, command=ShowViewSaplama, activebackground="green",
                relief="ridge")
    lb.place(x=100, y=450)


def ViewFormSaplama():
    global treesaplama
    TopViewForm = Frame(viewform3, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform3, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform3, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products", font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('arial', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", )
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", )
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", )
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    treesaplama = ttk.Treeview(MidViewForm, columns=(
    "Stok Kodu", "Kalite", "DIN Formu", "Kaplama", "Cap", "Boy", "Adet", 'Raf', "Dokum NO", "Iz NO", "NOT"),
                               selectmode="extended", height=100, yscrollcommand=scrollbary.set,
                               xscrollcommand=scrollbarx.set)
    scrollbary.config(command=treesaplama.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=treesaplama.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    treesaplama.heading("Stok Kodu", text="Stok Kodu", anchor=W)
    treesaplama.heading('Kalite', text="Kalite", anchor=W)
    treesaplama.heading('DIN Formu', text="DIN Formu", anchor=W)
    treesaplama.heading('Kaplama', text="Kaplama", anchor=W)
    treesaplama.heading('Cap', text="Cap", anchor=W)
    treesaplama.heading('Boy', text="Boy", anchor=W)
    treesaplama.heading('Adet', text="Adet", anchor=W)
    treesaplama.heading('Raf', text="Raf", anchor=W)
    treesaplama.heading('Dokum NO', text="Dokum NO", anchor=W)
    treesaplama.heading('Iz NO', text="Iz NO", anchor=W)
    treesaplama.heading('NOT', text="NOT", anchor=W)

    treesaplama.column('#0', stretch=NO, minwidth=0, width=0)
    treesaplama.column('#1', stretch=NO, minwidth=0, width=0)
    treesaplama.column('#2', stretch=NO, minwidth=0, width=200)
    treesaplama.column('#3', stretch=NO, minwidth=0, width=120)
    treesaplama.column('#4', stretch=NO, minwidth=0, width=120)
    treesaplama.column('#5', stretch=NO, minwidth=0, width=120)
    treesaplama.column('#6', stretch=NO, minwidth=0, width=120)
    treesaplama.column('#7', stretch=NO, minwidth=0, width=120)
    treesaplama.column('#8', stretch=NO, minwidth=0, width=120)
    treesaplama.column('#9', stretch=NO, minwidth=0, width=120)
    treesaplama.column('#10', stretch=NO, minwidth=0, width=120)

    treesaplama.pack()
    DisplayDataSaplama()


def Logout():
    result = tkMessageBox.askquestion('Çelik Metal San.Paz. ve Dış Tic.Ltd.Şti', 'Emin misiniz ?', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()


def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Boş alanları doldurun !", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")

            ShowHome()


        else:
            lbl_result.config(text="Kullanıcı adı veya parola yanlış !", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Giriş Yap", command=ShowLoginForm)
filemenu.add_command(label="Programı Kapat", command=Exit)
menubar.add_cascade(label="Menü", menu=filemenu)
filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_command(label="Envanteri Aç", command=openexcel)
filemenu2.add_command(label="ABC Analizi", command=abc_analizi)
menubar.add_cascade(label="Envanter", menu=filemenu2)
#img = Image.open("login.png")
#imm2 = img.resize((20, 20), Image.ANTIALIAS)
#eimg = ImageTk.PhotoImage(imm2)
filemenu3 = Menu(menubar, tearoff=0)
filemenu3.add_command(label="Üretim Emirleri", command=ShowView)
filemenu3.add_command(label="Üretim Planı", command=uretim_plani)#image=eimg)

menubar.add_cascade(label="Üretim", menu=filemenu3)

root.config(menu=menubar)

# ========================================FRAME============================================
frame3 = Frame(root, width=600, height=100, bg="black", bd=1, relief=SOLID)
frame3.pack(side=TOP, pady=20)

lbl_text3 = Label(frame3, text="Envanter Yönetim Sistemi", font=('arial', 30), fg="white", bg="black", width=600)
lbl_text3.pack(fill=X)

#canvas = Canvas(root, bg="gray25", width=700, height=600, highlightthickness=0)
#canvas.pack(pady=50)

#image = Image.open("celik7.png")
#resize_image = image.resize((400, 400))

#background = ImageTk.PhotoImage(resize_image)
#canvas.create_image(350, 200, image=background)
canvas3= tk.Canvas(root, bg="gray25", width=700, height=600, highlightthickness=0)
canvas3.pack(pady=20)
photo3 = tk.PhotoImage(file='celik7.png')
canvas3.create_image(350, 200, image=photo3)

# ========================================LABEL WIDGET=====================================


# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()



