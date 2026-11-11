# .agents

`~/.agents`에 두고 사용하는 **user-level 에이전트 지침**, 스킬, 프로젝트 초기화 템플릿을 모아둔 저장소입니다.

## 저장소 구성

| 경로 | 설명 |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | user-level 에이전트 지침 |
| [`docs/`](docs/) | 개발 절차, 코딩 스타일, 하위 에이전트 모델 선택, Hindsight 설정 |
| [`skills/`](skills/) | user-level에서 사용하는 스킬 |
| [`library/`](library/) | 각 프로젝트에 복사해서 사용하는 지침, 스킬, 에이전트 템플릿 |

## 프로젝트에서 사용하기

1. 새 프로젝트에서 `/init`으로 기본 지침을 만든 뒤 `init-project`를 사용합니다. 기존 프로젝트 지침을 바탕으로 `library/`의 공통 템플릿을 적용합니다.
2. 구현 계획 작성이나 코드 리뷰에 필요한 스킬은 `skill-load`로 가져옵니다. 복사한 지침과 스킬은 각 프로젝트에서 관리합니다.

## 주요 스킬

| 스킬 | 설명 |
| --- | --- |
| [`init-project`](skills/init-project/SKILL.md) | 새 프로젝트에 공통 에이전트 지침을 적용합니다. |
| [`skill-load`](skills/skill-load/SKILL.md) | `library/`의 스킬과 에이전트를 프로젝트로 가져옵니다. |
| [`parallel`](skills/parallel/SKILL.md) | 독립적인 개발 작업을 나누고 결과를 통합합니다. |
| [`dev-tool`](skills/dev-tool/SKILL.md) | 반복해서 쓰는 빌드·테스트 명령을 `./dev`로 묶습니다. |
| [`agent-sessions`](skills/agent-sessions/SKILL.md) | 이전 에이전트 세션을 찾아 작업을 이어받을 수 있게 합니다. |
| [`writing-plan`](library/skills/writing-plan/SKILL.md) | 구현 계획을 문서로 작성합니다. |
| [`pair-review`](library/skills/pair-review/SKILL.md) | 변경 사항을 별도 리뷰 에이전트로 검토합니다. |

## 설치형 스킬 업데이트

`dev-tool`과 `agent-sessions`는 각 원본 저장소에서 관리합니다. 원본 변경이 merge되면 다음 명령으로 전역 설치본을 갱신합니다. [dev-tool 원본](https://github.com/dev-yunseong/dev-tool) · [agent-sessions 원본](https://github.com/dev-yunseong/agent-sessions)

```sh
npx skills update -g dev-tool agent-sessions
```

갱신 결과를 이 저장소에 기록할 때는 `skills/`의 변경과 `.skill-lock.json`을 함께 커밋합니다.
