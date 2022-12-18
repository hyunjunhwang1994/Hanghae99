public class q25 {

    public static void main(String[] args) {



        System.out.println(solution(24,27));


    }


    public static int solution(int left, int right){
        int answer=0;


        // 1. 약수 체크.
        // 2. 짝수면 더하고
        // 3. 홀수면 빼기

        int count = 0;

        for (int i=1; i<=right; i++){

            if(left <= right){

                for(int j=1; j<=left; j++){

                    if(left % j == 0){
                        count++;
                    }

                }
                if(count % 2 == 0){
                    answer += left;
                    count =0;
                } else if (count % 2 == 1) {
                    answer-= left;
                    count =0;
                }

                left++;
            }else {
                break;
            }

        }


        return answer;

    }
}
