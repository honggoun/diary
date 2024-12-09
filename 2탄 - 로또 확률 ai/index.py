import pandas as pd

# CSV 파일 읽기 및 확률 계산
def load_lotto_data(file_name):
    try:
        data = pd.read_csv(file_name, header=None)
        numbers = data.iloc[0].tolist()  # 번호 리스트
        counts = data.iloc[1].tolist()  # 각 번호의 당첨 횟수
        total_counts = sum(counts)  # 전체 당첨 횟수 합산
        return {num: count / total_counts for num, count in zip(numbers, counts)}
    except FileNotFoundError:
        raise FileNotFoundError(f"'{file_name}' 파일을 찾을 수 없습니다.")
    except Exception as e:
        raise ValueError(f"파일을 읽는 중 문제가 발생했습니다: {e}")


# 사용자 입력 번호 검증
def get_user_numbers():
    print("로또 번호 6개를 입력하세요 (1~45 사이, 중복 없이):")
    user_numbers = list(map(int, input().split()))
    if len(user_numbers) != 6 or any(num < 1 or num > 45 for num in user_numbers) or len(set(user_numbers)) != 6:
        raise ValueError("잘못된 입력입니다. 1~45 사이의 중복되지 않는 번호 6개를 입력하세요.")
    return user_numbers


# 당첨 확률 계산
def calculate_probability(user_numbers, probabilities):
    final_probability = 1
    for num in user_numbers:
        final_probability *= probabilities.get(num, 0)
    return final_probability


# 메인 함수
def main():
    lotto_file = "lotto.csv"
    try:
        probabilities = load_lotto_data(lotto_file) 
        user_numbers = get_user_numbers()
        final_probability = calculate_probability(user_numbers, probabilities)
        print(f"입력하신 번호 {user_numbers}의 당첨 확률은 약 {final_probability:.15f}입니다.")
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)


# 실행
if __name__ == "__main__":
    main()
