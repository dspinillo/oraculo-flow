# {{nome}}

> {{one-liner}}
>
> **Tipo:** {{tipo}} · **Nível:** {{nivel}} · **Stack:** {{stack}}
> **Plane:** {{plane-url-do-projeto}} · **Plano visual (F0):** {{link-artifact}}

## Visão

{{2-3 parágrafos: que problema resolve, para quem, o que NÃO é.}}

## Mapa do projeto

```
{{slug}}/
├── README.md      # este arquivo — visão + como rodar
├── STATUS.md      # onde paramos (atualizado toda sessão)
├── HANDOFF.md     # como retomar (N2+)
├── ROADMAP.md     # o que vem, priorizado (N2+)
├── decisions/     # ADRs NNNN-slug.md (N2+)
└── {{dirs de código}}
```

## Como rodar

```bash
{{comandos de build/run/teste}}
```

## Deploy

{{Apenas tipo vps-service/saas: onde roda, como sobe, onde estão os logs. Remover caso contrário.}}
