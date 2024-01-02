from tkinter import *
from tkinter import messagebox
import pytube

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x250")
        self.root.resizable(False, False)
        self.root.title("Загрузчик с YouTube")
        self.root.config(bg='#FF0000')
        
#        self.root.config(bg='#D3D3D3')

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="---Загрузите видео с YouTube---", font=('Arial', 15, 'bold'), bg='#D3D3D3').pack(pady=15)

        Label(self.root, text="Ссылка на видео :", font=('Arial', 15, 'bold'), bg='#D3D3D3').place(x=10, y=80)

        self.link1 = StringVar()
        Entry(self.root, textvariable=self.link1, font=('Arial', 15, 'bold')).place(x=230, y=80)

        Button(self.root, text="Скачать", font=('Arial', 10, 'bold'), bd=4, command=self.download).place(x=330, y=130)
        Button(self.root, text="Очистить", font=('Arial', 10, 'bold'), bd=4, command=self.reset).place(x=160, y=190)
        Button(self.root, text="Выход", font=('Arial', 10, 'bold'), bd=4, command=self.root.destroy).place(x=250, y=190)

    def download(self):
        try:
            ytlink = self.link1.get()
            youtubelink = pytube.YouTube(ytlink)
            video = youtubelink.streams.get_highest_resolution()
            video.download()
            messagebox.showinfo("Готово", "Загрузка завершена")
        except:
            messagebox.showerror("Ошибка", "Недопустимая ссылка")

    def reset(self):
        self.link1.set("")

if __name__ == "__main__":
    root = Tk()
    YouTubeDownloader(root)
    root.mainloop()