text = []
import tkinter as tk

class TextEditor(tk.Tk):
  
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
  

    self.text = tk.Text(self)
    self.text.pack(fill='both', expand=True)

    self.menu = tk.Menu(self)
    self.config(menu=self.menu)

    file_menu = tk.Menu(self.menu)
    self.menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='Open', command=self.open_file)
    file_menu.add_command(label='Save', command=self.save_file)
    file_menu.add_command(label='Help', command=self.save_file)
    

  def open_file(self):
    file = tk.filedialog.askopenfile(mode='r')
    if file:
      self.text.insert('1.0', file.read())

  def save_file(self):
    file = tk.filedialog.asksaveasfile(mode='w')
    if file:
      file.write(self.text.get('1.0', 'end'))

if __name__ == '__main__':
  app = TextEditor()
  app.mainloop()