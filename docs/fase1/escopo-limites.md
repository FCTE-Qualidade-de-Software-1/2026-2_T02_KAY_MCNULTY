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

> **[ESPAÇO RESERVADO PARA A DUPLA JOÃO E DAVI]**  
> Inserir aqui a profundidade de inspeção de Confiabilidade nos 4 módulos e os limites do escopo (ex.: medição de taxas de erro observáveis e persistência vs o que não será feito, como testes destrutivos de injeção de falhas ou derrubada forçada de servidores).
