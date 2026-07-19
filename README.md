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

## O que vem na caixa

**Briefing → Plano visual → Fatias → Build → Teste → Docs → Ship.** Cada peça alimenta a seguinte: o briefing vira o plano visual que o `novo-projeto` publica; o plano vira tarefas com critérios de aceite; o `planner` detalha, o `builder` implementa, o `tester` produz a evidência que o `documenter` registra no STATUS — que é exatamente o que a próxima sessão lê para continuar. Nada se perde entre sessões porque cada etapa sabe o que veio antes.

### Skills

| Skill | Papel | O que faz |
|---|---|---|
| `/oraculo-flow:instalar` | Onboarding | Rodar 1x. Pergunta seu layout (monorepo ou repo-por-projeto), instala as regras (CLAUDE.md) no lugar certo, cria a estrutura e configura o Plane opcional. Nunca sobrescreve nada sem mostrar. |
| `/oraculo-flow:novo-projeto` | Fundador de projeto | Recebe seu briefing bagunçado (texto, prints, links, restrições) e devolve estrutura: docs do nível certo, plano visual em artifact com 2–3 variações de mockup pra você escolher, projeto + issues no Plane, memória. **Para na sua aprovação antes de qualquer código.** |
| `/oraculo-flow:migrar-projeto` | Arqueólogo | Traz um projeto existente para o padrão: classifica tipo/nível, normaliza nomes de docs, extrai decisões enterradas em ADRs, preserva todo o histórico. Documenta o que EXISTE, não inventa estado. |

### Agentes (subagents)

| Agente | Seu especialista | O que faz |
|---|---|---|
| `planner` | Arquiteto | Transforma UMA tarefa ambígua em plano executável: paths exatos verificados no código real, ordem, o que reusar, riscos. Não escreve código. |
| `builder` | Dev sênior | Implementa UMA fatia com critérios de aceite definidos. Diff pequeno no padrão do código vizinho, build rodado com saída real anexada. Relata honestamente o que não validou. |
| `tester` | QA | Veredito PASSOU/FALHOU por critério de aceite, com comando e saída. Tenta casos de borda, checa regressão. Não corrige — reporta. "O build passou" não é critério de aceite. |
| `documenter` | Tech writer | Fecha o ciclo: CHANGELOG, STATUS ("onde paramos"), HANDOFF, ADRs. Só documenta o que tem evidência do tester — nunca o otimismo do builder. |

O **Manager** é a sua própria sessão principal: fatia, distribui, revisa e nunca coda direto. O fluxo completo, a matriz de quando usar qual agente e os anti-patterns estão em [`templates/agents/WORKFLOW.md`](templates/agents/WORKFLOW.md).

### Docs (templates)

Cada doc responde UMA pergunta — e só ela. É isso que impede a documentação de virar pântano:

| Doc | A pergunta que responde | Nível |
|---|---|---|
| `README.md` | O que é isso e como rodo? | N1+ |
| `STATUS.md` | Onde paramos? (histórico de sessões preservado em `<details>`) | N1+ |
| `HANDOFF.md` | Como retomo amanhã sem perder o fio? | N2+ |
| `ROADMAP.md` | O que vem, em que ordem? | N2+ |
| `decisions/` | Por que é assim? (ADRs numerados, com o porquê) | N2+ |
| `ARCHITECTURE.md` | Como funciona por dentro? | N3 |
| `PRD.md` | O que o produto é — e o que decidimos que NÃO é? | N3 |
| `CHANGELOG.md` | O que entrou de fato? (fonte de verdade; checkboxes mentem, ele não) | N3 |
| `CLAUDE.md` do projeto | O que todo agente precisa saber antes de tocar neste código? | N3 |

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

Depois:

```
/oraculo-flow:instalar        # setup 1x: pergunta seu layout, coloca as regras + Plane opcional
/oraculo-flow:novo-projeto    # cria seu primeiro projeto (mande o briefing junto!)
/oraculo-flow:migrar-projeto  # traz um projeto existente para o padrão
```

Funciona com **monorepo** (projetos em `projects/<slug>/`, regras no CLAUDE.md da raiz) ou **um repo por projeto** (regras em `~/.claude/CLAUDE.md`, cada projeto nasce com `git init`) — a skill `instalar` pergunta e configura.

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
