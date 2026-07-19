# {{nome}} — Arquitetura

> Atualizado em **{{data}}** · HEAD `{{commit}}`. Decisões com porquê: `decisions/`.

## 1. Camadas

```
{{diagrama ASCII: UI → lógica → dados / componentes e setas}}
```

## 2. Componentes

| Componente | Responsabilidade | Onde |
|---|---|---|
| {{nome}} | {{o que faz}} | `{{path}}` |

## 3. Persistência

| Modelo/Tabela | Campos-chave | Observações |
|---|---|---|
| {{Model}} | {{campos}} | {{migração/versão do schema}} |

## 4. Integrações externas

- {{API/serviço, auth, limites conhecidos}}

## 5. Estrutura de pastas

```
{{tree enxuto dos dirs de código}}
```

## 6. Build & tooling

{{JDK/toolchain, comandos, particularidades de sandbox/aparelho.}}
