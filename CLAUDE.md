# Oráculo Flow — convenção de projetos

> Regras para todo desenvolvimento nos seus projetos (funciona em monorepo ou um-repo-por-projeto — ver seção Git). Esqueletos e criação de projeto: skills `oraculo-flow:novo-projeto` / `oraculo-flow:migrar-projeto`.

## Docs por nível de porte

| Nível | Quando | Docs obrigatórios |
|---|---|---|
| **N1** experimento | ideia em teste, pode morrer | `README.md` + `STATUS.md` |
| **N2** projeto ativo (default) | vai ser usado de verdade | N1 + `HANDOFF.md`, `ROADMAP.md`, `decisions/` |
| **N3** produto | instalado em aparelho de terceiros, ou multi-frente | N2 + `ARCHITECTURE.md`, `PRD.md`, `CHANGELOG.md`, `CLAUDE.md` próprio |

Promoção de nível cruza o critério → registrar como ADR do projeto. Em N3, **CHANGELOG.md é a fonte de verdade do que entrou**; checkboxes de planos podem mentir, ele não.

## Tipo de projeto (declarado na criação)

`mobile` · `saas/web` · `vps-service` · `desktop` · `cli/script` · `misto`. Registrado no README. Exigências extras:

- **mobile / saas** (qualquer UI): fase de design no F0 — 2-3 variações de mockup por tela-chave se não houver design definido; escolha vira `decisions/0002-design.md`.
- **vps-service**: documentar deploy no README (onde roda, como sobe, onde estão os logs); manter playbook do provedor se houver cotas/limites.
- **misto**: `ARCHITECTURE.md` obrigatório desde o início.

## F0 = planejamento visual, antes de qualquer código

Todo projeto novo abre com um plano em **artifact web** (roteiro: `templates/projeto/plano-visual.md`; no Codex usar GPT Sites) — visão, funcionalidades por fase, arquitetura, mockups, fatiamento, riscos. Nunca só texto no terminal. Link do artifact vai para README e ROADMAP.

## Fatiamento

Fases `F0..Fn` → tarefas `TX.Y` (campos: **Objetivo · Passos · Critérios de aceite · Depende de**) → fatias que buildam sozinhas. Fases/tarefas viram issues no seu Plane (`PLANE_BASE_URL`) via `scripts/plane.py`. Vocabulário de status em qualquer doc: `✅ feito · 🟡 parcial · ▶️ próximo · ⏸️ aguardando · 🔒 bloqueado · ⬜ não iniciado`.

## Git

> A skill `instalar` apaga o modo que não se aplica a você.

**Modo monorepo:**
- Projeto novo nasce em `projects/<slug>/` **dentro do monorepo**. Exceção (repo standalone) exige ADR em `decisions/` da raiz.
- Commits: Conventional Commits escopados por projeto — `feat(<slug>): ...`, `fix(<slug>): ...`. Um commit não mistura projetos.

**Modo multi-repo (um repo por projeto):**
- Projeto novo nasce como repo próprio (`git init` + remoto quando houver), com os docs do nível na raiz.
- Commits: Conventional Commits simples — `feat: ...`, `fix: ...`.

**Ambos:**
- Nunca commitar sem o usuário pedir; nunca commitar segredos.

## ADRs

Decisão de arquitetura/stack/pivô → `decisions/NNNN-slug.md` **no projeto** (formato: Contexto / Decisão / Consequências). No modo monorepo, decisões que afetam o monorepo inteiro → `decisions/` da raiz. Não contrariar ADR vigente sem escrever o ADR que o substitui.

## Protocolo de sessão

Ao **abrir** sessão num projeto: ler `STATUS.md` → `HANDOFF.md` → tarefa atual. Ao **encerrar**:

1. Rodar build/testes e reportar resultado real.
2. Atualizar `STATUS.md`: "Onde paramos" novo, sessão anterior colapsada em `<details>`, data + HEAD no cabeçalho.
3. Atualizar `HANDOFF.md` se a forma de retomar mudou.
4. `CHANGELOG.md` se N3.
5. Projeto **fora do padrão**? Propor migração (`playbooks/migrar-projeto.md`) antes de aprofundar.

## Memória

Projeto novo ganha memory file `<slug>-project.md` no auto-memory + linha no MEMORY.md. Memória guarda só o não-derivável do repo: paths, package/applicationId, armadilhas de aparelho, estado de fase. O resto vive nos docs do projeto.

## Orquestração multi-agente

Para N3 ou tarefa multi-frente (N1 nunca): fluxo e contratos em `templates/agents/WORKFLOW.md`; agentes executáveis `planner`, `builder`, `tester`, `documenter` em `.claude/agents/`. Regras mínimas:

- Manager (a sessão principal) fatia e revisa; **não coda direto**.
- Handoff: entra tarefa TX.Y + critérios de aceite; sai diff + evidência de teste (comando + saída real).
- Modelos (assinatura com uso alto, sem economizar): **Fable pensa** (Manager + Planner), **Sonnet produz** (Builder/Tester/Documenter), **Codex confronta**. Fatia crítica escala Builder para Fable.
- **Confronto com Codex é padrão** (limites altíssimos): plano ambíguo → Fable e Codex planejam às cegas e o Manager compara; bug difícil → investigação paralela; fatia crítica → Codex como 2º tester. Divergência entre os dois = sinal de risco, investigar antes de codar.
- Trabalho distribuído referencia issue do Plane; Manager fecha a issue após merge.
