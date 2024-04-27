import tkinter as tk


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)


def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.itemconfig(selected_task, bg="medium aquamarine")


bg_clr = "LightSteelBlue2"
bg_clr2 = "ghost white"
bg_txt = "LightSteelBlue1"

root = tk.Tk()
root.title('Task list')
root.configure(background=bg_clr)

text1 = tk.Label(root, text="Введите новую задачу:", width=43, bg=bg_txt)
text1.pack(pady=10, padx=10)

task_entry = tk.Entry(root, width=50, bg=bg_clr2, fg="grey10")
task_entry.pack(pady=5, padx=10)

add_task_btn = tk.Button(root, text="Добавить задачу", command=add_task, width=30)
add_task_btn.pack(pady=5, padx=10)

text2 = tk.Label(root, text="Список задач", width=43, bg=bg_txt)
text2.pack(pady=5, padx=10)

task_listbox = tk.Listbox(root, height=10, width=50, bg=bg_clr2)
task_listbox.pack(pady=5, padx=10)

delete_btn = tk.Button(root, text="Удалить задачу", command=delete_task, width=30)
delete_btn.pack(pady=5, padx=10)

mark_btn = tk.Button(root, text="Отметить выполненную задачу", command=mark_task, width=30)
mark_btn.pack(pady=5, padx=10)

root.mainloop()
