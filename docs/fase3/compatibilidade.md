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

I. **Avaliação de Coexistência entre Navegadores (*Cross-Browser*):**
   
   * **Indicador Operacional:** Taxa de Compatibilidade Entre Navegadores ($TCBN$).
   
   * **Questão Vinculada:** Questão Q1 (*O sistema preserva a funcionalidade e a integridade de layout nos navegadores modernos mais difundidos?*).
   
   * **Procedimento:** Execução padronizada de fluxos operacionais nos quatro motores web dominantes, inspecionando paridade funcional, renderização de folhas de estilo e ausência de exceções JavaScript não tratadas no console.

II. **Avaliação de Coexistência Multi-resolução (*Responsividade Cross-Device*):**
   
  * **Indicador Operacional:** Índice de Conformidade Responsiva ($ICR$).
  
  * **Questão Vinculada:** Questão Q2 (*As páginas e componentes dos quatro módulos adaptam-se de forma consistente às diferentes dimensões de tela?*).
   
  * **Procedimento:** Inspeção visual e funcional em cinco viewports padronizadas representando dispositivos móveis compactos, intermediários, tablets e monitores desktop de alta definição.

III. **Avaliação de Interoperabilidade e Troca de Dados (*Interoperabilidade de APIs HTTP*):**
   
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


---

### 4.2 Roteiro de Conformidade Responsiva Multi-resolução (ICR / Questão Q2)

Este ensaio tem como finalidade medir a capacidade de adaptação visual e ergonômica das telas do Portal Detran Digital DF frente a diferentes larguras de exibição (*viewports*), assegurando que o cidadão consiga utilizar os serviços tanto em smartphones simples quanto em monitores desktop de alta resolução.

#### Viewports de Referência Padronizadas

As medições realizam-se obrigatoriamente sobre cinco resoluções fixas configuradas via *Device Mode* do DevTools (`Ctrl+Shift+M`):

1. **VP-01 — Mobile Pequeno (360 × 640 px):** Dispositivos móveis de entrada e telas compactas.
2. **VP-02 — Mobile Médio (414 × 896 px):** Smartphones intermediários e padrão de mercado moderno.
3. **VP-03 — Tablet Retrato (768 × 1024 px):** Dispositivos intermediários (e.g., Apple iPad).
4. **VP-04 — Desktop HD (1366 × 768 px):** Notebooks corporativos e monitores de resolução padrão.
5. **VP-05 — Desktop Full HD (1920 × 1080 px):** Monitores amplos e estações de alta definição.

#### Procedimento Passo a Passo de Inspeção Responsiva

* **Passo 1:** No navegador de referência (Google Chrome ou Edge), abrir o DevTools (`F12`) e ativar a barra de emulação de dispositivos (*Toggle device toolbar* / `Ctrl+Shift+M`).
* **Passo 2:** No seletor de dimensões, selecionar o modo **"Responsive"** (Responsivo).
* **Passo 3:** Ajustar a largura e altura para a viewport correspondente (iniciando em `360 × 640 px`).
* **Passo 4:** Fixar o zoom do emulador em **100%** e o fator de escala de dispositivo (*Device Pixel Ratio - DPR*) em 1.0 ou 2.0.
* **Passo 5:** Recarregar a página (`Ctrl+F5`) para que as media queries e scripts de redimensionamento sejam computados a frio.
* **Passo 6:** Para o módulo sob teste (Infração, Atendimento, Protocolo ou Chatbot), executar a inspeção visual e de controle conforme os critérios abaixo:
  * **Checagem de Rolagem Horizontal (Overflow):** Tentar rolar a tela lateralmente. A largura do documento deve ser estritamente contida na viewport (`document.documentElement.scrollWidth === window.innerWidth`).
  * **Checagem de Sobreposição de Elementos Flutuantes:** Localizar o widget do Chatbot e verificar se o botão flutuante sobrepõe botões de submissão ("Consultar", "Avançar", "Salvar") ou campos de formulário.
  * **Checagem de Rótulos e Quebras de Linha:** Avaliar se títulos, instruções e campos de formulário mantêm legibilidade, sem caracteres cortados ou sobreposição de linhas.
  * **Checagem de Menu e Navegação:** No mobile (VP-01 e VP-02), verificar se o menu principal colapsa para o ícone de hambúrguer e se a abertura/fechamento do menu ocorre sem deslocar o cabeçalho.
* **Passo 7:** Registrar o resultado na planilha de inspeção e capturar a tela completa da viewport.

#### Tabela 2 — Matriz de Pontos de Inspeção Responsiva ($T_{tot} = 20$ pontos)

| Código | Módulo Avaliado | Viewport Avaliada | Dimensão (px) | Foco Principal da Inspeção |
| :---: | :--- | :---: | :---: | :--- |
| **RESP-01** | Infração | VP-01 (Mobile Pequeno) | 360 × 640 | Contenção da tabela de débitos e campos de placa/Renavam sem overflow |
| **RESP-02** | Infração | VP-02 (Mobile Médio) | 414 × 896 | Alinhamento dos botões de consulta e mensagem de retorno |
| **RESP-03** | Infração | VP-03 (Tablet) | 768 × 1024 | Distribuição em grade dos cartões de serviços de veículos |
| **RESP-04** | Infração | VP-04 (Desktop HD) | 1366 × 768 | Proporção de tela e margens laterais |
| **RESP-05** | Infração | VP-05 (Desktop Full HD) | 1920 × 1080 | Centralização de layout e preenchimento de espaço útil |
| **RESP-06** | Atendimento | VP-01 (Mobile Pequeno) | 360 × 640 | Empilhamento do calendário e grade de horários sem corte de dias |
| **RESP-07** | Atendimento | VP-02 (Mobile Médio) | 414 × 896 | Toque preciso nos seletores de postos de atendimento |
| **RESP-08** | Atendimento | VP-03 (Tablet) | 768 × 1024 | Exibição lado a lado de unidade física e grade de horários |
| **RESP-09** | Atendimento | VP-04 (Desktop HD) | 1366 × 768 | Navegabilidade do fluxo sequencial de agendamento |
| **RESP-10** | Atendimento | VP-05 (Desktop Full HD) | 1920 × 1080 | Renderização limpa e espaçamento confortável dos componentes |
| **RESP-11** | Protocolo | VP-01 (Mobile Pequeno) | 360 × 640 | Sanfonas explicativas e botão de upload adaptados a telas estreitas |
| **RESP-12** | Protocolo | VP-02 (Mobile Médio) | 414 × 896 | Visibilidade da lista de documentos e status de carregamento |
| **RESP-13** | Protocolo | VP-03 (Tablet) | 768 × 1024 | Adaptação de formulários longos de peticionamento |
| **RESP-14** | Protocolo | VP-04 (Desktop HD) | 1366 × 768 | Estabilidade das áreas de arraste (*drag-and-drop*) |
| **RESP-15** | Protocolo | VP-05 (Desktop Full HD) | 1920 × 1080 | Integridade de margens e contêineres de instrução normativa |
| **RESP-16** | Chatbot | VP-01 (Mobile Pequeno) | 360 × 640 | Comportamento do modal aberto (deve ocupar tela inteira sem vazar) |
| **RESP-17** | Chatbot | VP-02 (Mobile Médio) | 414 × 896 | Teclado virtual simulado sem ocultar a caixa de digitação |
| **RESP-18** | Chatbot | VP-03 (Tablet) | 768 × 1024 | Posicionamento do balão e ausência de bloqueio de cliques úteis |
| **RESP-19** | Chatbot | VP-04 (Desktop HD) | 1366 × 768 | Proporção da janela flutuante em relação à página |
| **RESP-20** | Chatbot | VP-05 (Desktop Full HD) | 1920 × 1080 | Fixação no canto inferior direito sem deslocamento ao rolar a página |

*Fonte: Elaborado pelos autores.*

#### Critério de Pontuação da Métrica ICR
Cada um dos 20 pontos de inspeção recebe pontuação binária:
* **Conforme ($T_{conf} = 1$):** Zero rolagem horizontal não planejada, zero sobreposição obstrutiva do Chatbot e textos 100% contidos e legíveis.
* **Não Conforme ($T_{conf} = 0$):** Ocorrência de qualquer uma das três anomalias visuais acima.

O índice final é a razão entre os pontos aprovados e o total de 20 pontos:

$$ICR = \left(\frac{T_{conf}}{20}\right) \times 100\%$$


---

### 4.3 Roteiro de Interoperabilidade e Monitoramento de Rede (TSIS / Questão Q3)

Este ensaio analisa a integridade das trocas de informações e chamadas a serviços externos (Gov.br, SEFAZ-DF/Bancos, SEI-GDF e motor InBot) a partir do tráfego HTTP/HTTPS de borda do cliente.

#### Configuração das Ferramentas de Inspeção de Rede
1. No navegador, abrir o DevTools (`F12`) e selecionar a aba **"Rede" (Network)**.
2. Marcar a caixa de seleção **"Preservar registro" (Preserve log)**: imprescindível para não perder as requisições em páginas que realizam recarga ou redirecionamento.
3. Marcar a caixa **"Desativar cache" (Disable cache)**.
4. Aplicar o filtro **"Fetch/XHR"** na barra de ferramentas da aba Rede para isolar chamadas de API, descartando imagens estáticas, fontes e ícones que não representam integrações funcionais.

#### Procedimento Passo a Passo de Coleta de Rede

* **Passo 1:** Limpar o histórico de requisições clicando no botão "Limpar" (*Clear network log* / ícone de círculo cortado).
* **Passo 2:** Iniciar a execução do fluxo sob teste no portal (ex.: acionar consulta de infração, iniciar agendamento ou abrir o Chatbot).
* **Passo 3:** Observar o fluxo contínuo de linhas na tabela da aba Rede.
* **Passo 4:** Para cada requisição de serviço externo, inspecionar:
  * **Nome / URL da Requisição:** Endpoint de destino (identificando se é do domínio próprio do Detran ou barramento integrado).
  * **Status Code HTTP:** Código numérico de retorno do servidor.
  * **Método HTTP:** `GET`, `POST`, `OPTIONS` ou `PUT`.
  * **Tipo / Formato:** Payload retornado (`application/json`, `application/pdf`, etc.).
  * **Tempo de Resposta:** Latência de transferência em milissegundos.
* **Passo 5:** Verificar se há requisições marcadas em vermelho (falha de rede, bloqueio por CORS ou status HTTP 4xx/5xx).
* **Passo 6:** Ao final do fluxo, clicar com o botão direito sobre a tabela da aba Rede e selecionar **"Salvar tudo como HAR com conteúdo"** (*Save all as HAR with content*).
* **Passo 7:** Capturar a tela mostrando a lista de requisições com os códigos de status legíveis.

#### Tabela 3 — Mapeamento das Integrações Críticas Avaliadas

| Código | Módulo | Serviço Externo Integrado | Ponto Crítico de Troca de Dados | Status HTTP Esperado |
| :---: | :--- | :--- | :--- | :---: |
| **INT-01** | Atendimento / Infração | Provedor de Identidade Gov.br | Handshake OAuth2/OIDC, redirecionamento e validação de token | 302 (Redirect) / 200 (OK) |
| **INT-02** | Infração | Barramento Bancário / SEFAZ-DF | Emissão do Documento Único do Detran (DUD) e chave Pix | 200 (OK com payload JSON/PDF) |
| **INT-03** | Protocolo | Barramento do SEI-GDF | Consulta de processos, validação de metadados e pré-anexo | 200 (OK) |
| **INT-04** | Chatbot | Plataforma InBot / Nuvem AWS | Comunicação assíncrona XHR/WebSocket para envio e recepção de diálogo | 200 (OK) / 101 (Switching Protocols) |

*Fonte: Elaborado pelos autores.*

#### Critério de Classificação da Métrica TSIS
Cada chamada de rede inspecionada é categorizada de acordo com seu código de status:
* **Requisição Bem-Sucedida ($Req_{ok}$):**
  * Códigos da família **2xx** (Sucesso): `200 OK`, `201 Created`, `204 No Content`.
  * Códigos da família **3xx** (Redirecionamento válido): `301 Moved`, `302 Found`, `304 Not Modified`, `307 Temporary Redirect`.
* **Requisição com Falha ($Req_{falha}$):**
  * Códigos de erro de cliente gerados por contratos de API inconsistentes (**4xx**): `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `422 Unprocessable Entity`.
  * Códigos de erro interno de servidor ou timeout de gateway (**5xx**): `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`, `504 Gateway Timeout`.
  * Falhas de rede que abortam a requisição (`(failed)`, `net::ERR_CONNECTION_REFUSED`, `net::ERR_BLOCKED_BY_ORB` ou erro de CORS).

A taxa percentual consolidada calcula-se como:

$$TSIS = \left(\frac{Req_{ok}}{Req_{tot}}\right) \times 100\%$$

---

## 5. Protocolo de Registro de Evidências e Nomenclatura de Arquivos

Para garantir a auditabilidade integral das medições, todas as evidências coletadas pelos avaliadores devem seguir rigorosamente o padrão de nomenclatura abaixo, sendo armazenadas em diretório específico no repositório (`docs/assets/evidencias/fase3/compatibilidade/`):

### 5.1 Padrão de Nomenclatura para Capturas de Tela
* **Ensaios Cross-Browser:**
  * `CB_[MODULO]_[NAVEGADOR].png`
  * *Exemplos:* `CB_INFRACAO_CHROME.png`, `CB_ATENDIMENTO_FIREFOX.png`, `CB_PROTOCOLO_EDGE.png`, `CB_CHATBOT_SAFARI.png`.
* **Ensaios de Responsividade Multi-resolução:**
  * `RESP_[MODULO]_[LARGURA]px.png`
  * *Exemplos:* `RESP_INFRACAO_360px.png`, `RESP_ATENDIMENTO_414px.png`, `RESP_PROTOCOLO_768px.png`, `RESP_CHATBOT_1920px.png`.
* **Ensaios de Interoperabilidade e Tráfego de Rede:**
  * `NET_[MODULO]_[SERVICO].png` (Captura da tabela de rede do DevTools)
  * `NET_[MODULO]_[SERVICO].har` (Dump estruturado do tráfego HTTP com cabeçalhos e tempos)
  * *Exemplos:* `NET_INFRACAO_DUD.har`, `NET_ATENDIMENTO_GOVBR.png`.

---

## 6. Cronograma de Execução das Baterias de Avaliação

O cronograma operacional define as janelas de realização das baterias de medição de Compatibilidade, alinhadas aos marcos da Entrega 2 (Ponto de Controle 2 — 16/11/2026) e à margem de consolidação de resultados prevista para 22/11/2026. As datas foram calibradas para que a Fase 4 (execução em campo) transcorra de maneira estruturada e sem atritos operacionais.

### Tabela 4 — Cronograma Operacional das Baterias de Avaliação

| Rodada | Período | Atividade Principal | Métricas Cobertas | Responsáveis |
| :---: | :---: | :--- | :---: | :--- |
| **R0** | 15/11/2026 | Revisão final do plano e execução dos ensaios piloto em um único módulo (Infração) para calibrar os roteiros | TCBN, ICR, TSIS | Artur Fernandes Galdino e Nicole Jovita Fernandes |
| **R1** | 16/11/2026 | Bateria completa Cross-Browser (TCBN): execução dos ensaios TC-CB-01 a TC-CB-04 nos quatro navegadores | TCBN | Artur Fernandes Galdino e Nicole Jovita Fernandes |
| **R2** | 17/11/2026 | Bateria completa de Responsividade (ICR): inspeção dos 20 pontos de viewport (RESP-01 a RESP-20) | ICR | Artur Fernandes Galdino e Nicole Jovita Fernandes |
| **R3** | 18/11/2026 | Bateria completa de Interoperabilidade (TSIS): monitoramento de tráfego de rede nas integrações INT-01 a INT-04 | TSIS | Artur Fernandes Galdino e Nicole Jovita Fernandes |
| **R4** | 19/11/2026 | Compilação de dados brutos, cálculo dos índices TCBN, ICR e TSIS e registro de discrepâncias para reteste | TCBN, ICR, TSIS | Artur Fernandes Galdino e Nicole Jovita Fernandes |
| **R5** | 20/11/2026 – 21/11/2026 | Reteste de itens reprovados ou inconclusos; redação do relatório consolidado de resultados (Fase 4) | TCBN, ICR, TSIS | Artur Fernandes Galdino e Nicole Jovita Fernandes |
| **R6** | 22/11/2026 | Revisão final de evidências, publicação dos resultados e encerramento da Fase 4 | — | Artur Fernandes Galdino e Nicole Jovita Fernandes |

*Fonte: Elaborado pelos autores.*

### 6.1 Considerações de Calendário

- As rodadas R1, R2 e R3 são independentes entre si e podem ser executadas em paralelo pelos dois avaliadores, desde que cada avaliador cubra módulos distintos para prevenir conflitos de concorrência de sessão no portal.
- A rodada R0 é mandatória: o piloto valida que os roteiros operacionais das Seções 4.1, 4.2 e 4.3 são perfeitamente reproduzíveis no ambiente de produção antes da execução integral.
- O cronograma harmoniza-se com a métrica de calendário CID (*Compressed Issue Duration*) monitorada no painel PSM da equipe, garantindo janela de execução de 5 a 7 dias úteis para os artefatos da Entrega 2.

---

## 7. Perfil e Requisitos dos Avaliadores

Para assegurar a reprodutibilidade dos ensaios por qualquer engenheiro de software avaliador independente, os requisitos mínimos de conhecimento técnico e de domínio foram formalizados a seguir.

### 7.1 Conhecimento de Domínio

| Área | Nível Exigido | Justificativa |
| :--- | :---: | :--- |
| Navegação em portais web governamentais | Básico | O avaliador precisa compreender a taxonomia de serviços e menus do Detran Digital DF para navegar nos fluxos sem desvio |
| Conceitos de compatibilidade de navegadores (*Cross-Browser*) | Básico | Capacidade de distinguir divergências reais de renderização entre motores Blink, Gecko e WebKit |
| Conceitos de design responsivo e viewport | Básico | Compreensão de media queries CSS, quebras de layout e operação da ferramenta Device Mode |
| Protocolo HTTP (*status codes*, métodos e cabeçalhos) | Intermediário | Necessário para classificar requisições em $Req_{ok}$ (2xx/3xx) ou $Req_{falha}$ (4xx/5xx/CORS) na métrica TSIS |
| Análise de tráfego de rede via DevTools | Intermediário | Habilidade técnica para filtrar requisições Fetch/XHR, inspecionar payloads e exportar arquivos `.har` |

### 7.2 Habilidades Técnicas com Ferramentas

| Ferramenta | Operação Esperada | Nível Exigido |
| :--- | :--- | :---: |
| DevTools — Aba Console | Identificar exceções JavaScript impeditivas (`Uncaught TypeError`, `SyntaxError`) e violações de CORS | Básico |
| DevTools — Aba Network | Aplicar filtro Fetch/XHR, habilitar *Preserve log*, manter *Disable cache* ativo e exportar arquivo `.har` | Intermediário |
| DevTools — Device Toolbar | Configurar larguras e alturas fixas de viewport e ajustar DPR (1.0 e 2.0) | Básico |
| Ferramenta de Captura de Tela | Capturar telas integrais da área de visualização e salvar em formato `.png` com a taxonomia do plano | Básico |
| Controle de Versão (Git) | Versionar relatórios e evidências no repositório GitHub da equipe | Básico |

### 7.3 Conhecimentos e Acessos Desnecessários

Os ensaios operacionais foram desenhados para **não exigir**:

- Escrita ou compilação de código-fonte (scripts de automação, testes unitários ou suites E2E automatizadas).
- Ferramentas externas pagas ou pesadas (Selenium Grid, BrowserStack corporativo, proxies locais como Charles ou Fiddler).
- Acesso a código-fonte proprietário, esquemas de bancos de dados ou documentação restrita de APIs do Detran-DF.
- Credenciais reais de cidadão ou contas com nível Prata/Ouro no Gov.br (todas as validações utilizam massa de dados sintética pública).

---

## 8. Matriz de Rastreabilidade (Fase 2 para Fase 3)

Esta matriz comprova a rastreabilidade estrita entre a especificação teórica da Fase 2 e os métodos operacionais da Fase 3:

| Métrica Formal (Fase 2) | Questão e Hipótese | Medidas Básicas (PSM) | Seção no Plano (Fase 3) | Instrumentos e Ferramentas | Artefatos de Evidência | Níveis de Julgamento (Fase 2) |
| :--- | :---: | :--- | :---: | :--- | :--- | :--- |
| **M1 – TCBN** | Q1, H1 | $N_{ap}$, $N_{tot}$ | Seção 4.1 | Chrome, Firefox, Edge e Safari | Capturas de tela comparativas e checklist | Excelente: ≥ 95%<br>Bom: 85% a 94%<br>Satisfatório: 70% a 84%<br>Insuficiente: < 70% |
| **M2 – ICR** | Q2, H2 | $T_{conf}$, $T_{tot}$ | Seção 4.2 | DevTools Device Mode (5 viewports) | Capturas de tela com réguas e matriz de 20 pontos | Excelente: ≥ 95%<br>Bom: 80% a 94%<br>Satisfatório: 70% a 79%<br>Insuficiente: < 70% |
| **M3 – TSIS** | Q3, H3 | $Req_{ok}$, $Req_{tot}$ | Seção 4.3 | DevTools Network (Fetch/XHR) | Arquivos `.har` e capturas com status HTTP | Excelente: ≥ 98%<br>Bom: 90% a 97%<br>Satisfatório: 80% a 89%<br>Insuficiente: < 80% |

*Fonte: Elaborado pelos autores.*

---

## 9. Limitações Metodológicas e Mitigação de Riscos Éticos

1. **Acesso Não-Autenticado versus Áreas Restritas:** Parte dos serviços transacionais profundos exige login formal via Gov.br (com biometria facial ou conta bancária). A equipe mitiga qualquer risco jurídico ou de integridade executando os ensaios de interoperabilidade nas requisições públicas de handshake e direcionamento, sem expor dados pessoais reais.
2. **Prevenção de Sobrecarga de Servidores Governamentais:** Todos os ensaios de rede são executados manualmente ou com cadência espaçada (mínimo de 3 segundos entre chamadas), prevenindo bloqueios por firewall de aplicação web (*Web Application Firewall - WAF*) ou negação acidental de serviço.
3. **Ambiente Safari / WebKit:** Nos casos em que hardware Apple nativo com macOS não estiver disponível em tempo integral, o motor WebKit é inspecionado através de dispositivo móvel iPhone físico complementar associado ao ambiente de automação Playwright WebKit para validação de layout.
