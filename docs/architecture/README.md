# Архитектурная документация

Учебный MVP дневника СМЭР. Для него выбран [UX‑A](../product/hypotheses-and-options.md#итоговое-решение-заказчика--26112026). Ограничения заказчика от 24.11.2026: stateless Python без локального хранения, Render, до 10 пользователей, <1 входящего запроса/с. ADR-0001–0006 Accepted (Telegram, внешний state, адаптер, Supabase, safety). Gemini — выбранное направление учебного MVP, ADR-0007 Proposed для модели/условий; Render Postgres — опция stage/demo. Аналитический контур отложен. [Этапы и сроки](../technical/implementation-plan.md).

| Документ | Назначение |
|---|---|
| [Readiness](architecture-readiness.md) | Требования, комментарии заказчика, вопросы и готовность |
| [Overview](architecture-overview.md) | Согласованная конфигурация, границы и жизненный цикл |
| [Реестр ADR](decisions/README.md) | Шесть принятых ADR, один Proposed и открытые вопросы |
| [Ревью](architecture-review.md) | История независимых ревью, обработка комментариев, проверки |

Независимое ревью №3 на `ff5612e0c483e01f4a2fea039307aeef19404e19` подтвердило 5/5 прежних замечаний FIXED. Требуется повторное независимое ревью текущей конфигурации. Три диаграммы прошли локальный рендер Mermaid. Planning Readiness Gate: BLOCKED.
