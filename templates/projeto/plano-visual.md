# Template do plano visual (F0)

> Não é um doc do projeto — é o roteiro do **artifact web** que abre todo projeto novo (regra do `dh/CLAUDE.md`). No Claude Code: Artifact (carregar skill `artifact-design` antes). No Codex: GPT Sites. O plano NUNCA é só texto no terminal. O link do artifact publicado vai para o README e o ROADMAP do projeto.

## Seções obrigatórias do artifact

1. **Visão** — nome, one-liner, tipo, para quem. Uma dobra, sem rolagem.
2. **Funcionalidades por fase** — cards/tabela F0..Fn com o que cada fase entrega e critério de "pronto". Marcar o marco atual.
3. **Arquitetura** — diagrama (mermaid) dos componentes: app, dados, serviços externos, VPS quando houver. Decisões de stack com o porquê em 1 linha cada.
4. **Design / mockups** — obrigatório para tipo `mobile` e `saas/web` sem design definido: **2 a 3 variações por tela-chave** (HTML/CSS inline no próprio artifact), com nome de direção (ex.: "A — densa", "B — respirada", "C — brutalista") e 1 linha sobre a intenção de cada. O usuário escolhe; a escolha vira `decisions/0002-design.md`.
5. **Fatiamento** — tabela de tarefas da primeira fase real (TX.Y · objetivo · critério de aceite · dependências), espelho do que vai virar issue no Plane.
6. **Riscos e perguntas em aberto** — o que precisa de decisão do usuário antes de codar.

## Regras

- Tema claro/escuro, responsivo, autocontido (CSP bloqueia recursos externos).
- Favicon estável por projeto.
- Mockups são descartáveis — o objetivo é escolher direção, não pixel-perfection.
- Se o usuário JÁ tem design definido, a seção 4 vira "Design vigente" com referência a ele.
