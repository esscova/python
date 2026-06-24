import pandas as pd
import datetime
import matplotlib.pyplot as plt
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# 1. CONFIGURAÇÃO DE DADOS E GRÁFICO
def criar_dados_mock():
    """Cria um DataFrame de exemplo para o relatório"""
    dados = {
        'Regiao': ['Sudeste', 'Nordeste', 'Sul', 'Norte', 'Centro-Oeste'],
        'Vendas': [150000.50, 85000.00, 120000.75, 45000.20, 95000.00],
        'Meta': [140000.00, 90000.00, 130000.00, 50000.00, 90000.00],
        'Status': ['Atingida', 'Não Atingida', 'Não Atingida', 'Não Atingida', 'Atingida']
    }
    return pd.DataFrame(dados)

def gerar_grafico_mock(df, caminho_arquivo="grafico_temp.png"):
    """Gera um gráfico de barras simples e salva como imagem"""
    plt.figure(figsize=(8, 4))
    plt.bar(df['Regiao'], df['Vendas'], color='skyblue', label='Vendas')
    plt.plot(df['Regiao'], df['Meta'], color='red', marker='o', linestyle='--', label='Meta')
    plt.title("Vendas vs Meta por Região")
    plt.xlabel("Região")
    plt.ylabel("Valor (R$)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(caminho_arquivo, dpi=150)
    plt.close() # Fecha o gráfico para liberar memória
    return caminho_arquivo


# 2. CLASSE DO PDF (fpdf2)
class RelatorioVendasPDF(FPDF):

    def header(self):
        self.set_font("Helvetica", "B", 15)
        self.cell(0, 10, "Relatório de Vendas Mensal", border=False, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")

        self.set_font("Helvetica", "I", 8)
        self.cell(0, 5, f"Data de Emissão: {self.data_emissao}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="R")

        self.ln(2)
        y_atual = self.get_y()
        self.line(10, y_atual, 200, y_atual) # Linha dinâmica
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")


# 3. FUNÇÃO GERADORA DO RELATÓRIO
def gerar_relatorio_vendas(df, caminho_da_imagem, arquivo_saida="relatorio_automatico.pdf"):
    """Função que automatiza a geração do relatório de vendas em PDF."""
    print("Iniciando a geração do relatório...")

    pdf = RelatorioVendasPDF()
    pdf.alias_nb_pages()
    pdf.data_emissao = datetime.datetime.now().strftime("%d/%m/%Y")
    pdf.add_page()

    # --- Texto Introdutório ---
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 6, "Relatório automático gerado pelo sistema. Resumo das vendas da empresa no último período.")
    pdf.ln(5)

    # --- Tabela ---
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Desempenho por Região:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

    # Cabeçalho
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(220, 220, 220)
    pdf.cell(50, 8, "Região", border=1, align="C", fill=True)
    pdf.cell(40, 8, "Vendas (R$)", border=1, align="C", fill=True)
    pdf.cell(40, 8, "Meta (R$)", border=1, align="C", fill=True)
    pdf.cell(60, 8, "Status", border=1, align="C", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Linhas de Dados
    pdf.set_font("Helvetica", size=10)
    for index, row in df.iterrows():
        cor_texto = (0, 128, 0) if row['Status'] == 'Atingida' else (255, 0, 0)

        pdf.cell(50, 8, row['Regiao'], border=1, align="L")

        pdf.set_text_color(0, 0, 0)
        vendas_formatado = f"R$ {row['Vendas']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        meta_formatado = f"R$ {row['Meta']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Alinhamento à direita exige new_x=XPos.RIGHT
        pdf.cell(40, 8, vendas_formatado, border=1, align="R", new_x=XPos.RIGHT)
        pdf.cell(40, 8, meta_formatado, border=1, align="R", new_x=XPos.RIGHT)

        pdf.set_text_color(*cor_texto)
        pdf.cell(60, 8, row['Status'], border=1, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)

    # --- Imagem ---
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Análise Gráfica:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(2)

    pos_x = (210 - 150) / 2 # Centraliza a imagem no A4
    pdf.image(caminho_da_imagem, x=pos_x, w=150)

    # --- Output ---
    pdf.output(arquivo_saida)
    print(f"✅ Relatório gerado com sucesso: {arquivo_saida}")


# 4. BLOCO PRINCIPAL DE EXECUÇÃO
if __name__ == "__main__":
    # 1. Cria os dados fictícios
    df_vendas = criar_dados_mock()

    # 2. Gera a imagem do gráfico
    imagem_grafico = gerar_grafico_mock(df_vendas)

    # 3. Chama a função que monta o PDF
    gerar_relatorio_vendas(
        df=df_vendas,
        caminho_da_imagem=imagem_grafico,
        arquivo_saida="meu_relatorio_final.pdf"
    )
