# Реестр архитектурных решений

ADR-0001–0006 Accepted, ADR-0007 Proposed (Gemini выбран как направление; конкретная модель/условия ещё проверяются). Render/stateless/no local storage — требования заказчика. [Readiness](../architecture-readiness.md) · [Overview](../architecture-overview.md).

| ID | Вопрос | Готовность | ADR | Рекомендация |
|---|---|---|---|---|
| Q01 | Топология | READY | [0001](0001-application-topology.md) | Accepted: один stateless Python HTTP-сервис на Render; Telegram |
| Q02 | Состояние | READY | [0002](0002-dialogue-state.md) | Accepted: явные переходы, авторство и внешнее транзакционное состояние |
| Q03 | LLM | CONDITIONAL | [0003](0003-llm-boundary.md) | Accepted: валидируемый адаптер, версии и независимое происхождение |
| Q04 | Хранение | CONDITIONAL | [0004](0004-persistence.md) | Accepted: Supabase Postgres, immutable Save; аналитика отложена |
| Q05 | Safety | CONDITIONAL | [0005](0005-safety-boundary.md) | Accepted: отдельные durable входы и блокировка, статическая помощь |
| Q06 | UI | CONDITIONAL | [0006](0006-interface.md) | Accepted: Telegram и UX‑A. Допуск в Q09 |
| Q07 | Модель | CONDITIONAL | [0007](0007-llm-provider.md) | Proposed: Gemini — выбранное направление, Flash-Lite кандидат; сверить квоты/политику |
| Q08 | UX | READY | — | [Выбран UX‑A с подтверждением актуальной карточки](../../product/hypotheses-and-options.md#итоговое-решение-заказчика--26112026) |
| Q09 | Данные/доступ | BLOCKED | — | Согласовать режим, идентификацию, все обработчики и жизненный цикл |
| Q10 | Голос | DEFERRED | — | При включении H-05 |
| Q11 | Внешняя БД | CONDITIONAL | [0004](0004-persistence.md) | Supabase выбран; Render Postgres — отдельный stage/demo |

3 READY / 6 CONDITIONAL / 1 BLOCKED / 1 DEFERRED. Gate BLOCKED. Согласованные решения и нерешённые условия различаются; зависимости и критерии готовности внутри ADR.

Прослеживаемость: R1/R7/R8/R11/R12 → Q01/Q06 → ADR-0001/0006 → Render/API/UI, чистый запуск и ручные доказательства. R2–R5/R10 → Q02/Q04/Q11 → ADR-0002/0004 → транзакционный state, уникальная попытка, TC-08/13/14 и C-W01–05. R5/R6/R10 → Q05 → ADR-0005 → durable safety, W6–W19 и C-W03–07. R13 → Q07/Q03 → ADR-0007/0003 → сравнение моделей/квот, synthetic smoke-test. R14 → Q04/Q11: возможность аналитики сохранена как будущая опция; в MVP отсутствие доступа/экспорта C-W08. R15 → Q07/Q09 → ограниченный синтетический профиль Gemini. R9 → Q08/Q10 → выбор UX/голоса. [Исходные комментарии](../architecture-review.md#обработка-комментариев-заказчика) · [Согласование решений C-07–C-14](../architecture-review.md#обработка-комментариев-заказчика--согласование-решений-c-07c-14).
