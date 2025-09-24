# 🦕 Primitive Name Generator MCP

구석기 시대로 떠나는 상상의 여행! 원시인 이름을 키워드 기반으로 재미있게 생성하는 MCP 서버입니다!

## ✨ 주요 기능

### 1. `generate_primitive_name` 
키워드와 스타일을 기반으로 재미있는 원시인 이름을 생성합니다.

**파라미터:**
- `keywords`: 이름에 반영할 키워드들 (예: `["fire", "strong", "mammoth"]`)
- `style`: 이름 스타일 - `"caveman"`, `"shaman"`, `"hunter"`, `"chief"`, `"funny"` (기본값: `"caveman"`)
- `gender`: 성별 - `"male"`, `"female"`, `"any"` (기본값: `"any"`)
- `count`: 생성할 이름 개수 (1-10, 기본값: 3)

**예시 사용:**
```json
{
  "keywords": ["fire", "strong", "hunt"],
  "style": "hunter",
  "count": 5
}
```

### 2. `get_primitive_name_meaning`
원시인 이름의 의미를 해석해줍니다.

**파라미터:**
- `name`: 해석할 원시인 이름 (예: `"우가-불꽃-사냥꾼"`)

### 3. `suggest_primitive_keywords`
원시인 이름 생성에 사용할 수 있는 키워드들을 카테고리별로 제안합니다.

### 4. `create_primitive_tribe_story` 🆕
부족과 구성원들로 재미있는 부족 이야기를 만들어줍니다!

**파라미터:**
- `tribe_name`: 부족 이름 (예: `"우가족"`)
- `member_names`: 부족 구성원 이름들

## 🎨 지원하는 키워드 카테고리

| 카테고리 | 키워드 예시 |
|----------|-------------|
| 불/열 | fire, hot |
| 사냥/전투 | hunt, strong, brave |
| 동물 | mammoth, bear, tiger, eagle |
| 자연 | cave, rock, tree, water, wind |
| 음식 | fruit, meat, fish |
| 도구 | stone, stick, club |
| 감정 | happy, angry, funny, sleepy |
| 날씨 | rain, sun, cold, snow |
| 색깔 | red, blue, green, yellow, black, white |

## 🎭 원시인 이름 스타일

- **caveman** (동굴인): 우가-불꽃-이, 그르-바위-돌이
- **shaman** (주술사): 타오-영혼대화, 별빛-예언자  
- **hunter** (사냥꾼): 맘모스-사냥꾼, 창질-추적자
- **chief** (족장): 위대한-쿵쾅-대장, 무서운-으르릉-족장
- **funny** (재미있는): 활활-꺄르르-웃음보, 쿵덕-우걱우걱-삐뽀

## 🚀 사용 예시

### 용감한 맘모스 사냥꾼 만들기
```python
generate_primitive_name(
    keywords=["mammoth", "brave", "hunt"],
    style="hunter",
    count=3
)
```
**결과 예시:** 
- 맘모스-사냥꾼 (맘모스족 소속 사냥꾼)
- 용감-추적자 (그르족 소속 전사)
- 으르릉-창던지기 (불꽃족 소속 사냥대장)

### 재미있는 부족 개그맨 만들기  
```python
generate_primitive_name(
    keywords=["funny", "happy"],
    style="funny",
    count=4
)
```
**결과 예시:**
- 깔깔-꺄르르-웃음보 (와우족 소속 개그맨)
- 기뻐-삐뽀삐뽀-방긋 (뭉가족 소속 개그맨)
- 웃겨-왈왈-껄껄 (돌록족 소속 개그맨)

### 신비한 부족 주술사 만들기
```python
generate_primitive_name(
    keywords=["fire", "wind", "cave"],
    style="shaman",
    count=3
)
```
**결과 예시:**
- 불꽃-별보기 (맘모스족 소속 주술사)
- 바람-영혼대화 (동굴족 소속 주술사)  
- 동굴-꿈해석 (우가족 소속 주술사)

## 🏕️ 부족 이야기 만들기

```python
create_primitive_tribe_story(
    tribe_name="우가족",
    member_names=["우가-불꽃-족장", "그르-맘모스-사냥꾼", "뭉가-열매-채집이"]
)
```

**결과 예시:**
```
🦕 우가족 이야기 🦕

옛날 옛적, 약 4만년 전 구석기 시대...
큰바위 동굴에 불을 가장 잘 다루는 우가족이 살고 있었습니다.

👥 부족 구성원:
• 우가-불꽃-족장 (족장)
• 그르-맘모스-사냥꾼 (사냥대장)
• 뭉가-열매-채집이 (열매채집장)

🌅 부족의 하루:
• 해 뜰 때 다함께 우가우가 인사하기
• 맘모스 사냥 작전 회의하기
• 달빛 아래 부족 춤 추기

우가우가! 이들의 모험은 계속됩니다...
```

## 🎯 활용 분야

### 엔터테인먼트
- **코미디**: 개그 콘텐츠의 캐릭터 이름
- **웹툰/만화**: 원시인 캐릭터 작명
- **게임**: 원시시대 배경 게임의 NPC
- **유튜브**: 재미있는 콘텐츠 소재

### 교육
- **역사 수업**: 구석기 시대 학습 도구
- **언어 교육**: 의성어/의태어 학습
- **창의성 교육**: 상상력 발달 도구

### 창작 활동  
- **소설/시나리오**: 원시 부족 설정
- **연극/뮤지컬**: 선사시대 작품
- **아동도서**: 재미있는 캐릭터 이름

## 💡 재미 요소들

### 🗣️ 원시인 언어 특징
- **의성어 많이 사용**: 우가우가, 그르릉, 쿵쾅
- **단순하고 직관적**: 불꽃, 사냥, 맘모스
- **자연과 밀접**: 동굴, 바위, 나무, 물

### 🏃‍♂️ 부족 사회
- **12개 부족**: 우가족, 그르족, 뭉가족 등
- **다양한 역할**: 족장, 사냥꾼, 주술사, 도구제작자
- **공동체 생활**: 함께 사냥하고 춤추고 이야기하기

### 🎪 유머 포인트
- **웃긴 조합**: 활활-꺄르르-웃음보
- **의외의 매칭**: 졸려-꾸벅꾸벅-새근새근
- **귀여운 어미**: -이, -돌이, -순이

## 📦 배포 정보

- **Server Name**: `primitive-name-generator`
- **Entry Point**: `primitive_main.py`
- **FastMCP Cloud URL**: `https://primitive-name-generator.fastmcp.app/mcp`
- **GitHub Repository**: `https://github.com/quanttraderkim/primitive-name-generator-mcp`

### MCP 클라이언트 설정

**Claude Desktop / Cursor 설정** (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "primitive-name-generator": {
      "command": "npx",
      "args": ["@modelcontextprotocol/inspector", "https://primitive-name-generator.fastmcp.app/mcp"]
    }
  }
}
```

## 🛠️ 로컬 개발

```bash
# 가상환경 생성
python3 -m venv venv
source venv/bin/activate

# 의존성 설치
pip install fastmcp

# 로컬 실행
fastmcp dev primitive_main.py
```

## 🦴 재미있는 사실들

- **똑똑한 조상들**: 구석기 인류는 현재 인류와 같은 뇌 용량을 가졌어요!
- **예술가들**: 동굴 벽화는 약 4만년 전부터 그려졌답니다
- **도구 제작**: 정교한 돌도구를 만드는 고도의 기술을 가졌어요
- **언어 발달**: 복잡한 언어와 문화를 가졌을 것으로 추정돼요

---

**Created with 🦕 for prehistoric fun and imagination!**

*우가우가! 구석기 시대로 떠나는 즐거운 상상여행!* 🔥🏹
