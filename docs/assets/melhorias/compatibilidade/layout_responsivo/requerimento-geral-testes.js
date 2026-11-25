/* Testes automáticos do protótipo (carregado só com ?teste=1).
   Roda no navegador e grava o resultado em <pre id="resultado-testes"> como JSON,
   lido por validar.py. Não mede o portal: mede o comportamento deste protótipo. */
(function () {
  "use strict";

  var modo = window.prototipo.modoAtual ? "atual" : "prototipo";

  function ev(el, tipo) { el.dispatchEvent(new Event(tipo, { bubbles: true })); }
  function digitar(id, valor) {
    var el = document.getElementById(id);
    el.value = valor;
    ev(el, "input");
  }
  function telaVisivel() {
    var ids = ["lista", "form", "revisao", "confirmacao"];
    for (var i = 0; i < ids.length; i++) {
      if (!document.getElementById("tela-" + ids[i]).hidden) return ids[i];
    }
    return "nenhuma";
  }
  function irParaForm() {
    document.querySelector('[data-ir="form"]').click();
    digitar("objeto", ""); digitar("placa", ""); digitar("renavam", "");
    document.getElementById("resumo-erros").hidden = true;
  }
  function enviar() { document.getElementById("form").requestSubmit(); }
  function msgVisivel(campo) {
    var el = document.getElementById("erro-" + campo);
    return !el.hidden && el.textContent.length > 0;
  }

  var resultados = [];
  function registrar(id, descricao, esperado, obtido) {
    resultados.push({
      id: id, modo: modo, descricao: descricao,
      esperado: esperado, obtido: obtido, passou: esperado === obtido
    });
  }

  /* Cenários de erro da linha de base (E-PRO-01, 08 e 09, EV-07):
     o resultado é "avancou" se o fluxo chegou à etapa de assinatura. */
  function cenarioErro(id, descricao, valores) {
    irParaForm();
    digitar("objeto", valores.objeto);
    digitar("placa", valores.placa);
    digitar("renavam", valores.renavam);
    enviar();
    var tela = telaVisivel();
    var avancou = tela === "revisao" || tela === "confirmacao";
    var comMensagem = msgVisivel(valores.campo);
    registrar(id, descricao + " – avançou sem bloquear?", modo === "atual" ? "sim" : "nao", avancou ? "sim" : "nao");
    if (modo === "prototipo") {
      registrar(id + "-msg", descricao + " – mensagem junto do campo?", "sim", comMensagem ? "sim" : "nao");
    }
  }

  var OK = { objeto: "Solicito informações sobre o prazo para renovação da minha CNH.", placa: "ABC1D23", renavam: "12345678900" };

  cenarioErro("E-PRO-01", "Objeto vazio",
    { objeto: "", placa: OK.placa, renavam: OK.renavam, campo: "objeto" });
  cenarioErro("E-PRO-08", "Placa incompleta",
    { objeto: OK.objeto, placa: "ABC12", renavam: OK.renavam, campo: "placa" });
  cenarioErro("E-PRO-09", "Renavam curto",
    { objeto: OK.objeto, placa: OK.placa, renavam: "1234567", campo: "renavam" });

  if (modo === "prototipo") {
    // Renavam com 11 números e dígito verificador errado.
    irParaForm();
    digitar("objeto", OK.objeto); digitar("placa", OK.placa); digitar("renavam", "12345678901");
    enviar();
    registrar("E-PRO-09b", "Renavam com dígito verificador errado – bloqueado?", "sim",
      telaVisivel() === "form" && msgVisivel("renavam") ? "sim" : "nao");

    // Campos opcionais vazios com objeto válido: deve seguir para a revisão.
    irParaForm();
    digitar("objeto", OK.objeto);
    enviar();
    registrar("F-01", "Placa e Renavam opcionais vazios – segue para a revisão?", "revisao", telaVisivel());

    // Fluxo válido completo.
    irParaForm();
    digitar("objeto", OK.objeto); digitar("placa", OK.placa); digitar("renavam", OK.renavam);
    enviar();
    registrar("F-02", "Dados válidos – chega à revisão?", "revisao", telaVisivel());
    var texto = document.getElementById("dados-revisao").textContent;
    registrar("F-03", "Revisão mostra os dados informados?", "sim",
      texto.indexOf(OK.objeto) >= 0 && texto.indexOf(OK.placa) >= 0 && texto.indexOf(OK.renavam) >= 0 ? "sim" : "nao");
    registrar("F-04", "Botão de assinatura começa desabilitado?", "sim",
      document.getElementById("btn-assinar").disabled ? "sim" : "nao");
    var avisoVisivel = !!document.querySelector(".rg-aviso") &&
      document.querySelector(".rg-aviso").textContent.indexOf("validade legal") >= 0;
    registrar("F-05", "Aviso sobre a validade legal está na revisão?", "sim", avisoVisivel ? "sim" : "nao");

    // Voltar e editar mantém os dados.
    document.querySelector('#tela-revisao [data-ir="form-editar"]').click();
    registrar("F-06", "Voltar e editar mantém o que foi digitado?", "sim",
      telaVisivel() === "form" && document.getElementById("objeto").value === OK.objeto ? "sim" : "nao");

    // Confirmar a revisão habilita a assinatura.
    enviar();
    var chk = document.getElementById("confirma-revisao");
    chk.checked = true; ev(chk, "change");
    registrar("F-07", "Marcar a ciência habilita o botão?", "sim",
      document.getElementById("btn-assinar").disabled ? "nao" : "sim");
    document.getElementById("btn-assinar").click();
    registrar("F-08", "Chega à etapa de assinatura (simulada)?", "confirmacao", telaVisivel());

    // Acessibilidade mínima verificável por código.
    irParaForm();
    digitar("objeto", ""); digitar("placa", "ABC12"); digitar("renavam", "");
    enviar();
    var invalido = document.getElementById("placa").getAttribute("aria-invalid") === "true";
    registrar("A-01", "Campo inválido recebe aria-invalid?", "sim", invalido ? "sim" : "nao");
    registrar("A-02", "Resumo de erros tem role=alert?", "sim",
      document.getElementById("resumo-erros").getAttribute("role") === "alert" ? "sim" : "nao");

    /* Compatibilidade: o avatar do assistente não pode cobrir botões de ação (mesmo critério do ICR da
       melhoria de compatibilidade). Mede a área de interseção (px²) em cada tela, no topo e no fim da página.
       Campos de texto não entram: o avatar flutuante pode cobri-los em alguns pontos da rolagem. */
    var largura = window.innerWidth;
    var lancador = document.querySelector(".inbot-launcher-btn");
    function visivel(el) {
      var r = el.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && !el.closest("[hidden]");
    }
    function sobreposicao() {
      var a = lancador.getBoundingClientRect();
      var total = 0;
      document.querySelectorAll(".detran-btn, .rg-subbarra button").forEach(function (el) {
        if (!visivel(el)) return;
        var b = el.getBoundingClientRect();
        var w = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        var h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        if (w > 0 && h > 0) total += w * h;
      });
      return Math.round(total);
    }
    function medirTela(nome) {
      window.scrollTo(0, 0);
      var topo = sobreposicao();
      window.scrollTo(0, document.documentElement.scrollHeight);
      var fim = sobreposicao();
      window.scrollTo(0, 0);
      registrar("C-" + nome, "Avatar do assistente sem sobrepor botões de ação (" + largura + " px), tela " + nome, "0", String(topo + fim));
    }
    if (lancador) {
      irParaForm(); medirTela("form");
      digitar("objeto", OK.objeto); enviar(); medirTela("revisao");
      var chk2 = document.getElementById("confirma-revisao");
      chk2.checked = true; ev(chk2, "change");
      document.getElementById("btn-assinar").click(); medirTela("confirmacao");
    } else {
      registrar("C-launcher", "Avatar do assistente presente na página", "sim", "nao");
    }
  } else {
    // Linha de base: o fluxo vai direto à assinatura, sem revisão.
    irParaForm();
    digitar("objeto", OK.objeto); digitar("placa", OK.placa); digitar("renavam", OK.renavam);
    enviar();
    registrar("F-02", "Dados válidos – vai direto à assinatura, sem revisão?", "confirmacao", telaVisivel());
  }

  var saida = document.createElement("pre");
  saida.id = "resultado-testes";
  saida.textContent = JSON.stringify(resultados);
  document.body.appendChild(saida);
})();
