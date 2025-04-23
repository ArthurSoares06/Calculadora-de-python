import tkinter as tk


janela = tk.Tk()
janela.title("Calculadora Top de Linha")
janela.configure(bg="black")
janela.geometry("400x450")  


fonte_padrao = ("Segoe UI", 12)


historico = []


def atualizar_historico():
    historico_text.config(state="normal")
    historico_text.delete("1.0", tk.END)
    ultimas = historico[-5:]  
    for linha in ultimas:
        historico_text.insert(tk.END, linha + "\n")
    historico_text.config(state="disabled")


def calcular(op):
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        if op == "+":
            resultado = n1 + n2
        elif op == "-":
            resultado = n1 - n2
        elif op == "*":
            resultado = n1 * n2
        elif op == "/":
            if n2 == 0:
                resultado_label.config(text="Erro: divisão por zero")
                return
            resultado = n1 / n2
        resultado_texto = f"{n1} {op} {n2} = {round(resultado, 4)}"
        resultado_label.config(text=f"Resultado: {round(resultado, 4)}")
        historico.append(resultado_texto)
        atualizar_historico()
    except ValueError:
        resultado_label.config(text="Erro: entrada inválida!")


label1 = tk.Label(janela, text="Digite o Número 1:", fg="white", bg="black", font=fonte_padrao)
label1.pack(pady=(320, 5))
entrada1 = tk.Entry(janela, font=fonte_padrao, bg="#222", fg="white", insertbackground="white")
entrada1.pack(pady=(0, 10))


label2 = tk.Label(janela, text="Digite o Número fodase:", fg="white", bg="black", font=fonte_padrao)
label2.pack(pady=5)
entrada2 = tk.Entry(janela, font=fonte_padrao, bg="#222", fg="white", insertbackground="white")
entrada2.pack(pady=(0, 10))


frame_botoes = tk.Frame(janela, bg="black")
frame_botoes.pack(pady=15)

estilo_botao = {
    "font": fonte_padrao,
    "width": 5,
    "bg": "#8c52ff",
    "fg": "#000",
    "activebackground": "#38b6ff",
    "activeforeground": "#000",
    "relief": "flat",
    "bd": 0,
    "highlightthickness": 0,
    "cursor": "hand2",
    "padx": 5,
    "pady": 5
}

tk.Button(frame_botoes, text="+", command=lambda: calcular("+"), **estilo_botao).grid(row=0, column=0, padx=10)
tk.Button(frame_botoes, text="-", command=lambda: calcular("-"), **estilo_botao).grid(row=0, column=1, padx=10)
tk.Button(frame_botoes, text="×", command=lambda: calcular("*"), **estilo_botao).grid(row=0, column=2, padx=10)
tk.Button(frame_botoes, text="÷", command=lambda: calcular("/"), **estilo_botao).grid(row=0, column=3, padx=10)


resultado_label = tk.Label(janela, text="", font=fonte_padrao, fg="#00ffcc", bg="black")
resultado_label.pack(pady=10)


historico_label = tk.Label(janela, text="Histórico (últimos 5):", fg="white", bg="black", font=("Segoe UI", 10, "italic"))
historico_label.pack()


historico_text = tk.Text(janela, height=5, width=40, bg="#111", fg="#38b6ff", font=("Consolas", 10))
historico_text.pack(pady=5)
historico_text.config(state="disabled")  

janela.mainloop()