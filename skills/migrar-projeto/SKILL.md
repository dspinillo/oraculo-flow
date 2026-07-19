---
name: migrar-projeto
description: Migra um projeto existente para a convenção Oráculo Flow — classifica tipo/nível, normaliza nomes de docs, completa o kit, extrai ADRs, cria no Plane. Use ao trabalhar num projeto fora do padrão.
---

# migrar-projeto

Você vai fazer o retrofit de um projeto existente para a convenção. Siga o checklist completo em `${CLAUDE_PLUGIN_ROOT}/playbooks/migrar-projeto.md`, usando os esqueletos de `${CLAUDE_PLUGIN_ROOT}/templates/projeto/`.

Resumo do fluxo:

1. **Classificar** tipo e nível (confirme com o usuário via AskUserQuestion).
2. **Normalizar nomes** (`PLAN.md`→`ROADMAP.md`, `NEXT-SESSION.md`→fundir no `HANDOFF.md`, decisões em arquivo único→`decisions/NNNN-slug.md`).
3. **Completar o kit do nível** preenchendo com o estado REAL do projeto (não aspiracional); converter histórico de STATUS existente sem apagar nada.
4. **Plane** — criar projeto + issues das fases abertas (`${CLAUDE_PLUGIN_ROOT}/scripts/plane.py`), se o usuário usar Plane.
5. **Memória** — atualizar o memory file do projeto com tipo, nível e data da migração.
6. **Oferecer commit** `docs(<slug>): migra para a convenção` (não commitar sem confirmação).

Regra de ouro: migração documenta o que EXISTE; não inventa estado nem apaga histórico.
