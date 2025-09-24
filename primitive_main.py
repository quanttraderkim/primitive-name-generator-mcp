from fastmcp import FastMCP
from typing import List, Optional
import random
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# MCP 서버 생성
mcp = FastMCP("PrimitiveNameGenerator")

# 원시인 부족 이름들
TRIBE_NAMES = [
    "우가족", "그르족", "뭉가족", "돌록족", "불꽃족", "맘모스족",
    "동굴족", "바위족", "나무족", "강물족", "썬더족", "와우족"
]

# 원시인 직책/역할
PRIMITIVE_ROLES = [
    "족장", "사냥꾼", "주술사", "전사", "수집가", "불지기", 
    "동굴지킴이", "맘모스잡이", "돌도끼장인", "열매따기대장"
]

# 키워드별 원시인 이름 요소들
KEYWORD_ELEMENTS = {
    # 불/열 관련
    "fire": ["불꽃", "타오", "활활", "지지직", "후후", "타닥", "이글이글", "활활이", "불티"],
    "hot": ["뜨거", "후끈", "달궈", "뜨끔", "활활", "따끈", "후후", "호호", "뜨거뜨거"],
    
    # 사냥/전투 관련  
    "hunt": ["사냥", "창질", "돌멍", "으악", "그르릉", "으르렁", "휘둘", "찍찍", "쿡쿡"],
    "strong": ["쿵쾅", "바위", "돌주먹", "으랏차", "힘센", "쌘쌘", "뭉치", "꽈당", "쾅쾅"],
    "brave": ["용감", "무서워", "으르릉", "꺄르르", "위험해", "겁없", "대담", "용맹", "씩씩"],
    
    # 동물 관련
    "mammoth": ["맘모스", "거대코끼리", "털북숭", "엄청큰", "으리으리", "뚱뚱", "코길", "어마어마", "크으으"],
    "bear": ["곰돌", "털복숭", "꿀먹", "겨울잠", "으르릉", "포근", "모조리", "털털", "꺼끌"],
    "tiger": ["호랑", "줄무늬", "으르르", "날카로", "무서운", "어흥", "할큄", "쨘쨘", "야옹"],
    "eagle": ["독수리", "날개", "파닥파닥", "하늘", "낚아챔", "휘이이", "높이높이", "후둑", "꺄아악"],
    
    # 자연 관련
    "cave": ["동굴", "깊숙", "어두컴컴", "후둑", "숨숨", "구멍", "뜨악뜨악", "들어가", "밖으로"],
    "rock": ["바위", "돌멩", "딱딱", "쿵쿵", "단단", "무거워", "굴러", "쌓쌓", "돌돌"],
    "tree": ["나무", "잎사귀", "열매", "그늘", "올라가", "흔들흔들", "우수수", "싹싹", "초록초록"],
    "water": ["물", "첨벙", "시원", "마시마시", "철벅", "졸졸", "시냇물", "맑은맑은", "차가워"],
    "wind": ["바람", "휘이이", "시원시원", "휘익", "솨아아", "불어불어", "날려", "휘날", "후후"],
    
    # 음식 관련
    "fruit": ["열매", "달콤", "맛나", "냠냠", "쪽쪽", "따먹", "빨간빨간", "단단", "톡톡"],
    "meat": ["고기", "씹적씹적", "맛나맛나", "냠냠", "구워구워", "짭짭", "쫄깃쫄깃", "기름진", "향긋"],
    "fish": ["물고기", "펄떡펄떡", "잡았다", "미끄러져", "번쩍번쩍", "싱싱", "찰랑찰랑", "튀김튀김", "바다"],
    
    # 도구 관련
    "stone": ["돌", "깎아깎아", "날카로", "던져", "맞혀", "딱딱", "뾰족뾰족", "갈아갈아", "쪼개"],
    "stick": ["나무막대", "길쭉", "휘둘", "찌르", "휘익", "단단", "곧은곧은", "잡아", "두드려"],
    "club": ["몽둥이", "휘둘", "꽈당", "때려", "무거워", "쿵쾅", "후려", "단단", "뭉툭"],
    
    # 감정 관련
    "happy": ["기뻐", "좋아좋아", "웃음", "깔깔", "신나", "방긋", "헤헤", "와하하", "즐거워"],
    "angry": ["화나", "으악", "성내", "부글부글", "콧김", "펄펄", "으르릉", "노발대발", "부아악"],
    "funny": ["웃겨", "재밌어", "킥킥", "우스", "껄껄", "깔깔", "호호", "배꼽", "우스꽝"],
    "sleepy": ["졸려", "꾸벅꾸벅", "잠와", "새근새근", "쿨쿨", "드르렁", "눈감", "포근", "늘어져"],
    
    # 날씨 관련
    "rain": ["비", "후두둑", "촉촉", "젖어", "우산", "후드득", "찰랑찰랑", "시원", "톡톡"],
    "sun": ["해", "따뜻", "밝은밝은", "반짝", "뜨거뜨거", "눈부셔", "쨍쨍", "환한", "빛나"],
    "cold": ["추워", "부르르", "떨어", "얼음", "꽁꽁", "시려", "오들오들", "차가워", "후들후들"],
    "snow": ["눈", "하얀하얀", "포근", "펄펄", "동글동글", "미끄러져", "차가워", "폭신폭신", "눈사람"],
    
    # 색깔 관련
    "red": ["빨간빨간", "새빨간", "토마토", "딸기", "피", "불", "루비", "장미", "빨가면"],
    "blue": ["파란파란", "하늘", "바다", "시원", "깊은깊은", "맑은", "시냇물", "파랑새", "구슬"],
    "green": ["초록초록", "나뭇잎", "풀풀", "싱그", "자연", "숲", "새싹", "개구리", "에메랄드"],
    "yellow": ["노란노란", "해", "바나나", "병아리", "밝은", "반짝", "금금", "레몬", "꽃잎"],
    "black": ["검은검은", "까만", "밤", "어둠", "깜깜", "숯", "그림자", "곰", "까마귀"],
    "white": ["하얀하얀", "새하얀", "눈", "구름", "깨끗", "순수", "면", "토끼", "우유"]
}

@mcp.tool
def generate_primitive_name(
    keywords: List[str],
    style: Optional[str] = "caveman",
    gender: Optional[str] = "any", 
    count: Optional[int] = 3
) -> dict:
    """
    키워드를 기반으로 재미있는 원시인 이름을 생성합니다.
    
    Args:
        keywords: 이름에 반영할 키워드들 (예: ["fire", "strong", "mammoth"])
        style: 이름 스타일 ("caveman", "shaman", "hunter", "chief", "funny")
        gender: 성별 ("male", "female", "any")
        count: 생성할 이름 개수 (1-10)
        
    Returns:
        dict: 생성된 이름들과 의미 설명
    """
    logger.info(f"원시인 이름 생성 요청: {keywords}, 스타일: {style}, 개수: {count}")
    
    if count > 10:
        count = 10
    elif count < 1:
        count = 1
        
    generated_names = []
    
    for _ in range(count):
        # 키워드에서 이름 요소 추출
        name_elements = []
        for keyword in keywords:
            if keyword.lower() in KEYWORD_ELEMENTS:
                name_elements.extend(KEYWORD_ELEMENTS[keyword.lower()])
        
        # 키워드 매칭이 없으면 기본 요소 사용
        if not name_elements:
            default_elements = ["우가", "그르", "뭉가", "돌록", "쿵쾅", "으악", "와우", "호호"]
            name_elements = default_elements
        
        # 부족 이름 선택
        tribe = random.choice(TRIBE_NAMES)
        
        # 스타일에 따른 이름 구성
        if style == "caveman":
            # 동굴인 스타일: 우가-[요소]-이
            element = random.choice(name_elements)
            suffix = random.choice(["이", "돌이", "순이", "갑이", "철이", "쇠", "바우", "돌"])
            full_name = f"우가-{element}-{suffix}"
            role = "동굴거주자"
            
        elif style == "shaman":
            # 주술사 스타일: [요소]-[신비로운접미사]
            element = random.choice(name_elements)
            mystic_suffix = random.choice(["예언자", "바람속삭임", "영혼대화", "꿈해석", "별보기", "신내림"])
            full_name = f"{element}-{mystic_suffix}"
            role = "부족 주술사"
            
        elif style == "hunter":
            # 사냥꾼 스타일: [요소]-사냥꾼/잡이
            element = random.choice(name_elements)
            hunter_suffix = random.choice(["사냥꾼", "잡이", "추적자", "창던지기", "활쏘기", "덫놓기"])
            full_name = f"{element}-{hunter_suffix}"
            role = "부족 사냥꾼"
            
        elif style == "chief":
            # 족장 스타일: 위대한-[요소]-대장/족장
            element = random.choice(name_elements)
            chief_prefix = random.choice(["위대한", "강한", "현명한", "용감한", "거대한", "무서운"])
            chief_suffix = random.choice(["대장", "족장", "우두머리", "리더", "왕", "보스"])
            full_name = f"{chief_prefix}-{element}-{chief_suffix}"
            role = "부족 족장"
            
        else:  # funny
            # 재미있는 스타일: 의성어/의태어 조합
            element1 = random.choice(name_elements)
            element2 = random.choice(name_elements)
            funny_words = ["꺄르르", "우걱우걱", "쿵덕쿵덕", "삐뽀삐뽀", "왈왈", "멍멍", "꽥꽥"]
            funny_element = random.choice(funny_words)
            if element1 != element2:
                full_name = f"{element1}-{funny_element}-{element2}"
            else:
                full_name = f"{element1}-{funny_element}-웃음보"
            role = "부족 개그맨"
        
        # 역할이 정해지지 않은 경우 랜덤 역할 부여
        if 'role' not in locals() or not role:
            role = random.choice(PRIMITIVE_ROLES)
        
        # 이름 의미 생성
        meaning_parts = []
        for keyword in keywords:
            if keyword.lower() in KEYWORD_ELEMENTS:
                if keyword.lower() == "fire":
                    meaning_parts.append("불의 힘을 가진")
                elif keyword.lower() == "strong":
                    meaning_parts.append("무시무시한 힘의")
                elif keyword.lower() == "mammoth":
                    meaning_parts.append("맘모스를 사냥하는")
                elif keyword.lower() == "happy":
                    meaning_parts.append("항상 웃음이 넘치는")
                else:
                    meaning_parts.append(f"{keyword}의 기운을 가진")
        
        if not meaning_parts:
            meaning_parts.append("원시시대의 용감한")
            
        meaning = f"{', '.join(meaning_parts)} {style} 스타일의 원시인"
        
        generated_names.append({
            "name": full_name,
            "meaning": meaning,
            "tribe": tribe,
            "role": role,
            "era": "구석기 시대",
            "sound": "우가우가! 그르릉!"
        })
    
    return {
        "names": generated_names,
        "keywords_used": keywords,
        "style": style,
        "total_count": count,
        "tribal_greeting": "우가우가! (안녕하세요!)",
        "time_period": "약 4만년 전 구석기 시대"
    }

@mcp.tool  
def get_primitive_name_meaning(name: str) -> dict:
    """
    원시인 이름의 의미를 해석합니다.
    
    Args:
        name: 해석할 원시인 이름
        
    Returns:
        dict: 이름의 의미 해석과 설명
    """
    # 원시인 이름 요소별 의미 사전
    primitive_meanings = {
        # 기본 의성어/의태어
        "우가": "기본적인 인사, 안녕의 의미",
        "그르": "으르릉, 강한 힘을 나타내는 소리",
        "뭉가": "뭉게뭉게, 부드럽고 포근한 느낌",
        "쿵쾅": "무거운 발걸음, 힘센 모습",
        "으악": "놀라거나 화가 날 때 내는 소리",
        "와우": "놀라움과 기쁨의 표현",
        
        # 불 관련
        "불꽃": "타오르는 불, 열정적인 성격",
        "타오": "활활 타오르는 불길",
        "활활": "불이 잘 타는 모습",
        "지지직": "불이 탈 때 나는 소리",
        
        # 힘/전투 관련
        "사냥": "먹이를 잡는 능력",
        "창질": "창을 잘 다루는 실력",
        "돌멍": "돌을 던지는 기술",
        "돌주먹": "돌처럼 단단한 주먹",
        
        # 동물 관련
        "맘모스": "거대한 털코끼리, 큰 존재",
        "곰돌": "곰처럼 강하고 털이 많은",
        "호랑": "호랑이처럼 용맹한",
        
        # 자연 관련
        "동굴": "안전한 거처, 보금자리",
        "바위": "단단하고 믿음직한 성격",
        "나무": "쭉쭉 자라는 성장력",
        "물": "생명의 근원, 깨끗함",
        
        # 역할 관련
        "족장": "부족을 이끄는 리더",
        "사냥꾼": "먹이를 구해오는 사람",
        "주술사": "영적인 능력을 가진 사람",
        "전사": "싸움을 담당하는 용사"
    }
    
    # 이름 분석 (하이픈으로 분리)
    name_parts = name.split("-")
    interpretations = []
    
    for part in name_parts:
        if part in primitive_meanings:
            interpretations.append(f"{part}: {primitive_meanings[part]}")
        else:
            # 패턴 매칭으로 의미 추측
            if "이" in part or "순" in part or "갑" in part:
                interpretations.append(f"{part}: 친근하고 정감가는 이름")
            elif "대장" in part or "족장" in part:
                interpretations.append(f"{part}: 리더십을 나타내는 호칭")
            elif "잡이" in part or "꾼" in part:
                interpretations.append(f"{part}: 전문 기술자를 의미")
            else:
                interpretations.append(f"{part}: 원시시대 특유의 표현")
    
    # 전체 의미 해석
    if interpretations:
        overall_meaning = f"'{name}'은(는) " + ", ".join([interp.split(': ')[1] for interp in interpretations]) + "를 의미하는 구석기 시대 원시인의 이름입니다."
    else:
        overall_meaning = f"'{name}'은(는) 원시시대 부족 사회의 독특한 문화를 반영한 이름입니다."
    
    return {
        "name": name,
        "parts_analysis": interpretations,
        "overall_meaning": overall_meaning,
        "time_period": "구석기 시대 (약 4만년 전)",
        "cultural_note": "원시인들은 자연현상, 동물, 도구 등에서 이름을 따왔으며, 의성어와 의태어를 많이 사용했습니다.",
        "tribal_greeting": "우가우가! (이 시대의 인사법)"
    }

@mcp.tool
def suggest_primitive_keywords() -> dict:
    """
    원시인 이름 생성에 사용할 수 있는 키워드들을 카테고리별로 제안합니다.
    
    Returns:
        dict: 카테고리별 키워드 목록
    """
    return {
        "categories": {
            "불/열": ["fire", "hot"],
            "사냥/전투": ["hunt", "strong", "brave"],
            "동물": ["mammoth", "bear", "tiger", "eagle"],
            "자연": ["cave", "rock", "tree", "water", "wind"],
            "음식": ["fruit", "meat", "fish"],
            "도구": ["stone", "stick", "club"],
            "감정": ["happy", "angry", "funny", "sleepy"],
            "날씨": ["rain", "sun", "cold", "snow"],
            "색깔": ["red", "blue", "green", "yellow", "black", "white"]
        },
        "styles": ["caveman", "shaman", "hunter", "chief", "funny"],
        "tribes": ["우가족", "그르족", "뭉가족", "돌록족", "불꽃족", "맘모스족"],
        "usage_tip": "의성어와 의태어를 활용한 재미있는 조합을 만들어보세요!",
        "time_travel_note": "구석기 시대로 떠나는 상상의 여행을 즐겨보세요! 우가우가!",
        "fun_fact": "원시인들은 실제로 현재 인류와 똑같이 똑똑했지만, 도구와 언어가 단순했을 뿐입니다!"
    }

@mcp.tool
def create_primitive_tribe_story(tribe_name: str, member_names: List[str]) -> dict:
    """
    원시인 부족과 구성원들로 재미있는 부족 이야기를 만들어줍니다.
    
    Args:
        tribe_name: 부족 이름
        member_names: 부족 구성원 이름들
        
    Returns:
        dict: 부족 이야기와 설정
    """
    
    # 부족 특성 랜덤 선택
    tribe_traits = [
        "불을 가장 잘 다루는", "맘모스 사냥의 전설적인", "동굴 그림이 유명한",
        "열매 채집이 뛰어난", "돌 도구 제작의 달인", "춤과 노래가 특기인"
    ]
    
    tribe_locations = [
        "큰바위 동굴", "맑은시냇물 근처", "높은나무 숲속", 
        "따뜻한남쪽 언덕", "거대동굴 깊숙이", "맘모스길 옆"
    ]
    
    daily_activities = [
        "해 뜰 때 다함께 우가우가 인사하기",
        "큰 불 피우고 둥글게 둘러앉기", 
        "맘모스 사냥 작전 회의하기",
        "동굴벽에 그림 그리며 이야기하기",
        "열매와 견과류 모으러 나가기",
        "달빛 아래 부족 춤 추기"
    ]
    
    selected_trait = random.choice(tribe_traits)
    selected_location = random.choice(tribe_locations)
    selected_activities = random.sample(daily_activities, 3)
    
    # 구성원별 역할 부여
    member_roles = {}
    available_roles = ["족장", "사냥대장", "주술사", "도구제작자", "열매채집장", "불지기", "동굴지킴이"]
    
    for i, member in enumerate(member_names[:len(available_roles)]):
        member_roles[member] = available_roles[i]
    
    # 남은 구성원들은 일반 부족원
    for member in member_names[len(available_roles):]:
        member_roles[member] = "부족원"
    
    story = f"""
🦕 {tribe_name} 이야기 🦕

옛날 옛적, 약 4만년 전 구석기 시대...
{selected_location}에 {selected_trait} {tribe_name}이 살고 있었습니다.

👥 부족 구성원:
{chr(10).join([f"• {name} ({role})" for name, role in member_roles.items()])}

🌅 부족의 하루:
{chr(10).join([f"• {activity}" for activity in selected_activities])}

우가우가! 이들의 모험은 계속됩니다...
    """
    
    return {
        "tribe_name": tribe_name,
        "story": story.strip(),
        "members": member_roles,
        "location": selected_location,
        "specialty": selected_trait,
        "daily_activities": selected_activities,
        "tribal_motto": "우가우가! 함께하면 맘모스도 무섭지 않다!",
        "time_period": "구석기 시대 (약 4만년 전)"
    }

if __name__ == "__main__":
    mcp.run()
