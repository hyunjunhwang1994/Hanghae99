import java.util.Arrays;

public class q27 {

    public static void main(String[] args) {

        int[] d = {2,2,3,3};
        int budget = 10;


        solution(d, budget);
    }

    public static int solution(int[] d, int budget){

        // 1. 배열 d를 오름차순 정렬
        // 2. budget에서 배열의 값을 하나하나 뺀다.
        int answer = 0;
        Arrays.sort(d);


        for (int i=0; i<d.length; i++){

            if(d[i] <= budget){

                budget -= d[i];
                answer++;

            }
        }

        return answer;
    }
}
