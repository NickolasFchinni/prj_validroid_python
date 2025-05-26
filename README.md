
# ValiDroid

ValiDroid é um projeto de **validação inteligente para builds mobile com IA**, simulando o ciclo completo de CI/CD (Integração e Entrega Contínua) usado em empresas para garantir qualidade antes do deploy.

---

## 🎯 Objetivo
Automatizar e validar o processo de build de aplicativos mobile:
- Simular o build do APK com logs reais de erros e avisos.
- Analisar os logs automaticamente usando IA (Google Gemini).
- Gerar um relatório consolidado com status e recomendações.
- Simular o deploy final do build aprovado.

---

## 🔧 Tecnologias utilizadas
- **Python** (requests, dotenv)
- **ShellScript** (simulação de build, limpeza, deploy)
- **GitHub Actions** (workflow CI/CD automatizado)
- **API do Gemini** (interpretação de logs com IA)
- **Variáveis seguras (dotenv + Secrets do GitHub)**

---

## 🗂️ Estrutura do Projeto
```
prj_validroid_plus/
├── app/ (opcional) - código do app real (não incluso aqui)
├── scripts/
│   ├── build_mobile.sh
│   ├── clear_cache.sh
│   ├── deployment_simulation.sh
├── validator/
│   ├── validator.py
│   ├── log_analyzer.py
│   └── report_generator.py
├── requirements.txt
├── .github/workflows/ci.yml
└── README.md
```

---

## 🚀 Como rodar localmente
1️⃣ Clone o repositório:  
```bash
git clone https://github.com/seuusuario/prj_validroid_python.git
cd prj_validroid_python
```

2️⃣ Instale as dependências Python:  
```bash
pip install -r requirements.txt
```

3️⃣ Configure a chave Gemini:  
- Crie um arquivo `.env` com a sua chave:  
```
GEMINI_API_KEY=sua-chave-aqui
```

4️⃣ Execute os scripts manualmente:  
```bash
chmod +x scripts/*.sh
./scripts/clear_cache.sh
./scripts/build_mobile.sh
python validator/validator.py
python validator/log_analyzer.py
python validator/report_generator.py
./scripts/deployment_simulation.sh
```

---

## 🤖 Fluxo automático no GitHub Actions
O projeto está configurado para rodar automaticamente **a cada push** no repositório.  
Etapas:
1. Preparação do ambiente.
2. Limpeza de cache antigo.
3. Simulação de build.
4. Validação do artefato.
5. Análise dos logs com IA.
6. Geração do relatório final.
7. Simulação do deploy.

> **Nota:** Configure a variável `GEMINI_API_KEY` como Secret no GitHub para que a integração com a IA funcione corretamente.

---

## 📄 Exemplo de Log e Resposta da IA
```
[ERROR] Cannot resolve dependency: react-native-device-info
[WARNING] Some deprecated APIs used
```
Resposta do Gemini:
```
A dependência 'react-native-device-info' está desatualizada. Sugiro rodar 'npm install react-native-device-info@latest' e limpar o cache.
```

---

## 📚 Autor
Feito por Nickolas Faquini.  
[LinkedIn](https://linkedin.com/in/nickolasfaquini) | [GitHub](https://github.com/NickolasFchinni)
