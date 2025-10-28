1. Arquitetura Django e Estrutura de Projeto
 - Separação entre configuração global (settings.py) e domínios específicos (apps).
   
 - padrão MVC/MVT (Model–View–Template) aplicado na prática.
   
2. Modelagem de Dados (ORM)
 - Criação de modelos relacionais com ForeignKey.

- Relação entre User → Team → Project → Task.

- Uso de auto_now_add, blank, null, choices, __str__.

- Migrações com makemigrations e migrate.

- Integração com o Django Admin.

3. Orientação a Objetos aplicada
 - Uso de classes e herança (Model, Serializer, ViewSet).

- Criação de métodos personalizados (get_queryset, perform_create).

- Encapsulamento da lógica dentro das views e permissões.

4. API REST com Django REST Framework
- Criação de serializers para converter Python ↔ JSON.

- Construção de ViewSets com CRUD completo.

- Criação de rotas automáticas com DefaultRouter().

- Controle de acesso com permissions (IsAuthenticated, BasePermission).

- Teste via Swagger UI.

5. Autenticação e Autorização
- Implementação de login/logout por sessão (frontend).

- Criação de cadastro de usuários com ModelForm.

- Integração com JWT (JSON Web Token) para autenticação via API.

- Proteção de rotas com @login_required.

- Uso de LOGIN_URL, LOGIN_REDIRECT_URL e LOGOUT_REDIRECT_URL no settings.py.

6. Frontend com Django Template + CSS
- Renderização dinâmica com {{ context }}.

- Criação de templates reutilizáveis (login, register, dashboard).

- Proteção de formulários com {% csrf_token %}.

- Estilização simples e responsiva em style.css.

- Integração de rotas HTML com o backend.

7. Swagger e Documentação de API
- Configuração do drf-yasg para documentação interativa.

- Geração automática de endpoints (/swagger/).

- Exibição pública de metadados e rotas da API.

8. Boas práticas de versionamento
- Criação de .gitignore funcional.

- Commits descritivos e organizados (init:, feat:, fix:).

- Estrutura limpa de repositório (venv fora do controle de versão).

- Preparação para deploy futuro (Render / Railway / Docker).

10. Princípios de Engenharia de Software
- Aplicação dos princípios SOLID básicos:

- Single Responsibility: cada app faz uma coisa.

- Open/Closed: fácil de extender (novas features sem quebrar as antigas).

- Camadas desacopladas: models, views, serializers e templates separados.

- Código limpo, legível e versionado.
