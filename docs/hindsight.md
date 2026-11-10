# Hindsight 공통 설정

## 통합 기준

모든 프로젝트와 디렉터리에서 같은 Hindsight 서버와 memory bank를 사용한다.

- 서버: `http://home:8888`
- 서버 모드: `self-hosted`
- bank ID: 정확히 `yunseong`
- 디렉터리 이름으로 bank ID를 생성하지 않는다.
- `coding-agent::yunseong`, `personal-agent::agents` 같은 별도 ID를 사용하지 않는다.
- Codex, Claude Code, OpenCode 등은 같은 사용자 설정을 공유한다.

## 설정 파일

| 환경 | 설정 파일 |
| --- | --- |
| Windows | `C:\Users\jys09\.hindsight\coding-agent.json` |
| WSL Ubuntu | `/home/yunseong/.hindsight/coding-agent.json` |
| `ssh home` | `/home/yunseong/.hindsight/coding-agent.json` |

최소 공통 설정은 다음과 같다.

```json
{
  "serverMode": "self-hosted",
  "apiUrl": "http://home:8888",
  "bankId": "yunseong",
  "dynamicBankId": false,
  "optInOnly": false
}
```

`mapPathToBank`는 제거한다. 설치된 runtime에서는 경로별 설정이 고정
`bankId`보다 먼저 적용되므로, 이 설정이 남으면 일부 디렉터리가 다른 bank를
사용한다. `harnesses` 안에도 서버, bank, 경로 제한을 다르게 지정하지 않는다.
`optInOnly: false`는 디렉터리별 허용 목록 없이 사용하기 위한 설정이다.

`HINDSIGHT_CONFIG`로 다른 설정 파일을 지정하거나, 에이전트 실행 설정에서
별도의 Hindsight 서버를 등록하지 않았는지도 확인한다. 같은 ID라도 서버가
다르면 서로 다른 메모리다. 이 구성에서는 별도의 daemon을 사용하지 않는다.

## 설치와 변경 절차

1. 기존 `coding-agent.json`을 날짜가 포함된 이름으로 백업한다.
2. Hindsight runtime이 없으면 설치하고 사용할 에이전트를 연결한다.
3. 공통 설정을 적용하고 경로별 bank 설정을 제거한다.
4. 새 MCP 프로세스에서 `hindsight_diagnose`를 호출한다.
5. 서로 다른 디렉터리에서도 `bank_id`가 `yunseong`, `api_url`이
   `http://home:8888`인지 확인한다.
6. 실행 중인 에이전트는 재시작해서 기존 MCP 연결과 session 설정을 갱신한다.

설치된 runtime으로 Linux의 Codex와 Claude Code를 연결하는 명령은 다음과 같다.

```bash
node ~/.hindsight/coding-agents/dist/installer.js install codex claude-code \
  --server self-hosted --api-url http://home:8888
```

이 명령은 에이전트 연결을 설정한다. 고정 `bankId`, `dynamicBankId`,
`optInOnly`는 위 JSON에 맞춰 별도로 확인한다. 기존 대화를 일괄 가져오는
`--import-conversations`는 이번 설정 변경에 사용하지 않았다.

서버 연결은 다음 명령으로 확인할 수 있다.

```bash
curl --fail http://home:8888/health
```

`home`의 Node는 NVM으로 설치되어 있다. 비대화형 SSH에서는 `node`가
`PATH`에 없을 수 있으므로, 진단 스크립트는 실제 NVM Node 실행 파일을
지정하거나 NVM을 먼저 로드한다. 이것을 bank 설정 오류로 판단하지 않는다.

## 2026-11-10 적용 기록

- 서버에 정확히 `yunseong`인 bank를 생성했다.
- Windows의 디렉터리별 자동 ID와 `notes`, `.agents` 경로별 예외를 제거했다.
- WSL Ubuntu에 Hindsight runtime `0.5.1`을 설치하고 Codex와 Claude Code를 연결했다.
- `home`의 기존 `daemon` 설정을 공통 `self-hosted` 서버로 변경했다.
- `home`의 `optInOnly: true`, 빈 허용 목록 제한을 해제했다.
- 변경한 기존 설정 파일은 각 환경의 `.hindsight`에 백업했다.
- Windows는 홈, `Documents/notes`, `.agents`에서 새 MCP 진단을 확인했다.
- WSL과 `home`은 각각 홈, `/tmp`, `.agents`에서 새 MCP 진단을 확인했다.
- 각 환경의 진단 결과가 `yunseong`과 `http://home:8888`로 일치했다.
- 세 환경 모두 Claude Code의 `.claude.json`에 등록된 MCP 설정으로 실행해
  `harness: claude-code`, `bank_id: yunseong`을 확인했다.
- Claude Code의 `SessionStart`, `UserPromptSubmit`, `Stop` Hindsight hooks가
  세 환경에 모두 등록되어 있음을 확인했다.
- WSL과 `home`에서 서버 API로 `yunseong` bank의 존재를 확인했다.

검증은 새로 실행한 MCP 프로세스와 서버 API를 기준으로 했다. 기존에 실행
중이던 모든 에이전트를 재시작하거나, 실제 대화 한 건의 수집부터 검색까지
전체 경로를 검증한 것은 아니다.

과거 bank와 그 안의 메모리는 삭제하거나 옮기지 않았다. 이번 작업은 앞으로
사용할 저장소의 통합이며, 과거 메모리의 통합은 별도 작업이다. 서버 생성
직후 `yunseong`의 `fact_count`는 `0`이었다.
