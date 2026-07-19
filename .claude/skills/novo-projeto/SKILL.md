---
name: novo-projeto
description: Cria um projeto novo no monorepo dh seguindo a convenção — docs por nível, plano visual F0 com mockups, projeto e issues no Plane, memória. Use quando o usuário quiser começar um projeto/app/sistema novo.
---

# /novo-projeto

Você vai criar um projeto seguindo a convenção do `dh/CLAUDE.md`. Checklist completo de referência: `playbooks/novo-projeto.md`.

## Passos

1. **Definição** — pergunte via AskUserQuestion (o que ainda não estiver claro na conversa): nome+slug, tipo (`mobile`/`saas/web`/`vps-service`/`desktop`/`cli/script`/`misto`), nível (N1/N2/N3 — default N2), stack, one-liner, se já existe design definido, e fases iniciais imaginadas.

2. **Estrutura** — crie `projects/<slug>/` copiando de `templates/projeto/` os docs do nível (N1: README+STATUS · N2: +HANDOFF, ROADMAP, decisions/0001-stack.md · N3: tudo · tipo misto: +ARCHITECTURE mesmo em N2). Preencha todos os placeholders `{{...}}`; remova seções marcadas como "remover caso contrário" que não se aplicam.

3. **F0 — plano visual** — monte o artifact conforme `templates/projeto/plano-visual.md`: carregue a skill `artifact-design`, escreva o HTML no scratchpad e publique via Artifact. Se tem UI e não há design definido: 2–3 variações de mockup por tela-chave, nomeadas, para o usuário escolher. Aguarde a escolha → registre `decisions/0002-design.md`. Ponha o link do artifact no README e ROADMAP.

4. **Plane** — `python3 scripts/plane.py create-project "<Nome>" --identifier <ID>` e depois `create-issue` para cada fase (F1..Fn) e para as tarefas TX.Y da fase corrente. Se o token não existir, oriente o usuário a gerar em seu Plane → Workspace Settings → API tokens → salvar em `~/.config/plane/token`, e siga sem bloquear (registre a pendência no STATUS).

5. **Memória** — crie o memory file `<slug>-project.md` no auto-memory (tipo `project`: dir, package se houver, tipo, nível, fase, link do artifact) + linha no MEMORY.md.

6. **Git** — ofereça o commit `chore(<slug>): scaffold do projeto` (não commite sem confirmação).

## Regras

- Nenhum código de produto antes do F0 aprovado pelo usuário.
- STATUS.md nasce com "Onde paramos" apontando a próxima ação real (▶️).
- Repo standalone fora do monorepo só com ADR na raiz justificando.
