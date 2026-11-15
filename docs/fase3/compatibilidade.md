# Plano de Avaliação – Característica: Compatibilidade

**Disciplina:** Qualidade de Software 1 (FGA0315) – Universidade de Brasília (UnB / FCTE)  
**Semestre:** 2026.2  
**Equipe:** Kay McNulty (Turma 02)  
**Objeto de Avaliação:** Portal Detran Digital DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home))  
**Norma Base:** ABNT NBR ISO/IEC 25040:2011 (Processo de Avaliação de Produto de Software, Seção 6.3 – *Design the evaluation*)  
**Característica:** Compatibilidade (ISO/IEC 25010:2023)  
**Subcaracterísticas:** Coexistência e Interoperabilidade  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot  
**Responsáveis:** Artur Fernandes Galdino e Nicole Jovita Fernandes  
**Marcos de Referência:** Marco M4 (*Plano de Avaliação e Metodologia Operacional*)

---

## 1. Métodos de Avaliação e Indicadores Operacionais

O Plano de Avaliação operacionaliza formalmente os objetivos, questões e métricas definidos na [Fase 2](../fase2/compatibilidade.md). O processo de medição fundamenta-se em princípios de auditoria diagnóstica externa de caixa-preta, garantindo repetibilidade e reprodutibilidade sem provocar efeitos colaterais adversos no portal governamental em produção.

A característica de **Compatibilidade** desdobra-se em três frentes metodológicas independentes e complementares:

1. **Avaliação de Coexistência entre Navegadores (*Cross-Browser*):**
   * **Indicador Operacional:** Taxa de Compatibilidade Entre Navegadores ($TCBN$).
   * **Questão Vinculada:** Questão Q1 (*O sistema preserva a funcionalidade e a integridade de layout nos navegadores modernos mais difundidos?*).
   * **Procedimento:** Execução padronizada de fluxos operacionais nos quatro motores web dominantes, inspecionando paridade funcional, renderização de folhas de estilo e ausência de exceções JavaScript não tratadas no console.
2. **Avaliação de Coexistência Multi-resolução (*Responsividade Cross-Device*):**
   * **Indicador Operacional:** Índice de Conformidade Responsiva ($ICR$).
   * **Questão Vinculada:** Questão Q2 (*As páginas e componentes dos quatro módulos adaptam-se de forma consistente às diferentes dimensões de tela?*).
   * **Procedimento:** Inspeção visual e funcional em cinco viewports padronizadas representando dispositivos móveis compactos, intermediários, tablets e monitores desktop de alta definição.
3. **Avaliação de Interoperabilidade e Troca de Dados (*Interoperabilidade de APIs HTTP*):**
   * **Indicador Operacional:** Taxa de Sucesso de Interoperabilidade de Serviços ($TSIS$).
   * **Questão Vinculada:** Questão Q3 (*Os fluxos de comunicação e troca de dados com serviços externos e barramentos ocorrem de maneira íntegra e padronizada?*).
   * **Procedimento:** Monitoramento passivo do tráfego de rede via DevTools (filtro *Fetch/XHR*), analisando códigos de resposta HTTP, integridade de cabeçalhos e conformidade de payloads durante transações reais com o Gov.br, SEI-GDF, emissão bancária de guias e motor de inteligência artificial do Chatbot.

### Tabela 1 — Síntese Metodológica das Métricas de Compatibilidade

| Indicador | Questão GQM | Unidade de Medida | Fórmula do Indicador | Instrumento de Coleta | Amostra Operacional |
| :--- | :---: | :---: | :---: | :--- | :---: |
| **TCBN** | Q1 | Percentual (%) | $TCBN = \left(\frac{N_{ap}}{N_{tot}}\right) \times 100$ | Google Chrome, Mozilla Firefox, Microsoft Edge e Apple Safari | 4 módulos × 4 navegadores = 16 ensaios |
| **ICR** | Q2 | Percentual (%) | $ICR = \left(\frac{T_{conf}}{T_{tot}}\right) \times 100$ | Emulação DevTools em 5 viewports (360px a 1920px) | 4 módulos × 5 viewports = 20 verificações |
| **TSIS** | Q3 | Percentual (%) | $TSIS = \left(\frac{Req_{ok}}{Req_{tot}}\right) \times 100$ | Aba *Rede (Network)* DevTools (Fetch/XHR) | Amostragem contínua de requisições de escopo |

*Fonte: Elaborado pelos autores com base na especificação da Fase 2.*

---

## 2. Requisitos e Especificação dos Ambientes de Medição

Para assegurar que qualquer engenheiro de software avaliador replique com exatidão as condições experimentais, o ambiente de teste é estritamente padronizado quanto a hardware, sistemas operacionais, versões de navegadores e ferramentas analíticas.

### 2.1 Hardware de Referência e Estações de Trabalho
* **Processador:** Arquitetura x86-64 ou ARM64 com mínimo de 4 núcleos físicos (2.4 GHz ou superior).
* **Memória RAM:** Mínimo de 8 GB (recomendado 16 GB) para evitar lentidão ou descarte de abas durante sessões de inspeção com ferramentas de desenvolvimento ativas.
* **Monitor Principal:** Resolução nativa mínima de 1920 × 1080 pixels (Full HD) calibrado em escala de exibição de 100% (sem zoom de sistema operacional), garantindo que as medições de pixel nos testes de viewport sejam 1:1.
* **Dispositivo Móvel Físico (Contraprova):** Smartphone Android (v13 ou superior) e dispositivo Apple iOS (v17 ou superior) para validação cruzada do comportamento de toque (*touch events*) e renderização móvel.

### 2.2 Navegadores e Motores de Renderização Homologados
A seleção dos navegadores fundamenta-se nos dados de participação de mercado no Brasil (fonte: StatCounter Global Stats para o Distrito Federal e território nacional), cobrindo mais de 98% dos acessos de cidadãos:

1. **Google Chrome:** Versão estável 130.0 ou superior (Motor: *Blink* / V8). Representa a referência majoritária de mercado.
2. **Mozilla Firefox:** Versão estável 131.0 ou superior (Motor: *Gecko* / SpiderMonkey). Essencial para avaliar padrões web puros e motores não-Chromium.
3. **Microsoft Edge:** Versão estável 130.0 ou superior (Motor: *Blink* / V8 em ambiente Windows). Relevante para ambientes corporativos e governamentais.
4. **Apple Safari:** Versão estável 17.0 ou superior (Motor: *WebKit* / JavaScriptCore em macOS/iOS, ou via emulador WebKit Playwright). Fundamental para assegurar compatibilidade no ecossistema Apple.

### 2.3 Ferramental Técnico de Inspeção
* **Navegador DevTools Integrado:**
  * Aba *Elements / Inspetor*: Para análise do DOM, regras de CSS computadas, detecção de overflow e classes responsivas.
  * Aba *Console*: Para monitoramento em tempo real de advertências de layout, falhas de scripts JS, quebras de CORS e erros de runtime.
  * Aba *Network*: Configurada com cache desativado (*Disable cache* ativado enquanto DevTools estiver aberto) e filtro ativo para `Fetch/XHR` e `Doc`.
  * Modo de Dispositivo (*Device Toolbar* / `Ctrl+Shift+M` ou `Cmd+Option+M`): Para fixação exata das resoluções de tela e densidade de pixels (DPR = 1.0, 2.0 e 3.0).
* **Capturador de Tráfego HTTP:** Capacidade de exportação de arquivos `.har` (*HTTP Archive*) para auditoria posterior de cabeçalhos e payloads.

---

## 3. Mapeamento de Massa de Dados e Conformidade com a LGPD

Como as medições ocorrem diretamente no ambiente de produção do Detran-DF ([portal.detran.df.gov.br](https://portal.detran.df.gov.br/#/home)), a equipe estabeleceu uma rigorosa política de **dados de teste sintéticos**, em total conformidade com a Lei Geral de Proteção de Dados (Lei Federal nº 13.709/2018 - LGPD).

### 3.1 Diretrizes de Segurança e Não-Interferência
1. **Zero Efeitos Colaterais no Banco Governamental:** Os ensaios não concluem transações que possam gerar débitos reais, agendamentos indevidos que ocupem vagas de cidadãos ou abertura definitiva de processos fictícios no SEI-GDF.
2. **Dados Pessoais Sintéticos:** Proibido o uso de CPFs, nomes completos ou dados sensíveis de terceiros. As buscas e simulações usam dados de domínio público, números sintéticos gerados por algoritmos matemáticos ou parâmetros deliberadamente inválidos para teste de resiliência.

### 3.2 Catálogo de Massa de Dados de Teste

| Módulo Alvo | Campo do Formulário | Tipo do Dado de Teste | Valor de Entrada Utilizado | Finalidade do Ensaio |
| :--- | :--- | :--- | :--- | :--- |
| **Infração** | Placa do Veículo | Padrão Mercosul Sintético | `BRA2E19` | Testar máscara de entrada e validação de formato sem consulta a veículo de terceiros |
| **Infração** | Placa do Veículo | Padrão Antigo (Cinza) | `JFP-1234` | Testar retrocompatibilidade do seletor e conversão de formato |
| **Infração** | RENAVAM | Sintético Válido (11 dígitos) | `00123456789` | Verificar disparo assíncrono da busca e máscara de campo |
| **Atendimento** | Serviço Solicitado | Categoria de Atendimento | `Veículo - Emissão de CRLV-e` | Acessar fluxo de agendamento e carregar o calendário de postos |
| **Atendimento** | Posto de Atendimento | Unidade Física | `Detran - Taguatinga (Shopping JK)` | Testar renderização de dropdown e carregamento de grade horária |
| **Protocolo** | Tipo de Processo | Categoria Administrativa | `Defesa Prévia de Notificação` | Abrir o formulário de peticionamento e carregar componentes |
| **Protocolo** | Anexo de Documento | Arquivo PDF de Referência | `documento_teste_conforme.pdf` (Tamanho: 512 KB) | Testar upload nominal, barra de progresso e validação de tipo MIME |
| **Protocolo** | Anexo de Documento | Arquivo Inválido de Teste | `arquivo_extensao_invalida.exe` (Tamanho: 100 KB) | Testar rejeição de formatos não suportados sem quebra de página |
| **Chatbot** | Caixa de Mensagem | Consulta Curta Nominal | `Como emitir segunda via da CNH?` | Avaliar tempo de resposta do assistente e renderização de botões rápidos |
| **Chatbot** | Caixa de Mensagem | Consulta com Caracteres Especiais | `Qual o valor da taxa de licenciamento 2026? & DUD / PIX` | Testar encoding UTF-8 e preservação de caracteres especiais na tela |

*Fonte: Elaborado pelos autores.*
