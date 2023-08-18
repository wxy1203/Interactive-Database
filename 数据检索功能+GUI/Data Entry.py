import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        mname = name_entry.get()
        
        if mname:
            mclass = class_combobox.get()
            msec_class = sec_class_combobox.get()
            
            registration_status = reg_status_var.get()
            nummaterial = nummaterial_spinbox.get()
            year = year_spinbox.get()
            
            print("Material Name: ", mname)
            print("Material Class: ", mclass, "Secondary Class: ", msec_class)
            print("Year: ", year, "# Same Material: ", nummaterial)
            print("Registration status", registration_status)
            print("------------------------------------------")
        else:
            tkinter.messagebox.showwarning(title="Error", message="Material's name is required.")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

window = tkinter.Tk()
window.title("碳排放因子数据库 Carbon Emission Factor Database")

frame = tkinter.Frame(window)
frame.pack()

cef_info_frame = tkinter.LabelFrame(frame, text="碳排放因子信息 Carbon Emission Factor Information")
cef_info_frame.grid(row= 0, column=0, sticky="news",padx = 20, pady=10)

name_label = tkinter.Label(cef_info_frame, text="材料名称 Material Name")
name_label.grid(row=0, column=0)
# class_label = tkinter.Label(cef_info_frame, text="材料类型 Material Class")
# class_label.grid(row=0, column=1)

name_entry = tkinter.Entry(cef_info_frame)
name_entry.grid(row=1, column=0)
# class_entry = tkinter.Entry(cef_info_frame)
# class_entry.grid(row=1, column=1)

class_label = tkinter.Label(cef_info_frame, text="材料类型 Material Class")
class_combobox = ttk.Combobox(cef_info_frame, values=["", "能源(Energy Sources)", "建筑材料(Building Materials)", "建材运输(Material Transportation)", "碳汇(Carbon Sink)"])
class_label.grid(row=0, column=1)
class_combobox.grid(row=1, column=1)

sec_class_label = tkinter.Label(cef_info_frame, text="细分类型 Secondary Class")
sec_class_combobox = ttk.Combobox(cef_info_frame, values=["", "化学原料及化学制品", "保温材料", "光伏设备及元器件", "其他金属"])
sec_class_label.grid(row=0, column=2)
sec_class_combobox.grid(row=1, column=2)

cef_label = tkinter.Label(cef_info_frame, text="碳排放因子 Carbon Emission Factor")
cef_spinbox = tkinter.Spinbox(cef_info_frame, from_=0, to=5000)
cef_label.grid(row=2, column=0)
cef_spinbox.grid(row=3, column=0)

unit_label = tkinter.Label(cef_info_frame, text="单位 Unit")
unit_combobox = ttk.Combobox(cef_info_frame, values=["kg CO2/KW*h", "kg CO2/kg", "kg CO2/m3", "kg CO2e/t", "kgCO2-eq/piece", "kg CO2e/m2", "t CO2-eq/ t"])
unit_label.grid(row=2, column=1)
unit_combobox.grid(row=3, column=1)

for widget in cef_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

material_frame = tkinter.LabelFrame(frame)
material_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(material_frame, text="登记记录 Registration Status")

reg_status_var = tkinter.StringVar(value="未登记 Not Registered")
registered_check = tkinter.Checkbutton(material_frame, text="是否登记 Currently Registered",
                                       variable=reg_status_var, onvalue="已登记 Registered", offvalue="未登记 Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

year_label = tkinter.Label(material_frame, text="年份 Year")
year_spinbox = tkinter.Spinbox(material_frame, from_=0, to=5000)
year_label.grid(row=0, column=1)
year_spinbox.grid(row=1, column=1)

nummaterial_label = tkinter.Label(material_frame, text= "同类型数量 # Same Material")
nummaterial_spinbox = tkinter.Spinbox(material_frame, from_=0, to=5000)
nummaterial_label.grid(row=0, column=2)
nummaterial_spinbox.grid(row=1, column=2)

for widget in material_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tkinter.LabelFrame(frame, text="条款与条件 Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="不接受 Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "接受条款与条件 I accept the terms and conditions.",
                                  variable=accept_var, onvalue="接受 Accepted", offvalue="不接受 Not Accepted")
terms_check.grid(row=0, column=0)

button = tkinter.Button(frame, text="输入数据 Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)
 
window.mainloop()
