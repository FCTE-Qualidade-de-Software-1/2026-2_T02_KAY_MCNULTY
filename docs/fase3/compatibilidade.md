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


---

## 4. Roteiros Operacionais Passo a Passo para o Avaliador

Para assegurar a repetibilidade e a reprodutibilidade dos ensaios em conformidade com a ISO/IEC 25040, os procedimentos a seguir detalham as ações exatas que o avaliador deve executar, as checagens visuais e funcionais a realizar e os critérios objetivos de aceitação ou reprovação de cada ensaio.

### 4.1 Roteiro de Compatibilidade Cross-Browser (TCBN / Questão Q1)

Este ensaio verifica se as interfaces e comportamentos dinâmicos dos quatro módulos operam de forma equivalente e sem degradação nos quatro navegadores em escopo (Google Chrome, Mozilla Firefox, Microsoft Edge e Apple Safari).

#### Pré-condições Gerais do Ensaio
1. Estação de trabalho com resolução de tela configurada em 1920 × 1080 pixels (escala 100%).
2. Navegador aberto em **janela anônima / privativa** (para prevenir interferência de extensões, ad-blockers ou cookies residuais).
3. Cache do navegador limpo antes do início da bateria.
4. Painel de Ferramentas do Desenvolvedor aberto (`F12`), aba *Console* visível para detecção de exceções JavaScript.

#### Procedimento de Execução por Módulo

##### Ensaio TC-CB-01 — Módulo Infração
* **Passo 1:** Acessar a URL inicial do portal: `https://portal.detran.df.gov.br/#/home`.
* **Passo 2:** Clicar no cartão de serviço correspondente a **"Veículo / Consulta de Débitos e Infrações"**.
* **Passo 3:** Inspecionar a renderização inicial da página: verificar se as fontes, ícones institucionais e campos de formulário carregam alinhados.
* **Passo 4:** No campo "Placa", digitar o dado sintético `BRA2E19`. Verificar se a máscara formata automaticamente ou aceita o padrão Mercosul.
* **Passo 5:** No campo "RENAVAM", preencher com `00123456789`.
* **Passo 6:** Pressionar a tecla `Tab` e acionar o botão "Consultar".
* **Passo 7:** Inspecionar o console do navegador (`F12` > *Console*).
* **Verificação de Sucesso:**
  * O formulário não trava e processa o envio da consulta.
  * Modal ou mensagem de validação ("Veículo não localizado" ou retorno de dados) é exibido centralizado e legível.
  * O console não apresenta erros fatais (`Uncaught TypeError`, `SyntaxError` ou falha de renderização de script).
* **Evidência Obrigatória:** Captura de tela inteira com o console aberto no momento da resposta, salva como `CB_INFRACAO_[BROWSER].png`.

##### Ensaio TC-CB-02 — Módulo Atendimento
* **Passo 1:** No menu superior ou página inicial, selecionar **"Agendamento de Atendimento"**.
* **Passo 2:** No seletor de serviços, escolher `Veículo - Emissão de CRLV-e`.
* **Passo 3:** No seletor de unidades físicas, escolher `Detran - Taguatinga (Shopping JK)`.
* **Passo 4:** Localizar o componente de calendário dinâmico de datas disponíveis.
* **Passo 5:** Clicar nos botões de avançar e retroceder mês.
* **Passo 6:** Clicar em um dos dias disponíveis destacados no calendário.
* **Passo 7:** Observar o carregamento da grade de horários disponíveis.
* **Verificação de Sucesso:**
  * O calendário responde de imediato aos cliques de navegação entre meses em todos os navegadores.
  * Os dias bloqueados e disponíveis possuem contraste visual distinguível.
  * A grade de horários carrega os botões de seleção de horário sem sobreposição de textos.
  * Não há congelamento de script ou desconfiguração da folha de estilo.
* **Evidência Obrigatória:** Captura de tela com a grade de horários aberta no calendário, salva como `CB_ATENDIMENTO_[BROWSER].png`.

##### Ensaio TC-CB-03 — Módulo Protocolo
* **Passo 1:** Acessar a área de **"Protocolo Online"**.
* **Passo 2:** Selecionar o tipo de peticionamento `Defesa Prévia de Notificação`.
* **Passo 3:** Expandir os itens sanfonados (*accordions*) de instruções gerais e documentação exigida.
* **Passo 4:** Localizar o componente de upload de arquivos (área de *drag-and-drop* ou botão "Anexar Documento").
* **Passo 5:** Selecionar o arquivo de teste `documento_teste_conforme.pdf` (512 KB).
* **Passo 6:** Verificar a resposta da interface quanto ao carregamento do arquivo.
* **Verificação de Sucesso:**
  * Os componentes sanfonados abrem e fecham suavemente sem cortes de texto.
  * O componente de upload reconhece o arquivo PDF e exibe o nome e tamanho na lista de anexos pendentes.
  * Botão de exclusão do anexo temporário funciona corretamente.
  * Ausência de alertas de incompatibilidade de DOM no console.
* **Evidência Obrigatória:** Captura de tela com o documento anexado na lista de arquivos, salva como `CB_PROTOCOLO_[BROWSER].png`.

##### Ensaio TC-CB-04 — Módulo Chatbot
* **Passo 1:** Em qualquer página do portal, localizar o widget flutuante do Chatbot no canto inferior direito.
* **Passo 2:** Clicar sobre o ícone do robô / balão de diálogo para expandir a janela.
* **Passo 3:** Observar o posicionamento do modal sobre o conteúdo da página.
* **Passo 4:** Digitar a mensagem de teste: `Como emitir segunda via da CNH?` e pressionar `Enter` (ou clicar no botão de envio).
* **Passo 5:** Aguardar o retorno da resposta automática do assistente.
* **Passo 6:** Clicar no botão "Minimizar" / "Fechar" do widget.
* **Verificação de Sucesso:**
  * O widget abre em camada superior (*z-index* correto) sem quebrar o layout da página subjacente.
  * O campo de digitação mantém foco e aceita digitação fluida.
  * A resposta textual e eventuais botões de atalho são renderizados com quebra de linha correta.
  * O widget fecha e retorna ao estado de botão flutuante sem deixar resíduos visuais na tela.
* **Evidência Obrigatória:** Captura de tela com o diálogo aberto e mensagem respondida, salva como `CB_CHATBOT_[BROWSER].png`.

#### Matriz de Julgamento da Métrica TCBN
Para cada módulo avaliado, o cenário de teste só é considerado **Aprovado** ($N_{ap} = 1$) se obtiver sucesso pleno nos **quatro navegadores testados**. Se houver qualquer falha impeditiva ou severa em um único navegador (e.g., Safari ou Firefox), o cenário do módulo é pontuado como **Reprovado** ($N_{ap} = 0$).

$$\text{Critério de Sucesso do Módulo:} \quad \text{Sucesso(Chrome)} \land \text{Sucesso(Firefox)} \land \text{Sucesso(Edge)} \land \text{Sucesso(Safari)}$$
