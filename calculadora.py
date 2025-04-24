
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