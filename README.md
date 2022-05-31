# Introduction

`redpen-sensei`는 [**GitHub Actions**](https://github.com/features/actions)으로 스케줄하여 텔레그램 봇으로 [**LeetCode**](https://leetcode.com/)의 일일 챌린지 문제를 알리는 파이썬 스크립트입니다.

# Setup

1. 이 저장소 fork 하거나 프로젝트 내의 모든 디렉토리와 파일을 복사하여 새 저장소에 붙여넣습니다.
2. 저장소의 `Settings > Secrets > Actions`에서 Action 실행에 필요한 **Secret**을 설정합니다. 자세한 설정 방법은 아래 [**Actions secrets**](#actions-secrets) 항목을 참고하세요.
3. `.github/workflows/redpen-scheduler.yml` 파일의 `on.schedule.cron[0]` 옵션을 수정하여 알림 시간을 설정합니다. 자세한 설정 방법은 아래 [**Cron Schedule**](#cron-schedule) 항목을 참고하세요.

# Actions secrets

**GitHub Action**을 통해 텔레그램으로 알림을 전송하려면 사용할 **텔레그램 봇의 토큰**과 **알림을 수신받을 계정들의 채팅 ID**를 **Actions secrets**으로 등록하여야 합니다. [**텔레그램 봇 소개**](https://core.telegram.org/bots) 문서를 참고하세요. 그러나 텔레그램 봇을 설정하고 토큰과 채팅 ID를 확인하는 방법에 대해서는 인터넷 블로그의 글이 더 유용할 수 있습니다!

텔레그램에서 확인한 정보는 저장소의 `Settings > Secrets > Actions`에서 `Repository secret`으로 등록해야 합니다. 등록해야 하는 정보는 아래와 같습니다.

- `TELEGRAM_BOT_TOKEN`: 알림을 전송할 텔레그램 봇의 토큰입니다.
- `TELEGRAM_CHAT_IDS`: 알림을 수신받을 계정들의 채팅 ID 목록입니다. 여러 계정으로 알림을 전송하려면, 대상 계정들을 쉼표 (`,`) 로 구분하여 띄어쓰기 없이 나열합니다.

# Cron Schedule

**GitHub Action**을 통해 주기적으로 알림을 전송할 수 있습니다. 이 주기는 `.github/workflows/redpen-scheduler.yml` 파일의 `on.schedule.cron[0]` 옵션에서 정의할 수 있습니다.

알림 주기 옵션은 [**cron 표현식**](https://ko.wikipedia.org/wiki/Cron)으로 정의합니다. 기준 시간대는 **UTC**로, 한국 표준시 (KST) 와는 9시간 차이가 나는 것에 유의하세요!

# Note

- GitHub Actions의 서비스 상태에 의해 알림이 지정한 시간보다 늦게 전송되거나 알림 전송에 실패할 수 있습니다.
