```markdown
# Gerador de PDF a partir de HTML

Este projeto permite converter arquivos HTML ou código HTML em string para PDF em formato A4, mantendo o estilo do HTML. Você pode usar tanto uma interface gráfica simples quanto a linha de comando.

## 🚀 Como Usar

### 1. Instale as dependências

No terminal, execute:
```sh
pip install weasyprint
```

### 2. Modo Gráfico (Recomendado para iniciantes)

Basta rodar:
```sh
python gerar_pdf.py
```
- Uma janela será aberta.
- Clique em **Selecionar** para escolher o arquivo HTML.
- Escolha onde salvar o PDF de saída.
- Clique em **Gerar PDF**.

### 3. Modo Terminal (Avançado)

#### Converter um arquivo HTML:
```sh
python gerar_pdf.py --input caminho/para/arquivo.html --output caminho/saida.pdf
```

#### Converter uma string HTML:
```sh
python gerar_pdf.py --string "<h1>Olá, mundo!</h1>" --output caminho/saida.pdf
```

## 📝 Observações

- O PDF gerado terá formatação otimizada para impressão em A4.
- O script aceita tanto arquivos HTML quanto código HTML em string.
- Se encontrar algum erro, verifique se o `weasyprint` está instalado corretamente.

---

Se precisar de mais opções ou personalizações, abra uma issue ou peça ajuda!
```
