# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Corinthians.

campeonato = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense',
              'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Bragantino',
              'Atlético-MG', 'Santos', 'Corinthians', 'Vasco da Gama',
              'EC Vitória', 'Internacional', 'Ceará SC', 'Fortaleza',
              'Juventude', 'Sport Recife')


print("=" * 38)
print("-- Campeonato Brasileiro de Futebol --")
print("=" * 38)
print(f"Lista de Times do Brasileirão: {campeonato}")
print(f"Os 5 primeiros times: {campeonato[:5]}")
print(f"Os últimos 4 colocados: {campeonato[-4:]}")
print(f"Times em ordem alfabética: {sorted(campeonato)}")
print(f"Posição do time Corinthians: {campeonato.index('Corinthians') + 1}ª posição.")
