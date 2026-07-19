# Playbook — novo projeto

Checklist completo por trás da skill `/novo-projeto`. Funciona também manualmente ou de outro cliente (Codex, etc.). Regras: `dh/CLAUDE.md`.

## 1. Definição

Perguntar/definir antes de criar qualquer arquivo:

| Campo | Valores |
|---|---|
| Nome + slug | slug kebab-case, vira `projects/<slug>/` |
| Tipo | `mobile` · `saas/web` · `vps-service` · `desktop` · `cli/script` · `misto` |
| Nível | N1 experimento · N2 ativo (default) · N3 produto |
| Stack | linguagem/framework pretendidos |
| One-liner | 1 frase do que é |
| Design definido? | se NÃO e tem UI → mockups obrigatórios no F0 |
| Fases iniciais | F0 (plano visual) + F1..Fn esboçadas |

## 2. Estrutura

- [ ] Criar `dh/projects/<slug>/` copiando de `dh/templates/projeto/` os docs do nível (N1: README+STATUS · N2: +HANDOFF, ROADMAP, decisions/ · N3: tudo).
- [ ] Preencher placeholders `{{...}}` (nome, slug, tipo, nível, stack, data).
- [ ] Tipo `misto` → incluir ARCHITECTURE.md mesmo em N2.

## 3. F0 — plano visual

- [ ] Montar o artifact seguindo `dh/templates/projeto/plano-visual.md` (Claude: Artifact + skill artifact-design; Codex: GPT Sites).
- [ ] UI sem design definido → 2-3 variações de mockup por tela-chave.
- [ ] Usuário escolheu direção → registrar `decisions/0002-design.md`.
- [ ] Link do artifact no README e ROADMAP.

## 4. Plane

- [ ] `python3 dh/scripts/plane.py create-project "<Nome>" --identifier <SLUG-CURTO>`
- [ ] Uma issue por fase: `python3 dh/scripts/plane.py create-issue <projeto> "F1 — <nome>" --desc "<critério de pronto>"`
- [ ] Tarefas TX.Y da fase corrente também viram issues (as demais, só quando a fase abrir).

## 5. Memória

- [ ] Criar memory file `<slug>-project.md` no auto-memory (tipo `project`): dir, package/applicationId se houver, tipo, nível, fase atual, link do artifact.
- [ ] Adicionar linha no `MEMORY.md`.

## 6. Git

- [ ] Oferecer commit: `chore(<slug>): scaffold do projeto`.
- [ ] Repo standalone em vez do monorepo? Só com ADR na raiz (`dh/decisions/`) justificando.
