from datetime import datetime
from dateutil.relativedelta import relativedelta

print("Maria pegou um empréstimo de 1.000.000 na data 20/12/2020, cada parcela vence no dia 20 com pagamento em 5 anos")

VALOR_A_SER_PAGO = 1_000_000

dataFormat = "%d/%m/%Y"
dataInicio = datetime.strptime("20/12/2020",dataFormat)
dataFim = dataInicio + relativedelta(years=5)

dateDif = relativedelta(dataFim, dataInicio)
total_meses = dateDif.years * 12 + dateDif.months

temp_datas = dataInicio
for parcela in range(1,total_meses+1):
    print(f"ParcelaNum: {parcela} - Date: {temp_datas.strftime(dataFormat)} - Valor: {(VALOR_A_SER_PAGO/total_meses):,.2f}")
    temp_datas = temp_datas + relativedelta(months=1)