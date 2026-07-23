# Workflow multi-agente

> Personas agnósticas de LLM: o papel define o contrato, não o modelo. Hoje: Claude (modelo por porte da tarefa) + GPT via plugin Codex. Ativar em projetos N3 ou tarefas multi-frente — experimento N1 não paga esse overhead.

## Papéis e a pergunta que cada um responde

| Papel | A pergunta | Quando entra | Executor default | Doc |
|---|---|---|---|---|
| **Manager** | O que devemos fazer agora? | sempre (é a sessão principal) | Fable | `MANAGER.md` |
| **Architect** | Isso mantém a arquitetura saudável? | só quando a tarefa toca contrato/módulo/schema/dependência, ou em N3 | Fable + Codex em confronto | `ARCHITECT.md` |
| **Planner** | Como implementar esta tarefa? | tarefa ambígua ou 3+ arquivos | Fable | `PLANNER.md` |
| **Builder** | Como escrever o código? | toda fatia | Sonnet; Codex em confronto | `BUILDER.md` |
| **Tester** | Funciona de verdade? | fim de toda fatia | Sonnet; Codex 2º tester em fatia crítica | `TESTER.md` |
| **Design-parity** | O entregue bate com o design aprovado? | gatilhado: fim de fase de UI | Fable; ótimo em confronto N-vias | `DESIGN_PARITY.md` |
| **Documenter** | O conhecimento foi preservado? | fim de ciclo | Sonnet | `DOCUMENTER.md` |

> Racional de modelo (assinatura com uso alto): Fable pensa, Sonnet 5 produz, **Codex confronta**. Opus 4.8 é geração anterior ao Sonnet 5 — não é o degrau acima; o degrau acima é Fable.
>
> **Architect e Planner são distintos**: o Planner responde *como implementar esta tarefa*; o Architect responde *esta tarefa mantém o sistema saudável* (bounded contexts, contratos, dependências, impacto estrutural). Na maioria das tarefas o Planner basta — chame o Architect só quando a mudança é estrutural. Não é papel fixo no pipeline.

## Fluxo

```
                 ┌─────────────┐
     usuário ───▶│   MANAGER   │ (sessão principal — nunca coda direto)
                 └──────┬──────┘
        fatia TX.Y + critérios de aceite
                        │
              ┌ (só se estrutural) ┐
              ▼                     │
        ┌───────────┐              │
        │ ARCHITECT │──── ok ──────┤
        └───────────┘              │
                        ▼
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
   ┌─────────┐    ┌──────────┐     ┌──────────┐
   │ PLANNER │───▶│ BUILDER  │────▶│  TESTER  │
   └─────────┘    └──────────┘     └────┬─────┘
    plano técnico   diff em             │ evidência de teste
                    worktree/branch     ▼
                                  ┌──────────────┐
                                  │  DOCUMENTER  │──▶ STATUS/CHANGELOG/ADR/LESSONS
                                  └──────────────┘
                        ▼
              MANAGER revisa → merge → sync docs → fecha issue no Plane
```

## Confronto com GPT (Codex) — quando é PADRÃO, não exceção

Os limites do Codex são altíssimos; usar de graça o segundo cérebro é regra:

1. **Decisão estrutural**: Architect (Fable) e Codex avaliam o impacto em paralelo, às cegas; divergência entre os dois é sinal de risco — investigar antes de codar.
2. **Plano de tarefa ambígua/crítica**: Planner (Fable) e Codex planejam em paralelo; Manager compara e funde.
3. **Diagnóstico difícil**: Claude e Codex investigam o mesmo bug em paralelo com o mesmo material.
4. **Fatia crítica** (schema/migração, alarmes, cripto, dinheiro): Codex roda como segundo tester independente antes do merge.
5. **Review de PR grande**: Codex revisa o diff que o Manager já revisou.

## Contrato de handoff entre papéis

- **Entra**: tarefa `TX.Y` com Objetivo, Passos, Critérios de aceite, Depende de + paths relevantes. Nunca "dá uma olhada no projeto".
- **Sai**: diff (ou plano/relatório) + evidência de validação (comando rodado e saída real). Sem evidência = não está pronto.
- Antes de começar, o Builder/Planner consulta `LESSONS.md` do projeto (erros e padrões já aprendidos). Ao fim, se o ciclo ensinou algo não-óbvio, o Documenter registra lá.
- Todo trabalho distribuído referencia a issue do Plane; quem fecha a issue é o Manager, depois do merge.

## Quando usar qual agente

| Situação | Use |
|---|---|
| Tarefa clara, 1-3 arquivos | Builder direto, sem Planner |
| Mudança estrutural (contrato, módulo, schema, dependência) | Architect (Fable+Codex) antes de tudo |
| Tarefa ambígua ou multi-arquivo | Planner (Fable) + Codex em confronto antes do Builder |
| Bug difícil | Claude e Codex em paralelo com o mesmo material |
| Fatias independentes | Builders em paralelo, worktrees isoladas |
| Fatia crítica (schema, alarme, cripto) | Builder escalado p/ Fable + Codex como 2º tester |
| Fim de fatia | Tester → Documenter, sempre nessa ordem |

## Anti-patterns

- Manager implementando "só essa coisinha" direto — vira sessão-monólito de novo.
- Architect convocado para tarefa trivial — cerimônia que mata velocidade; ele é gatilhado, não obrigatório.
- Builder recebendo a fase inteira em vez de uma fatia — diffs gigantes, review impossível.
- Documenter inventando estado — ele documenta a evidência do Tester, não o otimismo do Builder.
- Dois builders na mesma área de código sem worktree — conflito garantido.
- Pular o Tester porque "o build passou" — build não é critério de aceite.
- Repetir um erro que já está no `LESSONS.md` — a lição existe justamente para isso.

## Fontes de verdade (ordem prática)

| Pergunta | Onde |
|---|---|
| O que entrou de fato? | CHANGELOG.md (N3) / STATUS.md |
| Onde paramos? | STATUS.md → "Onde paramos" |
| Como retomar? | HANDOFF.md |
| Por que é assim? | decisions/ |
| O que já erramos/aprendemos? | LESSONS.md |
| O que vem? | ROADMAP.md + Plane |
