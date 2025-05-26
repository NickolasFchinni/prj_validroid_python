from datetime import datetime

if __name__ == "__main__":
  with open("build_log.txt", "r") as log:
    logs = log.read()

  try:
    with open("gemini_output.txt", "r") as gemini:
      ia_output = gemini.read()
  except FileNotFoundError:
    ia_output = "Sugestão de IA não disponível."

  report = f"""
    Relatorio da build - {datetime.now().strftime('%Y-%m-%d')}

    Logs da build:
    {logs}

    Resposta da IA:
    {ia_output}
  """

  with open("build_report.txt", "w") as report_file:
    report_file.write(report)

  print("Relatorio final gerado!")