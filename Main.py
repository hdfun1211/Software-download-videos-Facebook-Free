import os
import subprocess
import tkinter as tk
from tkinter import ttk
import threading
import time
from tkinter import messagebox
from random import randint
import random
import os
import time
import subprocess
import math
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
import codecs
import html
# Tạo cửa sổ giao diện
root = tk.Tk()
root.title("AUTO DOWNLOAD FACEBOOK V1.0 - Linda2703 - Zalo: 0906070291 - Telegram: @nguyencuong2703")
root.geometry('800x500')
# Hàm xử lý sự kiện khi chọn một mục từ Combobox
def selected_item(event):
    selected_value.set(combo_box.get())
# Biến lưu giá trị được chọn
selected_value = tk.StringVar()

# Hàm xử lý sự kiện khi giá trị của biến thay đổi
def update_label():
    global my_variable
    while True:
        my_variable += 1
        label.config(text=f"Giá trị của biến: {my_variable}")
        time.sleep(1)  # Chờ 1 giây trước khi cập nhật lại giá trị
def Show_scaned():
    with open(r"Da_login.txt", 'r') as fp:
        x = len(fp.readlines())
    with open(r"ok_mail.txt", 'r') as fp:
        ok = len(fp.readlines())
    with open(r"user.txt", 'r') as fp:
        total = len(fp.readlines())
    messagebox.showinfo('Kết quả', f' Chưa check: {total-x}\n Đã check: {x}\n Thành công: {ok} - (ok_mail.txt)')

def save_text():
    user_pass = data.get("1.0", tk.END)  # Lấy toàn bộ nội dung trong Textbox
    pr = proxy.get("1.0", tk.END)  # Lấy toàn bộ nội dung trong Textbox

    if(len(user_pass)<10):
        messagebox.showinfo('Thông báo', f'Chưa điền Data List!')
    elif (len(pr)<10):
        messagebox.showinfo('Thông báo', f'Chưa điền Proxy List!')
    else:    
        # trộn data
        d1=user_pass.split("\n")
        p1=pr.split("\n")
        dem=1
        with open('user.txt', 'w') as the_file:
            for u in range(0,len(d1)-1):
                if dem> len(p1)-2:
                    dem=1
                for k in range(dem,dem+1):
                   # ghi vào file user
                    the_file.write(f'{u}_{k}:{p1[k]}:{d1[u]}\n')
                    dem=dem+1
                
        messagebox.showinfo('Kết quả', f'OK')    

def open_notepad_with_file():
    file_path = "ok_mail.txt"  # Thay thế bằng đường dẫn thực tế của tệp tin
    subprocess.Popen(["notepad.exe", file_path])

        
def run():
    luong=combo_box.get()
    link_page = data.get("1.0", tk.END)  # Lấy toàn bộ nội dung trong Textbox
    add_text = proxy.get("1.0", tk.END)  # Lấy toàn bộ nội dung trong Textbox
    if (len(luong)>0 and len(link_page)>1 and len(add_text)>1):
        messagebox.showinfo('Thông báo', f'Bạn đã chọn '+luong)
        Link_video_page=link_page.split("\n")

        for l in range(0,len(Link_video_page)-1):
            # check link đưa vào download
            vi_tri = Link_video_page[l].find('/videos/')
            if vi_tri == -1:
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                #chrome_options.add_argument("user-data-dir="+current_path+"/profile")
                chrome_options.add_argument('--start-maximized')
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(Link_video_page[l])
                time.sleep(5)
                # Bỏ đăng nhập
                try:
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div').click()
                except:
                    print ("")
                # cuộn từ đầu trang tới cuối trang
                for p in range(1,2):
                    try:
                        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
                        time.sleep(1)
                    except:
                        print ('Hết trang!')

                time.sleep(5)

                # lấy vùng chỉ có video
                for pp in range(2,5):
                    try:
                        scroll = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div['+str(pp)+']')
                        nd=scroll.get_attribute("innerHTML")
                        break
                    except:
                        print ("Tray again!")
                idvideo=nd.split('/videos/')
                trung=""
                for v in idvideo:
                    #try:
                    idvideo=v.split('/')
                    #print ("ID video: "+idvideo[0])
                    if(trung !=idvideo[1] and len(idvideo[1])>5 and len(idvideo[1])< 50):
                        print (idvideo[1])
                        trung =idvideo[1]
                        link_video="https://www.facebook.com/watch/?v="+idvideo[1]
                        driver.get(link_video)
                        time.sleep(2)
                        # Bỏ qua cảnh báo đăng nhập
                        try:
                            driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div').click()
                        except:
                            print ("")
                        time.sleep(5)
                        md = html.unescape(driver.page_source)
                        chatluong=md.split('FBQualityLabel')
                        print("Số format: "+str(len(chatluong)))
                        link_dl=""
                        link_format=""
                        tg=0
                        for i in range(1,len(chatluong)):
                        
                            #console.log(chatluong[i]+"++++++++++++++++++++++++++++++")
                            format=chatluong[i].split('"')
                            format=format[1].split('\\')
                            format=format[0].replace('p','')
                            linkf=chatluong[i].split('BaseURL>')
                            linkf=linkf[1].split('\\u003C\\')
                            linkf=linkf[0].replace('\\','')
                            #linkf=linkf.replaceAll('\\','')

                            if tg < int(format):
                                tg=int(format)
                                link_format=format
                                video_url=linkf

                        print(link_format)		
                        print(video_url)
                        text_to_add = add_text
                        output_video = current_path+"/video/"+idvideo[1]+".mp4"
                        # Run ffmpeg command to add text to the video
                        ffmpeg_cmd = [
                            'ffmpeg',
                            '-i', video_url,
                            '-vf', f"drawtext=text='{text_to_add}':fontfile=/path/to/font.ttf:fontsize=24:fontcolor=white:x=(w-text_w)/2:y=h-150",
                            '-c:a', 'copy',
                            output_video
                        ]

                        subprocess.run(ffmpeg_cmd)
                driver.quit()
            else:
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                #chrome_options.add_argument("user-data-dir="+current_path+"/profile")
                chrome_options.add_argument('--start-maximized')
                driver = webdriver.Chrome(options=chrome_options)
                driver.get(Link_video_page[l])
                idvideo=Link_video_page[l].split('/videos/')
                time.sleep(5)
                # Bỏ qua cảnh báo đăng nhập
                try:
                    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div').click()
                except:
                    print ("")
                time.sleep(5)
                md = html.unescape(driver.page_source)
                chatluong=md.split('FBQualityLabel')
                print("Số format: "+str(len(chatluong)))
                link_dl=""
                link_format=""
                tg=0
                for i in range(1,len(chatluong)):
                
                    #console.log(chatluong[i]+"++++++++++++++++++++++++++++++")
                    format=chatluong[i].split('"')
                    format=format[1].split('\\')
                    format=format[0].replace('p','')
                    linkf=chatluong[i].split('BaseURL>')
                    linkf=linkf[1].split('\\u003C\\')
                    linkf=linkf[0].replace('\\','')
                    #linkf=linkf.replaceAll('\\','')

                    if tg < int(format):
                        tg=int(format)
                        link_format=format
                        video_url=linkf

                print(link_format)		
                print(video_url)
                text_to_add = add_text
                output_video = current_path+"/video/"+idvideo[1]+".mp4"
                # Run ffmpeg command to add text to the video
                ffmpeg_cmd = [
                    'ffmpeg',
                    '-i', video_url,
                    '-vf', f"drawtext=text='{text_to_add}':fontfile=/path/to/font.ttf:fontsize=24:fontcolor=white:x=(w-text_w)/2:y=h-150",
                    '-c:a', 'copy',
                    output_video
                ]

                subprocess.run(ffmpeg_cmd)
                driver.quit()                
    else:
        messagebox.showinfo('Thông báo', f'Chưa thiết lập đầy đủ thông tin!')
        
current_path = os.getcwd()
current_path=current_path.replace("\\","/")

lbl = tk.Label(root, text="Chọn loại Render", font=("Arial Bold", 10))
#Xác định vị trí của label
lbl.place(x=45, y=2)
# Tạo Combobox
combo_box = ttk.Combobox(root, textvariable=selected_value, state="readonly")
combo_box["values"] = ("Add Text", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
combo_box.grid(row=0, column=1)
combo_box.place(x=25, y=25)


'''
update_thread = threading.Thread(target=update_label)
update_thread.daemon = True  # Đặt luồng là daemon để tự động kết thúc khi chương trình chính kết thúc
update_thread.start()
'''
# hiện thị data list

lbl1 = tk.Label(root, text="Page videos List", font=("Arial Bold", 10))
#Xác định vị trí của label
lbl1.place(x=300, y=2)

data = tk.Text(root, width=35, height=25)
data.pack()
data.place(x=200, y=25)

# Hiển thị proxy list

lbl2 = tk.Label(root, text="Text", font=("Arial Bold", 10))
#Xác định vị trí của label
lbl2.place(x=620, y=2)

proxy = tk.Text(root, width=35, height=1)
proxy.pack()
proxy.place(x=500, y=25)




#Gọi hàm chạy tool
btn2 = tk.Button(root, text="Chạy Tool", width = 10, height = 2, bg="Yellow", font=("Times New Roman",13), command=run)
btn2.place(x=45, y=150)

'''
#Gọi hàm trộm data
btn1 = tk.Button(root, text="Trộn Data", width = 10, height = 2, bg="Yellow", font=("Times New Roman",13), command=save_text)
btn1.place(x=45, y=90)

#Gọi hàm xem kết quả
btn2 = tk.Button(root, text="Kết quả", width = 10, height = 2, bg="Yellow", font=("Times New Roman",13), command=Show_scaned)
btn2.place(x=45, y=210)

#Gọi hàm xem kết quả
btn2 = tk.Button(root, text="Mở kết quả", width = 10, height = 2, bg="Yellow", font=("Times New Roman",13), command=open_notepad_with_file)
btn2.place(x=45, y=270)
'''


# Hướng dẫn sử dụng
hd = tk.Label(root, text="Chú ý:", font=("Arial Bold", 10))
#Xác định vị trí của label
hd.place(x=5, y=420)
hd1 = tk.Label(root, text="- Cấu trúc Page videos list : https://www.facebook.com/xxxxx/videos - Mỗi link trên một hàng", font=("Arial Italic", 10))
#Xác định vị trí của label
hd1.place(x=45, y=445)

hd2 = tk.Label(root, text="- Cấu trúc videos list : https://www.facebook.com/xxxxxx/videos/1037963390668808 - Mỗi link trên một hàng", font=("Arial Italic", 10))
#Xác định vị trí của label
hd2.place(x=45, y=465)



# Main loop để chạy ứng dụng
root.mainloop()
