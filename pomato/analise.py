import csv


def somar_tempo_estudo(arquivo):
    total_segundos = 0

    with open(arquivo, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)

        # Ignorar o cabeçalho, se houver
        next(leitor_csv)

        for linha in leitor_csv:
            tempo_estudo = linha[1]  # Segunda coluna contém o tempo de estudo
            minutos, segundos = map(int, tempo_estudo.split(':'))
            total_segundos += minutos * 60 + segundos

    # Converter os segundos para horas, minutos e segundos
    total_horas = total_segundos // 3600
    total_minutos = (total_segundos % 3600) // 60
    total_segundos_resto = total_segundos % 60

    return total_horas, total_minutos, total_segundos_resto


arquivo = 'focus.csv'
total_horas, total_minutos, total_segundos = somar_tempo_estudo(arquivo)
print(
    f"Tempo total de estudo: {total_horas} hora(s), "
    f"{total_minutos} minuto(s) e {total_segundos} segundo(s)."
)
