/**
 * chatbot-resilience-fallback.js
 * 
 * Módulo de Resiliência e Fallback Cross-Browser do Chatbot (ISO/IEC 25040 - F4-C5)
 * Objeto: Portal Detran Digital DF (portal.detran.df.gov.br)
 * Autores: Artur Fernandes Galdino e Nicole Jovita Fernandes
 * Disciplina: Qualidade de Software 1 - UnB/FCTE (2026.2)
 *
 * Finalidade:
 * Tratar a falha de conexão detectada em navegadores Chromium (Microsoft Edge e Chrome)
 * onde a CDN externa da InBot retorna 'net::ERR_CONNECTION_RESET' no script
 * bot-loader-production.php ou em recursos de imagem associados.
 * 
 * Comportamento:
 * 1. Carrega o script do assistente de modo assíncrono com timeout seguro (3500ms).
 * 2. Em caso de sucesso (Firefox, Safari), inicializa normalmente o componente.
 * 3. Em caso de falha/timeout (Edge, Chrome), executa degradação graciosa (graceful degradation),
 *    ativando o canal alternativo nativo do Detran-DF (Central 154 / WhatsApp / FAQ) sem quebrar o layout.
 */

(function (window, document) {
  'use strict';

  const CONFIG = {
    cdnScriptUrl: 'https://inbot.detran.df.gov.br/bot-loader-production.php',
    timeoutMs: 3500,
    containerId: 'inbot-widget-container',
    fallbackElementId: 'detran-chatbot-fallback',
    centralTelefone: '154',
    whatsappUrl: 'https://api.whatsapp.com/send?phone=5561999999999&text=Ola%20Detran-DF'
  };

  const DetranChatbotManager = {
    status: 'INITIALIZING', // INITIALIZING | READY | FALLBACK_ACTIVE | ERROR
    loadStartTime: null,

    init: function () {
      this.loadStartTime = performance.now();
      this.injectChatbotWithResilience();
    },

    injectChatbotWithResilience: function () {
      const self = this;
      let timer = null;
      let scriptLoaded = false;

      // Criação dinâmica da tag script com crossorigin anônimo e defer
      const script = document.createElement('script');
      script.src = CONFIG.cdnScriptUrl;
      script.async = true;
      script.defer = true;

      const triggerFallback = (reason) => {
        if (scriptLoaded) return;
        scriptLoaded = true;
        clearTimeout(timer);
        
        self.status = 'FALLBACK_ACTIVE';
        console.warn(`[Detran Resiliencia] Falha ao carregar CDN InBot (${reason}). Ativando fallback nativo.`);
        self.renderFallbackInterface();
      };

      // Timeout preventivo caso a conexão seja derrubada ou fique em loop
      timer = setTimeout(() => {
        triggerFallback(`Timeout de conexao excedido (${CONFIG.timeoutMs}ms)`);
      }, CONFIG.timeoutMs);

      // Callback de sucesso
      script.onload = () => {
        if (scriptLoaded) return;
        scriptLoaded = true;
        clearTimeout(timer);

        self.status = 'READY';
        const loadDuration = (performance.now() - self.loadStartTime).toFixed(1);
        console.info(`[Detran Resiliencia] Assistente InBot carregado com sucesso em ${loadDuration}ms.`);
        self.applyResponsiveConstraints();
      };

      // Callback de erro de rede (ERR_CONNECTION_RESET, 404, CORS, etc.)
      script.onerror = () => {
        triggerFallback('Erro de rede ou conexao resetada (ERR_CONNECTION_RESET)');
      };

      document.head.appendChild(script);
    },

    applyResponsiveConstraints: function () {
      // Assegura que o container do chatbot herde as classes do patch de layout
      const container = document.getElementById(CONFIG.containerId);
      if (container) {
        container.classList.add('inbot-floating-widget-wrapper');
      }
    },

    renderFallbackInterface: function () {
      const container = document.getElementById(CONFIG.containerId);
      if (!container) return;

      container.innerHTML = `
        <div class="inbot-launcher-btn" id="detran-fallback-launcher" title="Canais de Atendimento Detran-DF" role="button" tabindex="0" aria-label="Abrir Atendimento Alternativo">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
          </svg>
        </div>
        <div class="detran-chatbot-fallback-modal" id="detran-fallback-popover" style="display: none;">
          <div class="detran-fallback-header">
            <strong>Atendimento Detran-DF</strong>
            <button type="button" class="detran-fallback-close" id="detran-fallback-close-btn" aria-label="Fechar">&times;</button>
          </div>
          <div class="detran-fallback-body">
            <p>O assistente virtual esta temporariamente indisponivel neste navegador. Acesse nossos canais diretos:</p>
            <ul style="list-style: none; padding: 0; margin: 8px 0; display: flex; flex-direction: column; gap: 8px;">
              <li><a href="tel:${CONFIG.centralTelefone}" class="detran-btn detran-btn-secondary" style="width: 100%; font-size: 13px;">Ligar para a Central 154</a></li>
              <li><a href="${CONFIG.whatsappUrl}" target="_blank" rel="noopener" class="detran-btn detran-btn-primary" style="width: 100%; font-size: 13px;">Atendimento via WhatsApp</a></li>
            </ul>
          </div>
        </div>
      `;

      // Event listeners para o popover nativo
      const launcher = document.getElementById('detran-fallback-launcher');
      const popover = document.getElementById('detran-fallback-popover');
      const closeBtn = document.getElementById('detran-fallback-close-btn');

      if (launcher && popover) {
        launcher.addEventListener('click', () => {
          popover.style.display = popover.style.display === 'none' ? 'block' : 'none';
        });
      }
      if (closeBtn && popover) {
        closeBtn.addEventListener('click', () => {
          popover.style.display = 'none';
        });
      }
    }
  };

  // Expor globalmente para testes e auditoria
  window.DetranChatbotManager = DetranChatbotManager;

  // Auto-inicializacao quando o DOM estiver pronto
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => DetranChatbotManager.init());
  } else {
    DetranChatbotManager.init();
  }
})(window, document);
