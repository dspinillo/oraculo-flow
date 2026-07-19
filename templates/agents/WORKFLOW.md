# Workflow multi-agente — dh

> Generalizado do `diario-maternidade/docs/agents/`. Personas agnósticas de LLM: o papel define o contrato, não o modelo. Hoje: Claude (modelo por porte da tarefa) + GPT via plugin Codex. Ativar em projetos N3 ou tarefas multi-frente — experimento N1 não paga esse overhead.

## Fluxo

```
                 ┌─────────────┐
     usuário ───▶│   MANAGER   │ (sessão principal — nunca coda direto)
                 └──────┬──────┘
        fatia TX.Y + critérios de aceite
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
   ┌─────────┐    ┌──────────┐     ┌──────────┐
   │ PLANNER │───▶│ BUILDER  │────▶│  TESTER  │
   └─────────┘    └──────────┘     └────┬─────┘
    plano técnico   diff em             │ evidência de teste
                    worktree/branch     ▼
                                  ┌──────────────┐
                                  │  DOCUMENTER  │──▶ STATUS/CHANGELOG/ADR
                                  └──────────────┘
                        ▼
              MANAGER revisa → merge → sync docs → fecha issue no Plane
```

## Papéis

| Papel | Foco | Executor default | Doc |
|---|---|---|---|
| Manager | fatiar, distribuir, revisar, sync de docs | sessão principal (Fable) | `MANAGER.md` |
| Planner | plano técnico de UMA tarefa | Fable (raciocínio máximo, volume baixo) | `PLANNER.md` |
| Builder | implementar UMA fatia que builda | Sonnet (workhorse da geração 5); Codex em confronto | `BUILDER.md` |
| Tester | validar critérios de aceite, tentar quebrar | Sonnet; Codex como 2º tester em fatia crítica | `TESTER.md` |
| Documenter | STATUS/CHANGELOG/ADR pós-fatia | Sonnet | `DOCUMENTER.md` |

> Racional (assinatura com uso alto): Fable pensa, Sonnet 5 produz, **Codex confronta**. Opus 4.8 é geração anterior ao Sonnet 5 — não é o degrau acima; o degrau acima é Fable.

## Confronto com GPT (Codex) — quando é PADRÃO, não exceção

Os limites do Codex são altíssimos; usar de graça o segundo cérebro é regra:

1. **Plano de tarefa ambígua/crítica**: Planner (Fable) e Codex planejam em paralelo, às cegas; Manager compara e funde. Divergência entre os dois é sinal de risco — investigar antes de codar.
2. **Diagnóstico difícil**: Claude e Codex investigam o mesmo bug em paralelo com o mesmo material.
3. **Fatia crítica** (schema/migração, alarmes, cripto, dinheiro): Codex roda como segundo tester independente antes do merge.
4. **Review de PR grande**: Codex revisa o diff que o Manager já revisou.

## Contrato de handoff entre papéis

- **Entra**: tarefa `TX.Y` com Objetivo, Passos, Critérios de aceite, Depende de + paths relevantes. Nunca "dá uma olhada no projeto".
- **Sai**: diff (ou plano/relatório) + evidência de validação (comando rodado e saída real). Sem evidência = não está pronto.
- Todo trabalho distribuído referencia a issue do Plane; quem fecha a issue é o Manager, depois do merge.

## Quando usar qual agente

| Situação | Use |
|---|---|
| Tarefa clara, 1-3 arquivos | Builder direto, sem Planner |
| Tarefa ambígua ou multi-arquivo | Planner (Fable) + Codex em confronto antes do Builder |
| Bug difícil | Claude e Codex em paralelo com o mesmo material |
| Fatias independentes | Builders em paralelo, worktrees isoladas |
| Fatia crítica (schema, alarme, cripto) | Builder escalado p/ Fable + Codex como 2º tester |
| Fim de fatia | Tester → Documenter, sempre nessa ordem |

## Anti-patterns

- Manager implementando "só essa coisinha" direto — vira sessão-monólito de novo.
- Builder recebendo a fase inteira em vez de uma fatia — diffs gigantes, review impossível.
- Documenter inventando estado — ele documenta a evidência do Tester, não o otimismo do Builder.
- Dois builders na mesma área de código sem worktree — conflito garantido.
- Pular o Tester porque "o build passou" — build não é critério de aceite.

## Fontes de verdade (ordem prática)

| Pergunta | Onde |
|---|---|
| O que entrou de fato? | CHANGELOG.md (N3) / STATUS.md |
| Onde paramos? | STATUS.md → "Onde paramos" |
| Como retomar? | HANDOFF.md |
| Por que é assim? | decisions/ |
| O que vem? | ROADMAP.md + Plane |
