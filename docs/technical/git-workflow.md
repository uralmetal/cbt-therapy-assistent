# Git Workflow для API Prototype

| Ветка | Кто ведёт | Куда направлять PR |
| --- | --- | --- |
| `prototype/api` | Тимлид | В `main` как итог этапа |
| `prototype/api-telegram` | Разработчик A | В `prototype/api` |
| `prototype/api-gemini` | Разработчик B | В `prototype/api` |

## 1. Общая стартовая версия

После согласования и merge [PR #2](https://github.com/uralmetal/cbt-therapy-assistent/pull/2) тимлид создаёт интеграционную ветку с актуальной версии `main`.

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

A работает в `prototypes/api/telegram_bot.py`. B — в `prototypes/api/gemini.py` и `prototypes/api/prompt.md`. Общие файлы ведёт тимлид. Изменения контракта и зависимостей согласуют A, B и тимлид до реализации.

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

1. Тимлид проверяет и объединяет рабочий PR A, проверенный с заглушкой.
2. B получает изменения A в своей рабочей ветке и обновляет свой PR.

   ```bash
   git fetch origin
   git switch prototype/api-gemini
   git merge origin/prototype/api
   git push
   ```

3. Тимлид проверяет и объединяет PR B. Для совместной проверки каждый получает итог этапа через `git fetch origin` и `git switch --detach origin/prototype/api`. Для дальнейшей работы вернитесь в свою ветку через `git switch -`.
4. После общего прогона тимлид открывает итоговый PR `prototype/api` → `main` с результатами.

При конфликте выполните `git status`. Конфликт собственного файла разберите с автором второй правки, затем сделайте `git add <путь>` и `git merge --continue`. При конфликте общего файла или нарушении контракта передайте тимлиду пути файлов, команды и пример несовпадения. Если продолжать разрешение нельзя, `git merge --abort` вернёт состояние до попытки merge. Тимлид координирует исправление.

Стажёры отправляют изменения в рабочие ветки. Merge и любые изменения `main` идут через тимлида и согласованный PR.
