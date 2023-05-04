
from tkinter import *
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder 
from datetime import datetime 
from tkinter import ttk, messagebox
from pil import Image,ImageTk
import requests 
import pytz

window = Tk()
window.title('Weather App')
window.geometry ('900x500+300+200')
window.config(background="#C6E2FF")
window.resizable(False,False)
window.iconbitmap("weather.ico")

img=Image.open("Weather_1.png")
imgtk=ImageTk.PhotoImage(img)
img = img.resize((50,50), Image.LANCZOS )
label=Label(window,image=imgtk)
label.place(x=550,y=100)

def getWeather(): 
    try:
    
        city=textfield.get()

        geolocartor=Nominatim(user_agent="geoapiExercises")
        location=geolocartor.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time) 
        name.config(text="THỜI TIẾT HIỆN TẠI")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e9a049373acc8f969e38677742eeb388"
        json_data = requests.get(api).json() 
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15) 
        pressure = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        


        t.config(text=(temp,"°"))
        c.config(text=(condition,'|',"FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        d.config(text=description)
        p.config(text=pressure)
    except Exception as e:
        messagebox.showerror("Chú ý!","Thành phố/Đất nước ko hợp lệ")




textfield=Entry(window,justify="center",font=("poppins",28,"bold"),bg="#99FF66",fg="#FF6600",border=0)
textfield.place(x=53,y=20,width=525,height=50) 
textfield.focus()



find_button=Button(window,text="Find",font=("poppins",20,"bold"),cursor="hand2",bg="#99CCFF",fg="#006633",command=getWeather)
find_button.place(x=710,y=20) 

#logo


#Bottom box 

#time
name=Label(window,font = ('Arial',20,'bold'),fg = "#EE7942",bg = "#8EE5EE")
name.place(x=30,y=100)
clock=Label(window,font=("Arial",20,"bold"),fg = "#EE7942",bg = "#8EE5EE")
clock.place(x=30,y=170)


#label
label1=Label(window,text = 'GIÓ', fg = "#8B658B",bg = "#8EE5EE",font = ('Arial',22,'bold'))
label1.place(x=120,y=375)

label3=Label(window,text = 'MÔ TẢ', fg ="#8B658B",bg = "#8EE5EE",font = ('Arial',22,'bold'))
label3.place(x=380,y=375)

label4=Label(window,text = 'ÁP SUẤT', fg ="#8B658B",bg = "#8EE5EE",font = ('Arial',22,'bold'))
label4.place(x=650,y=375)

t=Label(font = ('Arial',22,'bold'),fg = "#EE7942",bg = "#8EE5EE")
t.place(x=400,y=100)
c=Label(font=("Arial",20,"bold"),fg = "#EE7942",bg = "#8EE5EE")
c.place(x=150,y=250)

w=Label(window,text = '...',font = ('Arial',20,'bold'),fg = "#EE7942",bg = "#8EE5EE")
w.place(x=120,y=430)
d=Label(window,text = '...',font = ('Arial',20,'bold'),fg = "#EE7942",bg = "#8EE5EE")
d.place(x=350,y=430)
p=Label(window,text = '...',font = ('Arial',20,'bold'),fg = "#EE7942",bg = "#8EE5EE")
p.place(x=670,y=430)



window.mainloop()
