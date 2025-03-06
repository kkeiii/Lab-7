# import requests
# import tkinter as tk
# from PIL import Image, ImageTk
# from io import BytesIO


# def get_nasa(api_key):
#     url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data.get("url"), data.get("title"), data.get("explanation")
#     return None, None, None


# def update_photo():
#     img_url, title, explanation = get_nasa(API_KEY)
#     if img_url and img_url.endswith(('.jpg', '.png', '.jpeg')):
#         response = requests.get(img_url)
#         img_data = Image.open(BytesIO(response.content))
#         img_data = img_data.resize((600, 400))
#         img = ImageTk.PhotoImage(img_data)
#         label.config(image=img)
#         label.image = img
#         title_label.config(text=title)

# if __name__ == "__main__":
#     API_KEY = "6cgtlfqulaXLdmmt6lcx5IIrEp4KLKH5QoGgTbzB"

#     root = tk.Tk()
#     root.title("NASA Photo of the day")
#     root.geometry("800x600")

#     title_label = tk.Label(root, text="", font=("Times New Roman", 14))
#     title_label.pack(pady=10)

#     label = tk.Label(root)
#     label.pack()

#     buttonn = tk.Button(root, text="Change photo", command=update_photo)
#     buttonn.pack(pady=10)


#     update_photo()

#     root.mainloop()

import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def get_nasa_apod(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("url"), data.get("title")
    return None, None

def update_image():
    img_url, title = get_nasa_apod(API_KEY)
    if img_url and img_url.endswith(('.jpg', '.png', '.jpeg')):
        response = requests.get(img_url)
        img_data = Image.open(BytesIO(response.content))
        img_data = img_data.resize((600, 400))
        img = ImageTk.PhotoImage(img_data)
        label.config(image=img)
        label.image = img
        title_label.config(text=title)

if __name__ == "__main__":
    # Ваш API-ключ NASA (получите на https://api.nasa.gov)
    API_KEY = "6cgtlfqulaXLdmmt6lcx5IIrEp4KLKH5QoGgTbzB"

    # Создание окна
    root = tk.Tk()
    root.title("NASA Фото дня")
    root.geometry("800x600")  # Устанавливаем размер окна

    # Заголовок
    title_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Метка для изображения
    label = tk.Label(root)
    label.pack(pady=10)

    # Кнопка обновления
    btn = tk.Button(root, text="Обновить фото", command=update_image)
    btn.pack(pady=10)

    # Загрузка первой картинки
    update_image()

    # Запуск приложения
    root.mainloop()
