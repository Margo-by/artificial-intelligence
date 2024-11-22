from tkinter import ttk, scrolledtext,Toplevel,WORD,Label,Button,END,messagebox
from expert_system import ExpertSystem
from data import conclusion_to_group_of_rules_map

class App:
    def __init__(self, master):
        self.master = master
        self.inference_engine = ExpertSystem()

        master.title("Обратный вывод правил")        
        
        self.label = Label(master, text="Выберите цель для обратного вывода:")
        self.label.pack()
        
        self.values=[list(key) for key, value in conclusion_to_group_of_rules_map.items()]
        self.goal_combobox = ttk.Combobox(master, values=self.values)
        self.goal_combobox.pack()

        
        self.run_button = Button(master, text="Запустить", command=self.run_inference)
        self.run_button.pack()
        
        self.log_button = Button(master, text="Показать лог", command=self.show_log)
        self.log_button.pack()
        
        self.result_text = scrolledtext.ScrolledText(master, width=400, height=100)
        self.result_text.pack()

        self.log_file = None
        
    def run_inference(self):
        selected_index = self.goal_combobox.current()
        if selected_index != -1:  # Проверяем, выбрано ли что-то
            goal = self.values[selected_index]
            result = self.inference_engine.run_system(goal)
            output = f"Для достижения цели '{goal}', необходимо выполнить любую из групп условий:\n"
            output += "\n".join(f"- {premis}" for premis in result)

            # self.result_text.delete(1.0, END)
            self.result_text.insert(END, output)
        else:
            messagebox.showwarning("Внимание", "Выберите цель.")
            
    def show_log(self):
        log_window = Toplevel(self.master)
        log_window.title("Лог вывода")
    
        # Создаем поле для прокручиваемого текста
        log_text = scrolledtext.ScrolledText(log_window, wrap=WORD)
        log_text.pack(expand=True, fill='both')

        self.log_file =open('log1.txt', 'r', encoding='utf-8')
        log_content = self.log_file.read()

        # Вставляем содержимое лог-файла в текстовое поле
        log_text.insert(END, log_content)
    
        # Делаем поле только для чтения
        log_text.configure(state='disabled')
        
    def on_closing(self):
        
        self.log_file.close()
        self.master.destroy()