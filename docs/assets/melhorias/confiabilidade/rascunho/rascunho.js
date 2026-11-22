/*
 * Rascunho de formulário.
 * Guarda o preenchimento de um formulário no navegador e o restaura depois de
 * recarga da página, botão voltar ou retorno à aba. Não guarda senha, arquivo
 * nem campos marcados com data-sem-rascunho.
 */
(function (global) {
  'use strict';

  var PREFIXO = 'rascunho:';
  var VALIDADE_MS = 30 * 60 * 1000;
  var ATRASO_GRAVACAO_MS = 150;

  function armazenamento() {
    try {
      var teste = PREFIXO + 'teste';
      global.localStorage.setItem(teste, '1');
      global.localStorage.removeItem(teste);
      return global.localStorage;
    } catch (erro) {
      return null;
    }
  }

  function chaveDe(form) {
    return PREFIXO + (form.getAttribute('data-rascunho') || form.id);
  }

  function camposDe(form) {
    return Array.prototype.filter.call(form.elements, function (campo) {
      var tipo = campo.type;
      return campo.name && !campo.disabled &&
        tipo !== 'password' && tipo !== 'file' && tipo !== 'submit' &&
        tipo !== 'button' && !campo.hasAttribute('data-sem-rascunho');
    });
  }

  function valorDe(campo) {
    if (campo.type === 'checkbox') { return campo.checked; }
    if (campo.type === 'radio') { return campo.checked ? campo.value : null; }
    return campo.value;
  }

  function coletar(form) {
    var dados = {};
    camposDe(form).forEach(function (campo) {
      var valor = valorDe(campo);
      if (campo.type === 'radio') {
        if (valor !== null) { dados[campo.name] = valor; }
      } else {
        dados[campo.name] = valor;
      }
    });
    return dados;
  }

  function aplicar(campo, valor) {
    if (campo.type === 'checkbox') {
      campo.checked = valor === true;
    } else if (campo.type === 'radio') {
      campo.checked = campo.value === valor;
    } else {
      campo.value = valor;
    }
    campo.dispatchEvent(new Event('change', { bubbles: true }));
  }

  function lerRascunho(loja, form) {
    try {
      var bruto = loja.getItem(chaveDe(form));
      if (!bruto) { return null; }
      var registro = JSON.parse(bruto);
      if (!registro || Date.now() - registro.salvoEm > VALIDADE_MS) {
        loja.removeItem(chaveDe(form));
        return null;
      }
      return registro;
    } catch (erro) {
      return null;
    }
  }

  function iniciar(form, opcoes) {
    var configuracao = opcoes || {};
    var loja = armazenamento();
    var aviso = configuracao.aviso || null;
    var temporizador = null;

    if (!loja) { return { restaurado: false, descartar: function () {} }; }

    function gravar() {
      loja.setItem(chaveDe(form), JSON.stringify({ salvoEm: Date.now(), dados: coletar(form) }));
    }

    function agendarGravacao() {
      global.clearTimeout(temporizador);
      temporizador = global.setTimeout(gravar, ATRASO_GRAVACAO_MS);
    }

    function descartar() {
      global.clearTimeout(temporizador);
      loja.removeItem(chaveDe(form));
    }

    var registro = lerRascunho(loja, form);
    var restaurado = false;
    if (registro) {
      /* Restaura na ordem do formulário, para que campos dependentes (unidade, data, hora) sejam recriados antes do próximo. */
      camposDe(form).forEach(function (campo) {
        if (Object.prototype.hasOwnProperty.call(registro.dados, campo.name)) {
          aplicar(campo, registro.dados[campo.name]);
        }
      });
      restaurado = true;
      if (aviso) {
        var hora = new Date(registro.salvoEm).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' });
        aviso.textContent = 'Rascunho restaurado (salvo às ' + hora + '). Revise os campos antes de continuar.';
        aviso.hidden = false;
      }
    }

    form.addEventListener('input', agendarGravacao);
    form.addEventListener('change', agendarGravacao);
    form.addEventListener('submit', descartar);
    form.addEventListener('reset', descartar);

    return { restaurado: restaurado, descartar: descartar };
  }

  global.Rascunho = { iniciar: iniciar };
})(window);
