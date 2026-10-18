# Escopo, Profundidade e Limites da Avaliação

## 1. Escopo e Objetos de Avaliação

A avaliação da qualidade de produto de software abrange transversalmente os quatro módulos operacionais do portal Detran Digital DF: **Infrações**, **Atendimento**, **Protocolo** e **Chatbot**.

Para assegurar rigor técnico e validade científica, cada dupla estabelece a profundidade da análise de sua respectiva característica sobre os 4 módulos, bem como os cortes metodológicos explícitos (o que fica de fora e a justificativa técnica).

---

## 2. Profundidade e Limites de Compatibilidade

A avaliação da característica de Compatibilidade abrange transversalmente os quatro módulos operacionais do Detran Digital DF, delimitando com rigor técnico a profundidade investigada e os cortes metodológicos necessários:

### 2.1 Profundidade da Avaliação nos 4 Módulos
* **Módulo de Infração:** Análise de coexistência *cross-browser* (Chrome, Firefox, Edge, Safari) e responsividade na renderização das tabelas de autos de infração e na visualização/emissão de guias em PDF e código PIX em ambientes desktop e mobile; e verificação da interoperabilidade através da inspeção das chamadas de rede (status HTTP de resposta dos serviços de consulta de débitos e geração de guias bancárias).
* **Módulo de Atendimento:** Análise de coexistência durante a renderização interativa do componente de calendário e seleção de vagas em diferentes larguras de viewport (mobile de 360px a desktop de 1920px); e verificação da interoperabilidade quanto ao carregamento dinâmico assíncrono dos postos de atendimento disponíveis.
* **Módulo de Protocolo:** Análise de coexistência dos formulários de preenchimento e no comportamento responsivo da área de *upload* de arquivos e documentos comprobatórios em telas menores; e verificação da interoperabilidade quanto ao disparo de requisições de envio de processo e persistência de anexos sem quebra de sessão.
* **Módulo Chatbot:** Análise de coexistência da janela/widget flutuante do assistente virtual (verificando se o botão não sobrepõe campos essenciais e se o teclado mobile não quebra o layout); e verificação da interoperabilidade quanto à troca íntegra de mensagens via requisições de API de NLP.

### 2.2 O que Fica de Fora (Limites do Escopo) e Justificativas Técnicas
* **Navegadores obsoletos e descontinuados (ex.: Internet Explorer):** O suporte oficial ao Internet Explorer foi descontinuado e os padrões modernos de interface (CSS Flexbox/Grid e ES6+) requerem navegadores com ciclo de atualização contínua (*evergreen browsers*). A avaliação restringe-se aos líderes contemporâneos de mercado (Chrome, Firefox, Edge e Safari).
* **Testes de carga massiva ou estresse nas APIs de integração:** Como a auditoria ocorre externamente em ambiente real de produção do Detran-DF (sem ambiente de homologação dedicado), testes de carga com milhares de requisições simultâneas poderiam degradar a infraestrutura pública ou caracterizar ataque de negação de serviço (DoS). Portanto, a interoperabilidade é avaliada por amostragem funcional pontual de requisições.
* **Inspeção interna de código-fonte, bancos de dados ou barramentos do GDF:** A equipe não possui credenciais de acesso aos repositórios internos do governo nem aos servidores do SEI/SENATRAN. A avaliação adota rigorosamente a abordagem de teste caixa-preta (*Black-Box Testing*), limitando-se ao comportamento observável a partir da camada do cliente (browser e tráfego HTTP exposto).

---

## 3. Profundidade e Limites de Usabilidade (Natan e Yan)

> **[ESPAÇO RESERVADO PARA A DUPLA NATAN E YAN]**  
> Inserir aqui a profundidade de inspeção de Usabilidade nos 4 módulos e os limites do escopo (ex.: métodos de avaliação heurística e testes de tarefas vs o que não será feito, como testes laboratoriais presenciais com centenas de usuários).

---

## 4. Profundidade e Limites de Confiabilidade (João e Davi)

A Confiabilidade é avaliada nos quatro módulos do produto, considerando as subcaracterísticas **Disponibilidade**, **Ausência de Falhas** (*Maturidade* na edição de 2011 da ISO/IEC 25010), **Tolerância a Falhas** e **Recuperabilidade**. Por se tratar de uma auditoria externa em ambiente de produção, a avaliação é inferida apenas pelo comportamento observável no cliente.

### 4.1 Profundidade da Avaliação nos 4 Módulos
* **Módulo de Infração:** Monitoramento das páginas públicas; execução repetida da consulta de débitos, do detalhamento do auto e da emissão da guia (DUD/PIX), sem pagamento; entradas anômalas (placa, CPF e RENAVAM inválidos, campos vazios, envio duplicado); e interrupções (recarga e perda de conexão).
* **Módulo de Atendimento:** Carregamento de unidades, datas e horários; agendamento até a etapa anterior à confirmação definitiva; e cenários como horário indisponível, envio duplicado, botão voltar e sessão invalidada. A confirmação só ocorre se houver cancelamento imediato, para não subtrair vagas reais.
* **Módulo de Protocolo:** Preenchimento e anexação até a etapa anterior ao envio definitivo; arquivos inválidos; interrupção durante o *upload*; e preservação dos dados após recarga ou perda de conexão. Não são protocolados processos sem finalidade real, a fim de evitar registros indevidos no SEI-GDF.
* **Módulo Chatbot:** Monitoramento da disponibilidade; diálogos de perguntas frequentes; mensagens vazias, extensas ou com caracteres especiais; e comportamento da conversa após recarga ou perda de conexão.

### 4.2 O que Fica de Fora (Limites do Escopo) e Justificativas Técnicas
* **Engenharia do caos e injeção de falhas:** A equipe não controla a infraestrutura, e provocar falhas em serviço público em produção causaria dano direto aos cidadãos.
* **Testes de carga, estresse e resistência:** Poderiam degradar o serviço ou caracterizar negação de serviço (DoS). O comportamento sob picos de demanda não é avaliado, o que limita a validade dos resultados.
* **Métricas internas:** Tempo médio entre falhas (MTBF), tempo médio de reparo (MTTR), *logs*, *failover*, *backup* e recuperação de desastres exigem acesso a servidores e registros internos. A Recuperabilidade é avaliada somente pela ótica do usuário.
* **Automação de fluxos autenticados via Gov.br:** Depende de credenciais pessoais e fatores adicionais de verificação. Esses fluxos são executados manualmente, e o monitoramento automatizado restringe-se a recursos públicos.
* **Variação entre navegadores e resoluções:** É objeto da Compatibilidade (Seção 2). Aqui adota-se uma configuração de referência, definida na Fase 3.
* **Generalização temporal:** Os resultados valem apenas para o período de observação e não permitem extrapolar a disponibilidade anual. Manutenções programadas divulgadas pelo órgão são registradas à parte.
