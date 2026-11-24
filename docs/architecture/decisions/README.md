# Реестр архитектурных решений

Все семь ADR Proposed. Render/stateless/no local storage — ограничения заказчика, не принятие ADR. [Readiness](../architecture-readiness.md) · [Overview](../architecture-overview.md).

| ID | Вопрос | Готовность | ADR | Рекомендация |
|---|---|---|---|---|
| Q01 | Топология | READY | [0001](0001-application-topology.md) | Один stateless Python HTTP-сервис на Render; Telegram кандидат |
| Q02 | Состояние | READY | [0002](0002-dialogue-state.md) | Явные переходы, авторство и внешнее транзакционное состояние |
| Q03 | LLM | CONDITIONAL | [0003](0003-llm-boundary.md) | Валидируемый адаптер, версии и независимое происхождение |
| Q04 | Хранение | CONDITIONAL | [0004](0004-persistence.md) | Внешний Postgres, immutable Save и read-only аналитика |
| Q05 | Safety | CONDITIONAL | [0005](0005-safety-boundary.md) | Отдельные durable входы и блокировка, статическая помощь |
| Q06 | UI | CONDITIONAL | [0006](0006-interface.md) | Telegram первый кандидат; web UI альтернатива |
| Q07 | Модель | CONDITIONAL | [0007](0007-llm-provider.md) | Groq GPT-OSS 20B первый кандидат; сверить квоты/политику |
| Q08 | UX | BLOCKED | — | Выбор человека в #1 |
| Q09 | Данные/доступ | BLOCKED | — | Согласовать режим, идентификацию, все обработчики и жизненный цикл |
| Q10 | Голос | DEFERRED | — | При включении H-05 |
| Q11 | Внешняя БД | CONDITIONAL | [0004](0004-persistence.md) | Supabase, Neon альтернатива, Sheets/Airtable экспорт-кандидаты |

2 READY / 6 CONDITIONAL / 2 BLOCKED / 1 DEFERRED. Gate BLOCKED. Все рекомендации нуждаются в человеческом согласовании, зависимости/условия внутри ADR.

Прослеживаемость: R1/R7/R8/R11/R12 → Q01/Q06 → ADR-0001/0006 → Render/API/UI, чистый запуск и ручные доказательства. R2–R5/R10 → Q02/Q04/Q11 → ADR-0002/0004 → транзакционный state, уникальная попытка, TC-08/13/14 и C-W01–05. R5/R6/R10 → Q05 → ADR-0005 → durable safety, W6–W19 и C-W03–07. R13 → Q07/Q03 → ADR-0007/0003 → сравнение моделей/квот, synthetic smoke-test. R14 → Q04/Q11/Q09 → отдельная read-only аналитика C-W08. R9 → Q08/Q10 → выбор UX/голоса. [Результаты обработки](../architecture-review.md#обработка-комментариев-заказчика).
