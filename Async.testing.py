import tkinter
import time
import _thread
import obd
import time
import math




FONT_title = ('Helvetica', 16)
FONT_data = ('Helvetica', 22)


#Change these so the pod has the correct info in it for what you are displaying.
#Gauge1 - Left side Bottom
Gauge1String = 'MAP'
#Gauge2 - Right Side Top
Gauge2String = 'IAT'
#Gauge3 - Right Side Middle
Gauge3String = 'Timing'
#Gauge4 - Right Side Bottom
Gauge4String = 'TPS'



connection = obd.Async()
connection.watch(obd.commands.RPM)
connection.watch(obd.commands.COOLANT_TEMP)
connection.watch(obd.commands.SPEED)
connection.watch(obd.commands.FUEL_LEVEL)
connection.watch(obd.commands.INTAKE_PRESSURE)
connection.watch(obd.commands.INTAKE_TEMP)
connection.watch(obd.commands.TIMING_ADVANCE)
connection.watch(obd.commands.THROTTLE_POS)
connection.start()
class Menu:

    def __init__(self):    
        #Main window initialization
        self.main_window = tkinter.Tk()
        self.main_window.title("Dashboard Gauge Cluster")
        self.main_window.geometry("800x480")
        #Frames
        self.frame_2 = tkinter.Frame(self.main_window, bg='white') # Receiving DATAs
        #ReceiveLabel
        self.ReceiveLabel = tkinter.Label(self.frame_2,\
                                       text = '',\
                                       bg = 'White',\
                                       height = 2, width = 20)


        #RPM label creation
        self.GetRPMLabel = tkinter.Label(self.frame_2,text='RPM', bg = 'light gray', font = FONT_title)
        self.RPMValue = tkinter.StringVar()
        self.GetRPMValueLabel = tkinter.Label(self.frame_2,bg = 'light gray',
                                               textvariable = self.RPMValue,font = FONT_data)
        
        #Coolant label creation                                 
        self.GetCoolantTempLabel = tkinter.Label(self.frame_2,text='Coolant', bg = 'white', font = FONT_title)
        self.CoolantTempValue = tkinter.StringVar()
        self.GetCoolantTempValueLabel = tkinter.Label(self.frame_2, bg = 'blue', font = FONT_data,
                                               textvariable = self.CoolantTempValue)

        #VehicleSpeed Label creation
        self.GetSpeedLabel = tkinter.Label(self.frame_2,text='MPH', bg = 'light gray', font = FONT_title)
        self.SpeedValue = tkinter.StringVar()
        self.GetSpeedValueLabel = tkinter.Label(self.frame_2, bg = 'light gray', font = FONT_data,
                                               textvariable = self.SpeedValue)

        #Fuel Level
        self.GetFuelLevelLabel = tkinter.Label(self.frame_2,text='Fuel Level', bg = 'white', font = FONT_title)
        self.FuelLevelValue = tkinter.StringVar()
        self.GetFuelLevelValueLabel = tkinter.Label(self.frame_2, bg = 'light gray', font = FONT_data,
                                               textvariable = self.FuelLevelValue)

        #Gauge creation below is generic for ease of changing out what values are in them.
        #Guage 1 - 
        self.GetGauge1Label = tkinter.Label(self.frame_2,text= Gauge1String, bg = 'white', font = FONT_title)
        self.Gauge1Value = tkinter.StringVar()
        self.GetGauge1ValueLabel = tkinter.Label(self.frame_2, bg = 'light gray', font = FONT_data,
                                               textvariable = self.Gauge1Value)
        #Guage 2 - 
        self.GetGauge2Label = tkinter.Label(self.frame_2,text= Gauge2String, bg = 'white', font = FONT_title)
        self.Gauge2Value = tkinter.StringVar()
        self.GetGauge2ValueLabel = tkinter.Label(self.frame_2, bg = 'light gray', font = FONT_data,
                                               textvariable = self.Gauge2Value)
        #Guage 3 - 
        self.GetGauge3Label = tkinter.Label(self.frame_2,text= Gauge3String, bg = 'white', font = FONT_title)
        self.Gauge3Value = tkinter.StringVar()
        self.GetGauge3ValueLabel = tkinter.Label(self.frame_2, bg = 'light gray', font = FONT_data,
                                               textvariable = self.Gauge3Value)
        #Guage 4 - 
        self.GetGauge4Label = tkinter.Label(self.frame_2,text= Gauge4String, bg = 'white', font = FONT_title)
        self.Gauge4Value = tkinter.StringVar()
        self.GetGauge4ValueLabel = tkinter.Label(self.frame_2, bg = 'light gray', font = FONT_data,
                                               textvariable = self.Gauge4Value)
        

        #PACKING!!! F2
        self.frame_2.pack()
        self.frame_2.place(x=0, y=0, height=800, width=800)
        #ReceiveLabel
        self.ReceiveLabel.pack()
        self.ReceiveLabel.place(x=320, y=0)

        #RPM place label
        self.GetRPMLabel.pack()
        self.GetRPMLabel.place(x=320, y=20, height=20, width=160)
        self.GetRPMValueLabel.pack()
        self.GetRPMValueLabel.place(x=320, y=40, height=140, width=160)

        #VehicleSpeed Place Label
        self.GetSpeedLabel.pack()
        self.GetSpeedLabel.place(x=320, y=220, height=20, width=160)
        self.GetSpeedValueLabel.pack()
        self.GetSpeedValueLabel.place(x=320, y=240, height=140, width=160)

        #Coolant place label
        self.GetCoolantTempLabel.pack()
        self.GetCoolantTempLabel.place(x=0, y=0, height=20, width=160)
        self.GetCoolantTempValueLabel.pack()
        self.GetCoolantTempValueLabel.place(x=0, y=20, height=140, width=160)
        
        #Fuel Level Place Label
        self.GetFuelLevelLabel.pack()
        self.GetFuelLevelLabel.place(x=0, y=165, height=20, width=160)
        self.GetFuelLevelValueLabel.pack()
        self.GetFuelLevelValueLabel.place(x=0, y=185, height=140, width=160)


        #Gauge 1 Place Label - left side, bottom
        self.GetGauge1Label.pack()
        self.GetGauge1Label.place(x=0, y=325, height=20, width=160)
        self.GetGauge1ValueLabel.pack()
        self.GetGauge1ValueLabel.place(x=0, y=345, height=140, width=160)

        #Gauge 2 Place Label - right side top
        self.GetGauge2Label.pack()
        self.GetGauge2Label.place(x=640, y=0, height=20, width=160)
        self.GetGauge2ValueLabel.pack()
        self.GetGauge2ValueLabel.place(x=640, y=20, height=140, width=160)

        #Gauge 3 Place Label - right side middle
        self.GetGauge3Label.pack()
        self.GetGauge3Label.place(x=640, y=160, height=25, width=160)
        self.GetGauge3ValueLabel.pack()
        self.GetGauge3ValueLabel.place(x=640, y=185, height=140, width=160)

        #Gauge 4 Place Label - right side bottom
        self.GetGauge4Label.pack()
        self.GetGauge4Label.place(x=640, y=325, height=20, width=160)
        self.GetGauge4ValueLabel.pack()
        self.GetGauge4ValueLabel.place(x=640, y=345, height=140, width=160)


        #main loop and quit
        self.quitButton = tkinter.Button(self.main_window,\
                                          text = 'Quit',
                                          command = self.main_window.destroy,\
                                          height = 2, width = 6)
        self.quitButton.pack() 
        self.quitButton.place(x=500, y=240)


        self.main_window.after(2000, _thread.start_new_thread, self.GetData, ())
        tkinter.mainloop()

    def GetData(self):

        while(1):
            #Get RPM Value from OBD and convert to string
            RPMvalue = connection.query(obd.commands.RPM).value
            self.RPMValue.set(str(RPMvalue))

            #Get coolant value from obd and convert to string
            Coolantvalue = connection.query(obd.commands.COOLANT_TEMP).value
            Coolantint = int(Coolantvalue)#variable used to change bacckground color
            self.CoolantTempValue.set(str(Coolantvalue))
            #Change coolant widget background depending on temp
            if Coolantint < 65:
                ColorString = 'blue'
                self.GetCoolantTempValueLabel.configure(bg = ColorString)
            elif Coolantint >=65 and Coolantint < 105:
                ColorString = 'light gray'
                self.GetCoolantTempValueLabel.configure(bg = ColorString)
            else:
                ColorString = 'red'
                self.GetCoolantTempValueLabel.configure(bg = ColorString)

            #Get vehicle speed and convert to string
            Speedvalue = math.floor(connection.query(obd.commands.SPEED).value * .621371)
            self.SpeedValue.set(str(Speedvalue))

            #Get Fuel Level
            FuelLevelvalue = math.floor(connection.query(obd.commands.FUEL_LEVEL).value)
            self.FuelLevelValue.set(str(FuelLevelvalue))

            #Get Gauge 1 - bottome of the left side
            Gauge1 = connection.query(obd.commands.INTAKE_PRESSURE).value #Change this query to get collect different piece of info if desired
            Gauge1value = Gauge1
            self.Gauge1Value.set(str(Gauge1value))

            #Get Gauge 2 - top of the right side
            Gauge2 = connection.query(obd.commands.INTAKE_TEMP).value #Change this query to get collect different piece of info if desired
            Gauge2value = Gauge2
            self.Gauge2Value.set(str(Gauge2value))

            #Get Gauge 3 - middle of right side
            Gauge3 = connection.query(obd.commands.TIMING_ADVANCE).value #Change this query to get collect different piece of info if desired
            Gauge3value = Gauge3
            self.Gauge3Value.set(str(Gauge3value))

            #Get Gauge 4 - bottom of right side
            Gauge4 = connection.query(obd.commands.THROTTLE_POS).value #Change this query to get collect different piece of info if desired
            Gauge4value = math.floor(Gauge4)
            self.Gauge4Value.set(str(Gauge4value))

            time.sleep(0.25)#time delay

           

gui = Menu()
