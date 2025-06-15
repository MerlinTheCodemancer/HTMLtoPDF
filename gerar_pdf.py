"""
Script para converter HTML em PDF (A4), mantendo o estilo do HTML.

🇧🇷 Este script aceita um arquivo HTML ou um código HTML em string e gera um PDF legível, pronto para impressão em A4.
🇺🇸 This script takes an HTML file or HTML string and generates a readable PDF, ready for A4 printing.

Dependência:
    pip install weasyprint

Uso via terminal:
    python gerar_pdf.py --input caminho/para/arquivo.html --output saida.pdf
    python gerar_pdf.py --string "<h1>Olá, mundo!</h1>" --output saida.pdf

"""
from weasyprint import HTML
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
import argparse

def gui_main():
    def selecionar_arquivo():
        caminho = filedialog.askopenfilename(
            title="Selecione o arquivo HTML",
            filetypes=[("Arquivos HTML", "*.html;*.htm"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            entrada_var.set(caminho)

    def selecionar_saida():
        caminho = filedialog.asksaveasfilename(
            title="Salvar PDF como",
            defaultextension=".pdf",
            filetypes=[("PDF", "*.pdf")]
        )
        if caminho:
            saida_var.set(caminho)

    def gerar_pdf_gui():
        entrada = entrada_var.get()
        saida = saida_var.get()
        if not entrada or not saida:
            messagebox.showerror("Erro", "Selecione o arquivo HTML e o caminho do PDF de saída.")
            return
        try:
            # Adiciona CSS para melhor quebra de página A4
            from weasyprint import CSS
            # CSS mínimo: só define tamanho da página e quebras, sem forçar fundo/cor
            css_a4 = CSS(string='''
                @page {
                    size: A4;
                    margin: 0;
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
                html, body {
                    margin: 0 !important;
                    padding: 0 !important;
                }
            ''')
            # Dica: para forçar dark mode, descomente as linhas abaixo
            # css_a4 = CSS(string=css_a4.string + '''
            #     html, body { background: #23272f !important; color: #f4f6fa !important; }
            #     .main-content, .container, .content, #main, #root, .pagina, .pagina-a4 {
            #         background: #181a20 !important; color: #f4f6fa !important;
            #     }
            # ''')
            # Detecta se o fundo do HTML é claro e força dark mode se necessário
            # (Solução simples: sempre força dark mode se o usuário quiser, descomente para ativar)
            # Para forçar dark mode apenas se o fundo for claro, seria necessário analisar o HTML, o que é complexo.
            # Aqui, adicionamos uma opção simples para sempre forçar dark mode se o usuário quiser.
            # Opção: forçar dark ou light mode conforme escolha do usuário
            # Defina 'modo_forcado' como 'dark', 'light' ou None para respeitar o HTML
            modo_forcado = None  # Opções: 'dark', 'light', None
            if modo_forcado == 'dark':
                css_a4 = CSS(string=css_a4.string + '''
                    html, body { background: #23272f !important; color: #f4f6fa !important; }
                    .main-content, .container, .content, #main, #root, .pagina, .pagina-a4 {
                        background: #181a20 !important; color: #f4f6fa !important;
                    }
                ''')
            elif modo_forcado == 'light':
                css_a4 = CSS(string=css_a4.string + '''
                    html, body { background: #fff !important; color: #222 !important; }
                    .main-content, .container, .content, #main, #root, .pagina, .pagina-a4 {
                        background: #fff !important; color: #222 !important;
                    }
                ''')
            HTML(entrada).write_pdf(saida, stylesheets=[css_a4])
            messagebox.showinfo("Sucesso", f"PDF gerado com sucesso: {saida}")
        except Exception as e:
            messagebox.showerror("Erro ao gerar PDF", str(e))

    root = tk.Tk()
    root.title("Gerar PDF a partir de HTML")
    root.geometry("500x270")
    root.configure(bg="#23272f")  # Dark mode
    root.resizable(False, False)

    # Ícone customizado (opcional, precisa de um arquivo .ico na pasta)
    try:
        root.iconbitmap("icon.ico")
    except Exception:
        pass  # Se não houver ícone, ignora

    # Estilo dark mode
    fonte_titulo = ("Segoe UI", 16, "bold")
    fonte_label = ("Segoe UI", 11)
    fonte_btn = ("Segoe UI", 11, "bold")
    cor_btn = "#3b82f6"
    cor_btn_hover = "#2563eb"
    cor_fundo = "#23272f"
    cor_entrada = "#181a20"
    cor_texto = "#f4f6fa"
    cor_btn_gerar = "#22c55e"
    cor_btn_gerar_hover = "#15803d"

    def on_enter(e):
        e.widget['background'] = cor_btn_hover
    def on_leave(e):
        e.widget['background'] = cor_btn

    def on_enter_gerar(e):
        e.widget['background'] = cor_btn_gerar_hover
    def on_leave_gerar(e):
        e.widget['background'] = cor_btn_gerar

    # Variáveis de entrada e saída (devem ser criadas antes de usar nos widgets)
    entrada_var = tk.StringVar()
    saida_var = tk.StringVar()

    tk.Label(root, text="Conversor de HTML para PDF", font=fonte_titulo, bg=cor_fundo, fg=cor_texto).pack(pady=(18, 8))

    tk.Label(root, text="Arquivo HTML:", font=fonte_label, bg=cor_fundo, fg=cor_texto).pack(anchor='w', padx=30, pady=(0,2))
    frame1 = tk.Frame(root, bg=cor_fundo)
    frame1.pack(fill='x', padx=30)
    entrada_entry = tk.Entry(frame1, textvariable=entrada_var, width=38, font=fonte_label, bg=cor_entrada, fg=cor_texto, insertbackground=cor_texto, relief='solid', bd=1)
    entrada_entry.pack(side='left', expand=True, fill='x')
    btn1 = tk.Button(frame1, text="Selecionar", command=selecionar_arquivo, font=fonte_btn, bg=cor_btn, fg="#fff", activebackground=cor_btn_hover, activeforeground="#fff", relief='flat', cursor="hand2")
    btn1.pack(side='left', padx=7)
    btn1.bind("<Enter>", on_enter)
    btn1.bind("<Leave>", on_leave)

    tk.Label(root, text="PDF de saída:", font=fonte_label, bg=cor_fundo, fg=cor_texto).pack(anchor='w', padx=30, pady=(12,2))
    frame2 = tk.Frame(root, bg=cor_fundo)
    frame2.pack(fill='x', padx=30)
    saida_entry = tk.Entry(frame2, textvariable=saida_var, width=38, font=fonte_label, bg=cor_entrada, fg=cor_texto, insertbackground=cor_texto, relief='solid', bd=1)
    saida_entry.pack(side='left', expand=True, fill='x')
    btn2 = tk.Button(frame2, text="Selecionar", command=selecionar_saida, font=fonte_btn, bg=cor_btn, fg="#fff", activebackground=cor_btn_hover, activeforeground="#fff", relief='flat', cursor="hand2")
    btn2.pack(side='left', padx=7)
    btn2.bind("<Enter>", on_enter)
    btn2.bind("<Leave>", on_leave)

    btn_gerar = tk.Button(root, text="Gerar PDF", command=gerar_pdf_gui, font=fonte_btn, bg=cor_btn_gerar, fg="#fff", activebackground=cor_btn_gerar_hover, activeforeground="#fff", relief='flat', cursor="hand2", height=2, width=20)
    btn_gerar.pack(pady=22)
    btn_gerar.bind("<Enter>", on_enter_gerar)
    btn_gerar.bind("<Leave>", on_leave_gerar)

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
                        margin: 0;
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
                    html, body {
                        margin: 0;
                        padding: 0;
                    }
                ''')
                HTML(args.input).write_pdf(args.output, stylesheets=[css_a4])
                print(f'PDF gerado com sucesso a partir do arquivo {args.input}: {args.output}')
            elif args.string:
                from weasyprint import CSS
                css_a4 = CSS(string=''':
                    @page {
                        size: A4;
                        margin: 0;
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
                    html, body {
                        margin: 0;
                        padding: 0;
                    }
                ''')
                HTML(string=args.string).write_pdf(args.output, stylesheets=[css_a4])
                print(f'PDF gerado com sucesso a partir da string HTML: {args.output}')
        except Exception as e:
            print(f'Erro ao gerar PDF: {e}', file=sys.stderr)
            sys.exit(1)
