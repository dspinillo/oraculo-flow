---
name: instalar
description: Instala a convenção Oráculo Flow — pergunta o layout (monorepo ou um repo por projeto), coloca o CLAUDE.md com as regras no lugar certo e configura o Plane opcional. Rodar uma vez, logo após instalar o plugin.
---

# instalar

Você vai preparar o ambiente do usuário para a convenção Oráculo Flow.

## Passos

1. **Layout** — pergunte via AskUserQuestion como o usuário organiza os projetos:
   - **Monorepo**: vários projetos num repo só (ex.: `~/dev/projects/<slug>/`).
   - **Multi-repo**: um repositório git por projeto.

2. **CLAUDE.md** — copie `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` para o destino do layout e **apague da seção Git o modo que não se aplica** (e o blockquote de aviso):
   - Monorepo → raiz do monorepo (as regras valem para todas as sessões ali).
   - Multi-repo → `~/.claude/CLAUDE.md` (nível de usuário: as regras seguem a pessoa em qualquer pasta).
   - Se o destino JÁ tiver um CLAUDE.md, NÃO sobrescreva: mostre e proponha anexar a seção da convenção, resolvendo conflitos com o usuário.
   - Pergunte se quer ajustar: regras de commit, tipos de projeto que usa, modelos preferidos.

3. **Estrutura** (só monorepo) — crie `projects/` e `decisions/` na raiz se não existirem.

4. **Plane (opcional)** — pergunte se usa Plane. Se sim:
   - Monorepo → `.env` na raiz com `PLANE_BASE_URL=` e `PLANE_WORKSPACE=` (confirme que `.env` está no `.gitignore`).
   - Multi-repo → `~/.config/plane/config` com as mesmas duas linhas (vale em qualquer pasta).
   - Token: gerar em seu Plane → Workspace Settings → API tokens → salvar em `~/.config/plane/token`.
   - Valide com `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/plane.py" list-projects`.
   - Se não usa, siga — tudo funciona sem Plane.

5. **Confirme o resultado** — liste o que foi criado/configurado (incluindo o layout escolhido) e explique os próximos comandos: `oraculo-flow:novo-projeto` para criar projeto, `oraculo-flow:migrar-projeto` para trazer um existente para o padrão.

## Regras

- Nunca sobrescrever arquivo existente sem mostrar e confirmar.
- Não commitar nada sem o usuário pedir.
