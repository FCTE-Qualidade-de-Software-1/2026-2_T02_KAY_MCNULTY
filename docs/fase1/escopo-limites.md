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

## 3. Profundidade e Limites de Usabilidade 

A avaliação de Usabilidade abrange transversalmente os módulos de Infração, Atendimento, Protocolo e Chatbot, com foco em **Aprendibilidade**, **Operabilidade** e **Proteção contra Erros de Usuário**, conforme a especificação GQM registrada em [GQM – Característica: Usabilidade](../fase2/usabilidade.md).

### 3.1 Profundidade da avaliação nos quatro módulos

* **Módulo de Infração:** avaliar a facilidade de aprendizado durante a consulta de débitos e a compreensão das informações de infrações; observar a quantidade de passos necessários para emitir guias e acessar o código PIX; e verificar máscaras, validações e mensagens de orientação nos campos de placa, CPF e RENAVAM.
* **Módulo de Atendimento:** avaliar a facilidade de localizar unidades, compreender o calendário e selecionar datas e horários; observar a navegação e as áreas de toque em telas móveis; e verificar se há uma tela de confirmação com resumo dos dados antes da finalização do agendamento.
* **Módulo de Protocolo:** avaliar a clareza dos campos e da terminologia usada no cadastramento de processos; observar a quantidade de passos e o esforço necessário para anexar documentos em ambientes web e mobile; e verificar alertas sobre limites e formatos de arquivos, além da clareza das mensagens em caso de falha no envio.
* **Módulo Chatbot:** avaliar a compreensão do diálogo inicial e das opções disponíveis; observar a visibilidade e o posicionamento do componente em telas móveis, inclusive quando o teclado virtual está aberto; e verificar como o assistente responde a entradas vazias, incoerentes ou não reconhecidas e se oferece alternativas de recuperação.

### 3.2 Procedimentos e evidências

A inspeção será complementada por testes de tarefas guiadas com uma amostragem técnica reduzida de cidadãos e engenheiros avaliadores. Os registros devem permitir verificar a conclusão autônoma das tarefas, os passos/cliques realizados, os erros observados, as mensagens apresentadas e as possibilidades de recuperação. As evidências podem incluir registros de observação, capturas ou gravações de tela e planilhas de coleta, respeitando a privacidade dos participantes.

### 3.3 Limites do escopo e justificativas

* **Testes laboratoriais em larga escala:** não serão realizados testes presenciais de usabilidade com centenas de participantes, pois exigiriam infraestrutura e prazo incompatíveis com o planejamento acadêmico. Os resultados serão interpretados considerando o tamanho e o perfil da amostra efetivamente utilizada.
* **Auditoria avançada e exaustiva de acessibilidade:** embora a inclusão de pessoas com deficiência seja relevante para serviços públicos, esta etapa não contempla uma auditoria completa de acessibilidade com testes exaustivos de leitores de tela (por exemplo, NVDA e TalkBack), avaliação especializada de contraste e cobertura integral das diretrizes WCAG. Essas atividades ficam reservadas a estudos focados em acessibilidade.
* **Alteração do portal:** a avaliação é diagnóstica e adota a abordagem caixa-preta (*Black-Box Testing*). Não haverá alteração de código-fonte, refatoração ou aplicação direta de correções no ambiente de produção.

---

## 4. Profundidade e Limites de Confiabilidade (João e Davi)

> **[ESPAÇO RESERVADO PARA A DUPLA JOÃO E DAVI]**  
> Inserir aqui a profundidade de inspeção de Confiabilidade nos 4 módulos e os limites do escopo (ex.: medição de taxas de erro observáveis e persistência vs o que não será feito, como testes destrutivos de injeção de falhas ou derrubada forçada de servidores).
