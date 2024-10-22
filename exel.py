import xlsxwriter

def main(trdata):
    workbook = xlsxwriter.Workbook('Ymarket.xlsx')

    for prod in trdata:

        worksheet = workbook.add_worksheet(prod)
        worksheet.set_column(0, 0, 40)
        worksheet.set_column(1, 1, 8)
        worksheet.set_column(2, 2, 30)

        row = 0
        col = 0

        data = trdata[prod]
        for uid in data:
            result = []
            min_cost = 1000000000
            for item in data[uid]:
                if int(item[1]) <= min_cost:
                    min_cost = item[1]
            for item in data[uid]:
                if int(item[1]) == min_cost:
                    result.append(item)

            worksheet.write(row, col, result[0][0])
            worksheet.write(row, col + 1, result[0][1])
            if len(result) >= 20:
                worksheet.write(row, col + 2, "*")
            else:
                accplace = ""
                for i in result:
                    accplace = accplace + f"{i[2]}-{i[3]}\n"

                worksheet.write(row, col + 2, accplace)

            worksheet.write(row, col + 3, "https://market.yandex.ru/" + result[0][4])

            row += 1

    workbook.close()
