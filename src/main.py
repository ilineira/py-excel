from src.sistema.CargadorAExcel import CargadorAExcel


if __name__ == '__main__':
    path = 'output/outputCausa122692020.xlsx'
    app = CargadorAExcel(path)
    app.run()