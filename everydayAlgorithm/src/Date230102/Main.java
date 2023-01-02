package Date230102;



// 2023 01월 02일
// https://school.programmers.co.kr/learn/courses/30/lessons/12951
// JadenCase 문자열 만들기
public class Main {

    public static void main(String[] args) {

        Main solution = new Main();

        solution.solution("for the last week");

    }

    public String solution(String s) {
        String answer = "";
        char alphabet;
        boolean firstAlphabet = false;


        for (int i = 0; i < s.length(); i++) {

            alphabet = s.charAt(i);


            // 공백및 첫 문자 확인
            if (alphabet == 32 || (i == 0)) {
                firstAlphabet = true;
            }

            // 첫문자 확인하기위해 firstAlphabet확인, 공백은 넘김.
            if (firstAlphabet == true && alphabet != 32 ) {

                // 알파벳이 소문자이면 대문자로 바꾸기
                if (alphabet >= 97 && alphabet <= 122) {
                    alphabet = (char)(alphabet - 32);
                }
                firstAlphabet = false;
            } else if(alphabet >= 65 && alphabet <= 90) { // 첫문자가아닌데 대문자인경우 소문자로 변경
                alphabet = (char)(alphabet + 32);
            }
            answer += alphabet;

        }

        return answer;
    }



}
