

public class q6 {

    public static void main(String[] args) {

        System.out.println(solution(1599921244));

    }




    public static int solution(int n) {
        int answer = 0;

        while(n != 0){
            answer += n % 10; // 135 -> 135 % 10 = 5,    13 % 10 = 3
            n /= 10;    // 135 / 10 = 13.5 ->>>>> 13  ,   13 /10 --->> 1.3 ---> 1
        }
        return answer;
    }

}
