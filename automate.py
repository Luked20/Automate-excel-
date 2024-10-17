import pandas as pd

# Carregar a planilha Excel
df = pd.read_excel('dados.xlsx')


def verificar_e_gerar_links(row):
    
    if pd.notna(row['Frente']) and pd.notna(row['Direita']) and pd.notna(row['Esquerda']) and pd.notna(row['Verso']):
        
        links = {
            'frente': f"{row['Link Base']}/{row['Frente']}",
            'direita': f"{row['Link Base']}/{row['Direita']}",
            'esquerda': f"{row['Link Base']}/{row['Esquerda']}",
            'verso': f"{row['Link Base']}/{row['Verso']}"
        }
        return links
    else:
        
        return None


df['Links Gerados'] = df.apply(verificar_e_gerar_links, axis=1)


df_completos = df[df['Links Gerados'].notna()]


df_expandido = df_completos[['Nome', 'Código', 'Links Gerados']].explode('Links Gerados')


print(df_expandido)


df_expandido.to_excel('dados_com_links_gerados_completos.xlsx', index=False)
