"""
Script para converter HTML em PDF (A4), mantendo o estilo do HTML.

🇧🇷 Este script aceita um arquivo HTML ou um código HTML em string e gera um PDF legível, pronto para impressão em A4.
🇺🇸 This script takes an HTML file or HTML string and generates a readable PDF, ready for A4 printing.

Dependência:
    pip install weasyprint

Uso via terminal:
    python gerar_pdf.py --input caminho/para/arquivo.html --output saida.pdf
    python gerar_pdf.py --string "<h1>Olá, mundo!</h1>" --output saida.pdf

Autor: GitHub Copilot
"""
from weasyprint import HTML
import sys
import tkinter as tk
from tkinter import filedialog, messagebox

def gui_main():
    def selecionar_arquivo():
        caminho = filedialog.askopenfilename(
            title="Selecione o arquivo HTML",
            filetypes=[("Arquivos HTML", "*.html;*.htm"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            entrada_var.set(caminho)

    def gerar_pdf_gui():
        entrada = entrada_var.get()
        saida = saida_var.get()
        if not entrada or not saida:
            messagebox.showerror("Erro", "Selecione o arquivo HTML e o caminho do PDF de saída.")
            return
        try:
            # Adiciona CSS para melhor quebra de página A4
            from weasyprint import CSS
            css_a4 = CSS(string='''
                @page {
                    size: A4;
                    margin: 20mm 15mm 20mm 15mm;
                }
                html, body {
                    width: 100%;
                    height: 100%;
                }
                h1, h2, h3, h4, h5, h6 {
                    page-break-after: avoid;
                    page-break-before: avoid;
                }
                table, pre, blockquote {
                    page-break-inside: avoid;
                }
                p {
                    orphans: 3;
                    widows: 3;
                }
            ''')
            HTML(entrada).write_pdf(saida, stylesheets=[css_a4])
            messagebox.showinfo("Sucesso", f"PDF gerado com sucesso: {saida}")
        except Exception as e:
            messagebox.showerror("Erro ao gerar PDF", str(e))

    root = tk.Tk()
    root.title("Gerar PDF a partir de HTML")
    root.geometry("450x180")

    entrada_var = tk.StringVar()
    saida_var = tk.StringVar()

    tk.Label(root, text="Arquivo HTML:").pack(anchor='w', padx=10, pady=(10,0))
    frame1 = tk.Frame(root)
    frame1.pack(fill='x', padx=10)
    tk.Entry(frame1, textvariable=entrada_var, width=40).pack(side='left', expand=True, fill='x')
    tk.Button(frame1, text="Selecionar", command=selecionar_arquivo).pack(side='left', padx=5)

    tk.Label(root, text="PDF de saída:").pack(anchor='w', padx=10, pady=(10,0))
    frame2 = tk.Frame(root)
    frame2.pack(fill='x', padx=10)
    tk.Entry(frame2, textvariable=saida_var, width=40).pack(side='left', expand=True, fill='x')
    def selecionar_saida():
        caminho = filedialog.asksaveasfilename(
            title="Salvar PDF como",
            defaultextension=".pdf",
            filetypes=[("PDF", "*.pdf")]
        )
        if caminho:
            saida_var.set(caminho)
    tk.Button(frame2, text="Selecionar", command=selecionar_saida).pack(side='left', padx=5)

    tk.Button(root, text="Gerar PDF", command=gerar_pdf_gui, height=2, width=20).pack(pady=15)

    root.mainloop()

if __name__ == "__main__":
    # Só processa argumentos se houver argumentos além do script
    if len(sys.argv) == 1:
        gui_main()
    else:
        parser = argparse.ArgumentParser(description="Converta HTML em PDF (A4), mantendo o estilo do HTML.")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--input', type=str, help='Caminho para o arquivo HTML de entrada')
        group.add_argument('--string', type=str, help='Código HTML em string')
        parser.add_argument('--output', type=str, required=True, help='Caminho para o arquivo PDF de saída')
        args = parser.parse_args()
        try:
            if args.input:
                from weasyprint import CSS
                css_a4 = CSS(string=''':
                    @page {
                        size: A4;
                        margin: 20mm 15mm 20mm 15mm;
                    }
                    html, body {
                        width: 100%;
                        height: 100%;
                    }
                    h1, h2, h3, h4, h5, h6 {
                        page-break-after: avoid;
                        page-break-before: avoid;
                    }
                    table, pre, blockquote {
                        page-break-inside: avoid;
                    }
                    p {
                        orphans: 3;
                        widows: 3;
                    }
                ''')
                HTML(args.input).write_pdf(args.output, stylesheets=[css_a4])
                print(f'PDF gerado com sucesso a partir do arquivo {args.input}: {args.output}')
            elif args.string:
                from weasyprint import CSS
                css_a4 = CSS(string=''':
                    @page {
                        size: A4;
                        margin: 20mm 15mm 20mm 15mm;
                    }
                    html, body {
                        width: 100%;
                        height: 100%;
                    }
                    h1, h2, h3, h4, h5, h6 {
                        page-break-after: avoid;
                        page-break-before: avoid;
                    }
                    table, pre, blockquote {
                        page-break-inside: avoid;
                    }
                    p {
                        orphans: 3;
                        widows: 3;
                    }
                ''')
                HTML(string=args.string).write_pdf(args.output, stylesheets=[css_a4])
                print(f'PDF gerado com sucesso a partir da string HTML: {args.output}')
        except Exception as e:
            print(f'Erro ao gerar PDF: {e}', file=sys.stderr)
            sys.exit(1)
