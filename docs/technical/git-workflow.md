# Git Workflow для API Prototype

| Ветка | Кто ведёт | Куда направлять PR |
| --- | --- | --- |
| `prototype/api` | A и B, создаёт A по договорённости с B | В `main` как итог этапа |
| `prototype/api-telegram` | Разработчик A | В `prototype/api` |
| `prototype/api-gemini` | Разработчик B | В `prototype/api` |

## 1. Общая стартовая версия

Стартовый скелет уже в `main` после [PR #2](https://github.com/uralmetal/cbt-therapy-assistent/pull/2). Разработчик A создаёт общую интеграционную ветку с актуальной версии `main`.

```bash
git clone https://github.com/uralmetal/cbt-therapy-assistent.git
cd cbt-therapy-assistent
git fetch origin
git switch -c prototype/api origin/main
git push -u origin prototype/api
```

## 2. Рабочая ветка

Каждый разработчик клонирует репозиторий по командам выше и выполняет `git fetch origin`. Если репозиторий уже есть, достаточно перейти в него и выполнить `git fetch origin`.

```bash
# Разработчик A
git switch -c prototype/api-telegram origin/prototype/api

# Разработчик B, в своём клоне
git switch -c prototype/api-gemini origin/prototype/api
```

A работает в `prototypes/api/telegram_bot.py`. B — в `prototypes/api/gemini.py` и `prototypes/api/prompt.md`. A и B совместно ведут общие файлы и согласуют изменения контракта и зависимостей до реализации.

## 3. Коммит и рабочий PR

Сначала пройдите ручную проверку из [инструкции](api-prototype.md).

```bash
git status --short
# A
git add prototypes/api/telegram_bot.py
git commit -m "feat(prototype): integrate Telegram polling"
# B, в своей ветке
git add prototypes/api/gemini.py prototypes/api/prompt.md
git commit -m "feat(prototype): integrate Gemini and dialog context"
# Каждый отправляет свою текущую ветку
git push -u origin HEAD
```

В GitHub откройте **Pull requests → New pull request**. Установите **base** `prototype/api`, **compare** — свою ветку из таблицы. Pull Request соответствует Merge Request в GitLab. Опишите сделанное и результаты ручных проверок. Правки по ревью добавляйте новыми коммитами в ту же ветку через `git add`, `git commit`, `git push`.

## 4. Интеграция

1. B проверяет рабочий PR A, включая результат прогона с заглушкой. После ревью разработчики объединяют PR A в интеграционную ветку.
2. B получает изменения A в своей рабочей ветке и обновляет свой PR.

   ```bash
   git fetch origin
   git switch prototype/api-gemini
   git merge origin/prototype/api
   git push
   ```

3. A проверяет PR B. После ревью разработчики объединяют PR B. Для совместной проверки каждый получает итог этапа через `git fetch origin` и `git switch --detach origin/prototype/api`. Затем вместе пройдите [чек-лист](api-prototype.md#совместная-проверка). Для дальнейшей работы вернитесь в свою ветку через `git switch -`.
4. До 28 ноября включительно завершите реализацию, интеграцию и все проверки. Только после прохождения всего чек-листа один из разработчиков открывает итоговый PR `prototype/api` → `main`, прикладывает результаты и запрашивает финальное ревью тимлида. Если проверка заблокирована, зафиксируйте причину.

При конфликте выполните `git status` и вместе разберите изменения. После исправления выполните `git add <путь>` и `git merge --continue`. Если продолжать нельзя, `git merge --abort` вернёт состояние до попытки merge.

До передачи A и B отвечают за весь код, общий контракт, конфликты и интеграцию. Тимлид участвует только в финальном ревью. Замечания исправляют разработчики. В `main` изменения попадают через согласованный итоговый PR.
