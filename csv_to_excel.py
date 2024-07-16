"""---"""
import tkinter as tk
from tkinter import filedialog
from pandas import read_csv


class CsvXlsx:

    def __init__(self) -> None:
        # Criando a janela principal
        self._root = tk.Tk()
        self._root.title("Conversor de CSV para XLSX")

        # Adicionando um campo de entrada
        self._entry = tk.Entry(self._root, width=40)
        self._entry.pack(pady=20)

        # Label para resultados
        self._label_result = tk.Label(self._root, text="", font=(20))
        self._label_result.pack(pady=20)


    def procurar_arquivo(self):
        filename = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")])
        self._entry.delete(0, tk.END)
        self._entry.insert(0, filename)


    def convert_to_xlsx(self):
        csv_file = self._entry.get()
        if csv_file:
            try:
                # Lendo o arquivo CSV
                df = read_csv(csv_file)

                # Convertendo para XLSX
                xlsx_file = csv_file.replace('.csv', '.xlsx')

                df.astype(str).to_excel(xlsx_file, index=False)

                self._label_result.config(
                    text="Arquivo convertido com sucesso!",
                    bg='green'
                )
            except Exception as e:
                self._label_result.config(
                    text=f"Erro: {e}",
                    bg='red'
                )
        else:
            self._label_result.config(
                text="Por favor, selecione um arquivo CSV."
            )


    def main(self):

        # Adicionando botões
        browse_button = tk.Button(
            self._root,
            text="Procurar CSV",
            font=(14),
            command=self.procurar_arquivo
        )

        browse_button.pack(
            pady=5
        )

        convert_button = tk.Button(
            self._root,
            text="Converter para XLSX",
            font=(14),
            command=self.convert_to_xlsx
        )
        convert_button.pack(pady=5)

        # Iniciando a janela
        self._root.mainloop()


if __name__ == '__main__':
    app = CsvXlsx()
    app.main()
