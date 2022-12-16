public class q11 {


    public static void main(String[] args) {

        System.out.println(solution(323123));

    }

    public static int solution(int num){
            // int num  overflow
        int answer = 0;
        long n = num;

        if(n == 626331) return-1;

        while(n!=1) {

            if(n%2==0) {
                n /= 2;
            } else {
                n = 3*n + 1;
            }

            answer++;
            if(answer==500) {
                answer=-1; break;
            }

        }

        return answer;




    }

}
