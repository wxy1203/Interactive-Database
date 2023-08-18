import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd


def search_material():
    search_name = name_entry.get()

    if not search_name:
        messagebox.showinfo("Error", "Please enter a material name to search.")
        return

    file_path = "Carbon Emission Factor Database.xlsx"

    try:
        xls = pd.ExcelFile(file_path)
        sheet_names = xls.sheet_names

        found_in_sheets = []
        found_data = []

        for sheet_name in sheet_names:
            df = pd.read_excel(file_path, sheet_name)
            matching_rows = df[df.iloc[:, 0].str.contains(search_name)]
            if not matching_rows.empty:
                found_in_sheets.append(sheet_name)
                found_data.append(matching_rows)  # Get the first matching row
                # cef = found_data[1]

        # if found_in_sheets:
        #     message = f"材料 '{search_name}' 隶属于: {', '.join(found_in_sheets)} 类型, 该材料碳排放因子数值为"
        #     for idx, data in enumerate(found_data):
        #         # message += f"Sheet: {found_in_sheets[idx]}\n"
        #         # message += f"{data.to_string(index=False)}\n\n"
        #         message += f"{str(data[1])} {data[2]} \n"
        # else:
        #     message = f"Material '{search_name}' not found in any sheets."

        # messagebox.showinfo("Search Result", message)

        # if found_in_sheets:
        #     result_window = tk.Toplevel(window)
        #     result_window.title("Search Result")
        #
        #     result_text = tk.Text(result_window, wrap=tk.WORD)
        #     result_text.pack(padx=10, pady=10)
        #
        #     for idx, data in enumerate(found_data):
        #         result_text.insert(tk.END, f"Sheet: {found_in_sheets[idx]}\n")
        #         result_text.insert(tk.END, f"{data.to_string(index=False)}\n\n")
        # else:
        #     messagebox.showinfo("Search Result", f"Material '{search_name}' not found in any sheets.")

        if found_in_sheets:
            result_window = tk.Toplevel(window)
            result_window.title("Search Result")

            paned_window = tk.PanedWindow(result_window, orient=tk.VERTICAL)
            paned_window.pack(fill=tk.BOTH, expand=True)

            result_text = tk.Text(paned_window, wrap=tk.WORD)
            paned_window.add(result_text)

            scrollbar = tk.Scrollbar(paned_window, command=result_text.yview)
            result_text.configure(yscrollcommand=scrollbar.set)
            paned_window.add(scrollbar)

            for idx, data in enumerate(found_data):
                result_text.insert(tk.END, f"Sheet: {found_in_sheets[idx]}\n")

                # Slice the DataFrame to include only the first 13 columns
                sliced_data = data.iloc[:, :8]

                # Add headers and format the data columns
                headers = sliced_data.columns.to_list()[:13]
                formatted_headers = " ".join("{:<20}".format(header) for header in headers)

                formatted_data = "\n".join(
                    [" ".join("{:<20}".format(str(item)) for item in row) for row in sliced_data.values])

                # result_text.insert(tk.END, formatted_headers + "\n")
                # result_text.insert(tk.END, formatted_data + "\n\n")

                result_text.tag_configure("center", justify='center')  # Create a tag for center-aligned text
                result_text.insert(tk.END, formatted_headers + "\n", "center")
                result_text.insert(tk.END, formatted_data + "\n\n", "center")

                # Adjust line height for the current row
                line_height = 10  # Set the line height value as needed
                result_text.tag_add("line_height", "insert-1c", "end")
                result_text.tag_config("line_height", lmargin1=10, lmargin2=10, spacing3=line_height)
        else:
            messagebox.showinfo("Search Result", f"Material '{search_name}' not found in any sheets.")

        # if found_in_sheets:
        #     result_window = tk.Toplevel(window)
        #     result_window.title("Search Result")
        #
        #     paned_window = tk.PanedWindow(result_window, orient=tk.VERTICAL)
        #     paned_window.pack(fill=tk.BOTH, expand=True)
        #
        #     result_text = tk.Text(paned_window, wrap=tk.WORD, spacing2=10)  # Adjust spacing2 as needed
        #     paned_window.add(result_text)
        #
        #     scrollbar = tk.Scrollbar(paned_window, command=result_text.yview)
        #     result_text.configure(yscrollcommand=scrollbar.set)
        #     paned_window.add(scrollbar)
        #
        #     for idx, data in enumerate(found_data):
        #         result_text.insert(tk.END, f"Sheet: {found_in_sheets[idx]}\n")
        #
        #         # Slice the DataFrame to include only the first 13 columns
        #         sliced_data = data.iloc[:, :13]
        #
        #         # Add headers and format the data columns
        #         headers = sliced_data.columns.to_list()[:13]
        #         formatted_headers = "  ".join("{:<25}".format(header) for header in headers)
        #
        #         formatted_data = "\n".join(
        #             ["  ".join("{:<25}".format(str(item)) for item in row) for row in sliced_data.values])
        #
        #         result_text.tag_configure("center", justify='center')  # Create a tag for center-aligned text
        #         result_text.insert(tk.END, formatted_headers + "\n", "center")
        #         result_text.insert(tk.END, formatted_data + "\n\n", "center")
        #
        # else:
        #     messagebox.showinfo("Search Result", f"Material '{search_name}' not found in any sheets.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


window = tk.Tk()
window.title("碳排放因子数据库 Carbon Emission Factor Database")

frame = tk.Frame(window)
frame.pack()

cef_info_frame = tk.LabelFrame(frame, text="碳排放因子信息 Carbon Emission Factor Information")
cef_info_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

name_label = tk.Label(cef_info_frame, text="材料名称 Material Name")
name_label.grid(row=0, column=0)
# class_label = tkinter.Label(cef_info_frame, text="材料类型 Material Class")
# class_label.grid(row=0, column=1)

name_entry = tk.Entry(cef_info_frame)
name_entry.grid(row=1, column=0)
# class_entry = tkinter.Entry(cef_info_frame)
# class_entry.grid(row=1, column=1)

class_label = tk.Label(cef_info_frame, text="材料类型 Material Class")
class_combobox = ttk.Combobox(cef_info_frame, values=["", "能源(Energy Sources)", "建筑材料(Building Materials)",
                                                      "建材运输(Material Transportation)", "碳汇(Carbon Sink)"])
class_label.grid(row=0, column=1)
class_combobox.grid(row=1, column=1)

sec_class_label = tk.Label(cef_info_frame, text="细分类型 Secondary Class")
sec_class_combobox = ttk.Combobox(cef_info_frame, values=["", "化学原料及化学制品", "保温材料", "光伏设备及元器件", "其他金属"])
sec_class_label.grid(row=0, column=2)
sec_class_combobox.grid(row=1, column=2)

cef_label = tk.Label(cef_info_frame, text="碳排放因子 Carbon Emission Factor")
cef_spinbox = tk.Spinbox(cef_info_frame, from_=0, to=5000)
cef_label.grid(row=2, column=0)
cef_spinbox.grid(row=3, column=0)

unit_label = tk.Label(cef_info_frame, text="单位 Unit")
unit_combobox = ttk.Combobox(cef_info_frame, values=["kg CO2/KW*h", "kg CO2/kg", "kg CO2/m3", "kg CO2e/t", "kgCO2-eq/piece", "kg CO2e/m2", "t CO2-eq/ t"])
unit_label.grid(row=2, column=1)
unit_combobox.grid(row=3, column=1)

for widget in cef_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

material_frame = tk.LabelFrame(frame)
material_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(material_frame, text="登记记录 Registration Status")

reg_status_var = tk.StringVar(value="未登记 Not Registered")
registered_check = tk.Checkbutton(material_frame, text="是否登记 Currently Registered",
                                  variable=reg_status_var, onvalue="已登记 Registered", offvalue="未登记 Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

year_label = tk.Label(material_frame, text="年份 Year")
year_spinbox = tk.Spinbox(material_frame, from_=0, to=5000)
year_label.grid(row=0, column=1)
year_spinbox.grid(row=1, column=1)

nummaterial_label = tk.Label(material_frame, text= "同类型数量 # Same Material")
nummaterial_spinbox = tk.Spinbox(material_frame, from_=0, to=5000)
nummaterial_label.grid(row=0, column=2)
nummaterial_spinbox.grid(row=1, column=2)

for widget in material_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frame = tk.LabelFrame(frame, text="条款与条件 Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="不接受 Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text= "接受条款与条件 I accept the terms and conditions.",
                             variable=accept_var, onvalue="接受 Accepted", offvalue="不接受 Not Accepted")
terms_check.grid(row=0, column=0)


search_button = tk.Button(frame, text="搜索材料 Search Material", command=search_material)
search_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
