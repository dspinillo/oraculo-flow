# Oráculo Flow

**Uma convenção de desenvolvimento com IA para quem toca vários projetos sozinho.**

Sistema de organização para monorepos pessoais tocados com agentes (Claude Code, Codex): documentação padronizada por porte de projeto, planejamento visual antes de código, fatiamento em fases/tarefas com issues no [Plane](https://plane.so), e orquestração multi-agente (planner, builder, tester, documenter) com confronto entre LLMs.

A premissa central: **a continuidade vive nos docs, não na sessão.** Qualquer sessão — sua, do Claude, do Codex, de amanhã ou de daqui a seis meses — retoma qualquer projeto lendo `STATUS.md` → `HANDOFF.md`. O modelo esquece; o repo não.

## Como funciona

```
ideia ──▶ /novo-projeto ──▶ F0: plano visual ──▶ você aprova ──▶ F1..Fn
              │                (artifact web:         │
              │                 arquitetura,          └─ fases → tarefas TX.Y → fatias
              │                 mockups 2-3 opções,      issues no Plane
              │                 fatiamento)              orquestração multi-agente
              │
              └─ scaffold de docs + projeto no Plane + memória
```

### Os pilares

1. **Docs por nível de porte** — experimento (N1) leva 2 arquivos; produto (N3) leva o kit completo. Sem overhead onde não se paga. Ver `CLAUDE.md`.
2. **F0 visual** — nenhum código antes de um plano em artifact web com funcionalidades, arquitetura e 2–3 variações de mockup por tela-chave. Escolher direção olhando telas é mais barato que refatorar depois.
3. **Fatiamento com contrato** — fases → tarefas `TX.Y` (Objetivo/Passos/Critérios de aceite/Depende de) → fatias que buildam sozinhas. Espelhadas como issues no Plane.
4. **ADRs curtos** — toda decisão de arquitetura vira `decisions/NNNN-slug.md` (Contexto/Decisão/Consequências) com o porquê. Discussão não volta.
5. **Orquestração multi-agente** — a sessão principal é o Manager (nunca coda direto); planner/builder/tester/documenter são subagents com contrato de entrada/saída. Confronto entre Claude e GPT é padrão em tarefa ambígua: dois planos às cegas, divergência = sinal de risco. Ver `templates/agents/WORKFLOW.md`.
6. **Protocolo de sessão** — ao encerrar, STATUS ganha o "Onde paramos" e a sessão anterior colapsa em `<details>`; o histórico inteiro fica preservado e o topo fica legível.

## Estrutura deste repo

```
oraculo-flow/
├── CLAUDE.md               # as regras (vai para a raiz do SEU monorepo)
├── templates/
│   ├── projeto/            # esqueletos: README, STATUS, HANDOFF, ROADMAP, PRD,
│   │                       #   ARCHITECTURE, CHANGELOG, CLAUDE.md, ADR, plano-visual
│   └── agents/             # WORKFLOW + personas Manager/Planner/Builder/Tester/Documenter
├── playbooks/
│   ├── novo-projeto.md     # checklist de criação (o que a skill automatiza)
│   └── migrar-projeto.md   # retrofit de projeto existente, sob demanda
├── scripts/plane.py        # CLI da API do Plane (stdlib pura): projetos + issues
└── .claude/
    ├── skills/novo-projeto # skill /novo-projeto para o Claude Code
    └── agents/             # planner, builder, tester, documenter executáveis
```

## Como adotar

1. **Copie para o seu monorepo**: `CLAUDE.md`, `templates/`, `playbooks/`, `scripts/` e `.claude/` para a raiz. Projetos vivem em `projects/<slug>/`.
2. **Configure o Plane** (opcional — dá para usar tudo sem ele): crie um `.env` na raiz com `PLANE_BASE_URL=...` e `PLANE_WORKSPACE=...` (self-hosted ou `https://api.plane.so`), gere um API token no Plane e salve em `~/.config/plane/token`. Teste: `python3 scripts/plane.py list-projects`.
3. **Ajuste o CLAUDE.md** ao seu contexto (tipos de projeto que você usa, regras de commit, modelos preferidos).
4. **Crie o primeiro projeto**: abra o Claude Code na raiz e rode `/novo-projeto` com seu briefing — ideia, prints de referência, restrições, tudo. A skill pergunta o que faltar, monta a estrutura, publica o plano visual e para na sua aprovação.

Requisitos: [Claude Code](https://claude.com/claude-code) (skills + subagents); Python 3.10+ para o `scripts/plane.py`; plugin Codex (opcional) para o confronto entre LLMs.

## Filosofia

Este método foi destilado de um projeto real que acumulou 37 ADRs, 100+ KB de changelog e trocas de frente entre iOS, Android e backend sem perder o fio — e depois generalizado para um monorepo com 15+ projetos. As escolhas têm cicatriz por trás:

- **CHANGELOG como fonte de verdade** porque checkboxes de plano mentem.
- **"Honestidade de escopo"** como seção formal do PRD (o que está pela metade, o que decidimos não fazer).
- **Evidência em vez de adjetivo**: nada é "feito" sem comando + saída real. O tester existe porque "o build passou" não é critério de aceite.
- **Docs com dono único**: cada fato vive num arquivo só; os outros linkam.

## Licença

MIT.
