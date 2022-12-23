public class Main {

    // 12월 23일
    //https://school.programmers.co.kr/learn/courses/30/lessons/12945
    // 피보나치 수 n % 1234567


    public int solution(int n){
        int answer = 0;

        int n0 = 1;
        int n1 = 1;

        for(int i = 2; i<n; i++){

            answer = (n0 + n1) % 1234567;
            n0 = n1;
            n1 = answer;

        }


        return answer;
    }


    public static void main(String[] args) {

        Main test = new Main();
        System.out.println(test.solution(100000));

    }



}