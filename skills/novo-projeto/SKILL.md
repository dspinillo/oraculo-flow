---
name: novo-projeto
description: Cria um projeto novo seguindo a convenção Oráculo Flow — docs por nível, plano visual F0 com mockups, projeto e issues no Plane, memória. Use quando o usuário quiser começar um projeto/app/sistema novo.
---

# novo-projeto

Você vai criar um projeto seguindo a convenção Oráculo Flow (regras: `CLAUDE.md` do monorepo do usuário; se ainda não existir, rode antes a skill `oraculo-flow:instalar`). Checklist completo de referência: `${CLAUDE_PLUGIN_ROOT}/playbooks/novo-projeto.md`.

## Passos

1. **Definição** — pergunte via AskUserQuestion (o que ainda não estiver claro na conversa): nome+slug, tipo (`mobile`/`saas/web`/`vps-service`/`desktop`/`cli/script`/`misto`), nível (N1/N2/N3 — default N2), stack, one-liner, se já existe design definido, e fases iniciais imaginadas.

2. **Estrutura** — o destino depende do layout do usuário (está na seção Git do CLAUDE.md instalado; se ambíguo, pergunte):
   - **Monorepo**: crie `projects/<slug>/` na raiz do monorepo.
   - **Multi-repo**: pergunte onde ele guarda os repos, crie `<dir>/<slug>/` e rode `git init`.

   Em ambos, copie de `${CLAUDE_PLUGIN_ROOT}/templates/projeto/` os docs do nível (N1: README+STATUS · N2: +HANDOFF, ROADMAP, decisions/0001-stack.md · N3: tudo · tipo misto: +ARCHITECTURE mesmo em N2). Preencha todos os placeholders `{{...}}`; remova seções marcadas como "remover caso contrário" que não se aplicam.

3. **F0 — plano visual** — monte o artifact conforme `${CLAUDE_PLUGIN_ROOT}/templates/projeto/plano-visual.md`: carregue a skill `artifact-design`, escreva o HTML no scratchpad e publique via Artifact. Se tem UI e não há design definido: 2–3 variações de mockup por tela-chave, nomeadas, para o usuário escolher. Aguarde a escolha → registre `decisions/0002-design.md`. Ponha o link do artifact no README e ROADMAP.

4. **Plane** — `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/plane.py" create-project "<Nome>" --identifier <ID>` e depois `create-issue` para cada fase (F1..Fn) e para as tarefas TX.Y da fase corrente. Se faltar config/token, oriente: `PLANE_BASE_URL` e `PLANE_WORKSPACE` num `.env` na raiz do monorepo; token gerado em seu Plane → Workspace Settings → API tokens, salvo em `~/.config/plane/token`. Siga sem bloquear (registre a pendência no STATUS).

5. **Memória** — crie o memory file `<slug>-project.md` no auto-memory (tipo `project`: dir, package se houver, tipo, nível, fase, link do artifact) + linha no MEMORY.md.

6. **Git** — ofereça o commit do scaffold: `chore(<slug>): scaffold do projeto` no monorepo, `chore: scaffold do projeto` no multi-repo (não commite sem confirmação).

## Regras

- Nenhum código de produto antes do F0 aprovado pelo usuário.
- STATUS.md nasce com "Onde paramos" apontando a próxima ação real (▶️).
- (Modo monorepo) Repo standalone fora do monorepo só com ADR na raiz justificando.
