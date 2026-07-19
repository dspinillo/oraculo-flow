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

## Instalação (plugin do Claude Code)

Dentro do Claude Code:

```
/plugin marketplace add dspinillo/oraculo-flow
/plugin install oraculo-flow@oraculo-flow
```

Depois, na raiz do seu monorepo:

```
/oraculo-flow:instalar        # coloca o CLAUDE.md com as regras + estrutura + Plane opcional
/oraculo-flow:novo-projeto    # cria seu primeiro projeto (mande o briefing junto!)
/oraculo-flow:migrar-projeto  # traz um projeto existente para o padrão
```

Os agentes (`planner`, `builder`, `tester`, `documenter`) ficam disponíveis automaticamente como subagents após a instalação.

Requisitos: [Claude Code](https://claude.com/claude-code); Python 3.10+ para o CLI do Plane (opcional); plugin Codex (opcional) para o confronto entre LLMs.

## Estrutura deste repo

```
oraculo-flow/
├── .claude-plugin/
│   ├── plugin.json         # manifest do plugin
│   └── marketplace.json    # este repo é o próprio marketplace
├── CLAUDE.md               # as regras (a skill instalar copia p/ raiz do SEU monorepo)
├── skills/
│   ├── instalar/           # setup do monorepo (rodar 1x)
│   ├── novo-projeto/       # criação de projeto de ponta a ponta
│   └── migrar-projeto/     # retrofit de projeto existente
├── agents/                 # planner, builder, tester, documenter (subagents)
├── templates/
│   ├── projeto/            # esqueletos: README, STATUS, HANDOFF, ROADMAP, PRD,
│   │                       #   ARCHITECTURE, CHANGELOG, CLAUDE.md, ADR, plano-visual
│   └── agents/             # WORKFLOW + personas Manager/Planner/Builder/Tester/Documenter
├── playbooks/              # checklists manuais (funcionam fora do Claude Code também)
└── scripts/plane.py        # CLI da API do Plane (stdlib pura): projetos + issues
```

## Configurar o Plane (opcional)

Tudo funciona sem Plane. Para usar: `.env` na raiz do seu monorepo com `PLANE_BASE_URL=...` (self-hosted ou `https://api.plane.so`) e `PLANE_WORKSPACE=...`; API token gerado no Plane salvo em `~/.config/plane/token`. A skill `instalar` guia isso.

## Filosofia

Este método foi destilado de um projeto real que acumulou 37 ADRs, 100+ KB de changelog e trocas de frente entre iOS, Android e backend sem perder o fio — e depois generalizado para um monorepo com 15+ projetos. As escolhas têm cicatriz por trás:

- **CHANGELOG como fonte de verdade** porque checkboxes de plano mentem.
- **"Honestidade de escopo"** como seção formal do PRD (o que está pela metade, o que decidimos não fazer).
- **Evidência em vez de adjetivo**: nada é "feito" sem comando + saída real. O tester existe porque "o build passou" não é critério de aceite.
- **Docs com dono único**: cada fato vive num arquivo só; os outros linkam.

## Licença

MIT.
