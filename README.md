# ConectAves

Site do Laboratório de Ecologia Integrativa e Tecnologia para Conservação de Aves. O laboratório é uma iniciativa de pesquisa independente conduzida por Jonathan Ribeiro em Recife, PE.

## Páginas

- `/`: apresentação
- `/sobre/`: laboratório e pesquisador
- `/pesquisa/`: áreas de atuação
- `/projetos/`: índice para futuras páginas de projetos
- `/publicacoes/`: índice para futuras publicações
- `/contato/`: canais disponíveis

O site usa Jekyll sem plugins adicionais e é publicado pelo GitHub Pages a partir da branch principal. Cabeçalho e rodapé ficam em `_includes/`, a estrutura HTML em `_layouts/default.html`, e estilos e comportamento em `assets/`.

Para gerar uma prévia local sem Ruby, execute `python scripts/build_preview.py` e sirva a pasta `.preview/` com um servidor HTTP. O script requer `PyYAML` e `python-liquid`.
