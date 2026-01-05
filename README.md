# 📧 Mota Email Signatures

Este é um projeto simples de **freelance** focado no desenvolvimento e padronização de assinaturas de e-mail corporativas. O objetivo principal foi criar modelos profissionais, compatíveis com diversos clientes de e-mail (especialmente Outlook) e explorar automações com Python.

> ⚠️ **Nota:** Este repositório serve como um registro de aprendizado sobre renderização de HTML em e-mails, compatibilidade entre clients e manipulação de assets. Não é uma aplicação complexa, apenas um conjunto de soluções práticas.

---

## 🎯 Objetivos do Projeto

*   **Design Profissional:** Criação de assinaturas visuais para as marcas *Futura*, *Vitória* e *Grupo Teixeira Mota*.
*   **Compatibilidade (Cross-Client):** Desafio de fazer o HTML funcionar corretamente no **Outlook Desktop**, Gmail e Mobile.
    *   *Aprendizado:* O uso de `<table>` ainda é rei para e-mails. CSS moderno (`flexbox`, `grid`, `gradients`) muitas vezes quebra em clientes legados.
*   **Versões Offline vs Online:**
    *   **Online:** Imagens hospedadas externamente (GitHub Pages) para manter o e-mail leve.
    *   **Offline:** Imagens embutidas em **Base64** para garantir que a assinatura apareça mesmo sem conexão ou bloqueio de imagens externas.

---

## 🛠️ Tecnologias e Ferramentas

*   **HTML5 & CSS3:** Uso extensivo de tabelas HTML e estilos inline para garantir a renderização correta.
*   **Python 🐍:** Scripts criados para automatizar tarefas repetitivas:
    *   `resize_logos.py`: Redimensionamento automático de logotipos com alta qualidade (Lanczos).
    *   `resize_fotos.py`: Padronização de fotos de perfil (90x90px) e remoção de fundo.
    *   `convert_to_base64.py`: Script para converter assinaturas HTML "online" em versões "offline" (substituindo URLs por strings Base64 gigantes).
    *   `convert_images_to_base64.py`: Gera arquivos `.txt` com o código Base64 de todas as imagens da pasta `etc/` para uso rápido.

---

## 📂 Estrutura do Projeto

*   `/Aprovadas`: Modelos finais validados pelo cliente.
    *   `/offline`: Versões autocontidas (pesadas) com imagens embutidas.
*   `/Entrega` & `/Entrega2`: Versões anteriores e iterações de design (Pill buttons, designs circulares, etc.).
*   `/etc`: Recursos e assets (Imagens originais, ícones, scripts de redimensionamento).
    *   `/base64`: Banco de imagens convertidas em texto para fácil acesso.

---

## 🚀 Como usar (Aprendizado)

Se você está aprendendo sobre assinaturas de e-mail, aqui vai a dica de ouro deste projeto:

1.  **Copie e Cole:** A melhor maneira de instalar uma assinatura no Outlook não é importando o arquivo, mas abrindo o HTML no navegador, dando `Ctrl+A` (Selecionar tudo), `Ctrl+C` e colando diretamete no editor de assinatura do Outlook.
2.  **Base64:** É útil para testes e uso offline, mas aumenta drasticamente o tamanho do e-mail (KB/MB), o que pode alertar filtros de spam. Use com moderação.

---

### Autor

Natã Felix - *Freelance & Estudos*
