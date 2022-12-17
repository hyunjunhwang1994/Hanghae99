public class q23 {
    public static void main(String[] args) {



        System.out.println( solution("x X zdqwqwZsaVSDJasdjkqnjckCNJK", 26));



    }



    // 아스키 코드 활용 만들어보기.

    public static String solution(String s, int n){
        String answer = "";


        // 일단 AB를 BC로 만드는 과정부터 해보기.
        // String을 알파벳 별로 캐릭터로 바꿔야한다.
        // 그다음은 n만큼 미는것 추가.

        // z 처리하기.
        // 공백을 밀었을때 예외를 처리하기. (아스키코드 32 공백)

        // 마지막 특수문자 처리하기.
        // 65:A,  90:Z
        // 97:a,  122:z
        // 위의 아스키코드외 나머지는 표현x

        for (int i=0; i<s.length();i++){

            char c = s.charAt(i);
            char moveC = (char) (c + n);

            //공백처리
            if(c == 32){

            }else if(moveC > 122){
                c = (char) (moveC -26);

            }else if(c < 91 && moveC > 90){
                c = (char) (moveC -26);
            } else{
                c += n;
            }

            answer += c;



        }


        return answer;
    }
}
