# Módulo 9: Monitoring, Logging y Debugging

## Introducción

Bienvenido al módulo sobre monitoring y debugging. En este módulo aprenderás:

- Interpretar logs de workflows
- Debugging de workflows
- Notificaciones y alertas
- Status checks y badges
- Workflow insights

## ¿Por qué es importante?

Saber monitorear y debuggear workflows es crucial para mantener pipelines saludables y resolver problemas rápidamente cuando ocurren.

## Conceptos Principales

### 1. Entender los Logs

**Niveles de logging:**
```yaml
steps:
  - name: Debug info
    run: |
      echo "::debug::This is a debug message"
      echo "::notice::This is a notice"
      echo "::warning::This is a warning"
      echo "::error::This is an error"
```

**Output en logs:**
```
::debug::This is a debug message
::notice::This is a notice
::warning file=app.js,line=10::This is a warning
::error file=app.js,line=20::This is an error
```

### 2. Debugging Steps

**Habilitar debug logging:**
```yaml
# En Settings → Secrets, crear:
# ACTIONS_STEP_DEBUG = true
# ACTIONS_RUNNER_DEBUG = true
```

**Debug interactivo con tmate:**
```yaml
steps:
  - name: Setup tmate session
    uses: mxschmitt/action-tmate@v3
    if: failure()
```

**Guardar state para debugging:**
```yaml
- name: Save state on failure
  if: failure()
  run: |
    echo "Last command: $LAST_COMMAND"
    echo "Working directory: $(pwd)"
    ls -la
    env | sort
```

### 3. Grouping y Masking

**Agrupar logs:**
```yaml
- name: Build
  run: |
    echo "::group::Installing dependencies"
    npm ci
    echo "::endgroup::"
    
    echo "::group::Building project"
    npm run build
    echo "::endgroup::"
    
    echo "::group::Running tests"
    npm test
    echo "::endgroup::"
```

**Ocultar valores sensibles:**
```yaml
- name: Mask secrets
  run: |
    SECRET_VALUE="my-secret"
    echo "::add-mask::$SECRET_VALUE"
    echo "Secret is: $SECRET_VALUE"  # Aparecerá como: ***
```

### 4. Notificaciones

**Notificación por Slack:**
```yaml
- name: Slack Notification
  uses: slackapi/slack-github-action@v1
  if: always()
  with:
    payload: |
      {
        "text": "Workflow ${{ job.status }}: ${{ github.workflow }}",
        "blocks": [
          {
            "type": "section",
            "text": {
              "type": "mrkdwn",
              "text": "*Status:* ${{ job.status }}\n*Workflow:* ${{ github.workflow }}\n*Commit:* ${{ github.sha }}"
            }
          }
        ]
      }
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

**Notificación por Email:**
```yaml
- name: Send email
  uses: dawidd6/action-send-mail@v3
  if: failure()
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: "Build Failed: ${{ github.repository }}"
    body: "Workflow ${{ github.workflow }} failed on commit ${{ github.sha }}"
    to: team@example.com
```

**Notificación por Discord:**
```yaml
- name: Discord notification
  uses: Ilshidur/action-discord@master
  env:
    DISCORD_WEBHOOK: ${{ secrets.DISCORD_WEBHOOK }}
  with:
    args: 'Deployment to production completed successfully!'
```

### 5. Status Checks

**Requerir status checks:**
```yaml
# En Settings → Branches → Branch protection rules
# Require status checks to pass before merging
# - build
# - test
# - lint
```

**Check individual steps:**
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - run: npm test
        id: tests
      
      - name: Comment PR
        uses: actions/github-script@v6
        if: always()
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: 'Tests ${{ steps.tests.outcome }}'
            })
```

### 6. Badges

**Badge de status:**
```markdown
![CI](https://github.com/user/repo/workflows/CI/badge.svg)
![Tests](https://github.com/user/repo/workflows/Tests/badge.svg?branch=main)
```

**Badge personalizado con shields.io:**
```markdown
![Custom](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/codecov/c/github/user/repo)
```

### 7. Workflow Insights

**Usar GitHub API para métricas:**
```yaml
- name: Get workflow metrics
  uses: actions/github-script@v6
  with:
    script: |
      const runs = await github.rest.actions.listWorkflowRuns({
        owner: context.repo.owner,
        repo: context.repo.repo,
        workflow_id: 'ci.yml',
        per_page: 10
      });
      
      const avgDuration = runs.data.workflow_runs
        .reduce((sum, run) => sum + (run.updated_at - run.created_at), 0) 
        / runs.data.workflow_runs.length;
      
      console.log(`Average duration: ${avgDuration}ms`);
```

## Implementación Práctica

### Ejemplo 1: Workflow con Monitoring Completo

```yaml
name: Production Deploy with Monitoring

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Start deployment
        id: deployment
        uses: chrnorm/deployment-action@v2
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          environment: production
      
      - name: Build
        run: |
          echo "::group::Build Process"
          npm ci
          npm run build
          echo "::endgroup::"
      
      - name: Deploy
        id: deploy
        run: |
          echo "Deploying to production..."
          # Deploy logic
          echo "url=https://myapp.com" >> $GITHUB_OUTPUT
      
      - name: Update deployment status
        uses: chrnorm/deployment-status@v2
        if: always()
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          deployment-id: ${{ steps.deployment.outputs.deployment_id }}
          state: ${{ job.status }}
          environment-url: ${{ steps.deploy.outputs.url }}
      
      - name: Notify Slack on Success
        if: success()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "✅ Deploy to production successful!",
              "blocks": [{
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": "*Deploy Status:* Success\n*URL:* ${{ steps.deploy.outputs.url }}\n*Commit:* ${{ github.sha }}"
                }
              }]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
      
      - name: Notify Slack on Failure
        if: failure()
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "❌ Deploy to production failed!",
              "blocks": [{
                "type": "section",
                "text": {
                  "type": "mrkdwn",
                  "text": "*Deploy Status:* Failed\n*Workflow:* ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}"
                }
              }]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
      
      - name: Create issue on failure
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'Deploy to production failed',
              body: `Deploy failed for commit ${context.sha}\n\nWorkflow: ${context.serverUrl}/${context.repo.owner}/${context.repo.repo}/actions/runs/${context.runId}`,
              labels: ['bug', 'deployment']
            })
```

### Ejemplo 2: Debug Helper Workflow

```yaml
name: Debug Helper

on:
  workflow_dispatch:
    inputs:
      debug_level:
        description: 'Debug level'
        required: true
        default: 'info'
        type: choice
        options:
          - info
          - debug
          - verbose

jobs:
  debug:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Show context information
        run: |
          echo "::group::GitHub Context"
          echo "Event: ${{ github.event_name }}"
          echo "Ref: ${{ github.ref }}"
          echo "SHA: ${{ github.sha }}"
          echo "Actor: ${{ github.actor }}"
          echo "::endgroup::"
          
          echo "::group::Runner Context"
          echo "OS: ${{ runner.os }}"
          echo "Arch: ${{ runner.arch }}"
          echo "Temp: ${{ runner.temp }}"
          echo "::endgroup::"
      
      - name: Show environment variables
        if: inputs.debug_level == 'debug' || inputs.debug_level == 'verbose'
        run: |
          echo "::group::Environment Variables"
          env | sort
          echo "::endgroup::"
      
      - name: Show file system
        if: inputs.debug_level == 'verbose'
        run: |
          echo "::group::File System"
          pwd
          ls -laR
          echo "::endgroup::"
      
      - name: Interactive debug session
        if: inputs.debug_level == 'verbose'
        uses: mxschmitt/action-tmate@v3
        timeout-minutes: 30
```

### Ejemplo 3: Performance Monitoring

```yaml
name: Performance Monitoring

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours

jobs:
  monitor:
    runs-on: ubuntu-latest
    steps:
      - name: Check API response time
        id: perf
        run: |
          START=$(date +%s%3N)
          curl -f https://api.example.com/health
          END=$(date +%s%3N)
          DURATION=$((END - START))
          echo "duration=$DURATION" >> $GITHUB_OUTPUT
          echo "Response time: ${DURATION}ms"
      
      - name: Alert if slow
        if: steps.perf.outputs.duration > 1000
        uses: slackapi/slack-github-action@v1
        with:
          payload: |
            {
              "text": "⚠️ API response time high: ${{ steps.perf.outputs.duration }}ms"
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

## Mejores Prácticas

1. **Usa grupos para logs largos**: Mejora legibilidad
2. **Notifica solo lo importante**: Evita spam
3. **Guarda artifacts en fallos**: Screenshots, logs, dumps
4. **Implementa health checks**: Verifica que el deploy funcionó
5. **Monitorea métricas**: Duración, tasa de éxito, etc.

## Conceptos clave para recordar

- 🔑 **Debug Logging**: ACTIONS_STEP_DEBUG y ACTIONS_RUNNER_DEBUG
- 🔑 **Grouping**: ::group:: y ::endgroup::
- 🔑 **Masking**: ::add-mask:: para ocultar valores
- 🔑 **Notifications**: Slack, Email, Discord para alertas
- 🔑 **Status Checks**: Requerir checks antes de merge
- 🔑 **Badges**: Mostrar status del workflow

## Próximos pasos

En el módulo final aprenderás sobre best practices, security y optimización de workflows.

¡Sigue aprendiendo! 🚀
