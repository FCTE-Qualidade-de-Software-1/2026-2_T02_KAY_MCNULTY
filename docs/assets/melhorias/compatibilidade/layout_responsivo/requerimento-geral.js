/* Protótipo de alta fidelidade – Requerimento Geral (Protocolo), integrado às telas do portal.
   Dados fictícios. Sem rede, sem armazenamento e sem assinatura real.

   Parâmetros de URL:
     ?estado=vazio | padrao | erro | revisao | confirmacao   abre direto no estado
     ?modo=atual    reproduz o portal atual: sem validação e sem revisão (linha de base)
*/
(function () {
  "use strict";

  var params = new URLSearchParams(window.location.search);
  var MODO_ATUAL = params.get("modo") === "atual";

  var telas = {
    lista: document.getElementById("tela-lista"),
    form: document.getElementById("tela-form"),
    revisao: document.getElementById("tela-revisao"),
    confirmacao: document.getElementById("tela-confirmacao")
  };
  var form = document.getElementById("form");
  var campos = {
    objeto: document.getElementById("objeto"),
    placa: document.getElementById("placa"),
    renavam: document.getElementById("renavam")
  };
  var resumo = document.getElementById("resumo-erros");
  var listaErros = document.getElementById("lista-erros");
  var contador = document.getElementById("contador-objeto");
  var confirma = document.getElementById("confirma-revisao");
  var btnAssinar = document.getElementById("btn-assinar");

  /* ---------- Regras de validação (O1) ---------- */

  function validarObjeto(v) {
    var t = v.trim();
    if (t.length === 0) {
      return "Informe o objeto do requerimento. Descreva o que você precisa, por exemplo: \"Solicito informações sobre o prazo para renovação da CNH\".";
    }
    if (t.length < 10) {
      return "Descreva o pedido com um pouco mais de detalhe (mínimo de 10 caracteres).";
    }
    return "";
  }

  function validarPlaca(v) {
    var t = v.trim().toUpperCase();
    if (t === "") return "";                       // campo opcional
    var limpa = t.replace("-", "");
    if (limpa.length < 7) {
      return "A placa está incompleta. Use 7 caracteres, como ABC1D23 ou ABC-1234.";
    }
    if (!/^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$/.test(limpa)) {
      return "A placa não tem um formato válido. Use 3 letras e 4 caracteres, como ABC1D23 ou ABC-1234.";
    }
    return "";
  }

  function digitoRenavam(base10) {
    var pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2];
    var soma = 0;
    for (var i = 0; i < 10; i++) soma += parseInt(base10.charAt(i), 10) * pesos[i];
    return ((soma * 10) % 11) % 10;
  }

  function validarRenavam(v) {
    var t = v.trim();
    if (t === "") return "";                       // campo opcional
    if (!/^[0-9]+$/.test(t)) {
      return "O Renavam deve ter apenas números, sem pontos nem traços.";
    }
    if (t.length < 11) {
      return "O Renavam está incompleto. Ele tem 11 números e você digitou " + t.length + ".";
    }
    if (digitoRenavam(t.substring(0, 10)) !== parseInt(t.charAt(10), 10)) {
      return "Esse Renavam não confere. Revise os números no documento do veículo.";
    }
    return "";
  }

  var validadores = { objeto: validarObjeto, placa: validarPlaca, renavam: validarRenavam };
  var rotulos = { objeto: "Objeto do requerimento", placa: "Placa do veículo", renavam: "Renavam" };

  /* ---------- Máscaras leves ---------- */

  campos.placa.addEventListener("input", function () {
    var v = campos.placa.value.toUpperCase().replace(/[^A-Z0-9-]/g, "");
    campos.placa.value = v;
  });
  campos.renavam.addEventListener("input", function () {
    campos.renavam.value = campos.renavam.value.replace(/[^0-9]/g, "");
  });
  campos.objeto.addEventListener("input", function () {
    contador.textContent = campos.objeto.value.length + " de 500 caracteres";
  });

  /* ---------- Mensagens por campo ---------- */

  function mostrarErro(nome, msg) {
    var el = document.getElementById("erro-" + nome);
    var campo = campos[nome];
    if (msg) {
      el.textContent = msg;
      el.hidden = false;
      campo.setAttribute("aria-invalid", "true");
    } else {
      el.textContent = "";
      el.hidden = true;
      campo.removeAttribute("aria-invalid");
    }
  }

  function validarTudo() {
    var erros = [];
    Object.keys(validadores).forEach(function (nome) {
      var msg = validadores[nome](campos[nome].value);
      mostrarErro(nome, msg);
      if (msg) erros.push({ nome: nome, msg: msg });
    });
    listaErros.innerHTML = "";
    erros.forEach(function (e) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = "#" + e.nome;
      a.textContent = rotulos[e.nome] + ": " + e.msg.split(/(?<=\.)\s/)[0];
      a.addEventListener("click", function (ev) {
        ev.preventDefault();
        campos[e.nome].focus();
      });
      li.appendChild(a);
      listaErros.appendChild(li);
    });
    resumo.hidden = erros.length === 0;
    return erros;
  }

  // Valida ao sair do campo, para a pessoa corrigir sem esperar o envio.
  Object.keys(campos).forEach(function (nome) {
    campos[nome].addEventListener("blur", function () {
      if (MODO_ATUAL) return;
      if (campos[nome].value === "" && !campos[nome].hasAttribute("aria-invalid")) return;
      mostrarErro(nome, validadores[nome](campos[nome].value));
    });
    campos[nome].addEventListener("input", function () {
      if (campos[nome].hasAttribute("aria-invalid")) {
        mostrarErro(nome, validadores[nome](campos[nome].value));
      }
    });
  });

  /* ---------- Navegação entre telas ---------- */

  var primeiraTela = true;
  function mostrar(nome) {
    Object.keys(telas).forEach(function (k) { telas[k].hidden = k !== nome; });
    var titulo = telas[nome].querySelector("h1");
    // Foco no título só depois da primeira navegação, para leitores de tela.
    if (titulo && !primeiraTela) titulo.focus({ preventScroll: false });
    primeiraTela = false;
  }

  function linha(dt, valor, vazio) {
    var d = document.createElement("div");
    var t = document.createElement("dt");
    var v = document.createElement("dd");
    t.textContent = dt;
    if (valor) { v.textContent = valor; } else { v.textContent = vazio || "Não informado"; v.className = "vazio"; }
    d.appendChild(t); d.appendChild(v);
    return d;
  }

  function preencherResumo(destino) {
    destino.innerHTML = "";
    destino.appendChild(linha("Objeto", campos.objeto.value.trim()));
    destino.appendChild(linha("Placa", campos.placa.value.trim().toUpperCase(), "Não informada"));
    destino.appendChild(linha("Renavam", campos.renavam.value.trim(), "Não informado"));
  }

  function irParaRevisao() {
    preencherResumo(document.getElementById("dados-revisao"));
    confirma.checked = false;
    btnAssinar.disabled = true;
    mostrar("revisao");
  }

  function irParaAssinatura() {
    preencherResumo(document.getElementById("dados-documento"));
    mostrar("confirmacao");
  }

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    if (MODO_ATUAL) {
      // Linha de base: avança sem validar e sem revisão.
      irParaAssinatura();
      return;
    }
    var erros = validarTudo();
    if (erros.length) {
      resumo.focus();
      return;
    }
    irParaRevisao();
  });

  confirma.addEventListener("change", function () {
    btnAssinar.disabled = !confirma.checked;
  });
  btnAssinar.addEventListener("click", function () {
    if (!btnAssinar.disabled) irParaAssinatura();
  });

  document.addEventListener("click", function (ev) {
    var alvo = ev.target.closest("[data-ir]");
    if (!alvo) return;
    var destino = alvo.getAttribute("data-ir");
    if (destino === "form" || destino === "form-editar") mostrar("form");
    else if (destino === "lista") mostrar("lista");
    else if (destino === "lista-reiniciar") {
      form.reset();
      Object.keys(campos).forEach(function (n) { mostrarErro(n, ""); });
      resumo.hidden = true;
      contador.textContent = "0 de 500 caracteres";
      mostrar("lista");
    }
  });

  /* ---------- Estados para avaliação e capturas ---------- */

  var OBJETO_OK = "Solicito informações sobre o prazo para renovação da minha CNH.";
  var PLACA_OK = "ABC1D23";
  var RENAVAM_OK = "12345678900"; // fictício, com dígito verificador válido

  function preencher(o, p, r) {
    campos.objeto.value = o; campos.placa.value = p; campos.renavam.value = r;
    contador.textContent = o.length + " de 500 caracteres";
  }

  function iniciar() {
    if (MODO_ATUAL) {
      document.getElementById("selo-modo").hidden = false;
      document.getElementById("bloco-etapas").hidden = true;
      document.getElementById("exemplo-objeto").hidden = true;
    }
    var estado = params.get("estado") || "vazio";
    switch (estado) {
      case "padrao":
        mostrar("form");
        break;
      case "erro":
        preencher("", "ABC12", "1234567");
        mostrar("form");
        validarTudo();
        break;
      case "revisao":
        preencher(OBJETO_OK, PLACA_OK, RENAVAM_OK);
        irParaRevisao();
        break;
      case "confirmacao":
        preencher(OBJETO_OK, PLACA_OK, RENAVAM_OK);
        irParaAssinatura();
        break;
      default:
        mostrar("lista");
    }
  }

  // Menu do cabeçalho em telas estreitas (botão de menu abre e fecha a lista).
  var menuBotao = document.getElementById("rg-menu-botao");
  var nav = document.getElementById("rg-nav");
  if (menuBotao && nav) {
    menuBotao.addEventListener("click", function () {
      var aberto = nav.classList.toggle("aberto");
      menuBotao.setAttribute("aria-expanded", aberto ? "true" : "false");
    });
  }

  // Exposto para o script de validação automática.
  window.prototipo = {
    validarObjeto: validarObjeto,
    validarPlaca: validarPlaca,
    validarRenavam: validarRenavam,
    modoAtual: MODO_ATUAL
  };

  iniciar();

  // Testes automáticos, só quando pedidos por ?teste=1 (usado por validar.py).
  if (params.get("teste") === "1") {
    var t = document.createElement("script");
    t.src = "requerimento-geral-testes.js";
    document.body.appendChild(t);
  }
})();
