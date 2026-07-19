# {{nome}} — instruções para agentes

## Antes de implementar qualquer coisa

Leia nesta ordem: `STATUS.md` (onde paramos) → `HANDOFF.md` (como retomar) → a tarefa TX.Y no ROADMAP/Plane. Decisões de arquitetura: `decisions/` — não recontrarie um ADR sem criar outro.

## Princípio de produto

{{o inegociável deste produto em 1 frase}}

## Como buildar e testar

```bash
{{comandos exatos, incluindo JAVA_HOME/env se preciso}}
```

## Armadilhas conhecidas

1. {{armadilha específica deste projeto — device, API, sandbox}}
2. {{...}}

## Convenções de código

- {{padrões deste projeto: nomenclatura, DI, onde vive cada coisa}}

## Ao encerrar a sessão

1. Rodar os testes/build e reportar resultado real.
2. Atualizar `CHANGELOG.md` (o que entrou) — fonte de verdade.
3. Atualizar `STATUS.md` ("Onde paramos" + colapsar sessão anterior em `<details>`).
4. Atualizar `HANDOFF.md` se a forma de retomar mudou.
5. Commitar apenas se o usuário pedir, escopo `tipo({{slug}}): ...`.
