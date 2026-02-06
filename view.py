#pour ajouter la fenetre
import tkinter as tk
class CalculatorView:
    def __init__(self,win_view):     
        self.win_view=win_view
        self.win_view.title("MVC Calculatrice CSI")
        self.win_view.configure(bg="#1C292C")
        
        self.entry = tk.Entry(
            win_view,
            font=("Arial",18),
            bg="#1C292C",
            fg="white",
            justify="right",
            relief="flat",
            )
        self.entry.grid(row=0,
                        column=0,
                        columnspan=3,
                        padx=0,
                        pady=0
                        )

        self.buttons=[]

        for i in range (9):
            btn=tk.Button(win_view,
                          text=str(9-i),
                          font=("Verdana",12),
                          bg="#6E7FCE",
                          fg="white",
                          width=5,
                          height=2
                          )
            btn.grid(
                row=i//3 + 2,
                column= i % 3,
                padx=1,
                pady=1,
                sticky="nsew"
            )
            self.buttons.append(btn)

            zero=tk.Button(win_view,
                           text=str(0),
                           font=("Verdana",12),
                           bg="#6E7FCE",
                           fg="white",
                           width=5,
                           height=2
                           )
            zero.grid(row=5,
                      column=1,
                      padx=1,
                      pady=1,
                      sticky="nsew"
                      )
            self.buttons.append(zero)

            virgul=tk.Button(win_view,
                           text=str("."),
                           width=5,
                           height=2
                           )
            virgul.grid(row=5,
                      column=0,
                      padx=1,
                      pady=1,
                      sticky="nsew"
                      )
            self.buttons.append(virgul)

        
        self.clear_btn=tk.Button(win_view,
                                 text="C",
                                 width=5,
                                 height=2
                                 )
        self.clear_btn.grid(row=1,
                            column=0,
                            padx=1,
                            pady=1,
                            sticky="nsew"
                            )
        
        self.delete=tk.Button(
            win_view,
            text="Del",
            bg="#9294AD",
            fg= "white",
            width=2,
            height=2,
            )
        self.delete.grid(
            row=0,
            column=3,
            padx=0,
            pady=0,
            sticky="nsesw"
        )

        self.addition_btn=tk.Button(win_view,
                                    text="+",
                                    bg="#0004FF",
                                    fg="white",
                                    width=5,
                                    height=2
                                    )
        self.addition_btn.grid(row=1,
                               column=3,
                               padx=1,
                               pady=1,
                               sticky="nsew"
                               )
        self.buttons.append(self.addition_btn)

        self.soustraction_btn=tk.Button(win_view,
                                        text="-",
                                        bg="#0004FF",
                                        fg="white",
                                        width=5,
                                        height=2
                                        )
        self.soustraction_btn.grid(row=2,
                                   column=3,
                                   padx=1,
                                   pady=1,
                                   sticky="nsew"
                                   )
        self.buttons.append(self.soustraction_btn)

        self.multiplication_btn=tk.Button(win_view,
                                          text="*",
                                          font=("arial",12),
                                          bg="#0004FF",
                                          fg="white",
                                          width=5,
                                          height=2
                                          )
        self.multiplication_btn.grid(row=3,
                                     column=3,
                                     padx=1,
                                     pady=1,
                                     sticky="nsew"
                                     )
        self.buttons.append(self.multiplication_btn)

        self.division_btn=tk.Button(win_view,
                                    text="/",
                                    bg="#0004FF",
                                    fg="white",
                                    width=5,
                                    height=2
                                    )
        self.division_btn.grid(row=4,
                               column=3,
                               padx=1,
                               pady=1,
                               sticky="nsew"
                               )
        self.buttons.append(self.division_btn)
        
        self.exposant_btn=tk.Button(win_view,
                                    text="^",
                                    width=5,
                                    height=2
                                    )
        self.exposant_btn.grid(row=1,
                               column=1,
                               padx=2,
                               pady=1,
                               sticky="nsew"
                               )
        self.buttons.append(self.exposant_btn)

        self.radical_btn=tk.Button(win_view,
                                   text="√",
                                   width=4,
                                   height=2
                                   )
        self.radical_btn.grid(row=1,
                              column=2,
                              padx=1,
                              pady=1,
                              sticky="nsew"
                              )
        self.buttons.append(self.radical_btn)

        self.egal_btn=tk.Button(win_view,
                                text="=",
                                bg="#05112B",
                                fg="white",
                                width=18,
                                height=2
                                )
        self.egal_btn.grid(row=5,
                           column=2,
                           columnspan= 3,
                           padx=1,
                           pady=1,
                           sticky="nsew"
                           )

    def set_entry(self,value):
        self.entry.delete(0,tk.END)
        self.entry.insert(0,value)
