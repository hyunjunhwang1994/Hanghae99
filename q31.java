public class q31 {

    public static void main(String[] args) {
        System.out.println(solution(10000000));

    }

    public static int solution(int n){
        int answer = 0;
        int count = 0;

        for(int i = 2; i <= n; i++){

            count = 0;

            if((i != 2) && (i % 2 == 0)){
                continue;
            }

            for(int j = 2; j<=Math.sqrt(i); j++){

                if(i % j == 0){
                    count++;
                    break;
                }

            }

            if(count >= 1){
                System.out.println(i+"는 소수가 아닙니다");
            }else{
                System.out.println(i+"는 소수 입니다.");
                answer++;
            }


        }

        return answer;
    }

}
