# Playbook — migrar projeto existente para a convenção

Retrofit **sob demanda**: ao trabalhar num projeto fora do padrão, propor esta migração antes de aprofundar (regra do `dh/CLAUDE.md`). Não migrar em massa.

## Checklist

### 1. Classificar

- [ ] Definir tipo (`mobile`/`saas`/`vps-service`/`desktop`/`cli`/`misto`) e nível (N1/N2/N3) — a maioria dos apps instalados no aparelho de terceiros é N3; experimento parado é N1.
- [ ] Registrar tipo/nível no README (criar do template se não existir — caso `my-meds`).

### 2. Normalizar nomes

| Encontrado | Vira |
|---|---|
| `PLAN.md` / `PLANO.md` / `docs/plano.md` | `ROADMAP.md` |
| `NEXT-SESSION.md` | fundir no `HANDOFF.md` |
| "Próximos passos"/"Cuidados p/ próximo chat" dentro do STATUS | seção do `HANDOFF.md` |
| `docs/decisions.md` (arquivo único) | `decisions/NNNN-slug.md` (um por decisão) |

### 3. Completar o kit do nível

- [ ] Criar docs faltantes a partir de `dh/templates/projeto/`, preenchendo com o estado REAL (não aspiracional).
- [ ] STATUS fora do formato → adotar cabeçalho datado + "Onde paramos" + histórico em `<details>` (converter histórico existente sem apagar).
- [ ] Decisões enterradas em STATUS/ROADMAP → extrair para ADRs `decisions/NNNN-slug.md`.
- [ ] N3 sem CHANGELOG → criar começando de agora (não reconstruir o passado; o histórico fica no git).

### 4. Plane

- [ ] Criar projeto no Plane (`scripts/plane.py create-project`) + issues das fases abertas do ROADMAP.

### 5. Memória

- [ ] Atualizar o memory file do projeto: tipo, nível, "migrado para a convenção em <data>".

### 6. Commit

- [ ] Oferecer `docs(<slug>): migra para a convenção de projetos`.

## Casos especiais

- **Repo git embedded** (projeto com `.git` próprio dentro do monorepo, sem estar declarado): decidir na migração — (a) adicionar `/projects/<slug>/` ao `.gitignore` da raiz e tratar como standalone, ou (b) remover o `.git` interno e absorver no monorepo. Registrar a escolha como ADR na raiz.
- **Standalone por decisão** (repo próprio fora do versionamento do monorepo): ganha só a normalização de docs; não mexer no git dele.
- **Tipo `misto`** (multi-componente: app + servidor + worker): ARCHITECTURE.md é obrigatório na migração; inventários avulsos podem ser absorvidos por ele.
