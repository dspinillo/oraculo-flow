---
name: instalar
description: Instala a convenção Oráculo Flow no monorepo atual — CLAUDE.md com as regras, pasta projects/, config do Plane. Rodar uma vez por monorepo, logo após instalar o plugin.
---

# instalar

Você vai preparar o monorepo atual (raiz = diretório do projeto/git root) para a convenção Oráculo Flow.

## Passos

1. **CLAUDE.md** — copie `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` para a raiz do monorepo.
   - Se já existir um `CLAUDE.md`, NÃO sobrescreva: mostre ao usuário e proponha anexar a seção da convenção ao fim, ajustando conflitos.
   - Pergunte se o usuário quer ajustar: regras de commit, tipos de projeto que usa, modelos preferidos.
2. **Estrutura** — crie `projects/` (se não existir) e `decisions/` na raiz (para ADRs do monorepo).
3. **Plane (opcional)** — pergunte se o usuário usa Plane. Se sim: crie/complete o `.env` na raiz com `PLANE_BASE_URL=` e `PLANE_WORKSPACE=`, confirme que `.env` está no `.gitignore`, e oriente a gerar o API token (seu Plane → Workspace Settings → API tokens → salvar em `~/.config/plane/token`). Valide com `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/plane.py" list-projects`. Se não usa, siga — tudo funciona sem Plane.
4. **Confirme o resultado** — liste o que foi criado e explique os próximos comandos: `oraculo-flow:novo-projeto` para criar projeto, `oraculo-flow:migrar-projeto` para trazer um existente para o padrão.

## Regras

- Nunca sobrescrever arquivo existente sem mostrar e confirmar.
- Não commitar nada sem o usuário pedir.
