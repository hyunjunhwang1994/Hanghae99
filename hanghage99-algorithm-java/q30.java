public class q30 {

    public static void main(String[] args) {
        System.out.println(solution(10));
    }



    public static int solution(int n ){
        int answer=0;

        int i = 1;
        while (true){


            if (n % i == 1){

                answer = i;
            break;
            }
            i++;



        }


        return answer;
    }
}
