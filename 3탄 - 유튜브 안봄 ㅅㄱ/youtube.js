const startRestrictionHour = 22; // 10 PM
const endRestrictionHour = 6; // 6 AM

let watch = confirm("유튜브 계속 볼거임?");

if (watch) {
    alert("재밌게 보든가;;");
} else {
    let minutes = parseInt(prompt("몇 분 동안 유튜브를 금지할까요?"), 10);

    // 유효한 시간 입력을 받은 경우
    if (!isNaN(minutes) && minutes > 0) {
        const endRestrictionTime = new Date(Date.now() + minutes * 60000); // 현재 시간 + 지정된 분 후

        function isRestrictedTime() {
            const now = new Date();
            return now < endRestrictionTime;
        }

        // 유튜브 접근 제한 함수
        function restrictYouTubeAccess() {
            if (isRestrictedTime()) {
                const youtubeDomain = "https://www.youtube.com/";
                const currentUrl = window.location.href;

                // 유튜브 도메인에 접근하려고 하는지 확인
                if (currentUrl.startsWith(youtubeDomain)) {
                    window.location.href = "about:blank"; // 빈 페이지로 리디렉션
                    alert(`${minutes}분 동안 유튜브 금지임ㅅㄱ`); // 접근 금지 경고 표시
                }
            }
        }

        // 접근 제한 시간마다 접근 제한 설정 (1초마다 확인)
        setInterval(restrictYouTubeAccess, 1000); // 1초마다 접근 확인
    } else {
        alert("유효한 시간을 입력해주세요.");
    }
}
