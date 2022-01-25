from datetime import datetime

def sample_respornses(input_text):
    user_message = str(input_text).lower()
    
    if user_message in ('hello', '안녕', "안녕하세요", "hi", "하이", "헬로우"):
        return "안녕! 반가워, 나는 덕덕이의 샘플 봇이야! 버그가 발견되었다면 @a1dmin9271 채널에서 덕덕이의 아이디를 찾아 연락줘!"
    
    if user_message in ('넌 누구니?', '너의 정체가 뭐야?'):
        return "덕덕이의 샘플 봇! @a1dmin9271"
    
    if user_message in ('시간', '지금시각', '시각', '날짜', '날', '날자'):
        now = datetime.now()
        
        return str(now)
    
    return '너의 말이 뭔지 모르겠어.'