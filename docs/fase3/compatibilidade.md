# Plano de Avaliação – Característica: Compatibilidade

**Responsáveis:** Artur Fernandes Galdino e Nicole Jovita Fernandes  
**Característica:** Compatibilidade (ISO/IEC 25010:2023)  
**Subcaracterísticas:** Coexistência e Interoperabilidade  
**Módulos Avaliados:** Infração, Atendimento, Protocolo e Chatbot (Portal Detran Digital DF)  
**Fase Normativa:** Fase 3 (Projeto da Avaliação – ISO/IEC 25040)

!!! note "Status do Documento"
    Documento em desenvolvimento ativo pela dupla responsável (Artur Fernandes Galdino e Nicole Jovita Fernandes). A estrutura metodológica, a matriz de rastreabilidade e os roteiros operacionais de teste preliminares estão definidos. A execução empírica dos testes em produção no Portal Detran Digital DF será realizada na sequência para alimentação da Fase 4.

---

## 1. Método de Avaliação

A avaliação da característica de **Compatibilidade** fundamenta-se nos objetivos conceituais, questões operacionais e métricas formais estabelecidos na [Fase 2](../fase2/compatibilidade.md). O plano operacional divide-se nas duas subcaracterísticas normativas:

1. **Coexistência (*Co-existence*):**
   * Avaliação de conformidade funcional e de renderização visual entre diferentes navegadores de mercado (*Cross-browser*), vinculada à métrica **TCBN** ($Taxa\ de\ Compatibilidade\ Entre\ Navegadores$) e à Questão Q1.
   * Avaliação de adaptabilidade responsiva em diferentes resoluções de tela (*Cross-device*), vinculada à métrica **ICR** ($Índice\ de\ Conformidade\ Responsiva$) e à Questão Q2.
2. **Interoperabilidade (*Interoperability*):**
   * Avaliação de consistência das trocas de mensagens e integridade das requisições com serviços externos e barramentos de integração (Gov.br, sistemas bancários/PIX e SEI-GDF), vinculada à métrica **TSIS** ($Taxa\ de\ Sucesso\ de\ Integração\ de\ Serviços$) e à Questão Q3.

### 1.1 Visão Geral dos Métodos e Métricas

| Métrica | Questão GQM | O que é medido | Instrumento / Ferramenta | Procedimento de Coleta | Amostra Planejada |
| :--- | :---: | :--- | :--- | :--- | :---: |
| **M1 – TCBN** | Q1 | Paridade funcional e integridade de renderização entre navegadores | Google Chrome, Mozilla Firefox, Microsoft Edge e Apple Safari | Execução manual dos cenários funcionais centrais nos 4 navegadores | 4 cenários × 4 navegadores = 16 ensaios |
| **M2 – ICR** | Q2 | Ausência de quebras de layout, truncamentos e sobreposição de controles | Emulador responsivo DevTools em viewports padronizadas (Mobile: 360px e 414px; Tablet: 768px; Desktop: 1366px e 1920px) | Verificação de pontos de quebra (*breakpoints*), barras de rolagem horizontais e contenção de elementos de tela | 4 módulos × 5 viewports = 20 verificações |
| **M3 – TSIS** | Q3 | Taxa de requisições com status HTTP esperado (2xx e 3xx) em fluxos de integração externa | Aba *Rede (Network)* do DevTools do navegador e console de inspeção HTTP | Registro de chamadas REST/XHR durante as transações entre o portal e serviços externos | Monitoramento contínuo das chamadas nos fluxos de escopo |

**Tabela 1 – Visão geral dos métodos operacionais de Compatibilidade.** Fonte: Elaborado pelos autores.

---

## 2. Roteiros Operacionais de Teste por Módulo

Os testes contemplam os quatro módulos delimitados no escopo da [Fase 1](../fase1/escopo-limites.md). Para cada cenário, a inspeção registra evidências auditáveis (capturas de tela padronizadas e registros de tráfego de rede).

### 2.1 Cenários de Teste para Compatibilidade Cross-Browser (TCBN / Q1)

| Código | Módulo | Descrição do Fluxo Operacional | Critério de Sucesso do Ensaio |
| :---: | :--- | :--- | :--- |
| **TC-CB-01** | Infração | Acesso à tela de consulta de infrações, preenchimento de campos de validação e disparo da busca. | Renderização correta dos seletores, máscara de entrada preservada e resposta da interface sem travamento ou erro de script. |
| **TC-CB-02** | Atendimento | Navegação pelo fluxo de agendamento presencial e seleção de data no calendário interativo. | Calendário dinâmico responsivo aos cliques, renderização das datas disponíveis e transição para o seletor de horários. |
| **TC-CB-03** | Protocolo | Abertura do formulário de protocolo e expansão dos itens informativos. | Campos de texto editáveis, sanfonas (*accordions*) funcionais e preservação da hierarquia visual. |
| **TC-CB-04** | Chatbot | Abertura do botão flutuante de atendimento, expansão do painel de diálogo e envio de mensagem de teste. | Painel renderizado com posicionamento fixo correto, diálogo exibido na íntegra e sem sobreposição de botões de fechamento. |

**Tabela 2 – Cenários operacionais para o ensaio Cross-Browser.** Fonte: Elaborado pelos autores.

### 2.2 Cenários de Teste para Responsividade Multi-resolução (ICR / Q2)

As verificações de responsividade avaliam o comportamento visual sob cinco viewports padrão da indústria:

1. **Mobile Pequeno (360 x 640 px):** Resolução base para dispositivos móveis de entrada.
2. **Mobile Médio (414 x 896 px):** Resolução representativa de smartphones intermediários e avançados.
3. **Tablet (768 x 1024 px):** Modo retrato em telas intermediárias.
4. **Desktop HD (1366 x 768 px):** Resolução comum em notebooks e monitores corporativos.
5. **Desktop Full HD (1920 x 1080 px):** Resolução widescreen padrão de alta definição.

Para cada viewport nos 4 módulos, inspecionam-se três falhas críticas de coexistência:
* Ocorrência de rolagem horizontal não planejada (*horizontal overflow*).
* Truncamento ou ocultação indevida de textos explicativos ou labels de formulário.
* Sobreposição de elementos flutuantes (especialmente o botão do Chatbot sobre campos de dados ou botões de confirmação).

### 2.3 Cenários de Teste para Interoperabilidade e Integrações (TSIS / Q3)

| Código | Módulo | Ponto de Integração Externa | Verificação Técnica de Rede |
| :---: | :--- | :--- | :--- |
| **TC-IN-01** | Atendimento / Infração | Redirecionamento e handshake com o provedor de identidade Gov.br. | Verificação de URLs de retorno, parâmetros de autenticação e ausência de códigos HTTP de erro (4xx/5xx). |
| **TC-IN-02** | Infração | Emissão e download do documento de arrecadação (DUD / boleto / PIX). | Obtenção do payload de emissão com status HTTP 200, preservação do tipo MIME (PDF/imagem) e geração íntegra do código de barras/QR Code. |
| **TC-IN-03** | Protocolo | Troca de metadados com o barramento do Sistema Eletrônico de Informações (SEI-GDF). | Verificação do endpoint de consulta de processos e estabilidade da comunicação REST. |
| **TC-IN-04** | Chatbot | Comunicação XHR/WebSocket entre a interface do portal e a plataforma InBot/AWS. | Entrega e recebimento de pacotes de dados sem quebra de conexão ou erros de timeout em tempo real. |

**Tabela 3 – Cenários de interoperabilidade de serviços externos.** Fonte: Elaborado pelos autores.

---

## 3. Recursos e Ambientes de Medição

A realização das medições segue especificações de hardware, software e conectividade padronizadas:

* **Hardware de Teste:**
  * Estação de trabalho base com processador de múltiplos núcleos e memória RAM mínima de 16 GB.
  * Dispositivos móveis reais (Android e iOS) para contraprova e validação dos achados do emulador.
* **Navegadores em Escopo (Versões Estáveis):**
  * Google Chrome (v130 ou superior)
  * Mozilla Firefox (v131 ou superior)
  * Microsoft Edge (v130 ou superior)
  * Apple Safari (v17 ou superior em ambiente macOS / iOS e WebKit DevTools)
* **Condições de Rede:** Conexão estável de banda larga (superior a 50 Mbps) e testes adicionais sob latência simulada (perfil *Fast 3G* nas ferramentas DevTools para avaliar resiliência de interoperabilidade).

---

## 4. Cronograma Operacional e Janela de Execução

| Período | Atividade Operacional | Responsáveis |
| :--- | :--- | :--- |
| 12/11 a 14/11 | Elaboração dos roteiros e validação da bateria de testes preliminares | Artur Galdino e Nicole Jovita |
| 15/11 a 17/11 | Execução empírica nos 4 navegadores e nas 5 resoluções de tela | Artur Galdino e Nicole Jovita |
| 18/11 a 19/11 | Análise de tráfego de rede e coleta dos dados brutos de integração | Artur Galdino e Nicole Jovita |
| 20/11 a 21/11 | Consolidação dos dados brutos, cálculo das métricas e redação da Fase 4 | Artur Galdino e Nicole Jovita |

**Tabela 4 – Cronograma operacional de Compatibilidade.** Fonte: Elaborado pelos autores.

---

## 5. Matriz de Rastreabilidade (Fase 2 para Fase 3)

Esta matriz demonstra a aderência do planejamento operacional aos conceitos especificados na Fase 2:

| Métrica Formal (Fase 2) | Questão e Hipótese | Medidas Básicas | Roteiro Operacional (Fase 3) | Evidências Exigidas | Níveis de Pontuação (Fase 2) |
| :--- | :---: | :--- | :--- | :--- | :--- |
| **M1 – TCBN** | Q1, H1 | $N_{ap}$, $N_{tot}$ | Seção 2.1 (Tabela 2) | Capturas de tela comparativas nos 4 navegadores | Excelente: 100%<br>Bom: 75% a 99%<br>Regular: 50% a 74%<br>Insuficiente: < 50% |
| **M2 – ICR** | Q2, H2 | $N_{cp}$, $N_{res}$ | Seção 2.2 (Viewports) | Prints com réguas de resolução ativadas no DevTools | Excelente: 100%<br>Bom: 80% a 99%<br>Regular: 60% a 79%<br>Insuficiente: < 60% |
| **M3 – TSIS** | Q3, H3 | $R_{suc}$, $R_{tot}$ | Seção 2.3 (Tabela 3) | Logs de rede (.har ou prints com código HTTP) | Excelente: ≥ 98%<br>Bom: 95% a 97%<br>Regular: 90% a 94%<br>Insuficiente: < 90% |

**Tabela 5 – Matriz de rastreabilidade entre Fase 2 e Fase 3 para Compatibilidade.** Fonte: Elaborado pelos autores.

---

## 6. Limitações Metodológicas e Mitigação de Riscos

1. **Acesso Autenticado em Ambiente Governamental:** Certos serviços avançados de emissão e protocolo requerem autenticação formal pelo Gov.br com contas nível Prata ou Ouro. A equipe mitiga restrições executando os ensaios até o estágio imediatamente anterior à gravação definitiva ou pagamento real.
2. **Ambiente Safari:** A execução no motor WebKit/Safari requer hardware Apple dedicado ou contraprova direta em dispositivos móveis iPhone/iPad, evitando distorções decorrentes de motores alternativos.
3. **Flutuações de Terceiros:** A indisponibilidade de serviços bancários ou barramentos do GDF durante a janela de testes é registrada como evento externo com timestamp, não penalizando a métrica caso a causa raiz seja externa ao portal avaliado.
